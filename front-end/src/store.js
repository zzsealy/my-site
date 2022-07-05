import Vue from 'vue'
import Vuex from 'vuex'


export default new Vuex.Store({
  state: {
    URL: 'http://localhost:8001',
    debug: true,
    is_login: window.localStorage.getItem('mysite-token') ? true : false,
    user_id: window.localStorage.getItem('mysite-user-id'),
    navStatus:{
      homeActive: false,
      cateActive: false,
      sentenceActive: false,
      historyActive: false,
      aboutActive: false,
      adminActive: false
  },
  },
  getters: {},
  mutations: {
    loginActinon(state, payload){
      state.is_login = true;
    },
    logoutAction(state, payload){
      window.localStorage.removeItem('mysite-token')
      window.localStorage.removeItem('mysite-user-id')
      state.is_login = false;
      state.user_id = 0;
    },
    toggleStatus(state, payload) {
      navName = payload.navName;
      switch (navName) {
          case "home":
              state.navStatus.homeActive = true;
              break;
          case "cate":
              state.navStatus.cateActive = true;
              break;
          case "sentence":
              state.navStatus.sentenceActive = true;
              break;
          case "history":
              state.navStatus.historyActive = true;
              break;
          case "about":
              state.navStatus.aboutActive = true;
              break;
          case "admin":
              state.navStatus.adminActive = true;
              break;
      }
    },
    cancelStatus(state, payload){
      state.navStatus.homeActive = false;
      state.navStatus.cateActive = false;
      state.navStatus.sentenceActive = false;
      state.navStatus.historyActive = false;
      state.navStatus.adminActive = false;
      state.navStatus.aboutActive = false;
    },

  },
  actions: {},
  modules: {}
})
