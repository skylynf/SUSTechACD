<template>
  <div class="app-container">
    <div class="filter-container">
      <div style="margin:0 0 5px 20px">
<!--        <input type="text"  ref="queryexpenseID">-->
        <el-button type=“button” @click="changeChart">查询未审批支出</el-button>

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
<!--        <el-checkbox label="approve">-->
<!--          <el-button type=“button” @click="changeChart">查询未审批支出</el-button>-->
<!--          <el-button type=“button” @click="changeChart">查询未审批支出</el-button>-->
<!--        </el-checkbox>-->
      </el-checkbox-group>
    </div>
    <!--经费编号	经费名称	课题组	经办人	支出类别一级	支出类别二级	内容摘要	支出金额（元）-->
    <el-table id="www" :key="key" :data="tableData" border fit highlight-current-row style="width: 100%">
      <el-table-column v-for="fruit in formThead" :key="fruit" :label="fruit">
        <template slot-scope="scope">
          {{ scope.row[fruit] }}
        </template>
      </el-table-column>
      <el-table-column >
        <template slot-scope="scope">
          <el-button type=“button” @click="approve(scope.row)">批准</el-button>
          <el-button type=“button” @click="reject(scope.row)">拒绝</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'
import * as echarts from 'echarts'

const defaultFormThead = ['expenseID', 'expenseName', 'fundID', 'amount', 'operator', 'category1', 'category2', 'abstract', 'remark', 'applicationState']

export default {
  mounted() {

  },
  methods: {
    initChart() {
      console.log(this.tableData)
    },
    approve(e){
      var url='http://127.0.0.1:5000/api/users/'+e.expenseID+'/accept';
      console.log((e.expenseID))
      axios.post(url)
      .then(res => {
        alert('批准成功！');
      })
      .catch(error => {
          const errorMessage = error.response.data.error;
          alert(errorMessage);
        });
    },
    reject(e){
      var url='http://127.0.0.1:5000/api/users/'+e.expenseID+'/reject';
      console.log((e.expenseID))
      axios.post(url)
      .then(res => {
        alert('拒绝成功！');
      })
      .catch(error => {
          const errorMessage = error.response.data.error;
          alert(errorMessage);
        });
    },
    changeChart() {
      var url = 'http://127.0.0.1:5000/api/expenses/pending' ;
      console.log("12345678")
      axios.get(url).then(response => {
        var result;
        result = response.data;
        console.log(result);
        this.tableData = [];

        // // if result is not iteratable
        // if (!result[Symbol.iterator]) {
        //   alert('not iteratable');
        // } else{
        //   alert('iteratable');
        // }


        result.forEach(item => {
          var tuple = {
            expenseID: item.expenseID,
            expenseName: item.expenseName,
            fundID: item.fundID,
            amount: item.amount,
            operator: item.operator,
            category1: item.category1,
            category2: item.category2,
            abstract: item.abstract,
            remark: item.remark,
            applicationState: item.applicationState,
            createDate: item.createDate
          }
          console.log(tuple.expenseID)
          this.tableData.push(tuple);
        });

        console.log(this.tableData)
        alert('查询成功！');
      })
      .catch(error => {
          const errorMessage = error.response.data.error;
          alert(errorMessage);
        });
    }
  },
  data() {
    return {
      tableData: [],
      key: 1,
      formTheadOptions: ['expenseID', 'expenseName', 'fundID', 'amount', 'operator', 'category1', 'category2', 'abstract', 'remark', 'applicationState'],
      checkboxVal: defaultFormThead,
      formThead: defaultFormThead
    }
  },
  watch: {
    checkboxVal(valArr) {
      this.formThead = this.formTheadOptions.filter(i => valArr.indexOf(i) >= 0)
      this.key = this.key + 1
    }
  }
}
</script>
