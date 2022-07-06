<template>
    <div class="docu-body">
        <!-- <input class="search_input" type="text" v-model="searchValue">
            <b-button @click="search" variant="outline-primary" class="search_button">搜索</b-button> -->
        <el-row :gutter="20">
            <el-col :span="14" :offset="4" style="padding: 0px">
                <h1>1111</h1>
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
            postabstract: PostAbstractList,
            sider: Sider,
        },
        data() {
            return {
                cates: ''
            }
        },
        methods: {
            // getTimePostData(){
            // const catePostByTimeUrl = global.URL + '/time_post_data'
            // let timePostData = this.$axios.get(catePostByTimeUrl)
            //                     .then((res) => {
            //                         // {"year": [{"time": "title"}, {"time": "title"}] }
            //                         window.console.log(res)
            //                     })
            // }
        },
        created() {
            // this.getTimePostData();
        }
    }
</script>