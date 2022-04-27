<template>
    <div class="docu-body">
        <!-- <input class="search_input" type="text" v-model="searchValue">
        <b-button @click="search" variant="outline-primary" class="search_button">搜索</b-button> -->
        <el-row :gutter="20">
            <el-col :span="14" :offset="4" style="padding: 0px;">
                <postabstract :posts="posts"></postAbstract>
            </el-col>
            <!-- document.getElementById('post-block').childNodes.length  这个是 统计元素子元素的数量-->
            <el-col :span="4" style="padding: 0px;">
                <div class="divi-line" style="float:left;width: 1px;height: 1000px; background: #C8C8C8;"></div>
                <sider></sider>
            </el-col>
        </el-row>

    </div>
</template>
<script>
    import global from './Global.vue'
    import PostAbstractList from '../components/Post-Abstract-List.vue'
    import Sider from '../components/Sider.vue'
    export default {
        name: 'Home',
        components: {
            postabstract: PostAbstractList,
            sider: Sider
        },
        data() {
            return {
                posts: '分角色附件二十、',
                imagePath: '',
                searchValue: ''
            };
        },

        mounted() {
            this.getAllPost();
            this.setProfileImage();
        },

        methods: {
            getAllPost() {
                const path = global.URL + "/posts";
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
                                'cate': element.cate,
                                'created': element.created
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
            search() {
                const searchPath = global.URL + "/posts";
                this.$axios.post(searchPath, { 'searchValue': this.searchValue })
                    .then((res) => {
                        this.handleSearchResult(res.data.search_result_list);
                    })

            },

            handleSearchResult(searchResultList) {
                let posts = [];
                if (searchResultList.length > 0) {
                    searchResultList.forEach(result => {
                        posts.push({
                            'id': result._id,
                            'title': result._source.title,
                            'subhead': result._source.subhead,
                            'body': result._source.body,
                            'cate': result._source.cate,
                            'created': result._source.created
                        })
                    })
                } else {
                    posts = [{
                        'title': '搜索结果为空！！！！！'
                    }]
                }


                this.posts = posts;
            },
            setProfileImage() {
                this.imagePath = global.URL + '/media/' + 'profile-photo.jpg';
            }

        },

    }
</script>


<style>
    .search_input {
        height: 35px;
        margin: 10px !important;
        border: #4569ff 1px solid;
    }

    .search_button {
        height: 35px;
        /* margin-top: 10px !important; */
        color: cadetblue;
    }

    .divi-line {
        margin-left: 3.5px;
    }

    .docu-body {
        margin-top: 20px;
    }
</style>