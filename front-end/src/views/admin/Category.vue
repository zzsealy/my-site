<template>

</template>


<script>
    export default {
        name: 'Category',
        data() {
            return {
                categories: ''
            }
        },

        methods: {
            getCategories() {
                const path = global.URL + '/categories'
                axios.get(path)
                    .then((res) => {
                        this.categories = res.data;
                    })
            }
        },

        created() {
            this.getCategories()
        }
    }
</script>