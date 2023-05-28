from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin
import pandas as pd
import math

app = Flask(__name__)
CORS(app)
expense = pd.read_csv('expense.csv')
users = pd.read_csv('user.csv')
fund = pd.read_csv('fund.csv')


# API 1. 获取课题组全部经费完成情况（支出情况）：
@app.route('/api/groups/<int:userID>/funds', methods=['GET'])  # 此处的userID，即为杨在文档中写的groupID，董认为userID和groupID是同一个东西
@cross_origin()
def get_user_finish_performance(userID):
      select = fund[fund['userID'] == userID]
      if len(select):
        items = [{
            "expenses": expense[expense['fundID'] == select.iloc[_]['fundID']].to_json(),
            "fund": select.iloc[_].to_json()
            # 杨在文档中说，执行率由前端计算。
            # 如果由后端计算，如下所示，前端可作为参考
            #, "fund_finish_performance": 0 if math.isnan(select.iloc[_]['usedQuota']) else select.iloc[_]['usedQuota'] / select.iloc[_]['totalQuota']
          } for _ in range(len(select))]
        return jsonify({'items': items}), 200
      else:
        return jsonify({'message': "This user doesn't have any fund."}), 200


# API 2. 查询若干个fundID的使用情况和执行率：
@app.route('/api/funds/<fundIDs>/', methods=['GET'])  # 此处的userID，即为杨在文档中写的groupID，董认为userID和groupID是同一个东西
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
      select = expense.loc[expense['expenseID'] == expenseID]
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
        return jsonify(select.to_json()), 200
      else:
        return jsonify({'message': "There is no pending expense."}), 200


# API 3. 增加一个经费：
@app.route('/api/funds/add', methods=['POST'])
@cross_origin()
def add_fund():
      fundName = request.json.get('fundName')  # request.form.get
      userID = request.json.get('userID')
      totalQuota = request.json.get('totalQuota')

      if fundName and userID and totalQuota:
          new_fund = {
            'fundID': int(fund.loc[len(fund) - 1]['fundID'] + 1),
            # 杨写的API，没有给fundID，董认为必须有fundID，否则后面无法删除
            # 暂时将fundID设为：此前最后一条fund的fundID + 1
            'fundName': fundName,
            'userID': userID,
            'totalQuota': totalQuota,
          }
          fund.loc[len(fund)] = new_fund
          fund.to_csv('fund.csv', index=False)
          return jsonify(new_fund), 201    # 返回值包含新生成的fundID
      else:
          return jsonify({'error': 'Invalid request params'}), 400


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
    expenseID = request.json.get('expenseID')
    expenseName = request.json.get('expenseName')
    fundID = request.json.get('fundID')
    amount = request.json.get('amount')
    operator = request.json.get('operator')
    category1 = request.json.get('category1')
    category2 = request.json.get('category2')
    abstract = request.json.get('abstract')
    remark = request.json.get('remark')
    applicationState = request.json.get('applicationState')
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
    expense.loc[len(expense)] = new_expense
    expense.to_csv('expense.csv', index=False)

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
  expense.loc[expense['expenseID'] == expenseID, 'applicationState'] = 1
  expense.to_csv('expense.csv', index=False)
  print("expense submit successfully")
  # 返回成功更新的响应
  return jsonify({'message': 'Expense submit successfully'}), 200

#修改支出
@app.route('/api/expenses/modify/<int:expenseID>', methods=['PUT'])
@cross_origin()
def modify_expense(expenseID):
    # 获取请求中的参数
    # expenseID = request.json.get('expenseID')
    expenseName = request.json.get('expenseName')
    fundID = request.json.get('fundID')
    amount = request.json.get('amount')
    operator = request.json.get('operator')
    category1 = request.json.get('category1')
    category2 = request.json.get('category2')
    abstract = request.json.get('abstract')
    remark = request.json.get('remark')
    applicationState = request.json.get('applicationState')
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
    index_to_update = expense[expense['expenseID'] == expenseID].index
    expense.loc[index_to_update] = new_expense
    expense.to_csv('expense.csv', index=False)
    return jsonify(new_expense), 200

#添加用户
@app.route('/api/user/add', methods=['POST'])
@cross_origin()
def add_user():
    # 获取请求中的参数
    userID = request.json.get('userID')
    userName = request.json.get('userName')
    privilege = request.json.get('privilege')
    # 创建新支出信息
    new_user = {
        'userID': userID,
        'userName': userName,
        'privilege': privilege,
    }
    # 将新支出信息添加到列表中
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
    userName = request.json.get('userName')
    privilege = request.json.get('privilege')
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

if __name__ == '__main__':
    app.run(debug=True)
