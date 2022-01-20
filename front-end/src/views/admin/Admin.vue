    
<template>
  <div>
    <h1 v-show="clickOneManger" class="title">后台管理页面</h1>
    <div v-show="clickOneManger" class="col">
    <b-container class="bv-example-row">
      <b-row>
        <b-col @click="clickManagePost"><router-link :to="{name: 'new-post'}"> 写文章 </router-link> </b-col>
        <b-col ><router-link :to="{name: 'admin-category'}">文章类别管理</router-link></b-col>
        <b-col >个人信息管理</b-col>
      </b-row>
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
      }
  },
};
</script>


<style>
.title {
  text-align: center;
  margin-top: 20px;
}

.col {
    width: 1000px;
    margin: 0 auto;

    margin-top: 30px;
}
</style>