<template>
    <div>
      <div>

      </div>
    </div>
</template>

<script>
    import global from './store.js'
    export default {
        name: 'Cate',
        data() {
            return {
                cates:''
            }
        },
        methods: {
            // getTimePostData(){
                // const catePostByTimeUrl = global.URL + '/time_post_data'
                // let timePostData = this.$axios.get(catePostByTimeUrl)
                //                     .then((res) => {
                //                         // {"year": [{"time": "title"}, {"time": "title"}] }
                //                         window.console.log(res)
                //                     })
            // }
        },
        created() {
            // this.getTimePostData();
        }
    }
</script>