<template>
    <div class="sider">
        <div>
            <span class="el-icon-search" id="search-icon"> </span>
            <el-input class="search-input" type="text" name="" id="" placeholder="Search"> </el-input>
            <!-- :prefix-icon="el-icon-search" -->
        </div>
        <div class="sider-cate-div">
            <p class="cate-title"><i class="el-icon-document-copy"></i> 文章分类</p>
            <el-divider class="divider"></el-divider>
            <div @click="cateClick(cate.name)" v-for="cate in cates" :key="cate.id" class="cate-name">
                <strong>{{cate.name}}</strong>
            </div>
        </div>
        <div v-for="nav in postNavList" :key="nav.id">
            <a class="post-nav-a" v-bind:href="'#' + nav.id ">{{ nav.title }}</a>
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
                window.console.log(val);
            },
            cateClick(cate) {
                let path = this.$route.path + '?cate=' + cate;
                this.$router.push(path);
                this.$router.go(0)
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

    .sider-cate-div {
        margin-top: 30px;
    }

    .collapse-item-cate {
        margin-left: 50px;
    }

    .cate-name {
        margin-bottom: 15px;
        margin-left: 20px;
    }

    .post-nav-a {
        color: #808080;
        text-decoration: none;
    }

    .post-nav-a:hover {
        color: black;
        text-decoration: underline;
    }

    .cate-title {
        margin-bottom: 0px;
    }

    .divider { 
        margin-top: 15px;
    }
</style>