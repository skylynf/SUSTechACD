<template>
  <div class="dashboard-editor-container">

    <panel-group @handleSetLineChartData="handleSetLineChartData" />

    <el-row style="background:#fff;padding:16px 32px 0;margin-bottom:32px;">
      <el-col :xs="24" :sm="24" :lg="10">
        <div class="chart-wrapper">
          <pie-chart />
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="chart-wrapper">
          <BarChart></BarChart>
        </div>
      </el-col>

    </el-row>
    <el-row style="background:#fff;padding:16px 32px 0;margin-bottom:32px;">
      <el-col :xs="24" :sm="24" :lg="15">
        <div class="chart-wrapper">
          <active-user-cloud />
        </div>
      </el-col>
    </el-row>
    <el-row style="background:#fff;padding:16px 32px 0;margin-bottom:32px;">
      <el-col :xs="24" :sm="24" :lg="25">
        <div class="app-container">
          <div style="margin:0 0 5px 20px">
            Top 10 active users
          </div>
          <FixedThead></FixedThead>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import FixedThead from './dynamic-table/components/FixedThead.vue'
import PanelGroup from './components/PanelGroup'
// import LineChart from './components/LineChart'
// import Chart from '@/components/Charts/Keyboard'
// import RaddarChart from './components/RaddarChart'
import PieChart from './components/PieChart'
// import WithoutIDPie from '@/views/users/admin/components/WithoutIDPie.vue'
import BarChart from './components/BarChart'
import axios from 'axios'
import ActiveUserCloud from '@/views/users/admin/components/ActiveUserCloud.vue'
// import BarChart from '@/views/dashboard/admin/components/BarChart.vue'

const lineChartData = {
  answers_distribution: {
    actualData: [1, 2, 3, 4, 5, 5, 6, 7]
  }
}

export default {
  name: 'DashboardAdmin',
  components: {
    BarChart,
    ActiveUserCloud,
    // GithubCorner,
    PanelGroup,
    // LineChart,
    // Chart,
    // WithoutIDPie,
    // RaddarChart
    PieChart,
    FixedThead
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

.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;


  .chart-wrapper {
    background: #fff;
    padding: 32px 32px 32px;
    margin-bottom: 32px;
    //margin-left: 50px;
    //position:relative;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 32px 32px 32px;
  }
}
</style>
