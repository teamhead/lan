<template>
<div>
  <head-top></head-top>
  <div class='steps'>
    <el-steps :active="active" finish-status="success">
      <el-step title="源实例信息"></el-step>
      <el-step title="目标实例信息"></el-step>
      <el-step title="其他参数配置"></el-step>
    </el-steps>
  </div>
  <el-form ref="form" :model="form" label-width="150px" :rules="rules">
    <!-- 第一步 -->
    <div v-show="active === 0" class='steps'>
      <el-col :span="24">
        <!-- 源表服务器地址 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="源服务器地址" prop='SourceServerIP'>
              <el-input v-model="form.SourceServerIP" placeholder="源服务器地址"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 源表服务器地址 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="源数据库名" prop='SyncDBName'>
              <el-input v-model="form.SyncDBName" placeholder="源数据库名"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 源表服务器地址 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="源数据库类型" prop='SyncSource'>
              <el-input v-model="form.SyncSource" placeholder="源数据库类型"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 源表服务器地址 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="源架构名" prop='SyncSchemaName'>
              <el-input v-model="form.SyncSchemaName" placeholder="源架构名"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="源表名" prop='SyncTableName'>
              <el-input v-model="form.SyncTableName" placeholder="请输入源表名"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="源用户" prop='SourceUser'>
              <el-input v-model="form.SourceUser" placeholder="请输入源用户"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 源密码 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="源密码" prop='SourcePW'>
              <el-input v-model="form.SourcePW" placeholder="请输入源密码" show-password></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 源列表名 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="源列表名" prop='SourceCols'>
              <el-input v-model="form.SourceCols" placeholder="请输入源列表名"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 源查询条件 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="源查询条件" prop='SourceCondition'>
              <el-input v-model="form.SourceCondition" placeholder="请输入源查询条件"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 查询语句 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="查询语句" prop='QuerySql'>
              <el-input  v-model="form.QuerySql" placeholder="请输入查询语句"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 主键 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="主键" prop='PKID'>
              <el-input v-model="form.PKID" placeholder="请输入主键"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
      </el-col>
    </div>
    <!-- 第二步 -->
    <div v-show="active === 1" class='steps'>
      <!-- 目标服务器名 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="目标服务器名" prop='TargetServerIP'>
            <el-input v-model="form.TargetServerIP" placeholder="请输入目标服务器名"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 源表名（不带架构） -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="目标数据库名" prop='TargetDBName'>
            <el-input v-model="form.TargetDBName" placeholder="请输入目标数据库名"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 导出文件路径 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="目标表名" prop='TargetTableName'>
            <el-input v-model="form.TargetTableName" placeholder="请输入目标表名"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 源用户 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="目标数据库类型" prop='SyncTarget'>
            <el-input v-model="form.SyncTarget" placeholder="请输入目标数据库类型"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 源密码 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="目标表列名" prop='TargetCols'>
            <el-input v-model="form.TargetCols" placeholder="请输入目标表列名"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 源列表名 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="目标用户名" prop='TargetUser'>
            <el-input v-model="form.TargetUser" placeholder="请输入目标用户名"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 源查询条件 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="目标密码" prop='TargetPW'>
            <el-input v-model="form.TargetPW" placeholder="请输入目标密码" show-password></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 查询语句 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="目标库执行前SQL" prop='TargetPresql'>
            <el-input v-model="form.TargetPresql" placeholder="请输入目标库执行前SQL"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 主键 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="目标库执行后sql" prop='TargetPostsql'>
            <el-input v-model="form.TargetPostsql" placeholder="请输入目标库执行后sql"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
    </div>
    <!-- 第三步 -->
    <div v-show="active === 2" class='steps'>
      <!-- 源表名（不带架构） -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="同步类型" prop='SyncType'>
            <el-input v-model="form.SyncType" placeholder="请输入同步类型（全量/增量）"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 源用户 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="是否有效" prop='IsEnableFlag'>
            <el-select v-model="form.IsEnableFlag" placeholder="请选择是否有效">
              <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 源密码 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="同步间隔/m" prop='SyncFrequence'>
            <el-input v-model="form.SyncFrequence" placeholder="同步间隔/m" type="number"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 源列表名 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="同步条目" prop='SyncCategory'>
            <el-input v-model="form.SyncCategory" placeholder="请输入同步条目"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <!-- 源查询条件 -->
      <el-row class='mt10' :gutter="20">
        <el-col class="empty" :span="2"></el-col>
        <el-col :span="10">
          <el-form-item label="备注" prop='Remark'>
            <el-input v-model="form.Remark" placeholder="备注"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
    </div>
  </el-form>
  <div class='steps_btn'>
    <el-button type="primary" round style="margin-top: 12px;" @click="back('form')">上一步</el-button>
    <el-button type="primary" round style="margin-top: 12px;" @click="next('form')">下一步</el-button>
  </div>
