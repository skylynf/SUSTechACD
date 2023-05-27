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


if __name__ == '__main__':
    app.run(debug=True)
