<template>
    <b-alert :show="dismissCountDown" :variant="variant" dismissible v-on:dismissed="dismissCountDown=0">
        {{ message }}
        <!--
                <b-progress
                :variant="variant"
                :max="dismissSecs"
                :value="dismissCountDown"
                height="4px"
                ></b-progress>
                -->
    </b-alert>
</template>

<script>
    export default {
        name: 'Alert',
        props: ['message', 'variant', 'dismissCountDown', 'dismissSecs'],
        
    }
</script>