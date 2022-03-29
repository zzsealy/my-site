<template>
    <div>
        <form action="post">
            <div class="form-header">
                <div class="submit-button">
                    <b-button @click="submitPost" variant="outline-primary">提交</b-button>
                    <b-form-select v-model="selected" :options="cates" size="sm" class="mt-3"></b-form-select>
                </div><br>
                <b-form-input v-model="postTitle" type="text" placeholder="标题"></b-form-input><br>
                <b-form-input v-model="postSubhead" type="text" placeholder="摘要"></b-form-input><br>
            </div> <br>

            <mavon-editor ref=md v-model="postBody" @imgAdd="$imgAdd" @imgDel="$imgDel" />
        </form>
    </div>
</template>


<script>
    import global from '../Global.vue'
    export default {
        name: "EditPost",
        data() {
            return {
                selected: null,
                postTitle: '',
                postSubhead: '',
                postBody: '',
                cates: '',
            };
        },
        methods: {
            getPostDataById(id) {
                let getPodtDataPath = global.URL + '/post/' + id;
                this.$axios.get(getPodtDataPath)
                    .then((res) => {
                        if (res.status == 200) {
                            let data = res.data;
                            this.postTitle = data.title;
                            this.postSubhead = data.subhead;
                            this.selected = data.cate_id;
                            this.postBody = data.body;
                        }
                    })
            },
            getAllCate() {
                const path = global.URL + "/categories";
                this.$axios.get(path)
                    .then((res) => {
                        let cates = []
                        res.data.forEach(element => {
                            cates.push({ 'value': element.id, 'text': element.name })
                        });
                        this.cates = cates
                    })
            },
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