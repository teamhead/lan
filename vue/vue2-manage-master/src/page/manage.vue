<template>
    <div class="manage_page fillcontain">
        <el-row style="height: 100%;">
            <el-col :span="4" style="min-height: 100%; background-color: #324057;">
                <el-menu :default-active="defaultActive" style="min-height: 100%;" theme="dark" router class="o-bg" background-color="rgb(50, 64, 87)" text-color="#fff" active-text-color="#20a0ff" >
                <!-- <el-menu default-active="defaultActive" class="el-menu-vertical-demo"  background-color="#545c64" text-color="#fff" active-text-color="#ffd04b"> -->
                    <el-menu-item index="manage">
                        <i class="el-icon-menu"></i>首页</el-menu-item>
                    <el-submenu index="2">
                        <template slot="title">
                            <i class="el-icon-refresh"></i>备份还原</template>
                        <el-menu-item index="sqlbackup">数据库备份</el-menu-item>
                        <el-menu-item index="sqlrestore">数据库还原</el-menu-item>
                        <el-menu-item index="userhandle">数据库用户问题处理</el-menu-item>
                    </el-submenu>
                    <el-submenu index="3">
                        <template slot="title">
                            <i class="el-icon-plus"></i>实例信息管理</template>
                        <el-menu-item index="addinstance">添加实例</el-menu-item>
                        <el-menu-item index="add_dbname">数据库名同步</el-menu-item>
                    </el-submenu>
                    <el-submenu index="4">
                        <template slot="title">
                            <i class="el-icon-star-on"></i>切换镜像</template>
                        <!-- <el-menu-item index="visitor">用户分布</el-menu-item> -->
                        <!-- <el-menu-item index="newMember">用户数据</el-menu-item> -->
                    </el-submenu>
                    <el-submenu index="5">
                        <template slot="title">
                            <i class="el-icon-edit"></i>大数据同步</template>
                        <el-menu-item index="big_data">大数据同步</el-menu-item>
                        <el-menu-item index="big_data_show">大数据同步信息管理</el-menu-item>
                    </el-submenu>
                    <el-submenu index="6">
                        <template slot="title">
                            <i class="el-icon-setting"></i>自动发现配置</template>
                        <el-menu-item index="autofind">查询自动发现配置</el-menu-item>
                        <el-menu-item index="add_autofind">添加自动发现配置</el-menu-item>
                    </el-submenu>
                    <el-submenu index="7">
                        <template slot="title">
                            <i class="el-icon-message"></i>短信功能管理</template>
                        <!-- <el-menu-item index="explain">说明</el-menu-item> -->
                    </el-submenu>
                    <el-submenu index="8">
                        <template slot="title">
                            <i class="el-icon-menu"></i>分区表管理</template>
                        <!-- <el-menu-item index="explain">说明</el-menu-item> -->
                    </el-submenu>
                </el-menu>
            </el-col>
            <el-col :span="20" style="height: 100%;overflow: auto;">
                <!-- <router-view></router-view> -->
                <keep-alive>
                    <router-view></router-view>
                </keep-alive>
            </el-col>
        </el-row>
    </div>
</template>
<script>
export default {
  computed: {
    defaultActive: function() {
      return this.$route.path.replace("/", "");
    }
  }
};
</script>
<style lang="less"
@import "../style/mixin";
.no-bg {
  background-color: none;
}
.el-submenu__title:hover{
    background-color: none !important;
}
</style>
