from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin
import pandas as pd

app = Flask(__name__)
CORS(app)
expense = pd.read_csv('expense.csv')


@app.route('/api/expenses/<int:expenseID>', methods=['GET', 'POST'])
@cross_origin()
def get_expense_by_id(expenseID):
    if request.method == 'GET':
        return jsonify(expense.loc[expense['expenseID'] == expenseID].to_json())
    # elif request.method == 'POST':
    #     # 处理 POST 请求
    #     json_data = request.get_json()
    #     if json_data:
    #         data = {'message': 'Received data: {}'.format(json_data)}
    #         return jsonify(data)
    #     else:
    #         return jsonify({'error': 'Invalid JSON'}), 400


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
    print(new_expense)

    # 返回新增的支出信息
    return jsonify(new_expense), 201

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
        print("delete successfully")
        return jsonify({'message': f'Expense with expenseID {expenseID} deleted successfully.'}), 200
    else:
        print("delete failed")
        return jsonify({'error': f'Expense with expenseID {expenseID} not found.'}), 404

@app.route('/api/expenses/submit/<int:expenseID>', methods=['POST'])
@cross_origin()
def submit_expense(expenseID):
  expense.loc[expense['expenseID'] == expenseID, 'applicationState'] = 1
  expense.to_csv('expense.csv', index=False)
  print("expense submit successfully")
  # 返回成功更新的响应
  return jsonify({'message': 'Expense submit successfully'}), 200

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
    print(new_expense)
    # 返回新增的支出信息
    return jsonify(new_expense), 200

if __name__ == '__main__':
    app.run(debug=True)
