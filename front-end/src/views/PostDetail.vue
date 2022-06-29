<template>
  <div class="docu-body">
    <el-row :gutter="20">
      <el-col :span="14" :offset="4">
        <h1 style="margin-top: 20px">{{ postTitle }}</h1>
        <p v-html="postBody"></p>
      </el-col>
      <el-col :span="4" style="padding: 0px">
        <div
          class="divi-line"
          style="float: left; width: 1px; height: 1000px; background: #c8c8c8"
        ></div>
        <sider :cates="cates" :showPostNav=true :postNavList="postNavList" :activeName="activeName"></sider>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import store from "./store.js";
import { mavonEditor } from "mavon-editor";
import Sider from "../components/Sider.vue";
export default {
  name: "PostDetail",
  components: {
    sider: Sider,
  },
  data() {
    return {
      postTitle: "",
      postSubhead: "",
      postBody: "",
      imagePath: "",
      cates: "",
      postNavList: "",
      activeName: ['2']
    };
  },
  methods: {
    getPostDetail(id) {
      let postDetailPath = store.URL + "/post/" + id;
      this.$axios.get(postDetailPath).then((res) => {
        let data = res.data;
        this.postTitle = data.title;
        this.postSubhead = data.subhead;
        const markdownIt = mavonEditor.getMarkdownIt();
        this.postBody = markdownIt.render(data.body);
        this.postNavList = this.createPostNavList();
      });
    },
    setProfileImage() {
      this.imagePath = store.URL + "/media/" + "profile-photo.jpg";
    },
    getCategories() {
      let catesPromise = this.common_func.getCates()
      catesPromise.then((res) => { this.cates = res.data})
    },
    createPostNavList() {
      let navList = []
      let h2IdList = this.postBody.match(/_\d{1,5}/g);
      h2IdList.forEach(h2Id => {
        let befor = h2Id + "\"></a>";
        let splitBefore = this.postBody.split(befor);
        let title = splitBefore[1].split('<')[0];
        navList.push({'id': h2Id, 'title': title})
      });
      return navList

    }
  },

  created() {
    let id = this.$route.params.id;
    this.getPostDetail(id);
    this.setProfileImage();
  },

  mounted() {
    this.getCategories();
  }
};
</script>


<style>
.card-img-top {
  width: 286px !important;
  height: 280px;
}
.divi-line {
  margin-left: 3.5px;
}

.search_input {
  height: 35px;
  margin: 10px !important;
  border: #4569ff 1px solid;
}

.search_button {
  height: 35px;
  /* margin-top: 10px !important; */
  color: cadetblue;
}

.docu-body {
  margin-top: 20px;
}
</style>