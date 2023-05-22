<template>
  <div>
  <div class="container">
     <div id="chart-container" />
      <div id="pie-container" />

  </div>
    <div style="margin:0 0 5px 20px">
      Single tags among top 20
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
    <div style="margin:0 0 5px 20px">
      Combination tags among top 20
    </div>
    <div class="app-container">
      <el-table :key="key2" :data="combination" border fit highlight-current-row style="width: 100%">
        <el-table-column v-for="fruit in formThead2" :key="fruit" :label="fruit">
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
const defaultFormThead = ['tag', 'value']
const defaultFormThead2 = ['tag1','tag2', 'value']
export default {
  name: 'TagsMostUpvotes',
  data() {
    return {
      tableData: [

      ],
      combination:[],
      key: 1, // table key
      key2:1,
      checkboxVal: defaultFormThead, // checkboxVal
      formThead: defaultFormThead, // 默认表头 Default header
      formThead2:defaultFormThead2,
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
      axios.get('http://localhost:9090/MostUpvotedTags')
        .then(response => {
          var keywords = []
          var piewords = []
          this.chart = echarts.init(document.getElementById('chart-container'))
          keywords = response.data
          // this.tableData = keywords
          for (let i = 0; i < 20; i++) {
            // console.log(keywords[i].name.charAt(0)=='[')
              if (keywords[i].name.charAt(0)=='[') {
                var tuple1 = {
                  tag1:keywords[i].name.slice(1, -1).split(',')[0],
                  tag2:keywords[i].name.slice(1, -1).split(',')[1],
                  value:keywords[i].value
                }
                // eslint-disable-next-line
                this.combination.push(tuple1);
              } else {
                var tuple2 = {
                  tag:keywords[i].name,
                  value:keywords[i].value
                }
                // eslint-disable-next-line
                this.tableData.push(tuple2);
              }

          }

          piewords = keywords
          var option = {
            title: {
              text: 'Tags with the \n most upvotes WordCloud',
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
              sizeRange: [10, 60],
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
              text: 'Tags with the \n most upvotes Pie',
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
                name: 'Tags with most upvotes',
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


</style>
