<template>
    <div class="sider">
        <div>
            <span class="el-icon-search" id="search-icon"> </span>
            <el-input class="search-input" type="text" name="" id="" placeholder="Search"> </el-input>
            <!-- :prefix-icon="el-icon-search" -->
        </div>
        <div class="sider-cate-text">
            <el-collapse v-model="activeNames" @change="handleChange">
                <el-collapse-item title="分类" name="1">
                    <div v-for="cate in cates" :key="cate.id">
                        {{cate.name}}
                    </div>
                </el-collapse-item>
                <el-collapse-item v-if="showPostNav" title="文章导航" name="2" @change="handleChange">
                    <div v-for="nav in postNavList" :key="nav.id">
                        <a class="post-nav-a" v-bind:href= "'#' + nav.id ">{{ nav.title }}</a>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </div>

    </div>
</template>


<script>
    export default {
        name: 'Sider',
        props: ['cates', 'showPostNav', 'postNavList', 'activeName'],
        data() {
            return {
                activeNames: this.activeName,
                showPostNav: this.showPostNav
            }
        },
        methods: {
            handleChange(val) {
                console.log(val);
            }
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

    .sider-cate-text {
        margin-top: 20px;
    }

    .post-nav-a {
        color: #808080;
        text-decoration: none;
    }
    .post-nav-a:hover {
        color: black;
        text-decoration: underline;
    }
</style>