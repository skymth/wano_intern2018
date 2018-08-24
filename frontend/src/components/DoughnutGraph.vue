<script>
// インポート
import { Doughnut } from 'vue-chartjs'

// ローカルコンポーネント 棒グラフ
var DoughnutGraph = {
  extends: Doughnut,
  mounted () {
    this.renderChart({
      // ラベル
      labels: ['天領', '薩摩', '長州', '土佐', '会津'],
      // データ詳細
      datasets: [{
        // データタイトル
        label: '藩と人口',
        // データ
        data: [13740000, 9072000, 7150000, 6148000, 341686],
        backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16', '#eddc44']
      }]
    })
  }
}

export default DoughnutGraph
</script>
