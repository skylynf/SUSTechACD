<template>
  <div class="app-container">
    <div class="filter-container">
<!--      'name', 'id', 'reputation','link','profile image','participation'-->
      <el-checkbox-group v-model="checkboxVal">
        <el-checkbox label="expenseID">
          expenseID
        </el-checkbox>
        <el-checkbox label="fundID">
          fundID
        </el-checkbox>
        <el-checkbox label="amount">
          amount
        </el-checkbox>
        <el-checkbox label="operator">
          operator
        </el-checkbox>
        <el-checkbox label="category1">
          category1
        </el-checkbox>
        <el-checkbox label="category2">
          category2
        </el-checkbox>
        <el-checkbox label="abstract">
          abstract
        </el-checkbox>
        <el-checkbox label="remark">
          remark
        </el-checkbox>
        <el-checkbox label="applicationState">
          applicationState
        </el-checkbox>

      </el-checkbox-group>
    </div>
<!--经费编号	经费名称	课题组	经办人	支出类别一级	支出类别二级	内容摘要	支出金额（元）-->
    <el-table :key="key" :data="tableData" border fit highlight-current-row style="width: 100%">
      <el-table-column v-for="fruit in formThead" :key="fruit" :label="fruit">
        <template slot-scope="scope">
          {{ scope.row[fruit] }}
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <!-- 这里可以添加您自定义的按钮内容和行为 -->
          <el-button type="primary" size="small" @click="handleButtonClick(scope.row)">Go to his/her profile</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'
import echarts from 'echarts'

const defaultFormThead = ['expenseID','fundID','amount','operator',	'category1',	'category2',	'abstract',	'remark','applicationState']

export default {
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  methods:{
    handleButtonClick(row){
      window.open(row.link, "_blank");
    },
    initChart(){
      axios.get('http://localhost:9090//api/expenses/{expenseID}')
      .then(response => {
        this.chart = echarts.init(document.getElementById('chart-container'))
        for (let i = 0; i < 1; i++) {
          var tuple = {
              expenseID: response.data[i].info.expenseID,
              expenseName: response.data[i].info.expenseName,
              fundID: response.data[i].info.fundID,
              amount: response.data[i].info.amount,
              operator: response.data[i].info.operator,
              category1: response.data[i].info.category1,
              category2: response.data[i].info.category2,
              abstract: response.data[i].info.abstract,
              remark: response.data[i].info.remark,
              applicationState: response.data[i].info.applicationState,
          }
          // "expenseID": 1827328,
          //   "expenseName": "办公用品采购",
          //   "fundID": 9374829,
          //   "amount": 50,
          //   "operator": "沈昀",
          //   "category1": "会议费",
          //   "category2": "学术会议费",
          //   "abstract": "购买会议必需品",
          //   "remark": "请尽快审批",
          //   "applicationState": 1
          // eslint-disable-next-line
          this.tableData.push(tuple);
        }
        console.log(this.tableData)
      })
    }
  },
  data() {
    return {
      tableData: [
        // {
        //   name: 'fruit-1',
        //   apple: 'apple-10',
        //   banana: 'banana-10',
        //   orange: 'orange-10'
        // },
        // {
        //   name: 'fruit-2',
        //   apple: 'apple-20',
        //   banana: 'banana-20',
        //   orange: 'orange-20'
        // }
      ],
      key: 1, // table key
      formTheadOptions: ['经费编号','经费名称','课题组','经办人',	'支出类别一级',	'支出类别二级',	'内容摘要',	'支出金额（元）'],
      checkboxVal: defaultFormThead, // checkboxVal
      formThead: defaultFormThead // 默认表头 Default header
    }
  },
  watch: {
    checkboxVal(valArr) {
      this.formThead = this.formTheadOptions.filter(i => valArr.indexOf(i) >= 0)
      this.key = this.key + 1// 为了保证table 每次都会重渲 In order to ensure the table will be re-rendered each time
    }
  }
}
</script>

