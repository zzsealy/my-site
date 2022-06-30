import Vue from 'vue'

export const navStatus = Vue.observable({
        homeActive: false,
        cateActive: false,
        sentenceActive: false,
        historyActive: false,
        aboutActive: false,
        adminActive: false
      
});

export const mutations = {
  cancelStatus(){
      navStatus.homeActive = false;
      navStatus.cateActive = false;
      navStatus.sentenceActive = false;
      navStatus.historyActive = false;
      navStatus.adminActive = false;
      navStatus.aboutActive = false;
  },
  toggleStatus(navName) {
      switch (navName) {
          case "home":
              navStatus.homeActive = true;
              break;
          case "cate":
              navStatus.cateActive = true;
              break;
          case "sentence":
              navStatus.sentenceActive = true;
              break;
          case "history":
              navStatus.historyActive = true;
              break;
          case "about":
              navStatus.aboutActive = true;
              break;
          case "admin":
              navStatus.adminActive = true;
              break;
      }
  },
}
      


export const store = {
      URL: 'http://localhost:8001',
      debug: true,
      state: {
        is_login: window.localStorage.getItem('mysite-token') ? true : false,
        user_id: window.localStorage.getItem('mysite-user-id')
      },
      loginActinon(){
        this.state.is_login = true;
      },
      logoutAction(){
        window.localStorage.removeItem('mysite-token')
        window.localStorage.removeItem('mysite-user-id')
        this.state.is_login = false;
        this.state.user_id = 0;
      },
      
    }
