<template>
  <div class="new-cate">
    <form @submit.prevent>
      <div class="form-group">
        <input
          v-model="newCate"
          class="form-control new-cate-input"
          id="new-cate"
          placeholder="新类别"
        />
        <button @click="submit" type="submit" class="btn btn-default">
          提交
        </button>
      </div>
    </form>
  </div>
</template>


<script>
// import axios from 'axios'
import global from "../Global.vue";
export default {
  name: "Category",
  data() {
    return {
      categories: "",
      newCate: "",
    };
  },

  methods: {
    getCategories() {
      const path = global.URL + "/categories";
      this.$axios
        .get(path)
        .then((res) => {
          this.categories = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    submit() {
      const path = global.URL + "/categories";
      const data = {
          "cate": this.newCate
      }
      this.$axios
        .post(path, data)
        .then((res) => {
          this.message = res.data.message;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    this.getCategories();
  },
};
</script>

<style >
.new-cate {
  width: 200px;
  margin-left: 40%;
  margin-top: 100px;
}
.new-cate-input {
  float: left;
  width: 100px;
  display: inline;
}
</style>