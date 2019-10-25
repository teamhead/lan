<template>
    <div>
        <head-top></head-top>
        <el-row class='mt10' :gutter="20">
            <el-col class="empty" :span="2"></el-col>
            <el-col :span="22">
                <div class='steps'>
                    <el-steps :active="active" finish-status="success">
                        <el-step title="还原参数配置"></el-step>
                        <el-step title="生成还原语句"></el-step>
                        <el-step title="执行还原操作"></el-step>
                    </el-steps>
                </div>
            </el-col>
        </el-row>
        <div v-show="active === 0" class='steps'>
            <!-- 实例名 -->
            <el-form ref="form" :model="form" label-width="80px" :rules="rules">
                <el-row class='mt10' :gutter="20">
                    <el-col class="empty" :span="2"></el-col>
                    <el-col :span="8">
                        <el-form-item label="实例名" prop="instance_id">
                            <el-select placeholder="请选择实例名" v-model="form.instance_id" @change="query_db">
                                <el-option :label="instance.instance_name" :value="instance.instance_id" v-for="instance in instance_list" :key="instance.instance_id"></el-option>
                            </el-select>
                        </el-form-item>

                    </el-col>
                </el-row>
                <!-- 数据库选择框 -->
                <el-row class='mt10' :gutter="20">
                    <el-col class="empty" :span="2"></el-col>
                    <el-col :span="20">
                        <el-form-item label="数据库">
                            <el-transfer v-model="form.selectData" :data="data" :titles="['数据库列表', '选择数据库']"></el-transfer>
                        </el-form-item>
                    </el-col>
                </el-row>
                <!-- 目标实例名 -->
                <el-row class='mt10' :gutter="20">
                    <el-col class="empty" :span="2"></el-col>
                    <el-col :span="20">
                        <el-form-item label="目标实例" prop="target_instance">
                            <el-select placeholder="请选择实例名" v-model="form.target_instance">
                                <el-option :label="target_instance.instance_name" :value="target_instance.instance_id" v-for="target_instance in instance_list" :key="target_instance.instance_id"></el-option>
                            </el-select>
                        </el-form-item>
                    </el-col>
                </el-row>
                <!-- 权限操作 -->
                <el-row class='mt10' :gutter="20">
                    <el-col class="empty" :span="2"></el-col>
                    <el-col :span="8">
                        <el-form-item label="权限操作" prop="jurisdiction_handle">
                            <el-select v-model="form.jurisdiction_handle" placeholder="请选择">
                                <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                                </el-option>
                            </el-select>
                        </el-form-item>
                    </el-col>
                </el-row>
                <!-- 用户名 -->
                <el-row class='mt10' :gutter="20">
                    <el-col class="empty" :span="2"></el-col>
                    <el-col :span="8">
                        <el-form-item label="用户名" prop="username">
                            <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <!-- 密码 -->
                <el-row class='mt10' :gutter="20">
                    <el-col class="empty" :span="2"></el-col>
                    <el-col :span="8">
                        <el-form-item label="密码" prop="password">
                            <el-input type="password" v-model="form.password" auto-complete="off" placeholder="请输入密码"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
            </el-form>
        </div>
        <div v-show='active === 1' class='steps_list'>
            <el-table :data="form.tableData" border style="width: 100%" :stripe='true'>
                <el-table-column fixed prop="db_name" label="数据库名" width="180" show-overflow-tooltip>
                </el-table-column>
                <el-table-column show-overflow-tooltip prop="restoreSql" label="还原语句">
                </el-table-column>
                <el-table-column fixed="right" label="操作" width="100">
                    <template slot-scope="scope">
                        <el-button type="text" size="small" @click="writeSql(scope.row)">编辑</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>

        <!-- 提交按钮 -->
        <el-row class='mt10' :gutter="20">
            <el-col class="empty" :span="2"></el-col>
            <el-col :span="22">
                <div class='steps_btn'>
                    <el-button type="primary" round style="margin-top: 12px;" @click="next('form')">下一步</el-button>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import headTop from "../components/headTop";
import { getDBInfo, getInstanceInfo, userHeadle } from "../api/getData_new";
export default {
  data() {
    return {
      // 实例名
      instance_name: null,
      // 实例名列表
      instance_list: [],
      // 定义数据库名
      data: [],
      // 选择数据库名
      selectData: [],
      value: [1, 4],
      active: 0,
      // 备份类型
      options: [
        {
          value: "add_user",
          label: "新建用户授权"
        },
        {
          value: "handle_user",
          label: "处理孤立用户"
        }
      ],
      form: {
        instance_id: "",
        instance_name: "",
        tableData: [],
        target_instance_name: "",
        jurisdiction_handle: "",
        username: "",
        password: ""
      },
      rules: {
        instance_id: [
          {
            required: true,
            message: "请选择实例名",
            trigger: "blur"
          }
        ],
        target_instance: [
          {
            required: true,
            message: "请选择目标实例名",
            trigger: "blur"
          }
        ],
        jurisdiction_handle: [
          {
            required: true,
            message: "请选择权限操作",
            trigger: "blur"
          }
        ],
        username: [
          {
            required: true,
            message: "请输入用户名",
            trigger: "blur"
          }
        ],
        password: [
          {
            required: true,
            message: "请输入密码",
            trigger: "blur"
          }
        ]
      }
    };
  },
  watch: {
    "form.target_instance"(val) {
      let obj = this.instance_list.find(item => item.instance_id === val);
      obj = typeof obj === "object" ? obj.instance_name : "";
      this.form.target_instance_name = obj;
    }
  },
  components: {
    headTop
  },
  created() {
    this.query_instance();
  },
  methods: {
    next(form) {
      if (this.active === 0) {
        userHeadle(this.form).then();
        this.active++;
      } else if (this.active === 1) {
        alert(1);
        this.active++;
      } else if (this.active === 2) {
        alert(2);
        this.active++;
      } else if (this.active === 3) {
        alert(3);
        this.active++;
      }
    },
    // 查询数据库名称
    query_db(instanceId) {
      let params = {};
      params.id = instanceId;
      params.name = this.instance_list.find(
        i => i.instance_id === instanceId
      ).instance_name;
      this.form.instance_name = params.name;
      getDBInfo(params).then(
        data => {
          this.data = data.map(i => ({
            key: i,
            label: i
          }));
        },
        function() {
          alert("没有数据库信息");
        }
      );
    },
    // 查询实例信息
    query_instance() {
      getInstanceInfo().then(data => {
        this.instance_list = data["msg"];
      });
    }
  }
};
</script>

<style lang="">
.empty {
  height: 1px;
}

.mt10 {
  margin-top: 20px;
}
</style>
