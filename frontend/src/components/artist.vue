<template>
  <div class="artist">
    <div class="profile">
      <img :src="image_src">
      <h1 id="name">
        {{ name }}
      </h1>
    </div>

    <hr class="dots">

    <div class="list-data">
      <h2> data だす </h2>
    </div>

    <hr class="dots">

    <div class="graph">
      <DoughnutGraph :width="900" :height="300"></DoughnutGraph>
    </div>

    <hr class="dots">

    <div id="uploadmusic"> <input @change="selectedFile" type="file" name="file">
      <button @click="upload" type="submit">upload</button>
    </div>

  </div>
</template>

<script>
import '@/assets/css/artist.css'
import DoughnutGraph from '../components/DoughnutGraph.vue'

export default {
  data () {
    return {
      image_src: require('../assets/noimage.png'),
      name: 'Artist name',
      uploadFile: null
    }
  },
  components: {
    DoughnutGraph
  },
  methods: {
    selectedFile: function (e) {
      e.preventDefault()
      let files = e.target.files
      this.uploadFile = files[0]
      this.formData = new FormData()
      this.reader = new FileReader()
      this.reader.onload = function() {
         this.result = e.target.result
      }
      this.reader.readAsBinaryString(this.uploadFile)
    },
    upload: function () {
      this.formData.append('fileName', this.uploadFile.name)
      this.formData.append('contentType', 'application/json')
      this.formData.append('contentData', base64.encode(this.reader.result))

      axios.post('http://localhost:3000/data/json/upload', this.formData).then(function (response) {
      }).catch(function (error) {
      })
    }
  }
}
</script>
