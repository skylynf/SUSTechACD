<template>
  <div class="app-container">
    <div class="filter-container">
      <div style="margin:0 0 5px 20px">
        <input type="text"  ref="queryexpenseID">
        <el-button type=“button” @click="changeChart">查询</el-button>

      </div>
      <el-checkbox-group v-model="checkboxVal">
        <el-checkbox label="fund_id">
          fund_id
        </el-checkbox>
        <el-checkbox label="fund_name">
          fund_name
        </el-checkbox>
        <el-checkbox label="user_id">
          user_id
        </el-checkbox>
        <el-checkbox label="total_quota">
          total_quota
        </el-checkbox>
        <el-checkbox label="used_quota">
          used_quota
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

  const defaultFormThead = ['fund_id', 'fund_name', 'user_id', 'total_quota', 'used_quota', 'abstract',  'remark']

  export default {
    mounted() {

    },
    methods: {
      initChart() {
        console.log(this.tableData)
      },
      changeChart() {
        var ID = this.$refs.queryexpenseID.value;
        // /api/users/{userID}/funds
        var url =  'http://127.0.0.1:5000/api/users/' + ID+'/funds' ;//: 'http://127.0.0.1:5000/api/expenses/findAll';
        console.log("12345678")
        axios.get(url).then(response => {
          var result;
          // if(ID){
          console.log(response.data['items'][0])
          result = JSON.parse(response.data);
          // }else{
          //   result = response.data;
          // }
          // console.log(result.items)
          this.tableData = [];

          result["items"][0]['fund'].forEach(item => {
            var tuple = {
              fund_id: item.fund_id,
              fund_name: item.fund_name,
              user_id: item.user_id,
              total_quota: item.total_quota,
              used_quota: item.used_quota,
              abstract: item.abstract,
              remark: item.remark,
            }
            console.log(tuple.expenseID)
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
        formTheadOptions: ['fund_id', 'fund_name', 'user_id', 'total_quota', 'used_quota', 'abstract', 'category2', 'abstract', 'remark'],
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
