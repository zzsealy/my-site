<template>
  <div>
    <form action="post">
      <div class="form-header">
        <div class="submit-button">
          <b-button @click="submitPost" variant="outline-primary">提交</b-button>
          <b-form-select v-model="selected" :options="cates" size="sm" class="mt-3"></b-form-select>
        </div><br>
        <b-form-input v-model="postTitle" type="text" placeholder="标题"></b-form-input><br>
        <b-form-input v-model="postSubhead" type="text" placeholder="摘要"></b-form-input><br>
      </div> <br>

      <mavon-editor ref=md v-model="postBody" @imgAdd="$imgAdd" @imgDel="$imgDel" />
    </form>
  </div>
</template>


<script>
  export default {
    name: "Addpost",
    data() {
      return {
        selected: null,
        postTitle: '',
        postSubhead: '',
        postBody: '',
        cates: '',
      };
    },
    methods: {
      submitPost() {
        let postData = {
          'title': this.postTitle,
          'subhead': this.postSubhead,
          'body': this.postBody,
          'cate_id': this.selected,
          'owner_id': this.$store.state.user_id
        }
        const path = this.$store.state.URL + '/post';
        this.$axios.post(path, postData)
          .then((res) => {
            window.console.log(res);
            this.$toasted.success('文章发布成功');
          })

      },
      getAllCate(){
        const path = this.$store.state.URL + "/categories";
        this.$axios.get(path)
          .then((res) => {
            let cates = []
            res.data.forEach(element => {
              cates.push({ 'value': element.id, 'text': element.name })
            });
            this.cates = cates
          })
      },
      $imgAdd(pos, $file){
            // 第一步.将图片上传到服务器.
           var formdata = new FormData();
           formdata.append('image', $file);
           const imageUrl = this.$store.state.URL + '/postimage'
           let backendUrl = this.$store.state.URL;
           this.$axios({
               url: imageUrl,
               method: 'post',
               data: formdata,
               headers: { 'Content-Type': 'multipart/form-data' },
           }).then((res) => {
               // 第二步.将返回的url替换到文本原位置![...](0) -> ![...](url)
               /**
               * $vm 指为mavonEditor实例，可以通过如下两种方式获取
               * 1. 通过引入对象获取: `import {mavonEditor} from ...` 等方式引入后，`$vm`为`mavonEditor`
               * 2. 通过$refs获取: html声明ref : `<mavon-editor ref=md ></mavon-editor>，`$vm`为 `this.$refs.md`
               */
              let url = backendUrl + res.data.url;
              this.$refs.md.$img2Url(pos, url);
           })
        },
        $imgDel(pos){
          let name = pos[1].name;
          let delData = {'name':name}
          const imageUrl = this.$store.state.URL + '/postimage';
          this.$axios.delete(imageUrl, {'data': delData})
            .then((data) => {
            window.console.log(data.message)
          })
        }
    },
    created(){
      this.getAllCate()
    }
  };
</script>


<style scoped>
  .mavonEditor {
    width: 100%;
    height: 100%;
  }

  .form-header {
    width: 1000px;
    margin: 0 auto;
  }

  .submit-button {
    width: 80px;
    margin: 0 auto;
  }
</style>