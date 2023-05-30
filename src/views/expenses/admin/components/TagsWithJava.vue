<template>
  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="180px" class="demo-ruleForm">
    <el-form-item label="支出编号" prop="expenseID">
      <el-input v-model="ruleForm.expenseID"></el-input>
    </el-form-item>
    <el-form-item label="支出名称" prop="expenseName">
      <el-input v-model="ruleForm.expenseName"></el-input>
    </el-form-item>
    <el-form-item label="经费号" prop="fundID">
      <el-input v-model="ruleForm.fundID"></el-input>
    </el-form-item>
    <el-form-item label="支出额度" prop="amount">
      <el-input v-model="ruleForm.amount"></el-input>
    </el-form-item>
    <el-form-item label="经办人" prop="operator">
      <el-input v-model="ruleForm.operator"></el-input>
    </el-form-item>
    <el-form-item label="支出类别一级" prop="category1">
      <el-select v-model="ruleForm.category1" >
        <el-option label="办公费" value="办公费"></el-option>
        <el-option label="办公设备配置" value="办公设备配置"></el-option>
        <el-option label="差旅费" value="差旅费"></el-option>
        <el-option label="电费" value="电费"></el-option>
        <el-option label="工会经费" value="工会经费"></el-option>
        <el-option label="会议费" value="会议费"></el-option>
        <el-option label="奖励金" value="奖励金"></el-option>
        <el-option label="劳务费" value="劳务费"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="支出类别二级" prop="category2">
      <el-select v-model="ruleForm.category2" >
        <el-option label="培训费" value="培训费"></el-option>
        <el-option label="其他" value="其他"></el-option>
        <el-option label="其他交通费用" value="其他交通费用"></el-option>
        <el-option label="其他资本性支出" value="其他资本性支出"></el-option>
        <el-option label="水费" value="水费"></el-option>
        <el-option label="维修（护）费" value="维修（护）费"></el-option>
        <el-option label="委托业务" value="委托业务"></el-option>
        <el-option label="无形资产" value="无形资产"></el-option>
        <el-option label="信息网络构建" value="信息网络构建"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="摘要" prop="abstract">
      <el-input type="textarea" v-model="ruleForm.abstract"></el-input>
    </el-form-item>
    <el-form-item label="备注" prop="remark">
      <el-input type="textarea" v-model="ruleForm.remark"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit()">修改</el-button>
    </el-form-item>
  </el-form>
</template>


<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        ruleForm: {
          expenseID: '',
          expenseName: '',
          fundID: '',
          amount: '',
          operator: '',
          category1: '',
          category2: '',
          abstract: '',
          remark: '',
          applicationState: ''
        },
        rules: {
          expenseID: [
            { required: true },
          ],
          expenseName: [
            { required: true },
          ],
          fundID: [
            { required: true },
          ],
          amount: [
            { required: true },
          ],
          operator: [
            { required: true },
          ],
          category1: [
            { required: true },
          ],
          category2: [
            { required: true },
          ],
          abstract: [
            { required: true },
          ],
          remark: [
            { required: true },
          ]
        }
      }
    },
    methods: {
      onSubmit() {
        var url = 'http://127.0.0.1:5000/api/expenses/modify/'+this.ruleForm.expenseID;
        console.log('submit!');
        axios.put(url, this.ruleForm)
        .then(response => {
          console.log(response.data)
          alert('修改成功！');
        })
      }
    }
  }
</script>












<!-- <template>
  <div>
  <div class="container">
    <div id="chart-container" />
    <div id="pie-container" />
  </div>
    <div style="margin:0 0 5px 20px">
      Top 20 tags with Java
    </div>
    <div class="app-container">
      <el-table :key="key" :data="tableData" border fit highlight-current-row style="width: 100%">
        <el-table-column v-for="fruit in formThead" :key="fruit" :label="fruit">
          <template slot-scope="scope">
            {{ scope.row[fruit] }}
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import echarts from 'echarts'
import 'echarts-wordcloud'
import axios from 'axios'
const defaultFormThead = ['name', 'value']
export default {
  name: 'TagsWithJava',
  data() {
    return {  tableData: [

      ],
      key: 1, // table key
      checkboxVal: defaultFormThead, // checkboxVal
      formThead: defaultFormThead, // 默认表头 Default header
      chart: null,
      pieChart: null
    }
  },
  mounted() {
    this.initChart()
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    if (!this.pieChart) {
      return
    }
    this.chart.dispose()
    this.chart = null
    this.pieChart.dispose()
    this.pieChart = null
  },
  methods: {
    initChart() {
      axios.get('http://localhost:9090/FrequentlyCooccurringTags')
      .then(response => {
        var keywords = []
        var piewords = []
        this.chart = echarts.init(document.getElementById('chart-container'))
        keywords = response.data
        piewords = keywords
        this.tableData = keywords
        var option = {
          title: {
            text: 'Tags frequently show with \n Java WordCloud',
            textStyle: {
              fontStyle: 'oblique',
              fontSize: 40,
              color: '#201e65'
            },
            left: 'center',
            top: '5%' // 调整标题的位置，这里设置为距离顶部的百分比
          },
          tooltip: {},
          toolbox: {
            show: true,
            feature: {
              mark: { show: true },
              dataView: { show: true, readOnly: false },
              restore: { show: true },
              saveAsImage: { show: true }
            }
          },
          series: [{
            type: 'wordCloud',
            shape: {
              cloudGrow: 0.2
            },
            sizeRange: [30, 60],
            rotationRange: [-30, 30],
            gridSize: 2,
            drawOutOfBound: false,
            layoutAnimation: true,
            keepAspect: true,
            textStyle: {
              fontWeight: 'bold',
              color: function() {
                return 'rgb(' + [
                  Math.round(Math.random() * 160),
                  Math.round(Math.random() * 160),
                  Math.round(Math.random() * 160)
                ].join(',') + ')'
              }
            },
            emphasis: {
              textStyle: {
                shadowBlur: 15,
                shadowColor: '#333'
              }
            },
            data: keywords
          }]
        }
        this.chart.setOption(option)

        this.pieChart = echarts.init(document.getElementById('pie-container'))
        var pieOption = {
          title: {
            text: 'Tags frequently show with \n Java Pie',
            textStyle: {
              fontStyle: 'oblique',
              fontSize: 40,
              color: '#201e65'
            },
            left: 'center',
            top: '5%' // 调整标题的位置，这里设置为距离顶部的百分比
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          legend: {
            right: 'center',
            top: 'bottom',
            data: [
              'rose1',
              'rose2',
              'rose3',
              'rose4',
              'rose5',
              'rose6',
              'rose7',
              'rose8'
            ]
          },
          toolbox: {
            show: true,
            feature: {
              mark: { show: true },
              dataView: { show: true, readOnly: false },
              restore: { show: true },
              saveAsImage: { show: true }
            }
          },
          series: [
            {
              name: 'Tags frequently show with java',
              type: 'pie',
              radius: [100,180],
              center: ['50%', '50%'],
              roseType: 'radius',
              itemStyle: {
                borderRadius: 10
              },
              emphasis: {
                label: {
                  show: true
                }
              },
              data: piewords
            }]
        }
        this.pieChart.setOption(pieOption)
      })
      .catch(errorMostUpvotedTags => {
        console.log('ERROR in MostUpvotedTags')
      })
    }
  }
}
</script>
<style scoped>
.container {
  display: flex;
}

#chart-container {
  height: 800px;
  width: 50%;
}

#pie-container {
  height: 800px;
  width: 50%;
}

</style> -->
