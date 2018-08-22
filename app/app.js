(function(){
    new Vue({
        el: '#app',
        data: {
            uploadFile: null
        },
        methods: {
            selectedFile: function(e) {
                e.preventDefault();
                let files = e.target.files;
                this.uploadFile = files[0];
            },
            upload: function() {
                console.log("unko");
                let formData = new FormData();
                formData.append('yourFileKey', this.uploadFile);
                let config = {
                    headers: {
                        'content-type': 'multipart/form-data'
                    }
                };
                axios
                    .post('http://localhost:3000/data/json/upload', formData, config)
                    .then(function(response) {
                    })
                    .catch(function(error) {
                    })
            }
        }
    });
})();
//http://0.0.0.0:3000/data/json/upload
//http://localhost:3000/data/json/upload
