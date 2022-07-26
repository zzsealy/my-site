<template>
    <div>
        <b-form-input v-model="sentenceBody" type="text" placeholder="句子"></b-form-input><br>
        <b-form-input v-model="author" type="text" placeholder="作者"></b-form-input><br>
    </div>
</template>

<script>
export default {
    name: 'AddSentence',
    data() {
        return {

        }
    },
    methods: {
        addSentence(body, author, cate){
            let path = this.$store.state.URL + '/sentence';
            this.$axios.post(path , {'body': body, 'author': author, 'cate': cate})
                .then((res) => {
                    data = res.data;
                    if(res.data.status_code == 200){
                        this.$toasted.success('句子发表成功');
                    }
                })
        }
    }
}
</script>

<style>

</style>