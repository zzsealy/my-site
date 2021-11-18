<template>
  <div id="app">
    <el-row>
      <el-col :span="10">
        <navbar></navbar>
      </el-col>
    <router-view />
    </el-row>
  </div>
</template>

<script>
  import Navbar from './components/Nav'

  export default {
    name: 'App',
    components: {
      navbar: Navbar
    },
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
</style>