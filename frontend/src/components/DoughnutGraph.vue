<div class="graph">
    <DoughnutGraph :country='country' :width="900" :height="300"></DoughnutGraph>
</div>

<script>
import { Doughnut } from 'vue-chartjs'

var DoughnutGraph = {
  extends: Doughnut,
  props: ['country'],
  mounted () {
    console.log(this.country)
    this.renderChart({
      labels: ['US', 'UK', 'RU', 'CN', 'JP', 'UGANDA'],
      datasets: [{
        label: 'country total sales',
        data: [this.country.data.data.US, this.country.data.data.UK, this.country.data.data.RU, this.country.data.data.CN, this.country.data.data.JP, this.country.data.data.UGANDA],
        backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16', '#eddc44']
      }]
    })
  }
}

export default DoughnutGraph
</script>
