<template>
    
            <p>{{ msg.ping }}</p>
</template>

<script>
    import axios from 'axios'
    import store from './store.js'
    export default {
        name: 'Ping',
        data() {
            return {
                msg: '',
            }
        },
        methods: {
            getMessage() {
                const path = store.URL + '/ping'
                axios.get(path)
                    .then((res) => {
                        this.msg = res.data;
                    })
            }
        },
        created() {
            this.getMessage()
        }
    }
</script>