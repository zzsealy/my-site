<template>
    <div>
        <h1>
            {{ postId }}
        </h1>
    </div>
</template>

<script>
import {store} from '../store.js'

export default {
    
    data() {
        return {
            postId: ''
        }
    },

    methods: {
       getPostDetail(postId){
           const path = store.URL + '/post/' + postId;
           this.$axios.get(path)
            .then((res) => {
                this.postDetail = res.data;
            })
       } 
    },

    created(){
        let postId = this.$route.params.id;
        this.getPostDetail(postId);
    }
}
</script>