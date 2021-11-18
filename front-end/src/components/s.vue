<template>
    <div id="home">
      <el-container>
        <el-aside width="auto">
          <div class="logo"></div>
          <el-menu class="el-menu-vertical-demo" collapse-transition="true" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-location"></i>
                <span slot="title">导航一</span>
              </template>
              <el-menu-item-group>
                  <el-menu-item>
                  <i class="el-icon-location"></i>
                  <span slot="title">选项1</span>
                  </el-menu-item>
                  <el-menu-item>
                  <i class="el-icon-location"></i>
                  <span slot="title">选项2</span>
                  </el-menu-item>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-container>
          <el-header>
            <i class="el-icon-location toggle" @click="toggleCollapse"></i>
          </el-header>
          <el-main>Main</el-main>
        </el-container>
      </el-container>
    </div>
  </template>
  <script>
  export default {
    data() {
      return {
        isCollapse: true
      };
    },
    methods: {
      handleOpen (key, keyPath) {
        console.log(key, keyPath)
      },
      handleClose (key, keyPath) {
        console.log(key, keyPath)
      },
      toggleCollapse () {
        console.log(123456789);
        
        this.isCollapse = !this.isCollapse
      }
    }
  }
  </script>
  <style lang="scss" scoped>
    #home {
      width: 100%;
      height: 100%;
      .el-menu-admin:not(.el-menu--collapse) {
        width: 200px;
        min-height: 400px;
      }
      .el-container {
        height: 100%;
      }
      .el-aside {
        background-color: #545c64;
      }
      .el-header {
        background-color: #fe4;
      }
      .el-main {
        background-color: #f20;
      }
      .toggle {
        font-size: 36px;
        color: #989898;
        cursor: pointer;
        line-height: 30px;
      }
   
    }
    
  </style>
 