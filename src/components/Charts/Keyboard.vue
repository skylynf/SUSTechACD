<template>
  <div :id="id" :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
import resize from './mixins/resize'
import axios from 'axios'

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    id: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '200px'
    },
    height: {
      type: String,
      default: '200px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.initChart()
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      axios.get('http://localhost:9090/QuestionResolutionTimeDistribution')
        .then(response => {
          var data = []
          data = response.data
          console.log(data)
          this.chart = echarts.init(document.getElementById(this.id))
          const xAxisData = []
          const data2 = []
          for (let i = 0; i < 18; i++) {
            xAxisData.push(data[i][0])
            data2.push(data[i][1])
          }
          this.chart.setOption({
            title: {
              text: 'Distribution of question resolution time ',
              textStyle: {
                fontStyle: 'oblique',
                fontSize: 40,
                color: '#f8f8ff'
              },
              left: 'center',
              top: '5%' // 调整标题的位置，这里设置为距离顶部的百分比
            },
            backgroundColor: '#08263a',
            grid: {
              left: '5%',
              right: '5%'
            },
            xAxis: [{
              show: true,
              data: xAxisData,
              name: 'resolution\ntime',
              nameTextStyle: {
                //y轴上方单位的颜色
                color: "#fff",
              },
              axisLabel: {
                textStyle: {
                  color: '#fff'
                }
              },
            }, {
              show: false,
              data: xAxisData,

            }],
            visualMap: {
              show: true,
              min: 0,
              max: 50,
              dimension: 0,
              inRange: {
                color: ['#4a657a', '#308e92', '#b1cfa5', '#f5d69f', '#f5898b', '#ef5055']
              }
            },
            yAxis: {
              name: 'question count',
              nameTextStyle: {
                //y轴上方单位的颜色
                color: "#fff",
              },
              axisLine: {
                show: true
              },
              axisLabel: {
                textStyle: {
                  color: '#fff'
                }
              },
              splitLine: {
                show: true,
                lineStyle: {
                  color: '#08263f'
                }
              },
              axisTick: {
                show: false
              }
            },
            series: [{
              name: 'back',
              type: 'bar',
              data: data2,
              z: 1,
              itemStyle: {
                normal: {
                  opacity: 0.4,
                  barBorderRadius: 5,
                  shadowBlur: 3,
                  shadowColor: '#111'
                }
              }
            }, {
              name: 'Simulate Shadow',
              type: 'line',
              data,
              z: 2,
              showSymbol: false,
              animationDelay: 0,
              animationEasing: 'linear',
              animationDuration: 1200,
              lineStyle: {
                normal: {
                  color: 'transparent'
                }
              },
              areaStyle: {
                normal: {
                  color: '#08263a',
                  shadowBlur: 50,
                  shadowColor: '#000'
                }
              }
            }, {
              name: 'front',
              type: 'bar',
              data,
              xAxisIndex: 1,
              z: 3,
              itemStyle: {
                normal: {
                  barBorderRadius: 5
                }
              }
            }],
            animationEasing: 'elasticOut',
            animationEasingUpdate: 'elasticOut',
            animationDelay(idx) {
              return idx * 20
            },
            animationDelayUpdate(idx) {
              return idx * 20
            }
          })
        })
        .catch(errorQuestionResolutionTimeDistribution => {
          console.log('ERROR in QuestionResolutionTimeDistribution')
        })
    }
  }
}
</script>
