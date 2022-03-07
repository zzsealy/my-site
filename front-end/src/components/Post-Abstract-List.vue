<template>
        <b-col md="8">
            <div class="index-post" v-for="(post, index) in posts" :key="post.id">
                <h2>{{ post.title }}</h2>
                <p class="post-body">{{ post.subhead }}</p>
                <strong>分类: </strong><span class="post-cate">{{ post.cate }}</span>
                <span class="post-time">{{ post.created }}</span>
            </div>
        </b-col>
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
    .post-cate{
        color: #6699ff;
    }
</style>