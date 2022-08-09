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
            <b-button v-show="showEditButton" class="edit-button" @click="editSentenceSubmit">提交修改</b-button>
            <b-button v-show="showCreateButton" class="submit-button" @click="createSentence">提交</b-button>
            <table>
                <tr class="table-title">
                    <th>句子</th>
                    <th>作者</th>
                    <th>
                        <!-- <el-dropdown :split-button="true" trigger="click" @command="handleCommand">
                            <span class="">
                                {{ nowCate }}
                            </span>
                            <el-dropdown-menu slot="dropdown">
                                <el-dropdown-item command="all" icon="el-icon-circle-check">全部</el-dropdown-item>
                                <el-dropdown-item :command="cate.name" v-for="cate in cates" :key="cate.id" icon="el-icon-circle-check">
                                {{ cate.name }}</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown> -->
                        类别
                    </th>
                    <th>操作</th>
                    <th>操作</th>
                </tr>
                <tr :class="sentence.class" v-for="(sentence, index) in sentences" :key="sentence.id">
                    <!-- <td v-for="post in posts" :key="post"></td> -->
                    <td>{{ sentence.body }}</td>
                    <td>{{ sentence.author }}</td>
                    <td>{{ sentence.cate_name }}</td>
                    <td @click="setEditSentence(sentence.id, sentence.body, sentence.author, sentence.cate)">
                        <b-button variant="warning">编辑</b-button>
                    </td>
                    <td @click="delPost(post.id, post.title)">
                        <b-button variant="danger">删除</b-button>
                    </td>
                </tr>
            </table>
        </b-container>
    </div>
</template>

<script>
    export default {
        name: 'AddSentence',
        data() {
            return {
                showEditButton: false,
                showCreateButton: true,
                sentenceId: '',
                sentenceBody: '',
                author: '',
                selected: '',
                sentenceCates: [],
                sentences: ''
                // options: [{"value":1},{"value":2}],
                // value: ''
            }
        },
        methods: {
            createSentence(body, author, cate='all') {
                let path = this.$store.state.URL + '/sentence' + '?cate=' + cate;
                this.$axios.post(path, { 'body': this.sentenceBody, 'author': this.author, 'cate': this.selected })
                    .then((res) => {
                        let data = res.data;
                        if (res.status == 200) {
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
                        this.selected = sentenceCates[0].id;
                    })
            },
            getSentence(cate=''){
                let path = this.$store.state.URL + '/sentences';
                this.$axios.get(path)
                    .then((res) => {
                        let sentences = res.data;
                        this.sentences = sentences;
                    })
            },
            setEditSentence(sentenceId, sentenceBody, sentenceAuthor, sentenceCate) {
                this.sentenceId = sentenceId;
                this.sentenceBody = sentenceBody;
                this.author = sentenceAuthor;
                this.selected = sentenceCate;
                this.showEditButton = true;
                this.showCreateButton = false;
            },
            editSentenceSubmit() {
                debugger;
                let path = this.$store.state.URL + '/sentence/' + this.sentenceId;
                let postData = {'body': this.sentenceBody, 'author': this.author, 'cate': this.selected}
                this.$axios.put(path, postData)
                    .then((res) => {
                        if(res.status == 200){
                            this.$toasted.success('修改句子成功!');
                            this.getSentence()
                        } else {
                            window.console.log("失败！！！！！！！！！")
                            this.$toasted.error('更新失败')
                        }
                    })
            }
        },

        created() {
            this.getSentenceCate();
            this.getSentence();
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
    .submit-button {
        margin-left: 10px;
    }
</style>