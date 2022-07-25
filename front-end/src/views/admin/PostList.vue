<template>
    <div>
        <b-alert :show="dismissCountDown" :variant="variant" dismissible v-on:dismissed="dismissCountDown = 0"
            @dismiss-count-down="countDownChanged">
            {{ message }}
        </b-alert>
        <b-container fluid class="post-list">
            <b-row>
                <b-col md="10" offset-md="2">
                    <table>
                        <tr class="table-title">
                            <th>标题</th>
                            <th>内容</th>
                            <th>
                                <el-dropdown :split-button="true" trigger="click" @command="handleCommand">
                                    <span class="">
                                        {{ nowCate }}
                                    </span>
                                    <el-dropdown-menu slot="dropdown">
                                        <el-dropdown-item command="all" icon="el-icon-circle-check">全部</el-dropdown-item>
                                        <el-dropdown-item :command="cate.name" v-for="cate in cates" :key="cate.id" icon="el-icon-circle-check">
                                        {{ cate.name }}</el-dropdown-item>
                                    </el-dropdown-menu>
                                </el-dropdown>
                            </th>
                            <th>操作</th>
                            <th>操作</th>
                        </tr>
                        <tr :class="post.class" v-for="(post, index) in posts" :key="post.id">
                            <!-- <td v-for="post in posts" :key="post"></td> -->
                            <td>{{ post.title }}</td>
                            <td>{{ post.subhead }}</td>
                            <td>{{ post.cate }}</td>
                            <td @click="goEditPage(post.id)">
                                <b-button variant="warning">编辑</b-button>
                            </td>
                            <td @click="delPost(post.id, post.title)">
                                <b-button variant="danger">删除</b-button>
                            </td>
                        </tr>
                    </table>
                    <el-pagination background :page-size="pageSize" :page-count="pageCount" layout="prev, pager, next"
                        :total="postTotalCount" @current-change="getPostByPageCate"></el-pagination>
                    </br>
                </b-col>
            </b-row>
        </b-container>

    </div>
</template>


<script>
    export default {
        name: 'PostList',
        data() {
            return {
                posts: '',
                delConfirm: '',
                variant: "",
                dismissCountDown: 0,
                dismissSecs: 5,
                pageSize: 10,
                postTotalCount: '', // 总共的文章数
                pageCount: '', // 页数
                cate: 'all', // 当前分类
                cates: '',
                nowCate: '全部'
            }
        },
        methods: {
            getPostByPageCate(page = 1) {
                let path = this.$store.state.URL + "/posts?";
                if (this.cate) {
                    path = path + "cate=" + this.cate + '&';
                }
                if (page) {
                    path = path + 'page=' + page;
                }
                path = path + '&page_size=' + this.pageSize;
                this.$axios.get(path)
                    .then((res) => {
                        let posts = []
                        res.data.forEach(element => {
                            posts.push({
                                'id': element.id,
                                'title': element.title,
                                'subhead': element.subhead,
                                'body': element.body,
                                'owner': element.owner,
                                'cate': element.cate
                            })
                        });
                        posts.forEach(function (post, index) {
                            if (index % 2 == 0) {
                                post['class'] = 'table-body'
                            } else {
                                post['class'] = ''
                            }
                        })
                        this.posts = posts
                    })
            },
            getPagingCount() {
                /*
                当前分类的页数，
                */
                let params = this.$route.query;
                let cate = params.cate || false;
                this.cate = cate;
                let pagingNumUrl = this.$store.state.URL + '/paging_data?'
                if (cate) {
                    pagingNumUrl = pagingNumUrl + "cate=" + cate;
                } else {
                    pagingNumUrl = pagingNumUrl + "cate=all";
                }
                this.$axios.get(pagingNumUrl)
                    .then((res) => {
                        this.postTotalCount = res.data.post_count;  // 文章数量
                        this.pageCount = Math.ceil(this.postTotalCount / this.pageSize) // 页数
                    })
                this.getPostByPageCate(); // 获取第一页的文章
            },

            goEditPage(id) { // 跳转到编辑文章页面
                let path = '/admin/edit-post/' + id;
                this.$router.push(path);
            },

            getCategories() {
                let catesPromise = this.common_func.getCates()
                catesPromise.then((res) => { this.cates = res.data})
            },

            delPost(id, title) {
                this.$bvModal.msgBoxConfirm('删除:' + title, + '?', {
                    okTitle: '确定',
                    cancelTitle: '取消'
                })
                    .then(value => {
                        if (value == true) {
                            const delPath = this.$store.state.URL + '/post';
                            let data = { 'id': id }
                            this.$axios.delete(delPath, { 'data': data })
                                .then((res) => {
                                    if (res.status == 200) {
                                        this.message = res.data.message;
                                        this.variant = "success";
                                        this.showAlert();
                                        this.getPostByPageCate();
                                    }
                                })
                        }
                    })
                // .catch(err => {
                //     // An error occurred
                // })
            },
            countDownChanged(dismissCountDown) {
                this.dismissCountDown = dismissCountDown;
            },
            showAlert() {
                this.dismissCountDown = this.dismissSecs;
            },

            handleCommand(cate) {
                // let nowPath = this.$route.path + '?cate=' + cate;
                // this.$router.push(nowPath);
                if(cate == 'all'){
                    this.$router.push({name: 'post-list'})
                } else {
                    this.$router.push({name: 'post-list', query: {cate:cate}})
                }
                this.$router.go(0)
                
            }
        },
        created() {
            this.getPagingCount();
            this.getCategories();
            let nowCate = this.$route.query.cate;
            if(nowCate) {

                this.nowCate = nowCate;
            }
        }
    }
</script>


<style>
    .post-list {
        margin-top: 100px;
    }

    .table-title {
        border: 1px solid;
        border-style: hidden hidden solid hidden;
    }

    .table-body {
        background-color: #DCDCDC;
    }
</style>