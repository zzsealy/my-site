import axios from 'axios'



// 基础配置
axios.defaults.timeout = 5000
axios.defaults.baseURL = 'http://localhost:8001'

// 增加 request interceptor

axios.interceptors.request.use(function (config) {
    const token = window.localStorage.getItem('mysite-token')
    if (token) {
        config.headers.Authorization = `${token}`
    }
    return config
}, function (error) {
    return Promise.reject(error)
})



export default axios

