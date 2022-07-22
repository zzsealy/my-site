<template>
  <div class="docu-body">
    <!-- <input class="search_input" type="text" v-model="searchValue">
        <b-button @click="search" variant="outline-primary" class="search_button">搜索</b-button> -->
    <el-row :gutter="20">
      <el-col :span="14" :offset="4" style="padding: 0px">
        <postabstract :posts="posts"></postabstract>
        <el-pagination background :page-size="pageSize" :page-count="pageCount" layout="prev, pager, next" :total="postTotalCount"
        @current-change="getPostByPageCate"></el-pagination>
      </el-col>
      <!-- document.getElementById('post-block').childNodes.length  这个是 统计元素子元素的数量-->
      <el-col :span="4" style="padding: 0px">
        <div
          class="divi-line"
          style="float: left; width: 1px; height: 1000px; background: #c8c8c8"
        ></div>
        <sider :cates="cates" :showPostNav=false :activeName="activeName"></sider>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import PostAbstractList from "../components/Post-Abstract-List.vue";
import Sider from "../components/Sider.vue";
export default {
  name: "Home",
  components: {
    postabstract: PostAbstractList,
    sider: Sider,
  },
  data() {
    return {
      posts: "",
      imagePath: "",
      searchValue: "",
      cates: '',
      activeName: ['1'],
      pageSize: 10,
      postTotalCount: '', // 总共的文章数
      pageCount: '', // 页数
      cate: 'all' // 当前分类
    };
  },

  mounted() {
    this.getPagingCount(); // 获取当前分类下的总文章数
    this.setProfileImage();
    this.getCategories();
  },

  methods: {
    getPostByPageCate(page=1) {
      let path = this.$store.state.URL + "/posts?";
      if(this.cate){
        path = path + "cate=" + this.cate + '&';
      }
      if(page){
          path = path + 'page=' + page;
      }
      path = path + '&page_size=' + this.pageSize;
      this.$axios.get(path).then((res) => {
        let posts = [];
        res.data.forEach((element) => {
          posts.push({
            id: element.id,
            title: element.title,
            subhead: element.subhead,
            body: element.body,
            owner: element.owner,
            cate: element.cate,
            created: element.created,
          });
        });
        posts.forEach(function (post, index) {
          if (index % 2 == 0) {
            post["class"] = "table-body";
          } else {
            post["class"] = "";
          }
        });
        this.posts = posts;
      });
    },
    getCategories() {
      let catesPromise = this.common_func.getCates()
      catesPromise.then((res) => { this.cates = res.data})
    },
    getPagingCount() {
      /*
      当前分类的页数，
      */
      let params = this.$route.query;
      let cate = params.cate||false;
      this.cate = cate;
      let pagingNumUrl = this.$store.state.URL + '/paging_data?'
      if(cate){
        pagingNumUrl = pagingNumUrl + "cate=" + cate;
      } else {
        pagingNumUrl = pagingNumUrl + "cate=all";
      }
      this.$axios.get(pagingNumUrl)
        .then((res) => {
          this.postTotalCount = res.data.post_count;  // 文章数量
          this.pageCount = Math.ceil(this.postTotalCount/this.pageSize) // 页数
        })
      this.getPostByPageCate(); // 获取第一页的文章
    },
    search() {
      const searchPath = this.$store.state.URL + "/posts";
      this.$axios
        .post(searchPath, { searchValue: this.searchValue })
        .then((res) => {
          this.handleSearchResult(res.data.search_result_list);
        });
    },

    handleSearchResult(searchResultList) {
      let posts = [];
      if (searchResultList.length > 0) {
        searchResultList.forEach((result) => {
          posts.push({
            id: result._id,
            title: result._source.title,
            subhead: result._source.subhead,
            body: result._source.body,
            cate: result._source.cate,
            created: result._source.created,
          });
        });
      } else {
        posts = [
          {
            title: "搜索结果为空！！！！！",
          },
        ];
      }
      this.posts = posts;
    },
    setProfileImage() {
      this.imagePath = this.$store.state.URL + "/media/" + "profile-photo.jpg";
    },
  },
};
</script>


<style>
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

.divi-line {
  margin-left: 3.5px;
}

.docu-body {
  margin-top: 20px;
}
</style>