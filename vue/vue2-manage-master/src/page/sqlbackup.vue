<template>
<div>
  <head-top></head-top>
  <el-form ref="form" :model="form" label-width="80px" :rules="rules">
    <!-- 实例名 -->
    <el-row class='mt10' :gutter="20">
      <el-col class="empty" :span="2"></el-col>
      <el-col :span="8">
        <!-- <el-form ref="form" :model="form" label-width="80px"> -->
        <el-form-item label="实例名" prop='instance_name'>
          <el-select placeholder="请选择实例名" v-model="form.instance_id" @change="query_db">
            <el-option :label="instance.instance_name" :value="instance.instance_id" v-for="instance in instance_list" :key="instance.instance_id"></el-option>
          </el-select>
        </el-form-item>
        <!-- </el-form> -->
      </el-col>
    </el-row>
    <!-- 数据库选择框 -->
    <el-row class='mt10' :gutter="20">
      <el-col class="empty" :span="2"></el-col>
      <el-col :span="20">
        <!-- <el-form ref="form" :model="form" label-width="80px"> -->
        <el-form-item label="数据库" prop='selectData'>
          <el-transfer v-model="form.selectData" :data="data" :titles="['数据库列表', '选择数据库']"></el-transfer>
        </el-form-item>
        <!-- </el-form> -->
      </el-col>
    </el-row>
    <!-- 备份路径 -->
    <el-row class='mt10' :gutter="20">
      <el-col class="empty" :span="2"></el-col>
      <el-col :span="8">
        <!-- <el-form ref="form" :model="form" label-width="80px"> -->
        <el-form-item label="备份路径" prop='back_path'>
          <el-input v-model="form.back_path" placeholder="请输入备份路径"></el-input>
        </el-form-item>
        <!-- </el-form> -->
      </el-col>
    </el-row>
    <!-- 项目key -->
    <el-row class='mt10' :gutter="20">
      <el-col class="empty" :span="2"></el-col>
      <el-col :span="8">
        <!-- <el-form ref="form" :model="form" label-width="80px"> -->
        <el-form-item label="项目名称" prop='KEY'>
          <el-input v-model="form.KEY" placeholder="例：E6"></el-input>
        </el-form-item>
        <!-- </el-form> -->
      </el-col>
    </el-row>
    <!-- 备份类型 -->
    <el-row class='mt10' :gutter="20">
      <el-col class="empty" :span="2"></el-col>
      <el-col :span="8">
        <!-- <el-form ref="form" :model="form" label-width="80px"> -->
        <el-form-item label="备份类型" prop='back_type'>
          <el-select v-model="form.back_type" placeholder="请选择">
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>
        <!-- </el-form> -->
      </el-col>
    </el-row>
    <!-- 提交按钮 -->
    <el-row class='mt10' :gutter="20">
      <el-col class="empty" :span="6"></el-col>
      <el-button type="primary" @click="exec_backup('form')">执行备份</el-button>
    </el-row>
  </el-form>
</div>
</template>

<script>
import headTop from '../components/headTop';
import {
  getDBInfo,
  getInstanceInfo,
  exeBackup
} from '../api/getData_new';
export default {
  data() {
    return {
      // 实例名列表
      instance_list: [],
      // 定义数据库名
      data: [],
      // 选择数据库
      value: [1, 4],
      form: {
        instance_name: '',
        selectData: [],
        back_path: '',
        back_type: '',
        KEY: '',
        action: 'backup'
      },
      // 备份类型
      options: [{
        value: 'back_all',
        label: '全备'
      }, {
        value: 'back_log',
        label: '日志'
      }, {
        value: 'back_diff',
        label: '差异'
      }],
      rules: {
        selectData: [{
          validator: function (rule, value, callback) {
            if (value && value.length === 0) {
              callback(new Error('数据库不能为空'));
            } else {
              callback()
            }
          },
          trigger: 'blur'
        }],
        back_path: [{
          required: true,
          message: '请输入备份路径',
          trigger: 'blur'
        }],
        back_type: [{
          required: true,
          message: '请选择备份类型',
          trigger: 'blur'
        }],
        KEY: [{
          required: true,
          message: '请输入项目名称',
          trigger: 'blur'
        }],
      }
    }
  },
  components: {
    headTop
  },
  created() {
    this.query_instance()
  },
  methods: {
    // 查询数据库名称
    query_db(instanceId) {
      let params = {};
      params.id = instanceId;
      params.name =  this.instance_list.find(i => i.instance_id === instanceId).instance_name;
      this.form.instance_name = params.name;
      getDBInfo(params).then(
        (data) => {
          this.data = data.map(i => ({
            key: i,
            label: i
          }));
        },
        function () {
          alert('没有数据库信息')
        }
      )
    },
    // 查询实例信息
    query_instance() {
      getInstanceInfo().then(
        (data) => {
            console.log(data)
          this.instance_list = data['msg'];
        }
      )
    },
    exec_backup(form) {
      this.$refs[form].validate(
        (valid) => {
          if (!valid) {
            this.$notify.error({
              title: '错误',
              message: '请仔细核对输入'
            })
          } else {
            exeBackup(this.form).then(
              (data) => {
                if (data['code'] === 0) {
                    this.$alert(data['msg'], '执行提醒', {
                      confirmButtonText: '确定',
                      callback: action => {
                        this.$message({
                          type: 'info',
                          message: `action: ${ action }`
                        });
                      }
                    })
                } else {
                  this.$alert(data['msg'], '执行错误', {
                    confirmButtonText: '确定',
                    callback: action => {
                      this.$message({
                        type: 'info',
                        message: `action: ${ action }`
                      });
                    }
                  }
                  )}
              }
            )
          }
        }
      )
    },
  },
}
</script>

<style lang="">
.empty {
  height: 1px;
}

.mt10 {
  margin-top: 20px;
}
</style>
