import Vue from 'vue'
import Router from 'vue-router'
import category from './views/admin/Category.vue'
import Admin from './views/admin/Admin.vue'
import Home from './views/Home.vue'
import NewPost from './views/admin/Newpost.vue'
import PostList from './views/admin/PostList.vue'
import EditPost from './views/admin/EditPost.vue'
import PostDetail from './views/PostDetail.vue'
import Record from './views/Record.vue'
import NewVerse from './views/admin/NewVerse.vue'
import VerseCate from './views/admin/verseCate'
import Verse from './views/Verse'


Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/cate/:cate',
      name: 'homeCate',
      component: Home
    },
    {
      path: '/page/:page',
      name: 'homePage',
      component: Home
    },
    {
      path: '/cate/:cate/page/:page',
      name: 'homeCatePage',
      component: Home
    },
    {
      path: '/verses/',
      name: 'verse',
      component: Verse
    },
    {
      path: '/records',
      name: 'record',
      component: Record
    },
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
      path: '/post/:id',
      name: 'postDetail',
      component: PostDetail,
    },
    {
      path: '/admin',
      component: Admin,
      children: [
        // when /admin/categories is matched
        // { path: '', name:'admin-info', component: AdminInfo},
        { path: 'categories', name:'admin-category', component: category},
        { path: 'new-post', name: 'new-post', component: NewPost },
        { path: 'post-list', name: 'post-list', component: PostList },
        { path: 'edit-post/:id', name: 'edit-post', component: EditPost },
        { path: 'new-verse', name:'new-verse', component: NewVerse},
        { path: 'verse-cate', name: 'verse-cate', component: VerseCate}
      ],
      meta: {
        requiresAuth: true
      }
    },
    { 
      path: '/post/:id', name: 'postDetail', component: PostDetail 
    }
  ]
})



router.beforeEach((to, from, next) => {
  const token = window.localStorage.getItem("mysite-token");
  if (to.matched.some(record => record.meta.requiresAuth) && (!token || token == null)) {
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
  } else if (to.matched.length === 0) {
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
