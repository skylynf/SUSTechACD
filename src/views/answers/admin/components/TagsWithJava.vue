<template>
  <el-form ref="form" :model="form" label-width="180px">
    <div style="margin: 20px;">修改一个支出并重新送审</div>
    <el-form-item label="支出编号">
      <el-input v-model="form.expenseID"></el-input>
    </el-form-item>
    <el-form-item label="支出名称">
      <el-input v-model="form.expenseName"></el-input>
    </el-form-item>
    <el-form-item label="该支出对应的经费号">
      <el-input v-model="form.fundID"></el-input>
    </el-form-item>
    <el-form-item label="支出额度">
      <el-input v-model="form.amount"></el-input>
    </el-form-item>
    <el-form-item label="经办人">
      <el-input v-model="form.operator"></el-input>
    </el-form-item>
    <el-form-item label="支出类别一级">
      <el-input v-model="form.category1"></el-input>
    </el-form-item>
    <el-form-item label="支出类别二级">
      <el-input v-model="form.category2"></el-input>
    </el-form-item>
    <el-form-item label="内容摘要">
      <el-input v-model="form.abstract"></el-input>
    </el-form-item>
    <el-form-item label="备注">
      <el-input v-model="form.remark"></el-input>
    </el-form-item>
    <el-form-item label="申请状态">
      <el-input v-model="form.applicationState"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">立即创建</el-button>
    </el-form-item>
  </el-form>
</template>


<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        form: {
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
        }
      }
    },
    methods: {
      onSubmit() {
        var url = 'http://127.0.0.1:5000/api/expenses/modify/'+this.form.expenseID;
        console.log('submit!');
        axios.put(url, this.form)
        .then(response => {
          console.log(response.data)
        })
        .catch(function (error) { // 请求失败处理
            console.log(error);
          });
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
