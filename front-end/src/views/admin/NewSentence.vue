<template>
    <div>
        <b-container>
            <textarea class="sentence-input" v-model="sentenceBody" type="text" placeholder="句子" cols="50"></textarea>
            <br>
            <b-form-input class="author-input" v-model="author" type="text" placeholder="作者"></b-form-input>
            <el-select v-model="selected">
                <el-option 
                v-for="cate in sentenceCates"
                :key="cate.name" 
                :label="cate.name" 
                :value="cate.id"></el-option>
            </el-select>
            <!-- <el-select v-model="value" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.value"
                  :value="item.value">
                </el-option>
            </el-select> -->
            <div class="submit-button">
                <b-button @click="submitSentence">提交</b-button>
            </div><br>
        </b-container>
    </div>
</template>

<script>
    export default {
        name: 'AddSentence',
        data() {
            return {
                sentenceBody: '',
                author: '',
                selected: '',
                sentenceCates: [],
                // options: [{"value":1},{"value":2}],
                // value: ''
            }
        },
        methods: {
            submitSentence(body, author, cate='all') {
                let path = this.$store.state.URL + '/sentence' + '?cate=' + cate;
                this.$axios.post(path, { 'body': this.sentenceBody, 'author': this.author, 'cate': this.selected })
                    .then((res) => {
                        let data = res.data;
                        window.console(data)
                        if (res.data.status_code == 200) {
                            this.$toasted.success('句子发表成功');
                        }
                    })
            },
            getSentenceCate(){
                let path = this.$store.state.URL + '/sentence_cates';
                this.$axios.get(path)
                    .then((res) => {
                        let sentenceCates = res.data;
                        this.sentenceCates = sentenceCates;
                        this.selected = sentenceCates[0].id
                    })
            }
        },

        created() {
            this.getSentenceCate();
        }
    }
</script>

<style>
    .sentence-input {
        height: 100px;
    }
    .author-input {
        margin-right: 10px;
        width: 500px !important;
    }
</style>