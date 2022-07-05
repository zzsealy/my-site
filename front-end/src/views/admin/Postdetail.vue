<template>
    <div>
        <h1>
            {{ postId }}
        </h1>
    </div>
</template>

<script>

export default {
    
    data() {
        return {
            postId: ''
        }
    },

    methods: {
       getPostDetail(postId){
           const path = this.$store.state.URL + '/post/' + postId;
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