</div>
</template>

<script>
import headTop from "../components/headTop";
import {
  insertBG
} from "../api/getData_new.js";
var convertKeys = ['QuerySql','PKID','TargetPresql','TargetPostsql','Remark'];
export default {
  data() {
    return {
      active: 0,
      form: {
          QuerySql:'',
          PKID:'',
          TargetPresql:'',
          TargetPostsql:'',
          Remark:''
      },
      options:[{value:1,
      label:'是'},{value:0,label:'否'}],
      rules: {
        SourceServerIP: [{
          required: true,
          message: "请输入源服务器地址",
          trigger: "blur"
        }],
        SyncDBName: [{
          required: true,
          message: "请输入源数据库名",
          trigger: "blur"
        }],
        SyncSource: [{
          required: true,
          message: "请输入源数据库类型",
          trigger: "blur"
        }],
        SyncSchemaName: [{
          required: true,
          message: "请输入源架构名",
          trigger: "blur"
        }],
        SyncTableName: [{
          required: true,
          message: "请输入源表名",
          trigger: "blur"
        }],
        SourceUser: [{
          required: true,
          message: "请输入源用户",
          trigger: "blur"
        }],
        SourcePW: [{
          required: true,
          message: "请输入源密码",
          trigger: "blur"
        }],
        SourceCols: [{
          required: true,
          message: "请输入源列表名",
          trigger: "blur"
        }],
        SourceCondition: [{
          required: true,
          message: "请输入源查询条件",
          trigger: "blur"
        }],
        TargetServerIP: [{
          required: true,
          message: "请输入目标服务器名",
          trigger: "blur"
        }],
        TargetDBName: [{
          required: true,
          message: "请输入目标数据库名",
          trigger: "blur"
        }],
        TargetTableName: [{
          required: true,
          message: "请输入目标表名",
          trigger: "blur"
        }],
        SyncTarget: [{
          required: true,
          message: "请输入目标数据库类型",
          trigger: "blur"
        }],
        TargetCols: [{
          required: true,
          message: "请输入目标表列名",
          trigger: "blur"
        }],
        TargetUser: [{
          required: true,
          message: "请输入目标用户名",
          trigger: "blur"
        }],
        TargetPW: [{
          required: true,
          message: "请输入目标密码",
          trigger: "blur"
        }],
        SyncType: [{
          required: true,
          message: "请输入同步类型（全量",
          trigger: "blur"
        }],
        IsEnableFlag: [{
          required: true,
          message: "是否有效",
          trigger: "blur"
        }],
        SyncFrequence: [{
          required: true,
          message: "同步间隔/m",
          trigger: "blur"
        }],
        SyncCategory: [{
          required: true,
          message: "请输入同步条目",
          trigger: "blur"
        }],
      }
    };
  },
  components: {
    headTop
  },
  filters: {
      formatNA(val) {
          if (val === 'N/A')  {
              return '';
          }
      }
  },
  methods: {
    init() {
      this.$router.push({
        path: '/big_data'
      })
    },
    next(form) {
      if (this.active === 0) {
        this.active++;
      } else if (this.active === 1) {
        this.active++;
      } else if (this.active === 2) {
        this.active++;
      } else if (this.active === 3) {
          let formCopy = {...this.form};
          Object.keys(formCopy).forEach(key => {
              if (convertKeys.some(i => i===key) && ''=== formCopy[key]) {
                  formCopy[key] = 'N/A';
              }
          })
        insertBG(formCopy).then(data => {

          this.$refs['form'].resetFields();
          this.active = 0;
        })
      }
    },
    back(form) {
      if (this.active > 0) {
        this.active--;
      } else {
        this.active = 0;
      }
    }
  },
};
</script>

<style lang="less">
@import "../style/mixin";

.explain_text {
  margin-top: 20px;
  text-align: center;
  font-size: 20px;
  color: #333;
}

.mt10 {
  margin-top: 20px;
}

.steps {
  margin-left: 300px;
  margin-top: 50px;
  margin-bottom: 50px;
}

.steps_btn {
  margin-top: 50px;
  margin-left: 550px;
  margin-bottom: 50px;
}
</style>
