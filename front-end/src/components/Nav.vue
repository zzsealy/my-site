<template>
  <div class="header">
        <!-- <p>
          嗨，这是我的个人网站。
        </p> -->
        <el-row :gutter="20">
            <el-col :span="10" :offset="3" style="padding: 0px;">
                    <hr class="nav-hr">
            </el-col>
            <el-col :span="10" style="padding: 0px;">
                <ul class="nav navbar-top">
                    <div @click="clickNav('home')" class="nav-div" v-bind:class = "{ active: homeActive}"><li role="presentation"><a href="#">首页</a></li></div>
                    <div @click="clickNav('cate')" class="nav-div" v-bind:class = "{ active: cateActive}"><li role="presentation"><a href="#">归档</a></li></div>
                    <div @click="clickNav('sentence')" class="nav-div" v-bind:class = "{ active: sentenceActive}"><li role="presentation"><a href="#">短句</a></li></div>
                    <div @click="clickNav('history')" class="nav-div" v-bind:class = "{ active: historyActive}"><li role="presentation"><a href="#">历史</a></li></div>
                    <div @click="clickNav('about')" class="nav-div" v-bind:class = "{ active: aboutActive}"><li role="presentation"><a href="#">关于我</a></li></div>
                    <div @click="clickNav('admin')" class="nav-div" v-bind:class = "{ active: adminActive}"><li v-if="is_login"><router-link to="/admin">后台</router-link></li></div>
                    <div class="nav-div"><li v-if="is_login" role="presentation" @click="cancelLogin"><a>注销登录</a></li></div>
                </ul>
            </el-col>
          </el-row>

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
                homeActive: false,
                cateActive: false,
                sentenceActive: false,
                historyActive: false,
                aboutActive: false,
                adminActive: false
            };
        },
        methods: {
            cancelLogin(){
                global.logoutAction()
            },
            clickNav(navName) {
                this.cancelClickStstus()
                this.toggleNav(navName);
            },

            toggleNav(navName){
                switch(navName){
                    case "home":
                        this.homeActive = true;
                        break;
                    case "cate":
                        this.cateActive = true;
                        break;
                    case "sentence":
                        this.sentenceActive = true;
                        break;
                    case "history":
                        this.historyActive = true;
                        break;
                    case "about":
                        this.aboutActive = true;
                        break;
                    case "admin":
                        this.adminActive = true;
                        break;
                }
            },
            cancelClickStstus() {
                this.homeActive = false;
                this.cateActive = false;
                this.sentenceActive = false;
                this.historyActive = false;
                this.adminActive = false;
                this.aboutActive = false;
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

    .header {
        margin-top: 5% !important;
    }

    .navbar-top li {
        margin: 20px 20px 0px 20px;
        padding: 0px;
    }

    .navbar-top li a {
        color: black;
        text-decoration: none;
    }

    .nav-hr {
        padding-right: 0px;
        margin-top: 44px;
    }

    .nav-div {
        border-bottom: 1px solid #C8C8C8;
    }

    .active {
        border: 1px solid black;
        border-bottom-color: #fff;
    }


</style>