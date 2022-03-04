<template>
    <div>
        <b-container fluid>
            <b-row>
                </b-col md="2">
                <b-card title="DRQ丶" :img-src="imagePath" img-alt="Image" img-top tag="article"
                    style="width: 300px; height: 280px;" class="mb-2">
                    <b-card-text>
                    </b-card-text>
                </b-card>
                </b-col>
                <b-col md="8">
                    <div class="index-post" v-for="(post, index) in posts" :key="post.id">
                        <h2>{{ post.title }}</h2>
                        <p class="post-body">{{ post.subhead }}</p>
                        <span class="post-cate">分类: {{ post.cate }}</span>
                        <span class="post-time">{{ post.created }}</span>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>
<script>
    import global from './Global.vue'
    export default ({
        name: 'Home',
        data() {
            return {
                posts: '',
                imagePath: ''

            };
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
            setProfileImage() {
                this.imagePath = global.URL + '/media/' + 'profile-photo.jpg';
            }

        },
        created() {
            this.getAllPost();
            this.setProfileImage();
        }

    })
</script>


<style>
.index-post {
    border-bottom: 1px dashed rgba(0,0,0,0.2);
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
</style>