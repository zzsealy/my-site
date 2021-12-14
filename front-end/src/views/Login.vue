<template>
    <div>
        <div>
            <b-alert :show="dismissCountDown" :variant="variant" dismissible v-on:dismissed="dismissCountDown=0"
                @dismiss-count-down="countDownChanged">
                {{ message }} <b></b>
                <!--
                <b-progress
                :variant="variant"
                :max="dismissSecs"
                :value="dismissCountDown"
                height="4px"
                ></b-progress>
                -->
            </b-alert>
        </div>
        <div class="login">
            <form @submit.prevent>
                <div class="form-group">
                    <label>用户名</label>
                    <input v-model="username" class="form-control" id="exampleInputEmail1" placeholder="用户名">
                </div>
                <input type="hidden" name="_token" :value="token">
                <div class="form-group">
                    <label>密码</label>
                    <input v-model="password" type="password" class="form-control" id="exampleInputPassword1"
                        placeholder="密码">
                </div>
                <button @click="submit" type="submit" class="btn btn-default">提交</button>
            </form>
        </div>
    </div>

    <!-- 
1、第一次登录的时候，前端调后端的登陆接口，发送用户名和密码

2、后端收到请求，验证用户名和密码，验证成功，就给前端返回一个token

3、前端拿到token，将token存储到localStorage和vuex中，并跳转路由页面

4、前端每次跳转路由，就判断 localStroage 中有无 token ，没有就跳转到登录页面，有则跳转到对应路由页面

5、每次调后端接口，都要在请求头中加token

6、后端判断请求头中有无token，有token，就拿到token并验证token，验证成功就返回数据，验证失败（例如：token过期）就返回401，请求头中没有token也返回401

7、如果前端拿到状态码为401，就清除token信息并跳转到登录页面
-->
</template>



<script>
    import axios from 'axios'
    import global from './Global.vue'
    export default {
        name: "login",
        data() {
            return {
                username: '',
                password: '',
                token: '',
                message: '',
                variant: '',
                dismissCountDown: 0,
                dismissSecs: 5,
            }
        },
        methods: {
            submit() {

                const cstftoken = global.CSRFTOKEN;
                const loginPath = global.URL + '/login';
                const data = {
                    "username": this.username,
                    "password": this.password
                }
                axios.post(loginPath, data)
                    .then((res) => {
                        this.message = res.data.message;
                        this.variant = "success"
                        if (res.data.status_code == 203) {
                            this.variant = 'warning';
                        }

                    })
                    .catch((error) => {
                        this.message = "发生错误";
                        this.variant = 'warning';
                    })

                this.dismissCountDown = this.dismissSecs;

            },
            countDownChanged(dismissCountDown) {
                // console.log(dismissCountDown); 
                this.dismissCountDown = dismissCountDown
            },
        },
    }
</script>

<style>
    .login {
        width: 300px;
        margin-left: 40%;
    }
</style>