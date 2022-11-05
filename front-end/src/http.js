import Vue from 'vue'
import axios from 'axios'
import router from './router'


// 基础配置
axios.defaults.timeout = 5000
axios.defaults.baseURL = 'http://localhost:8001'

// 增加 request interceptor

axios.interceptors.request.use(function (config) {
    // let navStatus = {
    //     homeActive: false,
    //     cateActive: false,
    //     verseActive: false,
    //     historyActive: false,
    //     aboutActive: false,
    //     adminActive: false
    //   }
    // window.sessionStorage.setItem("nav_status", navStatus)
    const token = window.localStorage.getItem('mysite-token')
    if (token) {
        config.headers.Authorization = `${token}`
    }
    return config
}, function (error) {
    return Promise.reject(error)
})

axios.interceptors.response.use(function (response) {
    // 响应成功结果
    return response
}, function (error) {
    // 处理响应失败的
    switch (error.response.status) {
        case 401:
            this.$store.commit('logoutAction', {});
            if (router.currentRoute.path !== '/login') {
                Vue.toasted.error('401: 认证已失效，请先登录', { icon: 'fingerprint' })
                router.replace({
                    path: '/login',
                    query: { redirect: router.currentRoute.path },
                })
            }
            break

        case 403:
            Vue.toasted.error('403: Forbidden', { icon: 'fingerprint' })
            router.back()
            break

        case 404:
            Vue.toasted.error('404: Not Found', { icon: 'fingerprint' })
            router.back()
            break

    }
    return Promise.reject(error)
}
)



export default axios

