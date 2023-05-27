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
      <!--      <el-table-column label="操作">-->
      <!--        <template slot-scope="scope">-->
      <!--          &lt;!&ndash; 这里可以添加您自定义的按钮内容和行为 &ndash;&gt;-->
      <!--          <el-button type="primary" size="small" @click="handleButtonClick(scope.row)">Go to his/her profile</el-button>-->
      <!--        </template>-->
      <!--      </el-table-column>-->
    </el-table>
  </div>
</template>

<script>
  import axios from 'axios'
  // import echarts from 'echarts'
  import * as echarts from 'echarts'

  const defaultFormThead = ['expenseID','fundID','amount','operator',	'category1',	'category2',	'abstract',	'remark','applicationState']

  // document.getElementById("button1").addEventListener("click", changeChart);
  export default {
    mounted() {
      // this.$nextTick(() => {
      //   this.initChart()
      // })
    },
    methods:{
      initChart(){
          console.log(this.tableData)
      },
      changeChart(){
        // var ID=this.$refs.queryexpenseID.value;
        var url='http://127.0.0.1:5000/api/expenses/1827328';
        console.log("12345678")
        axios.get(url);
        console.log("wwwwww111")
        axios.get(url).then(response => {
           // this.chart = echarts.init(document.getElementById('www'))
          console.log("wwwwww")
          var tuple = {
            // expenseID: response.data.info.expenseID[0],
            // expenseName: response.data.info.expenseName[0],
            // fundID: response.data.info.fundID[0],
            // amount: response.data.info.amount[0],
            // operator: response.data.info.operator[0],
            // category1: response.data.info.category1[0],
            // category2: response.data[0].info,
            // abstract: response.data.info,
            // remark: response.data[0],
            // applicationState: response.data,
            expenseID: "r22222ID[0]",
            expenseName: "222232332me[0]",
            fundID:"www",
            amount: "www",
            operator: "www",
            category1: "www",
            category2: "www",
            abstract: "www",
            remark: "www",
            applicationState: "www"
          }
          this.tableData.push(tuple);

          console.log("87654321")
        })
      }
    },
    data() {
      return {
        tableData: [
          {
            expenseID: "response.data.info.expenseID[0]",
            expenseName: "response.data.info.expenseName[0]",
            fundID:"www",
            amount: "www",
            operator: "www",
            category1: "www",
            category2: "www",
            abstract: "www",
            remark: "www",
            applicationState: "www",
          }
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
        formTheadOptions: ['expenseID','fundID','amount','operator',	'category1',	'category2',	'abstract',	'remark','applicationState'],
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




<!--<template>-->
<!--  <div class="app-container">-->
<!--    <div class="filter-container">-->
<!--      <div style="margin:0 0 5px 20px">-->
<!--        <input type="text"  ref="queryexpenseID">-->
<!--        <button @click="changeChart">查询</button>-->

<!--      </div>-->
<!--      <el-checkbox-group v-model="checkboxVal">-->
<!--        <el-checkbox label="expenseID">-->
<!--          expenseID-->
<!--        </el-checkbox>-->
<!--        <el-checkbox label="fundID">-->
<!--          fundID-->
<!--        </el-checkbox>-->
<!--        <el-checkbox label="amount">-->
<!--          amount-->
<!--        </el-checkbox>-->
<!--        <el-checkbox label="operator">-->
<!--          operator-->
<!--        </el-checkbox>-->
<!--        <el-checkbox label="category1">-->
<!--          category1-->
<!--        </el-checkbox>-->
<!--        <el-checkbox label="category2">-->
<!--          category2-->
<!--        </el-checkbox>-->
<!--        <el-checkbox label="abstract">-->
<!--          abstract-->
<!--        </el-checkbox>-->
<!--        <el-checkbox label="remark">-->
<!--          remark-->
<!--        </el-checkbox>-->
<!--        <el-checkbox label="applicationState">-->
<!--          applicationState-->
<!--        </el-checkbox>-->

<!--      </el-checkbox-group>-->
<!--    </div>-->
<!--    &lt;!&ndash;经费编号	经费名称	课题组	经办人	支出类别一级	支出类别二级	内容摘要	支出金额（元）&ndash;&gt;-->
<!--    <el-table :key="key" :data="tableData" border fit highlight-current-row style="width: 100%">-->
<!--      <el-table-column v-for="fruit in formThead" :key="fruit" :label="fruit">-->
<!--        <template slot-scope="scope">-->
<!--          {{ scope.row[fruit] }}-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      &lt;!&ndash;      <el-table-column label="操作">&ndash;&gt;-->
<!--      &lt;!&ndash;        <template slot-scope="scope">&ndash;&gt;-->
<!--      &lt;!&ndash;          &lt;!&ndash; 这里可以添加您自定义的按钮内容和行为 &ndash;&gt;&ndash;&gt;-->
<!--      &lt;!&ndash;          <el-button type="primary" size="small" @click="handleButtonClick(scope.row)">Go to his/her profile</el-button>&ndash;&gt;-->
<!--      &lt;!&ndash;        </template>&ndash;&gt;-->
<!--      &lt;!&ndash;      </el-table-column>&ndash;&gt;-->
<!--    </el-table>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--  import axios from 'axios'-->
<!--  import echarts from 'echarts'-->

<!--  const defaultFormThead = ['expenseID','fundID','amount','operator',	'category1',	'category2',	'abstract',	'remark','applicationState']-->

<!--  // document.getElementById("button1").addEventListener("click", changeChart);-->
<!--  export default {-->
<!--    mounted() {-->
<!--      this.$nextTick(() => {-->
<!--        this.initChart()-->
<!--      })-->
<!--    },-->
<!--//-->
<!--//   changeChart(){-->
<!--//     // var ID=this.$refs.queryexpenseID.value;-->
<!--//     var url='http://localhost:9090//api/expenses/';-->
<!--//     axios.get(url)-->
<!--//     .then(response => {-->
<!--//       this.chart = echarts.init(document.getElementById('chart-container'))-->
<!--//       // for (let i = 0; i < 1; i++) {-->
<!--//       var tuple = {-->
<!--//         // expenseID: response.data[i].info.expenseID,-->
<!--//         // expenseName: response.data[i].info.expenseName,-->
<!--//         // fundID: response.data[i].info.fundID,-->
<!--//         // amount: response.data[i].info.amount,-->
<!--//         // operator: response.data[i].info.operator,-->
<!--//         // category1: response.data[i].info.category1,-->
<!--//         // category2: response.data[i].info.category2,-->
<!--//         // abstract: response.data[i].info.abstract,-->
<!--//         // remark: response.data[i].info.remark,-->
<!--//         // applicationState: response.data[i].info.applicationState,-->
<!--//         expenseID: 1,-->
<!--//         expenseName:2,-->
<!--//         fundID: 2,-->
<!--//         amount: 2,-->
<!--//         operator: 2,-->
<!--//         category1: 2,-->
<!--//         category2: 2,-->
<!--//         abstract: 2,-->
<!--//         remark: 3,-->
<!--//         applicationState:2,-->
<!--//       }-->
<!--//       this.tableData.push(tuple);-->
<!--//       // }-->
<!--//       console.log(this.tableData)-->
<!--//     })-->
<!--// },-->
<!--    methods:{-->
<!--      handleButtonClick(row){-->
<!--        window.open(row.link, "_blank");-->
<!--      },-->
<!--      changeChart(){-->
<!--        // var ID=this.$refs.queryexpenseID.value;-->
<!--        var url='http://localhost:9090//api/expenses/';-->
<!--        axios.get(url)-->
<!--        .then(response => {-->
<!--          this.chart = echarts.init(document.getElementById('chart-container'))-->
<!--          // for (let i = 0; i < 1; i++) {-->
<!--          var tuple = {-->
<!--            // expenseID: response.data[i].info.expenseID,-->
<!--            // expenseName: response.data[i].info.expenseName,-->
<!--            // fundID: response.data[i].info.fundID,-->
<!--            // amount: response.data[i].info.amount,-->
<!--            // operator: response.data[i].info.operator,-->
<!--            // category1: response.data[i].info.category1,-->
<!--            // category2: response.data[i].info.category2,-->
<!--            // abstract: response.data[i].info.abstract,-->
<!--            // remark: response.data[i].info.remark,-->
<!--            // applicationState: response.data[i].info.applicationState,-->
<!--            expenseID: 1,-->
<!--            expenseName:2,-->
<!--            fundID: 2,-->
<!--            amount: 2,-->
<!--            operator: 2,-->
<!--            category1: 2,-->
<!--            category2: 2,-->
<!--            abstract: 2,-->
<!--            remark: 3,-->
<!--            applicationState:2,-->
<!--          }-->
<!--          this.tableData.push(tuple);-->
<!--          // }-->
<!--          console.log(this.tableData)-->
<!--        })-->
<!--      }-->
<!--    },-->
<!--    data() {-->
<!--      return {-->
<!--        tableData: [-->
<!--          // {-->
<!--          //   name: 'fruit-1',-->
<!--          //   apple: 'apple-10',-->
<!--          //   banana: 'banana-10',-->
<!--          //   orange: 'orange-10'-->
<!--          // },-->
<!--          // {-->
<!--          //   name: 'fruit-2',-->
<!--          //   apple: 'apple-20',-->
<!--          //   banana: 'banana-20',-->
<!--          //   orange: 'orange-20'-->
<!--          // }-->
<!--        ],-->
<!--        key: 1, // table key-->
<!--        formTheadOptions: ['expenseID','fundID','amount','operator',	'category1',	'category2',	'abstract',	'remark','applicationState'],-->
<!--        checkboxVal: defaultFormThead, // checkboxVal-->
<!--        formThead: defaultFormThead // 默认表头 Default header-->
<!--      }-->
<!--    },-->
<!--    watch: {-->
<!--      checkboxVal(valArr) {-->
<!--        this.formThead = this.formTheadOptions.filter(i => valArr.indexOf(i) >= 0)-->
<!--        this.key = this.key + 1// 为了保证table 每次都会重渲 In order to ensure the table will be re-rendered each time-->
<!--      }-->
<!--    }-->

<!--  }-->

<!--</script>-->

