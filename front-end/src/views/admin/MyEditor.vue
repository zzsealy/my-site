<template>
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
</template>

<script>
    import Vue from 'vue'
    import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
    
    export default Vue.extend({
        props: ['html'],
        components: { Editor, Toolbar },
        data() {
            return {
                editor: null,  // 实例
                toolbarConfig: { },  // 工具栏配置
                editorConfig: { placeholder: '请输入内容...' },  // 编辑器配置
                mode: 'default', // or 'simple'
            }
        },
        methods: {
            onCreated(editor) {
                this.editor = Object.seal(editor) // 一定要用 Object.seal() ，否则会报错
            },
            onChange(editor) {
                const html = editor.getHtml();
                this.html = html;
            }
        },
        mounted() {
            // 模拟 ajax 请求，异步渲染编辑器
            // setTimeout(() => {
            //     this.html = '<p>模拟 Ajax 异步设置内容 HTML</p>'
            // }, 1500)
        },

        updated(){
            this.$emit('getHtml', this.html);
        },
        
        beforeDestroy() {
            const editor = this.editor
            if (editor == null) return
            editor.destroy() // 组件销毁时，及时销毁编辑器
        }
    })
</script>

<style>
    .editor-content-view {
  border: 3px solid #ccc;
  border-radius: 5px;
  padding: 0 10px;
  margin-top: 20px;
  overflow-x: auto;
}

.editor-content-view p,
.editor-content-view li {
  white-space: pre-wrap; /* 保留空格 */
}

.editor-content-view blockquote {
  border-left: 8px solid #d0e5f2;
  padding: 10px 10px;
  margin: 10px 0;
  background-color: #f1f1f1;
}

.editor-content-view code {
  font-family: monospace;
  background-color: #eee;
  padding: 3px;
  border-radius: 3px;
}
.editor-content-view pre>code {
  display: block;
  padding: 10px;
}

.editor-content-view table {
  border-collapse: collapse;
}
.editor-content-view td,
.editor-content-view th {
  border: 1px solid #ccc;
  min-width: 50px;
  height: 20px;
}
.editor-content-view th {
  background-color: #f1f1f1;
}

.editor-content-view ul,
.editor-content-view ol {
  padding-left: 20px;
}

.editor-content-view input[type="checkbox"] {
  margin-right: 5px;
}
</style>

<style src="@wangeditor/editor/dist/css/style.css"></style>


<!-- 
<script>
export default {
    // 编辑器的配置
    editorConfig: {                       // JS 语法
        MENU_CONF: {
            'codeSelectLang': {
                'codeLangs': [
                    { text: 'Python', value: 'python' },
                    // 其他
                ]
            },
            'fontSize': ['100px']
        },
        // 其他属性...
        placeholder: '请输入内容...' 
    }

}
</script> -->