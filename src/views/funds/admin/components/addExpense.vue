<template>
  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
    <el-form-item label="经费号" prop="fundID">
      <el-input v-model="ruleForm.fundID"></el-input>
    </el-form-item>
    <el-form-item label="经费名称" prop="fundName">
      <el-input v-model="ruleForm.fundName"></el-input>
    </el-form-item>
    <el-form-item label="课题组" prop="userName">
      <el-input v-model="ruleForm.userName"></el-input>
    </el-form-item>
    <el-form-item label="经费总额度" prop="totalQuota">
      <el-input v-model="ruleForm.totalQuota"></el-input>
    </el-form-item>
    <el-form-item label="已使用额度" prop="usedQuota">
      <el-input v-model="ruleForm.usedQuota"></el-input>
    </el-form-item>
    <el-form-item label="摘要" prop="abstract">
      <el-input type="textarea" v-model="ruleForm.abstract"></el-input>
    </el-form-item>
    <el-form-item label="备注" prop="remark">
      <el-input type="textarea" v-model="ruleForm.remark"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit()">增加</el-button>
      <el-button @click="resetForm('ruleForm')">重置</el-button>
    </el-form-item>
  </el-form>
</template>


<script>
  import axios from 'axios'

  const url = 'http://127.0.0.1:5000/api/funds/add';

  export default {
    data() {
      return {
        ruleForm: {
          fundID: '',
          fundName: '',
          userName: '',
          totalQuota: '',
          usedQuota: '',
          abstract: '',
          remark: ''
        },
        rules: {
          fundID: [
            { required: true }
          ],
          fundName: [
            { required: true }
          ],
          userName: [
            { required: true }
          ],
          totalQuota: [
            { required: true }
          ],
          usedQuota: [
            { required: true }
          ],
          abstract: [
            { required: true }
          ],
          remark: [
            { required: true }
          ]
        }
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
        axios.post(url, this.ruleForm)
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          const errorMessage = error.response.data.error;
          alert(errorMessage);
        });
      },
      // submitForm(formName) {
      //   this.$refs[formName].validate((valid) => {
      //     if (valid) {
      //       alert('submit!');
      //     } else {
      //       console.log('error submit!!');
      //       return false;
      //     }
      //   });
      // },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>






<!-- <template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'

const animationDuration = 3000

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
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        radar: {
          radius: '66%',
          center: ['50%', '42%'],
          splitNumber: 8,
          splitArea: {
            areaStyle: {
              color: 'rgba(127,95,132,.3)',
              opacity: 1,
              shadowBlur: 45,
              shadowColor: 'rgba(0,0,0,.5)',
              shadowOffsetX: 0,
              shadowOffsetY: 15
            }
          },
          indicator: [
            { name: 'Sales', max: 10000 },
            { name: 'Administration', max: 20000 },
            { name: 'Information Technology', max: 20000 },
            { name: 'Customer Support', max: 20000 },
            { name: 'Development', max: 20000 },
            { name: 'Marketing', max: 20000 }
          ]
        },
        legend: {
          left: 'center',
          bottom: '10',
          data: ['Allocated Budget', 'Expected Spending', 'Actual Spending']
        },
        series: [{
          type: 'radar',
          symbolSize: 0,
          areaStyle: {
            normal: {
              shadowBlur: 13,
              shadowColor: 'rgba(0,0,0,.2)',
              shadowOffsetX: 0,
              shadowOffsetY: 10,
              opacity: 1
            }
          },
          data: [
            {
              value: [5000, 7000, 12000, 11000, 15000, 14000],
              name: 'Allocated Budget'
            },
            {
              value: [4000, 9000, 15000, 15000, 13000, 11000],
              name: 'Expected Spending'
            },
            {
              value: [5500, 11000, 12000, 15000, 12000, 12000],
              name: 'Actual Spending'
            }
          ],
          animationDuration: animationDuration
        }]
      })
    }
  }
}
</script> -->
