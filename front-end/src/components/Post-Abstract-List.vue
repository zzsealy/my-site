<template>
    <div>
            <div class="index-post" v-for="(post, index) in posts" :key="post.id">
                <h2 class="post-title"><router-link :to="{name: 'postDetail', params: {'id': post.id}}"> {{ post.title }} </router-link></h2>
                <span class="post-time">{{ post.created }}</span>
                <p class="post-body">{{ post.subhead }}</p>
                <div class="read-all-post"><span ><router-link :to="{name: 'postDetail', params: {'id': post.id}}"> 阅读全文》</router-link></span></div>
            </div>
            </div>
</template>


<script>
    // import global from './Global.vue'
    export default {
        name: 'PostAbstractList',
        props: ['posts'],
        data() {
            return {
                cData: ''
            }
        },

        // watch: {
        //     posts: function(newVal, oldVal){
        //         this.cData = newVal;
        //     }
        // }
    }
</script>

<style>

    .post-title a{
        color: #686868;
        text-decoration: none;
    }
    .post-cate {
        text-align: left;
    }

    .post-time {
        color: #808080;
    }

    .post-body {
        color: #9c9c9c;
        display: inline;
    }

    .index-post {
        margin-top: 25px;
    }

    .read-all-post span a {
        float: right;
        /* margin-bottom: 5px; */
        border: 1px solid #C8C8C8;
        font-size: 15px;
        padding: 5px 10px;
        border-radius: 7px;
        margin-right: 40px;
        text-decoration: none;
        color: #808080;
    }
    .read-all-post {
        display: inline;
    }
</style>