import numpy as np
from flask import Flask, request, jsonify, json, send_from_directory
from flask_cors import CORS, cross_origin
import pandas as pd
import math
import os

app = Flask(__name__)
CORS(app)
expense = pd.read_csv('expense.csv')
users = pd.read_csv('user.csv')
users['userID'] = users['userID'].astype(str)
fund = pd.read_csv('fund.csv')
fund['userID'] = fund['userID'].astype(str)
filtered_df = fund[fund['fundID'] == 5433912]
totalQuota = filtered_df['totalQuota'].values[0]
result = fund[fund['userID'] == 1]['fundID'].tolist()
result = expense[expense['fundID'].isin(result)]
print(result)

currentUser = '1'
# API 1. 获取课题组全部经费完成情况（支出情况）：
@app.route('/api/users/<userID>/funds', methods=['GET'])
@cross_origin()
def get_user_finish_performance(userID):
      select = fund[fund['userID'] == userID]
      if len(select):
        items = [{
            "expenses": expense[expense['fundID'] == select.iloc[_]['fundID']].to_json(),
            "fund": select.iloc[_].to_json()
            } for _ in range(len(select))]
        return jsonify({'items': items}), 200
      else:
        return jsonify({'message': "This user doesn't have any fund."}), 200


# API 1. 获取课题组全部经费完成情况（支出情况）Excel文件：
@app.route('/api/users/<userID>/funds/excel', methods=['GET'])
@cross_origin()
def get_user_finish_performance_excel(userID):
      select = fund[fund['userID'] == userID]
      if len(select):
        duo = pd.read_csv('多项经费使用一览表.csv')
        count = 0
        expense_3 = expense[expense['applicationState'] == 3]
        for _ in select['fundID']:
          count += 1
          lst_expense_amount = list(expense_3[expense_3['fundID'] == _]['amount'])
          sum_lea = sum(lst_expense_amount)
          lst_expense_amount += [0] * (12 - len(lst_expense_amount))

          l = list(select[select['fundID'] == _].iloc[0])
          duo.loc[len(duo)] = [count] + l[:2] + ['有效期fixme', l[3]] + lst_expense_amount + [sum_lea, l[3] - sum_lea, '天数fixme', str('%.2f' % (sum_lea / l[3] * 100)) + '%', '是' if sum_lea / l[3] > 0.6 else '否']

        zonge = sum(duo['经费总额'])
        yue = sum(duo['经费余额'])
        zxl = 1 - yue / zonge
        duo.loc[len(duo)] = ['', '', '合计', '', zonge, '', '', '', '', '', '', '', '', '', '', '', '',
                             sum(duo['已使用经费']), yue, '', str('%.2f' % (zxl * 100)) + '%',
                             '是' if zxl > 0.6 else '否']
        duo.to_excel('多项经费使用一览表.xlsx', index=False)

        return send_from_directory(os.getcwd(), '多项经费使用一览表.xlsx', as_attachment=True)
      else:
        return jsonify({'message': "This user doesn't have any fund."}), 200


# API 2. 查询若干个fundID的使用情况和执行率：
@app.route('/api/funds/<fundIDs>/', methods=['GET'])
@cross_origin()
def get_fund_finish_performance(fundIDs):
      fundID_lst = fundIDs.split(",")
      items = []
      for _ in fundID_lst:
        fundID = int(_)
        select = fund[fund['fundID'] == fundID]
        items.append(select.to_json() if len(select) else {'error': f'Fund with fundID {fundID} not found.'})
      return jsonify({'items': items}), 200


# API 1. 查询一笔支出的申请情况：
@app.route('/api/expenses/<int:expenseID>', methods=['GET'])
@cross_origin()
def get_expense_by_id(expenseID):
      select = expense.loc[expense['expenseID'] == expenseID].iloc[0]
      if len(select):
        return jsonify(select.to_json()), 200
      else:
        return jsonify({'error': f'Expense with expenseID {expenseID} not found.'}), 404


