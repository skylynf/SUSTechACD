<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'
import axios from 'axios'

const animationDuration = 6000

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '600px'
    },
    height: {
      type: String,
      default: '300px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
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

      axios.get('http://localhost:9090/SingleQuestionUserDistributionGraph')
      .then(response => {
        const xAxisData = []
        const yAxisData  = []
        var data =[]
        data = response.data
        for (let i = 0; i < 5; i++) {
          xAxisData.push(data[i][0])
          yAxisData.push(data[i][1])
        }
        this.chart = echarts.init(this.$el, 'macarons')
        this.chart.setOption({
          title: {
            text: 'Bar chart of Percentage(Comment/Answer) in questions',
            textStyle: {
              fontStyle: 'oblique',
              fontSize: 20,
              color: '#201e65'
            },
            left: 'center',
            top: '0%' // 调整标题的位置，这里设置为距离顶部的百分比
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: { // 坐标轴指示器，坐标轴触发有效
              type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
            }
          },
          grid: {
            top: 10,
            left: '2%',
            right: '2%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: [{
            type: 'category',
            data: xAxisData,
            axisTick: {
              alignWithLabel: true
            },
            axisLabel:{
              show:true,
              interval:0
            }
          }],
          yAxis: [{
            type: 'value',
            axisTick: {
              show: false
            }
          }],
          series: [{
            name: 'pageA',
            type: 'bar',
            stack: 'vistors',
            barWidth: '60%',
            data: yAxisData,
            animationDuration
          }]
        })
      })

    }
  }
}
</script>
