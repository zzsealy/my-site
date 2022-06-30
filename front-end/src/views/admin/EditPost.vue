<template>
    <div>
        <form action="post">
            <div class="form-header">
                <div class="submit-button">
                    <b-button @click="submitPost" variant="outline-primary">提交</b-button>
                    <b-form-select v-model="selected" :options="cates" size="sm" class="mt-3"></b-form-select>
                </div><br>
                <b-form-input v-model="title" type="text" placeholder="标题"></b-form-input><br>
                <b-form-input v-model="subhead" type="text" placeholder="摘要"></b-form-input><br>
            </div> <br>

            <mavon-editor ref=md v-model="body" @imgAdd="$imgAdd" @imgDel="$imgDel" />
        </form>
    </div>
</template>


<script>
    import {store} from '../store.js'
    export default {
        name: "EditPost",
        data() {
            return {
                selected: null,
                title: '',
                subhead: '',
                body: '',
                cate: '',
            };
        },
        methods: {
            getPostDataById(id) {
                let getPodtDataPath = store.URL + '/post/' + id;
                this.$axios.get(getPodtDataPath)
                    .then((res) => {
                        if (res.status == 200) {
                            let data = res.data;
                            this.title = data.title;
                            this.subhead = data.subhead;
                            this.selected = data.cate;
                            this.body = data.body;
                        }
                    })
            },
            getAllCate() {
                const path = store.URL + "/categories";
                this.$axios.get(path)
                    .then((res) => {
                        let cates = []
                        res.data.forEach(element => {
                            cates.push({ 'value': element.id, 'text': element.name })
                        });
                        this.cates = cates
                    })
            },
            submitPost() { // 提交修改
                let id = this.$route.params.id;
                const postEditPath = store.URL + '/post/' + id;
                let data = {
                    title: this.title,
                    subhead: this.subhead,
                    body: this.body,
                    cate: this.selected,
                    owner: state.user_id
                } 
                this.$axios.put(postEditPath, data)
                    .then((res) => {
                        if(res.status==200){
                            this.$router.push("/admin/post-list")
                        }
                    })
            }
        },
        created() {
            let id = this.$route.params.id;
            this.getPostDataById(id);
            this.getAllCate()
        }
    }
</script>


<style>
    .mavonEditor {
        width: 100%;
        height: 100%;
    }

    .form-header {
        width: 1000px;
        margin: 0 auto;
    }

    .submit-button {
        width: 80px;
        margin: 0 auto;
    }
</style>