# API 2. 查询待审批的所有支出列表：
@app.route('/api/expenses/pending', methods=['GET'])
@cross_origin()
def get_pending_expense():
      select = expense.loc[expense['applicationState'] == 1]  # 1:待审批; 0:已审批
      if len(select):
        return jsonify([select.iloc[_].to_dict() for _ in range(len(select))]), 200
      else:
        return jsonify({'message': "There is no pending expense."}), 200


# API 3. 增加一个经费：
@app.route('/api/funds/add', methods=['POST'])
@cross_origin()
def add_fund():
      fundID = int(request.json.get('fundID'))
      fundName = request.json.get('fundName')  # request.form.get
      userID = int(request.json.get('userID'))
      totalQuota = request.json.get('totalQuota')
      usedQuota = request.json.get('usedQuota')
      abstract = request.json.get('usedQuota')
      remark = request.json.get('usedQuota')

      new_fund = {
          'fundID': fundID,
          'fundName': fundName,
          'userID': userID,
          'totalQuota': totalQuota,
          'usedQuota': usedQuota,
          'abstract': abstract,
          'remark': remark,
      }

      print(fundID)
      print(fund['fundID'].values)

      if fundID in fund['fundID'].values:
          print('error success')
          return jsonify({'error': f'Duplicated fundID {fundID}.'}), 404

      fund.loc[len(fund)] = new_fund
      fund.to_csv('fund.csv', index=False)

      return jsonify(new_fund), 201


# API 3. 删除一个经费：
@app.route('/api/funds/delete/<int:fundID>', methods=['DELETE'])
@cross_origin()
def delete_fund(fundID):
    if fundID in fund['fundID'].values:
        fund.drop(fund[fund['fundID'] == fundID].index, inplace=True)
        fund.reset_index(drop=True, inplace=True)
        fund.to_csv('fund.csv', index=False)
        return jsonify({'message': f'Fund with fundID {fundID} deleted successfully.'}), 200
    else:
        return jsonify({'error': f'Fund with fundID {fundID} not found.'}), 404


# 增加支出

@app.route('/api/expenses/add', methods=['POST'])
@cross_origin()
def add_expense():
    # 获取请求中的参数
    expenseID = int(request.json.get('expenseID'))
    if expenseID in expense['expenseID'].values:
      print('error success')
      return jsonify({'error': f'Duplicated expenseID {expenseID}.'}), 404
    expenseName = request.json.get('expenseName')
    fundID = int(request.json.get('fundID'))
    if fundID not in fund['fundID'].values:
      return jsonify({'error': f'Unkowen fundID {expenseID}.'}), 404
    amount = float(request.json.get('amount'))
    operator = request.json.get('operator')
    category1 = request.json.get('category1')
    category2 = request.json.get('category2')
    abstract = request.json.get('abstract')
    remark = request.json.get('remark')
    applicationState = int(request.json.get('applicationState'))
    # 创建新支出信息
    new_expense = {
        'expenseID': expenseID,
        'expenseName': expenseName,
        'fundID': fundID,
        'amount': amount,
        'operator': operator,
        'category1': category1,
        'category2': category2,
        'abstract': abstract,
        'remark': remark,
        'applicationState': applicationState
    }
    filtered_df = fund[fund['fundID'] == fundID]
    # 获取 totalQuota 和 usedQuota 列的值
    totalQuota = filtered_df['totalQuota'].values[0]
    usedQuota = filtered_df['usedQuota'].values[0]
    if float(usedQuota) + amount > float(totalQuota):
      return jsonify({'error': f'expense exceed total quota.'}), 405
    usedQuota = float(usedQuota) + amount
    mask = fund['fundID'] == fundID
    fund.loc[mask, 'usedQuota'] = usedQuota
    print(expense['expenseID'].values)
    expense.loc[len(expense)] = new_expense
    expense.to_csv('expense.csv', index=False)
    fund.to_csv('fund.csv', index=False)
    # 返回新增的支出信息
    return jsonify(new_expense), 201

