<template>
    <div>
        <el-container style="height: 100%;">
            <el-aside width="auto">
                <el-menu v-if="is_hide" default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"
                    :collapse="isCollapse" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
                    <el-menu-item index="2">
                        <i class="el-icon-menu"></i>
                        <span slot="title">导航二</span>
                    </el-menu-item>
                    <el-menu-item index="4">
                        <i class="el-icon-setting"></i>
                        <span slot="title">导航四</span>
                    </el-menu-item>
                </el-menu>
            </el-aside>

            <el-container>
                <el-header>
                    <i class="el-icon-s-operation toggle" @click="toggleCollapse"></i>
                </el-header>
            </el-container>
        </el-container>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                isCollapse: false,
                is_hide: true
            };
        },
        methods: {
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            },
            toggleCollapse() {
                this.isCollapse = !this.isCollapse;
                setTimeout(this.hide_navbar(), 1000);
            },
            hide_navbar(){
                if(this.isCollapse == true){
                    this.is_hide = false
                } else{
                    this.is_hide = true
                }
            }
        }
    }
</script>

<style>
    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 200px;
        min-height: 400px;
    }
</style>