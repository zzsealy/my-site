<template>
    
        <el-col :span="12">
            <p>{{ msg.ping }}</p>
        </el-col>
</template>

<script>
    import axios from 'axios'
    import global from './Global.vue'
    export default {
        name: 'Ping',
        data() {
            return {
                msg: ''
            }
        },
        methods: {
            getMessage() {
                const path = global.url + '/ping'
                axios.get(path)
                    .then((res) => {
                        this.msg = res.data;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    })
            }
        },
        created() {
            this.getMessage()
        }
    }
</script>