#删除支出
@app.route('/api/expenses/delete/<int:expenseID>', methods=['DELETE'])
@cross_origin()
def delete_expense(expenseID):
    # 检查 DataFrame 中是否存在对应的 expenseID
    print("hi")
    if expenseID in expense['expenseID'].values:
        # 根据 expenseID 删除对应的数据行
        expense.drop(expense[expense['expenseID'] == expenseID].index, inplace=True)
        expense.reset_index(drop=True, inplace=True)
        expense.to_csv('expense.csv', index=False)
        return jsonify({'message': f'Expense with expenseID {expenseID} deleted successfully.'}), 200
    else:
        print("delete failed")
        return jsonify({'error': f'Expense with expenseID {expenseID} not found.'}), 404

#送审支出
@app.route('/api/expenses/submit/<int:expenseID>', methods=['POST'])
@cross_origin()
def submit_expense(expenseID):
  if expenseID in expense['expenseID'].values:
    expense.loc[expense['expenseID'] == expenseID, 'applicationState'] = 1
    expense.to_csv('expense.csv', index=False)
    print("expense submit successfully")
    # 返回成功更新的响应
    return jsonify({'message': 'Expense submit successfully'}), 200
  else:
    return jsonify({'error': f'Expense with expenseID {expenseID} not found.'}), 404




#修改支出
@app.route('/api/expenses/modify/<int:expenseID>', methods=['PUT'])
@cross_origin()
def modify_expense(expenseID):
    print(expenseID)
    # 获取请求中的参数
    if expenseID in expense['expenseID'].values:
      expenseName = request.json.get('expenseName')
      fundID = int(request.json.get('fundID'))
      if fundID not in fund['fundID'].values:
        return jsonify({'error': f'Unkowen fundID {expenseID}.'}), 404
      amount = float(request.json.get('amount'))
      operator = request.json.get('operator')
      category1 = request.json.get('category1')
      category2 = request.json.get('category2')
      abstract = request.json.get('abstract')
      remark = request.json.get('remark')
      applicationState = int(request.json.get('applicationState'))
      # 创建新支出信息
      new_expense = {
          'expenseID': expenseID,
          'expenseName': expenseName,
          'fundID': fundID,
          'amount': amount,
          'operator': operator,
          'category1': category1,
          'category2': category2,
          'abstract': abstract,
          'remark': remark,
          'applicationState': applicationState
      }
      # 将新支出信息添加到列表中
      filtered_df = expense[expense['expenseID'] == expenseID]
      old_amount = filtered_df['amount'].values[0]
      filtered_df = fund[fund['fundID'] == fundID]
      totalQuota = filtered_df['totalQuota'].values[0]
      usedQuota = filtered_df['usedQuota'].values[0]
      if float(usedQuota) + amount - float(old_amount) > float(totalQuota):
        return jsonify({'error': f'expense exceed total quota.'}), 404
      usedQuota = float(usedQuota) + amount - float(old_amount)
      mask = fund['fundID'] == fundID
      fund.loc[mask, 'usedQuota'] = usedQuota
      index_to_update = expense[expense['expenseID'] == expenseID].index
      expense.loc[index_to_update] = list(new_expense.values())
      expense.to_csv('expense.csv', index=False)
      fund.to_csv('fund.csv', index=False)
      return jsonify(new_expense), 200
    else:
      return jsonify({'error': f'Expense with expenseID {expenseID} not found.'}), 404

#添加用户
@app.route('/api/user/add', methods=['POST'])
@cross_origin()
def add_user():
    # 获取请求中的参数
    userID = int(request.json.get('userID'))
    userName = request.json.get('userName')
    privilege = int(request.json.get('privilege'))
    # 创建新支出信息
    new_user = {
        'userID': userID,
        'userName': userName,
        'privilege': privilege,
    }
    # 将新支出信息添加到列表中
    if userID in users['userID'].values:
      return jsonify({'error': f'Duplicated userID {userID}.'}), 404
    users.loc[len(users)] = new_user
    users.to_csv('user.csv', index=False)
    print(new_user)
    # 返回新增的支出信息
    return jsonify(new_user), 201

