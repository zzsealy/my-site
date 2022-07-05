<template>
    <div>
        <b-alert
        :show="dismissCountDown"
        :variant="variant"
        dismissible
        v-on:dismissed="dismissCountDown = 0"
        @dismiss-count-down="countDownChanged"
        >
            {{ message }}
        </b-alert>
        <b-container fluid class="post-list">
            <b-row>
                <b-col md="10" offset-md="2">
                    <table>
                        <tr class="table-title">
                            <th>标题</th>
                            <th>内容</th>
                            <th>分类</th>
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
            }
        },
        methods: {
            getAllPost() {
                const path = this.$store.state.URL + "/posts";
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
            goEditPage(id) {
                let path = '/admin/edit-post/' + id
                this.$router.push(path);
            },
            
            delPost(id, title) {
                this.$bvModal.msgBoxConfirm('删除:' + title, + '?', {
                    okTitle: '确定',
                    cancelTitle: '取消'
                })
                    .then(value => {
                        if(value==true){
                            const delPath = this.$store.state.URL + '/post';
                            let data = {'id':id}
                            this.$axios.delete(delPath, {'data': data})
                                .then((res) => {
                                    if(res.status==200){
                                        this.message = res.data.message;
                                        this.variant = "success";
                                        this.showAlert();
                                        this.getAllPost();
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
        },
        created() {
            this.getAllPost();
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