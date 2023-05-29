<template>
  <div class="dashboard-editor-container">

    <panel-group @handleSetLineChartData="handleSetLineChartData" />

    <!-- <el-row style="background:#fff;padding:16px 16px 32px;margin-bottom:32px;">
      <line-chart :chart-data="lineChartData" />
    </el-row> -->

    <el-row>
      <el-col :xs="24" :sm="24" :lg="24">
        <div class="chart-wrapper">
          <tmu />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import PanelGroup from './components/PanelGroup'
import LineChart from './components/LineChart'
import RaddarChart from './components/RaddarChart'
import tmu from './components/TagsMostUpvotes_admin'
import BarChart from './components/BarChart'
import axios from 'axios'

const lineChartData = {
  answers_distribution: {
    actualData: [1, 2, 3, 4, 5, 5, 6, 7]
  }
}

export default {
  name: 'DashboardAdmin',
  components: {
    tmu
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
