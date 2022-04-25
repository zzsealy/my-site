<template>
        <el-row>
            <el-col :span="18" class="grid-content">
            <div class="index-post" v-for="(post, index) in posts" :key="post.id">
                <h2 class="post-title"><router-link :to="{name: 'postDetail', params: {'id': post.id}}"> {{ post.title }} </router-link></h2>
                <span class="post-time">{{ post.created }}</span>
                <p class="post-body">{{ post.subhead }}</p>
                <div class="read-all-post"><span >阅读全文》</span></div>
            </div>
            </el-col>
        </el-row>
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

    .read-all-post {
        float: right;
        margin-bottom: 5px;
        display: inline;
    }
</style>