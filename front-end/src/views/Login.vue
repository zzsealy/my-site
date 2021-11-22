<template>
<div>
    <form @submit.prevent>
        <div class="form-group">
            <label>用户名</label>
            <input v-model="username" class="form-control" id="exampleInputEmail1" placeholder="用户名">
        </div>
        <input type="hidden" name="_token" :value="token"> 
        <div class="form-group">
            <label>密码</label>
            <input v-model="password" type="password" class="form-control" id="exampleInputPassword1" placeholder="密码">
        </div>
        <button @click="submit" type="submit" class="btn btn-default">Submit</button>
        <h1>{{message}}</h1>
    </form>
</div>
</template>

<

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
            message: ''
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
                    debugger;
                    console.log(this.message);
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        getTaken() {
            const path = global.URL + '/get-token';
            axios.get(path)
                .then((res) => {
                    this.token = res.data.token;
                })
                .catch((error) => {
                    console.error(error)
                })
        },
    },
    created() {
        this.getTaken();
    }
}
</script>
