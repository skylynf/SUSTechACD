# SUSTech_ACD API 开发者文档



## 简介

SUSTech_ACD是一个财务管理系统，用于管理课题组的经费和支出情况。

每个课题组都是一个用户，而每个经费属于一个课题组。

支出必须与特定的经费相关联，一个经费可以包含多笔支出。

支出的总金额不能超过经费的总额度。



## 操作列表

### 总览

查询：

1、（课题组）查询某课题组名下的全部经费的完成情况（支出情况），对应《财务系统.xlsx》多项经费使用一览表。

2、（课题组）查询一笔支出（expenseID）的申请情况，包含该支出的具体内容，和该支出的审批情况。

3、（管理员）可视化查看一笔经费的使用情况和支出项目。

4、（管理员）查询若干个fundID的使用情况和执行率（executionRate），对应《财务系统.xlsx》xx经费使用汇总表。

审批：

（管理员）查询待审批的所有支出列表，包含该支出的具体情况，并可审批。

增加/删除：

1、（管理员）增加或删除一个经费。

2、（课题组）增加（或删除）一个支出。

3、（课题组）送审一个支出。

修改：

1、（课题组）修改一个支出，并重新送审。



### 查询

1. 查询某课题组名下的全部经费的完成情况（支出情况）
   - 请求方式：GET
   - 路径：/api/users/{userID}/funds
   - 参数：userID（课题组ID）
   - 响应：返回该课题组下所有经费的完成情况和对应的支出情况
2. 查询一笔支出的申请情况
   - 请求方式：GET
   - 路径：/api/expenses/{expenseID}
   - 参数：expenseID（支出ID）
   - 响应：返回该支出的申请情况，包括具体内容和审批状态
3. 可视化查看一笔经费的使用情况和支出项目
   - 请求方式：GET
   - 路径：/api/funds/{fundID}/visualization
   - 参数：fundID（经费ID）
   - 响应：返回该经费的使用情况和支出项目的可视化信息
4. 查询若干个fundID的使用情况和执行率
   - 请求方式：GET
   - 路径：/api/funds
   - 参数：fundIDs（多个经费ID，逗号分隔）
   - 响应：返回指定经费ID的使用情况和执行率信息

### 审批

1. 查询待审批的所有支出列表
   - 请求方式：GET
   - 路径：/api/expenses/pending
   - 响应：返回待审批的支出列表及其详细情况
2. 审批支出
   - 请求方式：POST
   - 路径：/api/expenses/{expenseID}/approval
   - 参数：expenseID（支出ID）
   - 响应：返回审批结果的消息或状态

### 增加/删除

1. 增加或删除一个经费
   - 增加：
     - 请求方式：POST
     - 路径：/api/funds
     - 参数：经费相关信息（fundName、userID、totalQuota等）
     - 响应：返回新增的经费信息
   - 删除：
     - 请求方式：DELETE
     - 路径：/api/funds/{fundID}
     - 参数：fundID（待删除的经费ID）
     - 响应：返回删除成功的消息或状态
2. 增加或删除一个支出
   - 增加：
     - 请求方式：POST
     - 路径：/api/expenses
     - 参数：支出相关信息（expenseName、fundID、amount等）
     - 响应：返回新增的支出信息
   - 删除：
     - 请求方式：DELETE
     - 路径：/api/expenses/{expenseID}
     - 参数：expenseID（待删除的支出ID）
     - 响应：返回删除成功的消息或状态

### 修改

1. 修改一个支出并重新送审
   - 请求方式：PUT
   - 路径：/api/expenses/{expenseID}
   - 参数：expenseID（待修改的支出ID），支出相关信息（expenseName、amount等）
   - 响应：返回修改成功的支出信息
2. 修改一个经费
   - 请求方式：PUT
   - 路径：/api/funds/{fundID}
   - 参数：fundID（待修改的经费ID），经费相关信息（fundName、totalQuota等）
   - 响应：返回修改成功的经费信息



## Json对象内容 示例



### 经费（fund）

>一个唯一的经费号 fundID
>
>经费名称 fundName
>
>一个课题组 userID
>
>经费总额度 totalQuota
>
>已使用额度 usedQuota
>
>经费内容摘要 abstract
>
>经费备注 remark

```json
code{
  "fundID": 5433912,
  "fundName": "国自然",
  "userID": 12,
  "totalQuota": 500,
  "usedQuota": 10,
  "abstract": "this is a abstract",
  "remark": "no remark"
}
```



### 支出（expense）

