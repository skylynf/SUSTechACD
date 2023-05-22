
<template>
  <div>
    <div
      id="myChart"
      :style="{ width: '600px', height: '500px', margin: 'auto' }"
    ></div>
  </div>
</template>

<script>
export default {
  name:'ReputationScoreRelation',
  data() {
    return {}
  },
  mounted() {
    //调用接口函数
    this.getData()
  },
  methods: {
    getData() {
      /**
       * 散点图用的是二维数组
       */
      let dataArr = [
        { ender: 'female', height: '180.3', weight: 83.2 },
        { ender: 'male', height: '168', weight: 200 },
        { ender: 'male', height: '174', weight: 110 },
        { ender: 'female', height: '166', weight: 153 },
        { ender: 'male', height: '205', weight: 142 },
        { ender: 'male', height: '23.3', weight: 189 },
        { ender: 'female', height: '170', weight: 188 },
        { ender: 'female', height: '130.3', weight: 83.2 },
        { ender: 'male', height: '145', weight: 300 },
        { ender: 'male', height: '179', weight: 120 },
        { ender: 'female', height: '166', weight: 113 },
        { ender: 'male', height: '45', weight: 234 },
        { ender: 'male', height: '159.3', weight: 80 },
        { ender: 'female', height: '170', weight: 128 },
        { ender: 'female', height: '156', weight: 55 },
        { ender: 'male', height: '165', weight: 346 },
        { ender: 'male', height: '136.3', weight: 120 },
        { ender: 'female', height: '100', weight: 86 },
        { ender: 'female', height: '145.3', weight: 83.2 },
        { ender: 'male', height: '162', weight: 95 },
      ]
      let axisData = []
      // 把一维数组变成二维数组
      for (let i = 0; i < dataArr.length; i++) {
        const el = dataArr[i]
        let height = el.height
        let weight = el.weight
        let newArr = [height, weight]
        axisData.push(newArr)
      }
      let myChart = this.$echarts.init(document.getElementById('myChart'))
      let option = {
        xAxis: { type: 'value' },
        yAxis: { type: 'value' },
        series: [
          {
            // symbolSize: 10, //散点固定大小
            symbolSize: (arg) => {
              let height = arg[0] / 100
              let weight = arg[1]
              //bmi =体重/(身高*身高)>28为肥胖
              let bmi = weight / (height * height)
              return bmi > 28 ? 10 : 5
            },
            itemStyle: {
              // color: 'green',
              color: (arg) => {
                let height = arg.data[0] / 100
                let weight = arg.data[1]
                //bmi =体重/(身高*身高)>28为肥胖
                let bmi = weight / (height * height)
                return bmi > 28 ? 'red' : 'green'
              },
            },
            data: axisData,
            type: 'effectScatter', //散点图 scatter,涟漪动画,effectScatter
            // 涟漪动画大小
            rippleEffect: {
              scale: 10,
            },
            showEffectOn: 'render', //涟漪动画出现效果,render:加载出来就有效果, emphasis:鼠标滑过才有效果
          },
        ],
      }
      myChart.setOption(option)
    },
  },
}
</script>

<style>
</style>
