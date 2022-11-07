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

    </form>
    <div style="border: 1px solid #ccc;">
      <Toolbar
          style="border-bottom: 1px solid #ccc"
          :editor="editor"
          :defaultConfig="toolbarConfig"
          :mode="mode"
      />
      <Editor
          style="height: 500px; overflow-y: hidden;"
          v-model="html"
          :defaultConfig="editorConfig"
          :mode="mode"
          @onCreated="onCreated"
      />
    </div>
  </div>
</template>


<script>
  import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
  export default {
    name: "Addpost",
    components: { Editor, Toolbar },
    data() {
      return {
        selected: null,
        postTitle: '',
        postSubhead: '',
        cates: '',
        editor: null,
        html: '<p>hello</p>',
        text:'',
        toolbarConfig: { },
        editorConfig: { placeholder: '请输入内容...' },
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


<style src="@wangeditor/editor/dist/css/style.css"></style>