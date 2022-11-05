<template>
    <div>
        <b-container>
            <textarea class="verse-input" v-model="verseBody" type="text" placeholder="句子" cols="50"></textarea>
            <br>
            <b-form-input class="author-input" v-model="author" type="text" placeholder="作者"></b-form-input>
            <el-select v-model="selected">
                <el-option 
                v-for="cate in verseCates"
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
            <b-button v-show="showEditButton" class="edit-button" @click="editVerseSubmit">提交修改</b-button>
            <b-button v-show="showCreateButton" class="submit-button" @click="createVerse">提交</b-button>
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
                <tr :class="verse.class" v-for="(verse, index) in verses" :key="verse.id">
                    <!-- <td v-for="post in posts" :key="post"></td> -->
                    <td>{{ verse.body }}</td>
                    <td>{{ verse.author }}</td>
                    <td>{{ verse.cate_name }}</td>
                    <td @click="setEditVerse(verse.id, verse.body, verse.author, verse.cate)">
                        <b-button variant="warning">编辑</b-button>
                    </td>
                    <td @click="delVerse(verse.id)">
                        <b-button variant="danger">删除</b-button>
                    </td>
                </tr>
            </table>
        </b-container>
    </div>
</template>

<script>
    export default {
        name: 'AddVerse',
        data() {
            return {
                showEditButton: false,
                showCreateButton: true,
                verseId: '',
                verseBody: '',
                author: '',
                selected: '',
                verseCates: [],
                verses: '',
                mapCateIdCateName: ''
                // options: [{"value":1},{"value":2}],
                // value: ''
            }
        },
        methods: {
            createVerse(body, author, cate='all') {
                let path = this.$store.state.URL + '/verse/';
                this.$axios.post(path, { 'body': this.verseBody, 'author': this.author, 'cate_id': this.selected })
                    .then((res) => {
                        let data = res.data;
                        if (res.status == 200) {
                            this.$toasted.success('句子发表成功');
                            window.location.reload();
                        }
                    })
            },
            getVerseCate(){
                // 获取所有的 句子分类
                let path = this.$store.state.URL + '/verse_cates/';
                this.$axios.get(path)
                    .then((res) => {
                        let verseCates = res.data;
                        this.verseCates = verseCates;
                        this.selected = verseCates[0].id;  // 因为是创建新的句子，给新句子选择的分类直接是第一个

                        let mapCateIdCateName = new Map();
                        for(let i=0; i < verseCates.length; i++) {
                            mapCateIdCateName.set(verseCates[i].id, verseCates[i].name)
                        }
                        this.mapCateIdCateName = mapCateIdCateName;
                    })
            },
            getVerses(cate=''){
                let path = this.$store.state.URL + '/verses/' + '?cate=' + cate;
                this.$axios.get(path)
                    .then((res) => {
                        let verses = res.data;

                        for (let i = 0; i < verses.length; i++){
                            verses[i]['cate_name'] = this.mapCateIdCateName.get(verses[i].cate_id);
                        } // 把 cate_name 拼进来

                        this.verses = verses;
                    })
            },
            setEditVerse(verseId, verseBody, verseAuthor, verseCate) {
                this.verseId = verseId;
                this.verseBody = verseBody;
                this.author = verseAuthor;
                this.selected = verseCate;
                this.showEditButton = true;
                this.showCreateButton = false;
            },
            editVerseSubmit() {
                let path = this.$store.state.URL + '/verse/' + this.verseId + '/';
                let postData = {'body': this.verseBody, 'author': this.author, 'cate': this.selected}
                this.$axios.put(path, postData)
                    .then((res) => {
                        if(res.status == 200){
                            this.$toasted.success('修改句子成功!');
                            this.getVerse()
                        } else {
                            window.console.log("失败！！！！！！！！！")
                            this.$toasted.error('更新失败')
                        }
                    })
            },
            delVerse (verseId) {
                let path = this.$store.state.URL + '/verse/' + verseId + '/';
                this.$axios.delete(path)
                    .then((res) => {
                        if( res.status == 200 ) {
                            this.$toasted.success('删除句子成功!');
                            window.location.reload();
                        } else {
                            this.$toasted.success('删除句子失败!');
                            this.getVerse()
                        }
                    })
            }
        },

        created() {
            this.getVerseCate();
            this.getVerses();
        }
    }
</script>

<style>
    .verse-input {
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