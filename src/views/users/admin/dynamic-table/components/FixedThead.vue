<template>
  <div class="app-container">
    <div class="filter-container">
<!--      'name', 'id', 'reputation','link','profile image','participation'-->
      <el-checkbox-group v-model="checkboxVal">
        <el-checkbox label="name">
          name
        </el-checkbox>
        <el-checkbox label="id">
          id
        </el-checkbox>
        <el-checkbox label="reputation">
          reputation
        </el-checkbox>
        <el-checkbox label="link">
          link
        </el-checkbox>
        <el-checkbox label="participation">
          participation
        </el-checkbox>
      </el-checkbox-group>
    </div>

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

const defaultFormThead = ['name', 'participation']

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
      axios.get('http://localhost:9090/MostActiveUsers')
      .then(response => {
        this.chart = echarts.init(document.getElementById('chart-container'))
        for (let i = 0; i < 10; i++) {
          var tuple = {
            name: response.data[i].info.display_name,
            id:response.data[i].info.user_id,
            reputation:response.data[i].info.reputation,
            link:response.data[i].info.link,
            image:response.data[i].info.profile_image,
            participation: response.data[i].count,
          }
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
      formTheadOptions: ['name', 'id', 'reputation','link','image','participation'],
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

