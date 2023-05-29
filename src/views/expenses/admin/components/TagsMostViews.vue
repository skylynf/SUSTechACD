<template>
  <div class="app-container">
    <div class="filter-container">
      <div style="margin:0 0 5px 20px">
        <div style="margin: 20px;">送审支出（ExpenseID）</div>
        <input type="text" placeholder="expenseID"  ref="expenseID">
        <el-button type=“button” @click="changeChart">送审</el-button>
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
        var ID=this.$refs.expenseID.value;
        // var ID='1827328'
        var url='http://127.0.0.1:5000/api/expenses/submit/'+ID;

        axios.post(url).then(response => {
           console.log(response.data);
           alert(response.data['message']);
        })
        .then(res => {
          alert('送审成功！');
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
  <div>
  <div class="container">
    <div id="chart-container" />
    <div id="pie-container" />
  </div>
    <div style="margin:0 0 5px 20px">
      Top 20 tags with most views
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
  name: 'TagsMostViews',
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
      axios.get('http://localhost:9090/MostViewedTags')
      .then(response => {
        var keywords = []
        var piewords = []
        this.chart = echarts.init(document.getElementById('chart-container'))
        keywords = response.data
        piewords = keywords
        this.tableData = keywords
        var option = {
          title: {
            text: 'Tags with the \n most views WordCloud',
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
            sizeRange: [20, 60],
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
            text: 'Tags with the \n most views Pie',
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
              name: 'Tags with most views',
              type: 'pie',
              radius: [100,180],
              center: ['50%', '50%'],
              roseType: 'radius',
              itemStyle: {
                borderRadius: 50
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
