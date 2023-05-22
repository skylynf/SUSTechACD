/* eslint-disable */
<template>
  <div class="dashboard-editor-container">

    <panel-group @handleSetLineChartData="handleSetLineChartData" />

    <!--    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">-->
    <!--      <line-chart :chart-data="lineChartData" />-->
    <!--    </el-row>-->

    <div class="chart-container">
      <chart height="70%" width="100%" />
    </div>

    <!--    <el-row :gutter="32">-->
    <!--      <el-col :xs="24" :sm="24" :lg="8">-->
    <!--        <div class="chart-wrapper">-->
    <!--          <raddar-chart />-->
    <!--        </div>-->
    <!--      </el-col>-->
    <!--      <el-col :xs="24" :sm="24" :lg="8">-->
    <!--        <div class="chart-wrapper">-->
    <!--          <pie-chart />-->
    <!--        </div>-->
    <!--      </el-col>-->
    <!--      <el-col :xs="24" :sm="24" :lg="8">-->
    <!--        <div class="chart-wrapper">-->
    <!--          <bar-chart />-->
    <!--        </div>-->
    <!--      </el-col>-->
    <!--    </el-row>-->
  </div>
</template>
/* eslint-disable */
<script>

import PanelGroup from './components/PanelGroup'
// import LineChart from './components/LineChart'
import Chart from '@/components/Charts/Keyboard'
// import RaddarChart from './components/RaddarChart'
// import PieChart from './components/PieChart'
// import BarChart from './components/BarChart'
import axios from 'axios'

const lineChartData = {
  answers_distribution: {
    actualData: [1, 2, 3, 4, 5, 5, 6, 7]
  }
}

export default {
  name: 'DashboardAdmin',
  components: {
    // GithubCorner,
    PanelGroup,
    // LineChart,
    Chart
    // RaddarChart
    // PieChart,
    // BarChart
  },
  data() {
    return {
      lineChartData: null
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      axios.get('http://localhost:9090/AnswerDistribution')
        .then(response => {
          lineChartData.answers_distribution.actualData[0] = response.data[0]
          lineChartData.answers_distribution.actualData[1] = response.data[1]
          lineChartData.answers_distribution.actualData[2] = response.data[2]
          lineChartData.answers_distribution.actualData[3] = response.data[3]
          lineChartData.answers_distribution.actualData[4] = response.data[4]
          lineChartData.answers_distribution.actualData[5] = response.data[5]
          lineChartData.answers_distribution.actualData[6] = response.data[6]
          lineChartData.answers_distribution.actualData[7] = response.data['7+']
          console.log(lineChartData.answers_distribution)
          this.lineChartData = lineChartData.answers_distribution
        })
        .catch(errorAnswerDistribution => {
          console.log('ERROR in AnswerDistribution')
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.chart-container{
  position: relative;
  width: 100%;
  height: calc(100vh - 84px);
}

.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }

  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
