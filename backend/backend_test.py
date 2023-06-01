import unittest
import pandas as pd

from server import app

class TestGetFundFinishPerformance(unittest.TestCase):
  def setUp(self):
    # 在每个测试方法执行之前的准备工作
    self.app = app.test_client()

  def tearDown(self):
    # 在每个测试方法执行之后的清理工作
    pass

  def test_get_fund_finish_performance(self):
    # 构造测试数据和请求参数
    fundIDs = "1"
    expected_status_code = 200

    # 发起请求
    response = self.app.get(f'/api/funds/{fundIDs}/')
    # 验证响应状态码
    self.assertEqual(response.status_code, expected_status_code)
    # 验证响应数据
    data = response.get_json()
    print(data)
    data = response.get_json()

    items = data['items']
    for item in items:
      self.assertTrue(item['userID'] == 5)
    # 进一步验证响应数据的结构、内容等

  def test_get_expense_by_id(self):
    # 发送 GET 请求并获取响应
    response = self.app.get('/api/expenses/1')
    # 验证状态码是否为 200
    assert response.status_code == 200
    # 获取响应数据
    data = response.get_json()
    # 验证数据内容
    assert 'error' not in data  # 没有错误信息表示成功
    assert isinstance(data, dict)  # 数据类型为字典
    assert 'expenseID' in data  # 包含 expenseID 字段

  def test_get_pending_expense(self):
    # 发送 GET 请求并获取响应
    response = self.app.get('/api/expenses/pending')
    # 验证状态码是否为 200
    assert response.status_code == 200

    # 获取响应数据
    data = response.get_json()
    # 验证数据内容
    assert isinstance(data, list)  # 数据类型为列表
    assert len(data) >= 0  # 数据长度大于等于 0

  def test_delete_fund(self):
    # 读取测试用的 CSV 文件并设置为全局变量
    fund = pd.read_csv('fund.csv')
    # 发送 DELETE 请求并获取响应
    response = self.app.delete('/api/funds/delete/1')

    # 验证状态码是否为 200
    assert response.status_code == 200

    # 验证经费是否被删除
    assert 1 not in fund['fundID'].values

  def test_add_expense(self):
    # 读取测试用的 CSV 文件并设置为全局变量
    global expense, fund
    expense = pd.read_csv('expense.csv')
    fund = pd.read_csv('fund.csv')

    # 构造 POST 请求的数据
    data = {
      'expenseID': 1001,
      'expenseName': 'Test Expense',
      'fundID': 1,
      'amount': 100.0,
      'operator': 'John Doe',
      'category1': 'Category 1',
      'category2': 'Category 2',
      'abstract': 'Test Abstract',
      'remark': 'Test Remark',
      'applicationState': 1
    }
    # 发送 POST 请求并获取响应
    response = self.app.post('/api/expenses/add', json=data)

    # 验证状态码是否为 201
    assert response.status_code == 201

    # 验证新增的支出信息是否正确保存到数据库
    assert expense.loc[expense['expenseID'] == 1001, 'expenseName'].values[0] == 'Test Expense'

  def test_delete_expense(self):
    # 读取测试用的 CSV 文件并设置为全局变量
    global expense
    expense = pd.read_csv('expense.csv')

    # 发送 DELETE 请求并获取响应
    response = self.app.delete('/api/expenses/delete/1001')
    # 验证状态码是否为 200
    assert response.status_code == 200

    # 验证对应的 expenseID 是否被成功删除
    assert 1001 not in expense['expenseID'].values

  def test_modify_expense(self):
    # 读取测试用的 CSV 文件并设置为全局变量
    global expense, fund
    expense = pd.read_csv('expense.csv')
    fund = pd.read_csv('fund.csv')
    # 构造修改的请求体
    request_body = {
      'expenseName': 'New Expense Name',
      'fundID': 1,
      'amount': 200.0,
      'operator': 'John Doe',
      'category1': 'Category 1',
      'category2': 'Category 2',
      'abstract': 'New Abstract',
      'remark': 'New Remark'
    }
    # 发送 PUT 请求并获取响应
    response = self.app.put('/api/expenses/modify/10001', json=request_body)
    modified_expense = expense.loc[expense['expenseID'] == 10001].iloc[0].to_dict()
    assert modified_expense['expenseName'] == 'New Expense Name'
    assert modified_expense['fundID'] == 1
    assert modified_expense['amount'] == 200.0
    assert modified_expense['operator'] == 'John Doe'
    assert modified_expense['category1'] == 'Category 1'
    assert modified_expense['category2'] == 'Category 2'
    assert modified_expense['abstract'] == 'New Abstract'
    assert modified_expense['remark'] == 'New Remark'

  def test_valid_credentials(self):
    # 模拟有效的用户名和密码
    username = 'alice'
    passwd = 123456
    # 创建一个测试客户端
      # 模拟 GET 请求发送有效的用户名和密码
    response = self.app.get(f'/api/users/login?username={username}&passwd={passwd}')
    # 验证返回结果是否正确
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.get_json(), 1)

  def test_accept_existing_expense(self):
    # 模拟存在的 expenseID
    expense_id = 123
    response = self.app.post(f'/api/users/{expense_id}/accept')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.get_json(), 'accept successfully')

  def test_reject_existing_expense(self):
    # 模拟存在的 expenseID
    expense_id = 123
    # 创建一个测试客户端
    # 模拟 POST 请求发送存在的 expenseID
    response = self.app.post(f'/api/users/{expense_id}/reject')
    # 验证返回结果是否正确
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.get_json(), 'reject successfully')

  def test_get_user_funds_current_user(self):
      # 模拟 GET 请求发送当前用户的请求
    response = self.app.get('/api/users/funds')
    # 验证返回结果是否正确
    self.assertEqual(response.status_code, 200)
    # 验证返回的 JSON 数据是否包含预期的键
    self.assertIn('items', response.get_json())

  def test_generate_time_list_fund(self):
    # 模拟 GET 请求发送
    # 模拟 GET 请求发送
    response = self.app.get('/api/chart/fund')

    # 验证返回结果是否正确
    self.assertEqual(response.status_code, 200)
    # 验证返回的 JSON 数据是否包含预期的键
    self.assertIn('第0周', response.get_json())

  def test_get_user_finish_performance_excel(self):
    # 模拟 GET 请求发送
    # 模拟 GET 请求发送
    response = self.app.get('/api/users/funds/excel')
    # 验证返回结果是否正确
    self.assertEqual(response.status_code, 200)
    # 验证返回的文件名是否与预期相符
    self.assertEqual(response.headers['Content-Disposition'], 'attachment; filename="多项经费使用一览表.xlsx"')

  def test_add_fund(self):
    # 模拟 POST 请求发送
    # 构造请求数据
    data = {
      'fundID': 1,
      'fundName': 'Test Fund',
      'userName': 'testuser',
      'totalQuota': 1000,
      'usedQuota': 500,
      'abstract': 'Test abstract',
      'remark': 'Test remark'
    }

    # 模拟 POST 请求发送
    response = self.app.post('/api/funds/add', json=data)

    # 验证返回结果是否正确
    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.json['fundID'], 1)
    self.assertEqual(response.json['fundName'], 'Test Fund')

# 运行测试
if __name__ == '__main__':
  unittest.main()
