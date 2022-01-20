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

      <mavon-editor v-model="postBody" />
    </form>
  </div>
</template>


<script>
  import global from '../Global.vue'
  export default {
    name: "Addpost",
    data() {
      return {
        selected: null,
        postTitle: '',
        postSubhead: '',
        postBody: '',
        cates: ''
      };
    },
    methods: {
      submitPost() {
        let postData = {
          'cate_id': this.selected,
          'post_title': this.postTitle,
          'post_subhead': this.postSubhead,
          'post_body': this.postBody,
        }
        const path = global.URL + '/post';
        this.$axios.post(path, postData)
          .then((res) => {
            window.console.log(res);
          })

      },
      getAllCate(){
        const path = global.URL + "/categories";
        this.$axios.get(path)
          .then((res) => {
            let cates = []
            res.data.forEach(element => {;
              cates.push({ 'value': element.id, 'text': element.name })
            });
            this.cates = cates
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