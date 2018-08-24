<template>
  <div class="artist">
    <div class="profile">
      <img :src="image_src">
      <h1 id="name">
        {{ info.data.data.artist_id }}
      </h1>
    </div>

    <hr class="dots">

    <div class="list-data">
        <h2> Total sales: {{ info.data.data.total_sales }} JPY </h2>
        <h2> Total music: {{ info.data.data.total_music }} songs </h2>
    </div>

    <hr class="dots">
    <div class="graph">
      <DoughnutGraph :country='country' :width="900" :height="300"></DoughnutGraph>
    </div>
    <hr class="dots">

    <div id="uploadmusic"> <input @change="selectedFile" type="file" name="file">
            <button @click="upload" type="submit">upload</button>
    </div>

    <div id="uploadmusic"> <input @change="selectedFile" type="file" name="file">
        <vue-dropzone id="drop1" :options="dropOptions"></vue-dropzone>
    </div>

    <div class="classif">
        <h2> {{ result.data.result }} </h2>
    </div>
  </div>
</template>

<script>
import vueDropzone from 'vue2-dropzone'
import '@/assets/css/artist.css'
import { Doughnut } from 'vue-chartjs'
// import DoughnutGraph from '../components/DoughnutGraph.vue'
const axios = require('axios')

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

export default {
  props: ['id'],
  data () {
    return {
      image_src: require('../assets/noimage.png'),
      name: 'Artist name',
      info: {data: {data: {artist_id: '404', total_sales: 'Server Error', total_music: 'Server Error'}}},
      country: {data: {data: {US: 404, UK: 404, CN: 404, RU: 404, JP: 404, UGANDA: 404}}},
      result: {data: {result: 'Please upload file'}},
      uploadFile: null,
      dropOptions: {
        url: 'https://httpbin.org/post'
      }
    }
  },

  mounted () {
    axios
      .get('http://localhost:3000/getArtist/' + this.$route.params.id)
      .then(response => (this.info = response))

    axios
      .get('http://localhost:3000/getArtist/country/' + this.$route.params.id)
      .then(response => (this.country = response))
  },

  components: {
    DoughnutGraph,
    vueDropzone
  },
  methods: {
    selectedFile (e) {
      this.uploadFile = e.target.files[0]
      this.formData = new FormData()
      this.reader = new FileReader()
      this.reader.onload = (e) => {
        this.result = e.target.result
      }
      this.reader.readAsBinaryString(this.uploadFile)
    },

    upload () {
      this.formData.append('fileName', this.uploadFile.name)
      this.formData.append('contentType', 'application/json')
      this.formData.append('contentData', this.base64_encode(this.reader.result))

      axios.post('http://localhost:3000/data/json/upload', this.formData
      ).then((res) => {
        console.log(res)
        this.result = res
        // TODO: ここでresponseデータをあれこれする
      }).catch(error => {
        console.log(error)
      })
    },

    base64_encode (input) {
      var TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

      input = String(input)
      if (/[^\0-\xFF]/.test(input)) {
        console.error('The string to be encoded contains characters outside of the ' + 'Latin1 range.')
      }
      var padding = input.length % 3
      var output = ''
      var position = -1
      var a
      var b
      var c
      var buffer
      var length = input.length - padding

      while (++position < length) {
        a = input.charCodeAt(position) << 16
        b = input.charCodeAt(++position) << 8
        c = input.charCodeAt(++position)
        buffer = a + b + c
        // Turn the 24 bits into four chunks of 6 bits each, and append the
        // matching character for each of them to the output.
        output += (
          TABLE.charAt(buffer >> 18 & 0x3F) +
          TABLE.charAt(buffer >> 12 & 0x3F) +
          TABLE.charAt(buffer >> 6 & 0x3F) +
          TABLE.charAt(buffer & 0x3F)
        )
      }

      if (padding === 2) {
        a = input.charCodeAt(position) << 8
        b = input.charCodeAt(++position)
        buffer = a + b
        output += (
          TABLE.charAt(buffer >> 10) +
           TABLE.charAt((buffer >> 4) & 0x3F) +
           TABLE.charAt((buffer << 2) & 0x3F) +
           '='
        )
      } else if (padding === 1) {
        buffer = input.charCodeAt(position)
        output += (
          TABLE.charAt(buffer >> 2) +
          TABLE.charAt((buffer << 4) & 0x3F) +
          '=='
        )
      }

      return output
    }
  }
}
</script>
