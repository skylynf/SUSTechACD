<template>
  <div id="chart-container" />
</template>

/* eslint-disable */
<script>
import echarts from 'echarts'
import 'echarts-wordcloud'
import axios from 'axios'

export default {
  name: 'ActiveUserCloud',
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
      axios.get('http://localhost:9090/MostActiveUsers')
        .then(response => {
          var keywords = []
          this.chart = echarts.init(document.getElementById('chart-container'))
          for (let i = 0; i < 10; i++) {
            var tuple = {
              value: response.data[i].count,
              name: response.data[i].info.display_name
            }
            // eslint-disable-next-line
            keywords.push(tuple);
          }
          console.log(keywords)
          console.log(response.data)
          var option = {
            title: {
              text: 'Active Users in Threads',
              textStyle: {
                fontStyle: 'oblique',
                fontSize: 20,
                color: '#201e65'
              },
              left: 'center',
              top: '0%' // 调整标题的位置，这里设置为距离顶部的百分比
            },
            tooltip: {},
            series: [{
              type: 'wordCloud',
              shape: {
                cloudGrow: 0.2
              },
              sizeRange: [10, 90],
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
          console.log(this.chart)
        })
        .catch(errorMostActiveUsers => {
          console.log('ERROR in MostActiveUsers')
        })
    }
  }
}
</script>
<style scoped>
#chart-container {
  height: 800px;
  width: 100%;
}
</style>
