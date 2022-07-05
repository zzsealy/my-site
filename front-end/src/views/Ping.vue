<template>
   <div>
            <p>{{ msg.ping }}</p>
             {{ s }}
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Ping',
        data() {
            return {
                msg: '',
                s: this.a()
            }
        },
        methods: {
            getMessage() {
                const path = this.$store.state.URL + '/ping'
                axios.get(path)
                    .then((res) => {
                        this.msg = res.data;
                    })
            },
            a:s => {
                return 1
            }
        },
        created() {
            this.getMessage()
        }
    }
</script>