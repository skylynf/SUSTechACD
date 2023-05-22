<template> <div>
  <div class="container">
    <div id="chart-container"/>
    <div id="pie-container"/>
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
  name: 'FrequentlyDiscussedClasses',
  data() {
    return {
      tableData: [

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
      axios.get('http://localhost:9090/FrequentlyDiscussedClasses')
      .then(response => {
        var keywords = []
        var piewords = []
        this.chart = echarts.init(document.getElementById('chart-container'))
        keywords = response.data
        piewords = keywords
        this.tableData = keywords
        var option = {
          title: {
            text: 'Frequent Discussed Classes \nWordCloud',
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
            sizeRange: [30,90],
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
            text: 'Frequent Discussed Classes\n Pie Chart',
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
              name: 'Frequent classes',
              type: 'pie',
              radius: [20, 180],
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

</style>
