<template>
    <div class="sider">
        <div>
        <span class="el-icon-search" id="search-icon"> </span>
        <el-input  class="search-input" type="text" name="" id=""  placeholder="Search"> </el-input>
        <!-- :prefix-icon="el-icon-search" -->
        </div>
        <div v-for="cate in cates" :key="cate.id">
            <p>{{cate}}</p>
        </div>
    </div>
</template>


<script>
export default {
    name: 'Sider',
    props: ['cates'],
    data() {

    },
    methods: {
        
    }
}
</script>

<style>
.sider {
    margin-left: 25px;
}

.search-input {
    border-radius: 5px;
    border: #808080 1px solid;
    width: 60%;
}


#search-icon {
    position: absolute;
    top: 7px;
    left: 1px;
}



</style>