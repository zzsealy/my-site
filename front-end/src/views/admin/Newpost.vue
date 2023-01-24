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

      <MyEditor
      :html="html"
      @getHtml="getHtml"
      ></MyEditor>
    </form>
  </div>
</template>


<script>
  import MyEditor from './MyEditor'
  export default {
    name: "Newpost",
    components: {
      MyEditor
    },
    data() {
      return {
        selected: null,
        postTitle: '',
        postSubhead: '',
        cates: '',
        editor: null,
        html: '<p>hello</p>',
        text:'',
        mode: 'default', // or 'simple'
      };
    },
    methods: {
      submitPost() {
        let postData = {
          'title': this.postTitle,
          'subhead': this.postSubhead,
          'body': this.html,
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
      getHtml(html){
                this.html = html;
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
      onCreated(editor) {
            this.editor = Object.seal(editor) // 一定要用 Object.seal() ，否则会报错
        },
    },
    created(){
      this.getAllCate()
    },
    mounted() {
        // 模拟 ajax 请求，异步渲染编辑器
        setTimeout(() => {
            this.html = '<p>请输入内容...</p>'
        }, 1500)
    },
    beforeDestroy() {
        const editor = this.editor
        if (editor == null) return
        editor.destroy() // 组件销毁时，及时销毁编辑器
    }
  };
</script>
