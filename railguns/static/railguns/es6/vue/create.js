let content = new Vue({
    mixins: [base],
    el: '#content',
    data: function () {
        return {
            endpoint: '',
            data: {}
        }
    },
    methods: {
        onPrepare: function () {
            console.warn('onPrepare overwrite')
        },
        onLoadSuccess(response) {
            let url = new URL(document.URL)
            let next = url.searchParams.get('next')
            location = next ? next : '/'
        },
        submit: function (event) {
            // !this.data.name || !this.data.id_card_number ||
            if (!this.data.phone_number || !this.data.password || !this.data.code) {
                showAlert('请填写完整所有项')
                return
            }
            if (this.errors) {
                showAlert(JSON.stringify(this.errors))
                return
            }
            this.data.username = this.data.phone_number
            console.warn(this.data) // 返回的是一个包含很多内容东西的对象 里边还有不想要的东西
            let obj = JSON.stringify(this.data) // JSON.stringify() 方法用于将 JavaScript 值转换为 JSON 字符串. 为了清除不想要的东西
            console.log(obj)
            post(this.endpoint, this.data, response => {
                this.onLoadSuccess(response)
            }, error => {
                this.onLoadFailure(error)
            })
        }
    }
})
