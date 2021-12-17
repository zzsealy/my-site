<template>
    <div style="margin-top: 10%;">

        <div class="new-cate">
            <Alert :message="message" :variant="variant" :dismissCountDown="dismissCountDown" :dismissSecs=5>
            </Alert>
            <form @submit.prevent>
                <div class="form-group">
                    <input v-model="newCate" class="form-control new-cate-input" id="new-cate" placeholder="新类别" />
                    <button @click="submit" type="submit" class="btn btn-default">
                        提交
                    </button>
                </div>
            </form>
        </div>
        <div class="categories">
            <div v-for="cate in cates" :key="cate.id">
                <strong class="cate-name">{{ cate.name }}</strong>
                <button @click="delCate" type="submit" class="btn btn-danger cate-button">删除</button>
                <button @click="editCate" type="submit" class="btn btn-warning cate-button">编辑</button>
            </div>
        </div>
    </div>
</template>


<script>
    // import axios from 'axios'
    import global from "../Global.vue";
    import Alert from "../../components/Alert.vue"
    export default {
        name: "Category",
        data() {
            return {
                cates: "",
                newCate: "",
                message: "",
                dismissCountDown: 0,
                variant: '',
            };
        },
        components: {
            Alert
        },

        methods: {
            getCategories() {
                const path = global.URL + "/categories";
                this.$axios
                    .get(path)
                    .then((res) => {
                        this.cates = res.data;
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            },

            submit() {
                const path = global.URL + "/category";
                const data = {
                    "cate": this.newCate
                }
                this.$axios
                    .post(path, data)
                    .then((res) => {
                        this.message = res.data.message;
                        this.variant = "success";
                    })
                    .catch((error) => {
                        console.log(error);
                    });
                this.dismissCountDown = 5;
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
    .categories{
        width: 200px;
        margin: 0 auto;
    }
    .cate-name{
        margin-right: 10px;
    }
    .cate-button{
        margin-right: 10px;
    }
</style>