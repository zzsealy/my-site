<template>
  <div>
    <b-button v-b-toggle.sidebar-1>导航</b-button>
    <b-sidebar v-model="visible" id="sidebar-1" :backdrop-variant="dark" backdrop title="DRQ" shadow>
      <div class="px-3 py-2">
        <p>
          嗨，这是我的个人网站。
        </p>
        <b-img src="https://picsum.photos/500/500/" fluid thumbnail></b-img>
        <div class="container">
            <ul class="nav nav-tabs navbar-top">
                <li role="presentation"><a href="#">首页</a></li>
                <li role="presentation"><a href="#">随笔</a></li>
                <li role="presentation"><a href="#">文字</a></li>
                <li role="presentation"><a href="#">关于我</a></li>
                
            </ul>
            <b-button v-if="is_login" role="presentation" @click="cancelLogin"><a>注销登录</a></b-button>
            <b-button v-if="is_login"><router-link to="/admin">后台</router-link> </b-button>

        </div>
      </div>
    </b-sidebar>
  </div>
</template>

<script>
import global from "../views/Global.vue";
    export default {
        components: {
        },
        data() {
            return {
                showModal: false,
                is_login: false,
                visible: true,
            };
        },
        methods: {
            cancelLogin(){
                global.logoutAction()
            }
        },

        created(){
            this.is_login = global.state.is_login;
        },

        update(){
            this.is_login = global.state.is_login;
        }
    }
</script>

<style>
    .navbar-top {
        margin-top: 5% !important;
    }

    .navbar-top li {
        margin: 20px;
    }

    .navbar-top li a {
        color: black;
    }

</style>