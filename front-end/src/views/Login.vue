<template>
  <div>
    <div class="login">
      <form @submit.prevent>
        <div class="form-group">
          <label>用户名</label>
          <input
            v-model="username"
            class="form-control"
            id="exampleInputEmail1"
            placeholder="用户名"
          />
        </div>
        <div class="form-group">
          <label>密码</label>
          <input
            v-model="password"
            type="password"
            class="form-control"
            id="exampleInputPassword1"
            placeholder="密码"
          />
        </div>
        <button @click="submit" type="submit" class="btn btn-default">
          提交
        </button>
      </form>
    </div>
  </div>
</template>



<script>
import axios from "axios";
import store from "./store.js";
export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      message: "",
      type: "",
      dismissCountDown: 0,
      dismissSecs: 5,
    };
  },
  methods: {
    submit() {
      const loginPath = store.URL + "/login";
      window.console.log(store.state.is_login);
      window.console.log(store.state.user_id);
      const data = {
        username: this.username,
        password: this.password,
      };
      axios
        .post(loginPath, data)
        .then((res) => {
          this.message = res.data.message;
          this.type = "success";
          let token = res.data.token;
          let userId = res.data.user_id;
          if (res.data.status_code == 200) {
            window.localStorage.setItem("mysite-token", token);
            window.localStorage.setItem("mysite-user-id", userId);
            this.$notify({
              title: '登陆成功',
              message: '你登陆成功啦',
              type: 'success'
            });
            setTimeout(this.$router.push({name:'home'}), 2000);
          }
          if (res.data.status_code == 203) {
            this.variant = "warning";
            this.$notify.error({
              title: '登陆失败',
              message: '账号或者密码错误'
            });
          }
        })
        .catch((error) => {
          window.consolee.error(error);
        });
      this.showAlert();
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs;
    },
  },
};
</script>

<style>
.login {
  width: 300px;
  margin-left: 40%;
}
</style>