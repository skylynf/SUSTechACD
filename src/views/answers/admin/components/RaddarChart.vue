<template>
  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
    <el-form-item label="支出编号" prop="expenseID">
      <el-input v-model="ruleForm.expenseID"></el-input>
    </el-form-item>
    <el-form-item label="支出名称" prop="expenseName">
      <el-input v-model="ruleForm.expenseName"></el-input>
    </el-form-item>
    <el-form-item label="经费号" prop="fundID">
      <el-input v-model="ruleForm.fundID"></el-input>
    </el-form-item>
    <el-form-item label="支出额度" prop="amount">
      <el-input v-model="ruleForm.amount"></el-input>
    </el-form-item>
    <el-form-item label="经办人" prop="userID">
      <el-input v-model="ruleForm.userID"></el-input>
    </el-form-item>
    <el-form-item label="支出类别一级" prop="category1">
      <el-select v-model="ruleForm.category1" >
        <el-option label="办公费" value="办公费"></el-option>
        <el-option label="办公设备配置" value="办公设备配置"></el-option>
        <el-option label="差旅费" value="差旅费"></el-option>
        <el-option label="电费" value="电费"></el-option>
        <el-option label="工会经费" value="工会经费"></el-option>
        <el-option label="会议费" value="会议费"></el-option>
        <el-option label="奖励金" value="奖励金"></el-option>
        <el-option label="劳务费" value="劳务费"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="支出类别二级" prop="category2">
      <el-select v-model="ruleForm.category2" >
        <el-option label="培训费" value="培训费"></el-option>
        <el-option label="其他" value="其他"></el-option>
        <el-option label="其他交通费用" value="其他交通费用"></el-option>
        <el-option label="其他资本性支出" value="其他资本性支出"></el-option>
        <el-option label="水费" value="水费"></el-option>
        <el-option label="维修（护）费" value="维修（护）费"></el-option>
        <el-option label="委托业务" value="委托业务"></el-option>
        <el-option label="无形资产" value="无形资产"></el-option>
        <el-option label="信息网络构建" value="信息网络构建"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="摘要" prop="abstract">
      <el-input type="textarea" v-model="ruleForm.abstract"></el-input>
    </el-form-item>
    <el-form-item label="备注" prop="remark">
      <el-input type="textarea" v-model="ruleForm.remark"></el-input>
    </el-form-item>
    <el-form-item label="申请状态" prop="applicationState">
      <el-select v-model="ruleForm.applicationState" >
        <el-option label="未发送" value="0"></el-option>
        <el-option label="正在申请中" value="1"></el-option>
        <el-option label="被拒绝打回" value="2"></el-option>
        <el-option label="申请成功" value="3"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit()">增加</el-button>
      <el-button @click="resetForm('ruleForm')">重置</el-button>
      <el-button type="primary" @click="add()">送审</el-button>
    </el-form-item>
  </el-form>
</template>


<script>
  import axios from 'axios'

  const url = 'http://127.0.0.1:5000/api/expenses/add';

  export default {
    data() {
      return {
        ruleForm: {
          expenseID: '',
          expenseName: '',
          fundID: '',
          amount: '',
          operator: '',
          category1: '',
          category2: '',
          abstract: '',
          remark: '',
          applicationState: ''
        },
        rules: {
          expenseID: [
            { required: true },
          ],
          expenseName: [
            { required: true },
          ],
          fundID: [
            { required: true },
          ],
          amount: [
            { required: true },
          ],
          userID: [
            { required: true },
          ],
          category1: [
            { required: true },
          ],
          category2: [
            { required: true },
          ],
          abstract: [
            { required: true },
          ],
          remark: [
            { required: true },
          ],
          applicationState: [
            { required: true },
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
        .catch(function (error) { // 请求失败处理
            console.log(error);
          });
      },
      add() {
        var id=this.ruleForm.expenseID;
        var u='http://127.0.0.1:5000/api/expenses/submit/'+id;
        axios.post(u).then(response => {
          console.log(response.data);
          alert(response.data['message']);
        })
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>








<!-- <template>
  <div :class="className" :style="{height:height,width:width}" />
</template> -->

<!-- <script>
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
