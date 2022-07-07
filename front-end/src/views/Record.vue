<template>
    <div class="docu-body">
        <el-row :gutter="20">
            <el-col :span="14" :offset="4" style="padding: 0px">
                <!-- <h1>1111</h1> -->
                <div v-for="(postDataList, key, index) in timePostData">
                    <h1>{{ key }}</h1>
                    <ul>
                        <li class="post-title" v-for="postData in postDataList"> <a :href="'/post/' + postData.id" >{{ postData.title }}</a></li>
                    </ul>
                </div>
            </el-col>
            <!-- document.getElementById('post-block').childNodes.length  这个是 统计元素子元素的数量-->
            <el-col :span="4" style="padding: 0px">
                <div class="divi-line" style="float: left; width: 1px; height: 1000px; background: #c8c8c8"></div>
                <sider :cates="cates" :showPostNav=false :activeName="activeName"></sider>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import PostAbstractList from "../components/Post-Abstract-List.vue";
    import Sider from "../components/Sider.vue";
    export default {
        name: 'Cate',
        components: {
            sider: Sider,
        },
        data() {
            return {
                cates: '',
                timePostData: ''
            }
        },
        methods: {
            getTimePostData(){
            const catePostByTimeUrl = this.$store.state.URL + '/time_post_data'
            let timePostData = this.$axios.get(catePostByTimeUrl)
                .then((res) => {
                    // {"year": [{"time": "title"}, {"time": "title"}] }
                    this.timePostData = res.data.time_post_data;
                })
            }
        },
        created() {
            this.getTimePostData();
        }
    }
</script>

<style>
    .post-title a{
        color: #686868;
        text-decoration: none;
    }

    .post-title :hover {
        color: #686868;
        text-decoration: underline;
    }
</style>