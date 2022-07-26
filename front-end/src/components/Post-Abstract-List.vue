<template>
    <div>
            <div class="index-post" v-for="(post, index) in posts" :key="post.id">
                <h2 class="post-title"><a :href="'post/' + post.id"> {{ post.title }} </a></h2>
                <div><span class="post-time"><i class="el-icon-date"></i>{{ post.created }}</span></div>
                <p class="post-subhead">{{ post.subhead }}</p>
                <div class="read-all-post"><span ><a :href="'post/' + post.id"> 阅读全文》</a></span></div>
            </div>
            <el-divider></el-divider>
            </div>
</template>


<script>
    // import global from './store.js'
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
        color: #000000;
        text-decoration: none;
    }
    .post-cate {
        text-align: left;
    }

    .post-time {
        color: #808080;
        margin-left: 5px;
    }

    .post-subhead {
        color: #3a3535;
        display: inline;
        /* margin-left: 10px; */
    }

    .index-post {
        margin-bottom: 45px;
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