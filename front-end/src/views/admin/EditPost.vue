<template>
    <div>
        <form action="post">
            <div class="form-header">
                <div class="submit-button">
                    <b-button @click="submitPost" variant="outline-primary">提交</b-button>
                    <el-select v-model="selected">
                        <el-option 
                        v-for="cate in cates"
                        :key="cate.name" 
                        :label="cate.name" 
                        :value="cate.id"></el-option>
                    </el-select>
                </div><br>
                <b-form-input v-model="title" type="text" placeholder="标题"></b-form-input><br>
                <b-form-input v-model="subhead" type="text" placeholder="摘要"></b-form-input><br>
            </div> <br>
            <MyEditor
                :html="html"
                @getHtml="getHtml"
            ></MyEditor>
        </form>
    </div>

</template>


<script>
    import MyEditor from './MyEditor'
    export default {
        name: "EditPost",
        components: {
            MyEditor
        },
        data() {
            return {
                selected: null,
                title: '',
                subhead: '',
                cate: '',
                cates: '',
                editor: null,
                html: '',
                text:'',
                mode: 'default', // or 'simple'
            };
        },
        methods: {
            getPostDataById(id) {
                let getPodtDataPath = this.$store.state.URL + '/post/' + id + '/';
                this.$axios.get(getPodtDataPath)
                    .then((res) => {
                        if (res.status == 200) {
                            let data = res.data;
                            this.title = data.title;
                            this.subhead = data.subhead;
                            this.selected = data.cate;
                            this.html = data.body;
                        }
                    })
            },
            getHtml(html){
                this.html = html;
            },
            // onChange(editor) {
            //     const html = editor.getHtml();
            //     this.html = html;
            // },
            getAllCate() {
                const path = this.$store.state.URL + "/categories";
                this.$axios.get(path)
                    .then((res) => {
                        let cates = []
                        res.data.forEach(element => {
                            cates.push({ 'value': element.id, 'name': element.name })
                        });
                        this.cates = cates
                    })
            },
            submitPost() { // 提交修改
                let id = this.$route.params.id;
                const postEditPath = this.$store.state.URL + '/post/' + id + '/';
                let data = {
                    title: this.title,
                    subhead: this.subhead,
                    body: this.html,
                    cate: this.selected,
                } 
                this.$axios.put(postEditPath, data)
                    .then((res) => {
                        if(res.status==200){
                            this.$router.push("/admin/post-list")
                        }
                    })
            },
            onCreated(editor) {
                this.editor = Object.seal(editor) // 一定要用 Object.seal() ，否则会报错
            },
        },
        created() {
            let id = this.$route.params.id;
            this.getPostDataById(id);
            this.getAllCate()
        },
        beforeDestroy() {
            const editor = this.editor
            if (editor == null) return
            editor.destroy() // 组件销毁时，及时销毁编辑器
        }
    }
</script>


<style>

    .form-header {
        width: 1000px;
        margin: 0 auto;
    }

    .submit-button {
        width: 80px;
        margin: 0 auto;
    }
</style>