<template>
  <div class="app-container">
    <div class="filter-container">
      <div style="margin:0 0 5px 20px">
        <input type="text"  ref="queryexpenseID">
        <el-button type=“button” @click="changeChart">查询</el-button>

      </div>
      <el-checkbox-group v-model="checkboxVal">
        <el-checkbox label="expenseID">
          expenseID
        </el-checkbox>
        <el-checkbox label="expenseName">
          expenseName
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
    <el-table id="www" :key="key" :data="tableData" border fit highlight-current-row style="width: 100%">
      <el-table-column v-for="fruit in formThead" :key="fruit" :label="fruit">
        <template slot-scope="scope">
          {{ scope.row[fruit] }}
        </template>
      </el-table-column>

    </el-table>
  </div>
</template>

<script>
  import axios from 'axios'
  // import echarts from 'echarts'
  import * as echarts from 'echarts'

  const defaultFormThead = ['expenseID','expenseName','fundID','amount','operator',	'category1',	'category2',	'abstract',	'remark','applicationState']

  // document.getElementById("button1").addEventListener("click", changeChart);
  export default {
    mounted() {

    },
    methods:{
      initChart(){
          console.log(this.tableData)
      },
      changeChart(){
        var ID=this.$refs.queryexpenseID.value;
        // var ID='1827328'
        var url='http://127.0.0.1:5000/api/expenses/'+ID;
        console.log("12345678")
        axios.get(url);
        console.log("wwwwww111")
        axios.get(url).then(response => {
           // this.chart = echarts.init(document.getElementById('www'))

          var result = JSON.parse(response.data);
          console.log(result)
          this.tableData=[];
          // var x=result.expenseID.key;
          // console.log(x)
          
          var tuple = {
            expenseID: result.expenseID,
            expenseName: result.expenseName,
            fundID: result.fundID,
            amount: result.amount,
            operator: result.operator,
            category1: result.category1,
            category2: result.category2,
            abstract: result.abstract,
            remark: result.remark,
            applicationState: result.applicationState,
          }
          console.log(tuple.expenseID)
          if(tuple.expenseID!==undefined)
          this.tableData.push(tuple);
          


          console.log(this.tableData)
        })
      }
    },
    data() {
      return {
        tableData: [

        ],
        key: 1, // table key
        formTheadOptions: ['expenseID','expenseName','fundID','amount','operator',	'category1',	'category2',	'abstract',	'remark','applicationState'],
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