#修改用户
@app.route('/api/user/modify/<int:userID>', methods=['PUT'])
@cross_origin()
def modify_user(userID):
    # 获取请求中的参数
    if userID in users['userID'].values:
      userName = request.json.get('userName')
      privilege = int(request.json.get('privilege'))
      # 创建新支出信息
      new_user = {
          'userID': userID,
          'userName': userName,
          'privilege': privilege,
      }
      # 将新支出信息添加到列表中
      index_to_update = users[users['userID'] == userID].index
      users.loc[index_to_update] = new_user
      users.to_csv('user.csv', index=False)
      print(new_user)
      # 返回新增的支出信息
      return jsonify(new_user), 201
    else:
      return jsonify({'error': f'Expense with userID {userID} not found.'}), 404

#删除用户
@app.route('/api/user/delete/<int:userID>', methods=['DELETE'])
@cross_origin()
def delete_user(userID):
    # 检查 DataFrame 中是否存在对应的 expenseID
    print("hi")
    if userID in users['userID'].values:
        # 根据 expenseID 删除对应的数据行
        users.drop(users[users['userID'] == userID].index, inplace=True)
        users.reset_index(drop=True, inplace=True)
        users.to_csv('user.csv', index=False)
        print("delete successfully")
        return jsonify({'message': f'User with userID {userID} deleted successfully.'}), 200
    else:
        print("delete failed")
        return jsonify({'error': f'User with userID {userID} not found.'}), 404



def export_user_fund():
  global fund
  remainQuota = fund['totalQuota'] - fund['usedQuota']
  executeRate = fund['usedQuota'] / fund['totalQuota']
  fund['remainQuota'] = remainQuota
  fund['executeRate'] = executeRate
  fund = fund.drop('remark', axis=1)
  fund = fund.drop('abstract', axis=1)
  fund.rename(columns={'fundID': '经费编号', 'fundName': '经费名称', 'userID': '课题组', 'totalQuota': '可使用经费总额'
    , 'usedQuota': '已使用经费', 'remainQuota': '经费余额', 'executeRate': '执行率'}, inplace=True)
  fund.to_csv('经费使用汇总表.csv')
  fund = pd.read_csv('fund.csv')



@app.route('/api/users/login', methods=['GET'])
@cross_origin()
def examineUser():
  global currentUser
  username = request.args.get('username')
  passwd = int(request.args.get('passwd'))

  if username in users['userName'].values:
      if passwd == users.loc[users['userName'] == username, 'password'].values[0]:
        userID = users.loc[users['userName'] == username, 'userID'].values[0]
        currentUser = userID
        return jsonify(1), 200
  return jsonify(0), 200

@app.route('/api/users/<int:expenseID>/accept', methods=['POST'])
@cross_origin()
def accept_pending(expenseID):
  if expenseID in expense['expenseID'].values():
    expense.loc[expense['expenseID'] == expenseID, 'applicationState'] = 3
    return jsonify('accept successfully'), 200

  return jsonify({'error': f'Unknown expenseID'}), 404

@app.route('/api/users/<int:expenseID>/reject', methods=['POST'])
@cross_origin()
def reject_pending(expenseID):
  if expenseID in expense['expenseID'].values():
    expense.loc[expense['expenseID'] == expenseID, 'applicationState'] = 2
    return jsonify('reject successfully'), 200

@app.route('/api/expenses/findAll', methods=['GET'])
@cross_origin()
def find_all_expenses():
  result = fund[fund['userID'] == currentUser]['fundID'].tolist()
  result = expense[expense['fundID'].isin(result)]
  print(result.to_json(orient='records'))
  return result.to_json(orient='records'), 200


if __name__ == '__main__':
    app.run(debug=True)
