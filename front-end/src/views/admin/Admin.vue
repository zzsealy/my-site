    
<template>
  <div>
    <!-- <h1 v-show="clickOneManger" class="title">后台管理页面</h1> -->
    <div v-show="clickOneManger">
    <b-container class="bv-example-row">
      <!-- <b-row>
        <b-col > </b-col>
        <b-col > </b-col>
        <b-col ></b-col>
        <b-col >个人信息管理</b-col>
      </b-row> -->
      <!-- <el-row class="tac"> -->
          <h5>后台管理页面</h5>
          <el-menu
            default-active="activeIndex"
            class="el-menu-menu-demo"
            @select="handleSelect"
            mode="horizontal">
            <el-menu-item index="1"> <!-- 创建文章的时候， 隐藏导航-->
              <div @click="clickManagePost();toSubAdmin('new-post')">写文章</div>
            </el-menu-item>
            <el-menu-item index="2">
              <div slot="title" @click="toSubAdmin('post-list')">文章列表</div>
            </el-menu-item>
            <el-menu-item index="3">
              <div slot="title" @click="toSubAdmin('admin-category')">文章类别管理</div>
            </el-menu-item>
            <el-menu-item index="4">
              <div slot="title" @click="toSubAdmin('new-verse')">写个句子</div>
            </el-menu-item>
            <el-menu-item index="5">
              <div slot="title" @click="toSubAdmin('verse-cate')">短句分类</div>
            </el-menu-item>

          </el-menu>
        <!-- </el-col> -->
      <!-- </el-row> -->
    </b-container>
    </div>
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: "Admin",
  data() {
    return {
        clickOneManger: true
    };
  },
  methods: {
      clickManagePost(){
          this.clickOneManger = false;
      },
      toSubAdmin(subAdmin) {
        this.$router.push({'name': subAdmin});
      },
      popstate(){ // 回退的时候 进入这个页面，展示出来侧边导航
        this.clickOneManger = true;
      }
  },
  mounted(){
    let nowPath = this.$route.path;
    window.addEventListener('popstate', this.popstate, false);
  }
};
</script>


<style>
.title {
  text-align: center;
  margin-top: 20px;
}

.bv-example-row{
  margin-top: 20px;
}
.col {
    width: 1000px;
    margin: 0 auto;

    margin-top: 30px;
}
</style>