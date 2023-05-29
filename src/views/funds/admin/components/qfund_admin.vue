<template>
  <div class="app-container">
    <div class="filter-container">
      <div style="margin:0 0 5px 20px">
        <input type="text" placeholder="fundID"  ref="queryexpenseID">
        <el-button type=“button” @click="changeChart">查询</el-button>

      </div>
      <el-checkbox-group v-model="checkboxVal">
        <el-checkbox label="fundID">
          fundID
        </el-checkbox>
        <el-checkbox label="fundName">
          fundName
        </el-checkbox>
        <el-checkbox label="userID">
          userID
        </el-checkbox>
        <el-checkbox label="totalQuota">
          totalQuota
        </el-checkbox>
        <el-checkbox label="usedQuota">
          usedQuota
        </el-checkbox>
        <el-checkbox label="implementationRate">
          implementationRate
        </el-checkbox>
        <el-checkbox label="abstract">
          abstract
        </el-checkbox>
        <el-checkbox label="remark">
          remark
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
  import * as echarts from 'echarts'

  const defaultFormThead = ['fundID', 'fundName', 'userID', 'totalQuota', 'usedQuota','implementationRate', 'abstract',  'remark']

  export default {
    mounted() {

    },
    methods: {
      initChart() {
        console.log(this.tableData)
      },
      changeChart() {
        var ID = this.$refs.queryexpenseID.value;
        var url =  'http://127.0.0.1:5000/api/funds/' + ID ;//: 'http://127.0.0.1:5000/api/expenses/findAll';
        console.log("12345678")
        axios.get(url).then(response => {
          var result;
          // if(ID){
          console.log(response.data['items'])


          result = response.data['items'];//[0]['fund']);
          // }else{
          //   result = response.data;
          // }
          console.log(result)
          this.tableData = [];

          result.forEach(item => {
            var fun=item;
            var tuple = {
              fundID: fun['fundID'],
              fundName: fun['fundName'],
              userID: fun['userID'],
              totalQuota:fun['totalQuota'],
              usedQuota: fun['usedQuota'],
              abstract: fun['abstract'],
              remark: fun['remark'],
              implementationRate:fun['usedQuota']/fun['totalQuota'],
            }

            console.log(tuple.fundID)
            this.tableData.push(tuple);
          });

          console.log(this.tableData)
        })
      }
    },
    data() {
      return {
        tableData: [],
        key: 1,
        formTheadOptions: ['fundID', 'fundName', 'userID', 'totalQuota', 'usedQuota','implementationRate', 'abstract', 'remark'],
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
<!--"fund_id": 5433912,-->
<!--"fund_name": "国自然",-->
<!--"user_id": 012,-->
<!--"total_quota": 500,-->
<!--"used_quota": 10,-->
<!--"abstract": "this is a abstract",-->
<!--"remark": "no remark"-->
