<script>
// インポート
import { Doughnut } from 'vue-chartjs'

// ローカルコンポーネント 棒グラフ
var DoughnutGraph = {
  extends: Doughnut,
  mounted () {
    this.renderChart({
      // ラベル
      labels: ['天領', '薩摩', '長州', '土佐'],
      // データ詳細
      datasets: [{
        // データタイトル
        label: '藩と人口',
        // データ
        data: [13740000, 9072000, 7150000, 6148000]
      }]
    })
  }
}

export default DoughnutGraph
</script>
