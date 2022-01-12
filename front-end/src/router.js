import Vue from 'vue'
import Router from 'vue-router'
import category from './views/admin/Category.vue'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/ping',
      name: 'ping',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/Ping.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login.vue')
    },
    {
      path: '/admin',
      name: 'edit_cate',
      component: category,
      children: [
        // when /admin/categories is matched
        { path: 'categories', name:'admin-category', component: category}
      ],
      meta: {
        requiresAuth: true
      }

    }
  ]
})



router.beforeEach((to, from, next) => {
  const token = window.localStorage.getItem("mysite-token");
  if (to.matched.some(record => record.meta.requiresAuth ) && (!token || token == null)) {
    Vue.toasted.show("请登录", { icon: "fingerprint" })
    next({
      path: '/login/',
      query: { redirect: to.fullPath }
    })
  } else if (token && to.name == 'Login') {
    // 用户已经登陆但是访问了登录页面，不让他过去
    next({
      path: from.fullPath,
    })
  } else if (to.matched.length == 0) {
    // 前往的路径不存在时
    Vue.toasted.error('404: Not Found', { icon: "fingerprint" })
    if (from.name) {
      next({
        name: from.name
      })
    } else {
      next({
        path: '/'
      })
    }
  } else {
    next()
  }
})


export default router
