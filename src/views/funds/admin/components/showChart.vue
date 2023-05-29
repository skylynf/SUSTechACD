<template>
  <div>
    <input type="text" placeholder="请输入fund_ID" id="fundId" v-model="fundId">
    <el-button type="button" @click="showChart">展示</el-button>
    <div class="chart-container" ref="chartContainer"></div>
  </div>
</template>

<script>
import axios from 'axios';
import echarts from 'echarts';

export default {
  data() {
    return {
      fundId: '',
    };
  },
  methods: {
    showChart() {
      const url = `http://127.0.0.1:5000/api/funds/chart/${this.fundId}`;
      axios.get(url)
        .then(response => {
          const data = response.data;
          this.renderChart(data);
        })
        .catch(error => {
          console.error(error);
        });
    },
    renderChart(data) {
      const chartContainer = this.$refs.chartContainer;
      const chart = echarts.init(chartContainer);

      const options = {
        tooltip: {
          trigger: 'item',
          formatter: '{b} : {c} ({d}%)',
        },
        series: [
          {
            name: 'Funds',
            type: 'pie',
            radius: '55%',
            data: Object.entries(data).map(([name, value]) => ({ name, value })),
          },
        ],
      };

      chart.setOption(options);
    },
  },
};
</script>
<style>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
}

.input-container {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

label {
  margin-right: 10px;
  font-weight: bold;
  color: #333;
}

input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

input:focus {
  border-color: #007bff;
}

button {
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

.chart-container {
  width: 400px;
  height: 400px;
  border: 1px solid #ccc;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 4px;
}
</style>
