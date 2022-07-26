<template>
    <div class="docu-body">
        <el-row :gutter="20">
            <el-col :span="14" :offset="4" style="padding: 0px">
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


export default({
    name: 'Sentence',
    data() {
            return {
        }
    },
    methods: {
        
    },

})
</script>


<style>

</style>