> 唯一识别：支出编号 expenseID
>
> 支出名称 expenseName
>
> 该支出对应的经费号 fundID
>
> 支出额度 amount
>
> 经办人 operator
>
> 支出类别一级 category1
>
> 支出类别二级 category2
>
> 内容摘要 abstract
>
> 备注 remark
>
> 申请状态 ApplicationState = {0未发送, 1正在申请中, 2被拒绝打回, 3申请成功}

```json
code{
  "expenseID": 1827328,
  "expenseName": "办公用品采购",
  "fundID": 9374829,
  "amount": 50,
  "operator": "沈昀",
  "category1": "会议费",
  "category2": "学术会议费",
  "abstract": "购买会议必需品",
  "remark": "请尽快审批",
  "applicationState": 1
}
```



### 课题组（user）

>唯一识别：编号 userID
>
>课题组名称：userName 如“唐老师”
>
>密码：password

```json
code{
  "userID": 14,
  "userName": "唐老师",
  "password": "12345678"
}
```



## 后端API

1. 获取课题组全部经费完成情况（支出情况）

   - 请求方式：GET
   - 路径：/api/users/{userID}/funds
   - 参数：userID（课题组ID）
   - 响应：返回该课题组下所有经费的完成情况和支出情况

   ```json
        {
          "items": [
            {
              "expenses": 
                [
                  {expenseObject1},
                  {expenseObject2},
                  {expenseObject3}
                ],
              "fund": {fundObject}
            },
            {
              同上
            },
            {
              同上
            }
          ]
        }
   ```

2. 查询若干个fundID的使用情况和执行率，或是所有fundID的使用情况和执行率

   - 请求方式：GET
   - 路径：/api/funds
   - 参数：fundIDs（多个经费ID，逗号分隔）
   - 响应：返回指定经费ID的使用情况和执行率信息

   ```json
   {
     "items": [
       {fundObject1},
       {
         同上
       },
       {
         同上
       }
     ]
   }
   ```

3. 查询一笔支出的申请情况

   - 请求方式：GET
   - 路径：/api/expenses/{expenseID}
   - 参数：expenseID（支出ID）
   - 响应：返回该支出的申请情况

4. 查询待审批的所有支出列表

   - 请求方式：GET
   - 路径：/api/expenses/pending
   - 响应：返回待审批的支出列表及其详细情况

5. 增加或删除一个经费

   - 增加：
     - 请求方式：POST
     - 路径：/api/funds
     - 参数：经费相关信息
     - 响应：返回新增的经费信息
   - 删除：
     - 请求方式：DELETE
     - 路径：/api/funds/{fundID}
     - 参数：fundID（待删除的经费ID）
     - 响应：返回删除成功的消息或状态

6. 增加或删除一个支出

   - 增加：
     - 请求方式：POST
     - 路径：/api/expenses
     - 参数：支出相关信息
     - 响应：返回新增的支出信息
   - 删除：
     - 请求方式：DELETE
     - 路径：/api/expenses/{expenseID}
     - 参数：expenseID（待删除的支出ID）
     - 响应：返回删除成功的消息或状态

7. 送审一个支出

   - 请求方式：POST
   - 路径：/api/expenses/{expenseID}/submit
   - 参数：expenseID（待送审的支出ID）
   - 响应：返回送审成功的消息或状态

8. 修改一个支出并重新送审

   - 请求方式：PUT
   - 路径：/api/expenses/{expenseID}
   - 参数：expenseID（待修改的支出ID），支出相关信息
   - 响应：返回修改成功的支出信息

9. 修改一个经费

   - 请求方式：PUT
   - 路径：/api/funds/{fundID}
   - 参数：fundID（待修改的经费ID），经费相关信息
   - 响应：返回修改成功的经费信息

10. 用户操作

    - 增加用户
      - 请求方式：POST
      - 路径：/api/users
      - 参数：用户相关信息
      - 响应：返回新增的用户信息
    - 修改用户
      - 请求方式：PUT
      - 路径：/api/users/{userID}
      - 参数：userID（待修改的用户ID），用户相关信息
      - 响应：返回修改成功的用户信息
    - 删除用户
      - 请求方式：DELETE
      - 路径：/api/users/{userID}
      - 参数：userID（待删除的用户ID）
      - 响应：返回删除成功的消息或状态
    - 用户登录
      - 请求方式：POST
      - 路径：/api/users/login
      - 参数：用户名和密码
      - 响应：返回登录成功或失败的消息



## 注意事项



- API路径中的占位符（如{userID}、{fundID}、{expenseID}）应替换为实际的课题组ID、经费ID和支出ID。
- 增加API需要在后端进行相应的实现，使用Flask框架。
- Excel部分的实现可以使用Blob库。
- 请根据需要完善后端的相关功能和逻辑。