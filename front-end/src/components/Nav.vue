<template>
    <div>
        <div class="container">
            <ul class="nav nav-tabs navbar-top">
                <li class="li-first" role="presentation"><a href="#">首页</a></li>
                <li role="presentation"><a href="#">随笔</a></li>
                <li role="presentation"><a href="#">文字</a></li>
                <li role="presentation"><a href="#">关于我</a></li>
                <li @click="showModal = true">登陆</li>
            </ul>

        </div>
        <div v-if="showModal">
            <transition name="modal">
                <div class="modal-mask">
                    <div class="modal-wrapper">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title">Modal title</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true" @click="showModal = false">&times;</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                    <p>Modal body text goes here.</p>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary"
                                        @click="showModal = false">Close</button>
                                    <button type="button" class="btn btn-primary">Save changes</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </transition>
        </div>
    </div>


</template>

<script>
    export default {
        components: {
        },
        data() {
            return {
                showModal: false
            };
        },
        methods: {

        },
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