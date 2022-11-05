<template>
<!--  短句 组件 -->
    <div>
        <div v-for = 'verse in verses' :key="verse.id" :value="verse.id">
            <p>{{ verse.body }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Verse', 
        data() {
            return {
                verses: '',  // 所有短句

            }
        },
        methods: {
            getVerses(){
                // 获取所有的短句
                const path = this.$store.state.URL + '/verses/';
                this.$axios.get(path)
                    .then((res) => {
                        if (res.status == 200){
                            this.verses = res.data
                        } else {
                            this.$notify.error({
                                title: '获取句子失败',
                                message: '获取句子失败'
                            });
                        }
                    })
            }
        }
    }
</script>