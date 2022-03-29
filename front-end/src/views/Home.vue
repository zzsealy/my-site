<template>
    <div>
        <input class="search_input" type="text" v-model="searchValue">
        <b-button @click="search" variant="outline-primary" class="search_button">搜索</b-button>
        <b-container fluid>
            <b-row>
                </b-col md="2">
                <b-card title="DRQ丶" :img-src="imagePath" img-alt="Image" img-top tag="article"
                    style="width: 300px; height: 280px;" class="mb-2">
                    <b-card-text>
                    </b-card-text>
                </b-card>
                </b-col>
                <!-- <b-col md="8">
                    <div class="index-post" v-for="(post, index) in posts" :key="post.id">
                        <h2>{{ post.title }}</h2>
                        <p class="post-body">{{ post.subhead }}</p>
                        <span class="post-cate">分类: {{ post.cate }}</span>
                        <span class="post-time">{{ post.created }}</span>
                    </div>
                </b-col> -->
                <postabstract :posts="posts"></postAbstract>
            </b-row>
        </b-container>

    </div>
</template>
<script>
    import global from './Global.vue'
    import PostAbstractList from '../components/Post-Abstract-List.vue'
    export default {
        name: 'Home',
        components: {
            postabstract: PostAbstractList
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
    .index-post {
        border-bottom: 1px dashed rgba(0, 0, 0, 0.2);
    }

    .post-cate {
        text-align: left;
    }

    .post-time {
        float: right;
    }

    .post-body {
        color: #9c9c9c;
    }

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
</style>