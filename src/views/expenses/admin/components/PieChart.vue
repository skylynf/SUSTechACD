<template>
  <div class="app-container">
    <div class="filter-container">
      <div style="margin:0 0 5px 20px">
        <div style="margin: 20px;">删除支出（ExpenseID）</div>
        <input type="text"  ref="queryexpenseID">
        <el-button type=“button” @click="changeChart">删除支出</el-button>
      </div>
    </div>
    <!--经费编号	经费名称	课题组	经办人	支出类别一级	支出类别二级	内容摘要	支出金额（元）-->

  </div>
</template>

<script>
  import axios from 'axios'
  // import echarts from 'echarts'

  // document.getElementById("button1").addEventListener("click", changeChart);
  export default {
    mounted() {
    },
    methods:{
      changeChart(){
        var ID=this.$refs.queryexpenseID.value;
        // var ID='1827328'
        var url='http://127.0.0.1:5000/api/expenses/delete/'+ID;

        axios.delete(url).then(response => {
           console.log(response.data)
        })
        .catch(error => {
          const errorMessage = error.response.data.error;
          alert(errorMessage);
        });
      }
    },
    data() {
      return {
      }
    },
  }

</script>







<!-- <template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
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
      this.chart = echarts.init(this.$el, 'macarons')

      this.chart.setOption({
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          left: 'center',
          bottom: '10',
          data: ['Industries', 'Technology', 'Forex', 'Gold', 'Forecasts']
        },
        series: [
          {
            name: 'WEEKLY WRITE ARTICLES',
            type: 'pie',
            roseType: 'radius',
            radius: [15, 95],
            center: ['50%', '38%'],
            data: [
              { value: 320, name: 'Industries' },
              { value: 240, name: 'Technology' },
              { value: 149, name: 'Forex' },
              { value: 100, name: 'Gold' },
              { value: 59, name: 'Forecasts' }
            ],
            animationEasing: 'cubicInOut',
            animationDuration: 2600
          }
        ]
      })
    }
  }
}
</script> -->
