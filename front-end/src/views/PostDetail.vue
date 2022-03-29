<template>
    <div>
        <b-container fluid>
            <b-row>
                </b-col md="2">
                <b-card title="DRQ丶" :img-src="imagePath" img-alt="Image" img-top
                    tag="article" style="width: 300px; height: 280px;" class="mb-2">
                    <b-card-text>
                        
                    </b-card-text>
                </b-card>
                </b-col>
                <b-col md="8" >
                    <h1>{{ postTitle }}</h1>
                    <p v-html="postBody"></p>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>
<script>
    import global from './Global.vue'
    import { mavonEditor } from 'mavon-editor'
    export default ({
        name: 'PostDetail',
        data() {
            return {
                postTitle: '',
                postSubhead: '',
                postBody: '',
                imagePath: ''
            };
        },
        methods: {
            getPostDetail(id) {
                let postDetailPath = global.URL + '/post/' + id;
                this.$axios.get(postDetailPath)
                    .then((res) => {
                        let data = res.data;
                        this.postTitle = data.title;
                        this.postSubhead = data.subhead;
                        const markdownIt = mavonEditor.getMarkdownIt()
                        this.postBody = markdownIt.render(data.body);
                    })
            },
            setProfileImage(){
                this.imagePath = global.URL + '/media/' + 'profile-photo.jpg';
            }
        },

        created() {
            let id = this.$route.params.id;
            this.getPostDetail(id);
            this.setProfileImage();
        }

    })
</script>


<style>
.card-img-top {
    width:  286px !important;
    height: 280px;
}
</style>