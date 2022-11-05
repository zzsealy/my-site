import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    URL: 'http://localhost:8001',
    debug: true,
    is_login: window.localStorage.getItem('mysite-token') ? true : false,
    user_id: window.localStorage.getItem('mysite-user-id'),
    navStatusState: {
        homeActive: false,
        cateActive: false,
        verseActive: false,
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
      let navName = payload.navName;
      
      switch (navName) {
          case "home":
              state.navStatusState.homeActive = true;
              break;
          case "cate":
              state.navStatusState.cateActive = true;
              break;
          case "verse":
              state.navStatusState.verseActive = true;
              break;
          case "history":
              state.navStatusState.historyActive = true;
              break;
          case "about":
              state.navStatusState.aboutActive = true;
              break;
          case "admin":
              state.navStatusState.adminActive = true;
              break;
      }
      window.sessionStorage.setItem("nav_status", JSON.stringify(state.navStatusState))
    },
    cancelStatus(state, payload){
      state.navStatusState.homeActive = false;
      state.navStatusState.cateActive = false;
      state.navStatusState.verseActive = false;
      state.navStatusState.historyActive = false;
      state.navStatusState.adminActive = false;
      state.navStatusState.aboutActive = false;
    },

  },
  actions: {},
  modules: {}
})
