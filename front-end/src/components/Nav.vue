<template>
    <div class="header">
        <!-- <p>
          嗨，这是我的个人网站。
        </p> -->
        <el-row :gutter="20">

            <el-col :span="10" :offset="4" style="padding: 0px;">
                <h1>drq's Diary</h1>
                <p class="header-p">故事太多 需要有个地方记录</p>
                <hr class="nav-hr">
            </el-col>
            <el-col :span="10" style="padding: 0px;" class="nav-block">
                <ul class="nav navbar-top">
                    <a href="/" @click="clickNav('home')" class="nav-a" v-bind:class="{ nav_active: homeActive}">
                        <i class="el-icon-s-home">首页</i></a>
                    <a href="/cate/" @click="clickNav('cate')" class="nav-a" v-bind:class="{ nav_active: cateActive}">
                        <i class="el-icon-s-order">归档</i></a>
                    <a href="/verses/" @click="clickNav('sentence')" class="nav-a" v-bind:class="{ nav_active: sentenceActive}">
                        <i class="el-icon-water-cup">短句</i></a>
                    <a href="#" @click="clickNav('history')" class="nav-a" v-bind:class="{ nav_active: historyActive}">
                        <i class="el-icon-time">历史</i></a>
                    <a href="/about/" @click="clickNav('about')" class="nav-a" v-bind:class="{ nav_active: aboutActive}">
                        <i class="el-icon-user-solid">关于</i></a>
                    <a href="/admin/" @click="clickNav('admin')" class="nav-a" v-bind:class="{ nav_active: adminActive}">
                        <i v-if="is_login">后台</i></a>
                    <a class="nav-a">
                        <li v-if="is_login" @click="cancelLogin"><a>注销登录</a></li>
                    </a>
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
            cancelLogin() {
                global.logoutAction()
            },
            clickNav(navName) {
                this.cancelClickStstus()
                this.toggleNav(navName);
            },

            toggleNav(navName) {
                switch (navName) {
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

        created() {
            this.is_login = global.state.is_login;
        },

        update() {
            this.is_login = global.state.is_login;
        }
    }
</script>

<style>
    .header {
        margin-top: 3% !important;
    }

    .navbar-top a {
        cursor: default;
    }

    .navbar-top a:hover {
        text-decoration: underline;
        color: black;
    }

    .navbar-top a i {
        font-size: 14px;
    }

    /* .navbar-top {
        position: absolute;
        margin-top: 4.5%;
    } */



    .nav-hr {
        padding-right: 0px;
        margin-bottom: 0;
    }

    .nav-block {
        position: relative;
        top: 66px;
    }

    .nav-a {
        padding: 3px 20px 3px;
        border-bottom: 1px solid #C8C8C8;
        color: black;
        text-decoration: none;
    }

    .nav_active {
        border: 1px solid #C8C8C8;
        border-bottom-color: #fff;
        padding: 2px 20px 3px;
    }

    .header-p {
        margin-bottom: 0px;
    }
</style>