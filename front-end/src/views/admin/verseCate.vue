<template>
  <div>
    <b-container>
        <form @submit.prevent>
        <div class="form-group">
          <input
            v-model="newCate"
            class="form-control new-cate-input"
            id="new-cate"
            placeholder="新类别"
          />
          <button v-show="showSubmitButton" @click="submit" type="submit" class="btn btn-default">
            提交
          </button>
          <button v-show="showEditButton" @click="editSubmit" type="submit" class="btn btn-default">
            提交编辑
          </button>
        </div>
      </form>
      <el-divider></el-divider>
        <div v-for="cate in verseCates" :key="cate.id">
          {{ cate.name }}
            <b-button @click="
              setEditVerseCate(
                cate.id,
                cate.name
              )
            " variant="warning">编辑</b-button>
        </div>
    </b-container>
  </div>
</template>

<script>
export default {
  name: "",
  data() {
    return {
      verseCates: "",
      newCate: '',
      selected: '',
      showEditButton: false,
      showSubmitButton: true
    };
  },
  methods: {
    getVerseCate() {
      let path = this.$store.state.URL + "/verse_cates";
      this.$axios.get(path).then((res) => {
        let verseCates = res.data;
        this.verseCates = verseCates;
      });
    },
    submit() {
        let path = this.$store.state.URL + '/verse_cate';
        this.$axios.post(path, {'name': this.newCate})
            .then((res) => {
                if (res.status == 200) {
                    this.$toasted.success('分类添加成功');
                }
            })
    },
    editSubmit(){
        let id = this.selected;
        let name = this.newCate;
        let path = this.$store.state.URL + '/verse_cate/' + id;
        this.$axios.put(path, {'id': id, 'name': name})
            .then((res) => {
                if (res.status == 200){
                    this.$toasted.success('分类修改成功');
                }
                if (res.status == 250) {
                    this.$toasted.success('分类迁移成功！')
                }
            })
    },
    setEditVerseCate(cateId, cateName){
        this.selected = cateId;
        this.newCate = cateName;
        this.showEditButton = true;
        this.showSubmitButton = false;
    }
  },

  mounted() {
    this.getVerseCate();
  },
};
</script>

<style>
.new-cate {
  width: 200px;
  margin: 0 auto;
}

.new-cate-input {
  float: left;
  width: 100px !important;;
  display: inline;
}
</style>
