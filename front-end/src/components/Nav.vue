<template>
    <div>
        <div class="container">
            <ul class="nav nav-tabs navbar-top">
                <li class="li-first" role="presentation"><a href="#">首页</a></li>
                <li role="presentation"><a href="#">随笔</a></li>
                <li role="presentation"><a href="#">文字</a></li>
                <li role="presentation"><a href="#">关于我</a></li>
                <li v-if="is_login" role="presentation" @click="cancelLogin"><a>注销登录</a></li>
            </ul>

        </div>
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

    .li-first {
        margin-left: 600px !important;
    }

    .modal-mask {
        position: fixed;
        z-index: 9998;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .5);
        display: table;
        transition: opacity .3s ease;
    }

    .modal-wrapper {
        display: table-cell;
        vertical-align: middle;
    }
</style>