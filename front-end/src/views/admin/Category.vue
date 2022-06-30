<template>
  <div style="margin-top: 10%">
    <div class="new-cate">
      <b-alert
        :show="dismissCountDown"
        :variant="variant"
        dismissible
        v-on:dismissed="dismissCountDown = 0"
        @dismiss-count-down="countDownChanged"
      >
        {{ message }}
      </b-alert>
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
    <div class="categories">
      <div v-for="cate in cates" :key="cate.id" class="cate">
        <strong v-show="cate.showName" class="cate-name" key="cate.id">{{
          cate.name
        }}</strong>
        <input
          v-model="changeCateName"
          v-show="!cate.showName"
          class="cate-input"
          key="cate.id"
          type="text"
          :placeholder="cate.name"
        />
        <div class="cate-button">
          <button
            @click="delCate(cate.id)"
            type="submit"
            class="btn btn-danger cate-button"
          >
            删除
          </button>
          <button
            v-show="cate.showName"
            @click="editCate(cate.id)"
            type="submit"
            class="btn btn-warning cate-button"
          >
            编辑
          </button>
          <button
            v-show="!cate.showName"
            @click="submitEditCate(cate.id)"
            type="submit"
            class="btn btn-warning cate-button"
          >
            完成
          </button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
// import axios from 'axios'
import {store} from "../store.js";
export default {
  name: "Category",
  data() {
    return {
      cates: "",
      newCate: "",
      message: "",
      variant: "",
      changeCateName: "",
      dismissSecs: 5,
    };
  },

  methods: {
    getCategories() {
      const path = store.URL + "/categories";
      this.$axios
        .get(path)
        .then((res) => {
          this.cates = res.data;
          for (let i = 0; i < this.cates.length; i++) {
            this.$set(this.cates[i], "showName", true);
          }
        })
        .catch((error) => {
          window.console.log(error);
        });
    },

    submit() {
      const path = store.URL + "/categories";
      const data = {
        "name": this.newCate,
      };
      this.$axios
        .post(path, data)
        .then((res) => {
          this.message = res.data.message;
          this.variant = "success";
          this.getCategories();
        })
      this.showAlert();
    },

    delCate(cateId) {
      const path = store.URL + "/category/" + cateId;
      this.$axios
        .delete(path)
        .then((res) => {
          this.message = res.data.message;
          this.variant = "success";
          this.getCategories();
        })
        .catch((error) => {
          window.console.log(error);
        });
      this.showAlert();
    },

    editCate(cateId) {
      for (let i = 0; i < this.cates.length; i++) {
        if (this.cates[i].id == cateId) {
          this.$set(this.cates[i], "showName", false);
          this.changeCateName = this.cates[i].name;
        }
      }
    },

    submitEditCate(cateId) {
      const path = store.URL + "/category/" + cateId;
      const data = {
        "name": this.changeCateName,
      };
      this.$axios
        .put(path, data)
        .then((res) => {
          this.message = res.data.message;
          this.variant = "success";
          this.getCategories();
          this.changeCateName = "";
        })
        .catch((error) => {
          window.console.error(error);
        });
      this.showAlert();
    },

    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },

    showAlert() {
      this.dismissCountDown = this.dismissSecs;
    },
  },

  created() {
    this.getCategories();
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
  width: 100px;
  display: inline;
}
.categories {
  width: 200px;
  margin: 10px auto;
}
.cate {
  margin-top: 30px;
}
.cate-name {
  margin-right: 10px;
  width: 150px;
}
.cate-input {
  margin-bottom: 10px;
}
.cate-button {
  margin-right: 10px;
}
</style>