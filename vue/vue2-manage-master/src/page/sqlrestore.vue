<template>
<div>
  <head-top></head-top>
  <el-form ref="form" :model="form" label-width="150px" :rules="rules">
    <div class='steps'>
      <el-steps :active="active" finish-status="success">
        <el-step title="还原参数配置"></el-step>
        <el-step title="生成还原语句"></el-step>
        <el-step title="执行还原操作"></el-step>
      </el-steps>
    </div>
    <div v-show="active === 0" class='steps'>
      <el-col :span="24">
        <!-- 实例名 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="20">
            <el-form-item label="实例名" prop='instance_name'>
              <el-select placeholder="请选择实例名" v-model="form.instance_id" @change="query_db">
                <el-option :label="instance.instance_name" :value="instance.instance_id" v-for="instance in instance_list" :key="instance.instance_id"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 数据库选择框 -->
        <el-row>
          <el-row class='mt10' :gutter="20">
            <el-col class="empty" :span="2"></el-col>
            <el-col :span="20">
              <el-form-item label="数据库" prop='selectData'>
                <el-transfer v-model="form.selectData" :data="data" :titles="['数据库列表', '选择数据库']"></el-transfer>
              </el-form-item>
            </el-col>
          </el-row>
        </el-row>
        <!-- 数据库key -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="数据库KEY" prop='BKDBkey'>
              <el-input v-model="form.BKDBkey" placeholder="输入目标数据库key"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 目标实例名 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="20">
            <el-form-item label="目标实例" prop='target_instance'>
              <el-select placeholder="请选择实例名" v-model="form.target_instance">
                <el-option :label="target_instance.instance_name" :value="target_instance.instance_id" v-for="target_instance in instance_list" :key="target_instance.instance_id"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 还原类型 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="20">
            <el-form-item label="还原模式" prop='restore_type'>
              <el-select v-model="form.restore_type" placeholder="请选择">
                <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 备份文件路径 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="备份文件路径" prop='backfile_path'>
              <el-input v-model="form.backfile_path" placeholder="请输入备份文件路径"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 还原数据文件路径 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="数据文件路径路径" prop='datafile_path'>
              <el-input v-model="form.datafile_path" placeholder="请输入数据文件路径"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 还原数据文件路径 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="20">
            <el-form-item label="数据文件类型" prop='back_type'>
              <el-select v-model="form.back_type" placeholder="请选择">
                <el-option v-for="item in file_type" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <!-- 还原日志文件路径 -->
        <el-row class='mt10' :gutter="20">
          <el-col class="empty" :span="2"></el-col>
          <el-col :span="10">
            <el-form-item label="日志文件路径" prop='logfile_path'>
              <el-input v-model="form.logfile_path" placeholder="请输入日志文件路径"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
      </el-col>

    </div>
    <div v-show='active === 1' class='steps_list'>
      <el-table :data="tableData" border style="width: 100%" :stripe='true'>
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
    <div v-show='active === 2'>
      <el-collapse v-model="activeNames" @change="handleChange" class="exesql">
        <el-collapse-item title="数据库名" name="1">
          <div v-for="(dbname, index) in form.selectData" :key="index">{{ dbname }}</div>
        </el-collapse-item>
        <el-collapse-item title="还原语句" name="2">
          <div :title="sql['restoreSql']" style="width:100%; text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" class="restore" v-for="(sql,index) in tableData" :key="index">{{ sql['restoreSql'] }}</div>
        </el-collapse-item>
        <el-collapse-item title="目标实例" name="3">
          <div>{{ form.target_instance }}</div>
        </el-collapse-item>
        <el-collapse-item title="还原模式" name="4">
          <div>{{ getBackType() }}</div>
        </el-collapse-item>
      </el-collapse>
    </div>
  </el-form>
  <div class='steps_btn'>
    <el-button type="primary" round style="margin-top: 12px;" @click="next('form')">下一步</el-button>
  </div>
  <el-dialog title="编辑" :visible.sync="dialogVisible" width="30%">
    <el-row class='mt10' :gutter="20">
      <el-col class="empty" :span="2"></el-col>
      <el-col :span="20">
        <el-form ref="writeForm" :model="form" label-width="80px">
          <el-form-item label="sql" prop='logfile_path'>
            <el-input type="textarea" :rows="15" v-model="writeForm.restoreSql" placeholder="请输入日志文件路径">
            </el-input>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
    <span slot="footer" class="dialog-footer">
      <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
    </span>
  </el-dialog>
</div>
</template>

<script>
import headTop from "../components/headTop";
import {
  getDBInfo,
  getInstanceInfo,
  exeRestore,
  exeDetection,
  exeSQL
} from "../api/getData_new";
export default {
  data() {
    return {
      activeNames: "",
      // 实例名列表
      instance_list: [],
      data: [],
      tableData: [],
      value: [1, 4],
      active: 0,
      form: {
        instance_name: "",
        selectData: [],
        BKDBkey: "",
        target_instance: "",
        restore_type: "",
        backfile_path: "",
        datafile_path: "",
        logfile_path: "",
        textarea: "",
        back_type: "",
        action: "restore"
      },
      writeForm: {
        restoreSql: ""
      },
      dialogVisible: false,
      // 还原类型
      options: [{
          value: "recovery",
          label: "完全还原"
        },
        {
          value: "norecovery",
          label: "不完全还原"
        }
      ],
      // 备份类型
      file_type: [{
          value: "back_all",
          label: "全备"
        },
        {
          value: "back_log",
          label: "日志"
        },
        {
          value: "back_diff",
          label: "差异"
        }
      ],
      rules: {
        BKDBkey: [{
          required: true,
          message: "请输入项目名称",
          trigger: "blur"
        }],
        selectData: [{
          validator: function (rule, value, callback) {
            if (value && value.length === 0) {
              return callback(new Error("数据库不能为空"));
            } else {
              callback();
            }
          },
          trigger: "blur"
        }],
        target_instance: [{
          required: true,
          message: "请输入目标实例",
          trigger: "blur"
        }],
        restore_type: [{
          required: true,
          message: "请输入目标实例",
          trigger: "blur"
        }],
        backfile_path: [{
          required: true,
          message: "请输入备份文件路径",
          trigger: "blur"
        }],
        datafile_path: [{
          required: true,
          message: "请输入主数据文件路径",
          trigger: "blur"
        }],
        logfile_path: [{
          required: true,
          message: "请输入日志文件路径",
          trigger: "blur"
        }],
        textarea: [{
          required: true,
          message: "请输入目标实例",
          trigger: "blur"
        }],
        back_type: [{
          required: true,
          message: "请输入备份类型",
          trigger: "blur"
        }]
      }
    };
  },
  components: {
    headTop
  },
  created() {
    this.query_instance();
  },
  methods: {
    // 点击下一步执行的事件
    next(form) {
      console.log(this.active)
      // 如果为第一个页面点击下一步执行的操作
      if (this.active === 0) {
        // 判断是否符合规则
        this.$refs[form].validate(valid => {
          if (valid) {
            //判断是否选择了数据库
            if (this.active < 2) {
              // 执行查询sql接口
              exeRestore(this.form).then(data => {
                // 判断是否收到还原语句
                if (data["msg"] === {} || data['msg'] === String) {
                  this.$notify.error({
                    title: "错误",
                    message: "未生成还原语句，请检查DBBackupInfo表数据是否存在"
                  });
                } else {
                  this.tableData = Object.keys(data["msg"]).map(i => ({
                    db_name: i,
                    restoreSql: data["msg"][i]
                  }));
                }
              });
              //点击翻页
              this.active++;
            } else {
              this.active = 0;
            }
          } else {
            this.$notify.error({
              title: "错误",
              message: "请仔细核对输入"
            });
          }
        });
      } else if (this.active === 1) {
        this.active++;
      } else if (this.active === 2) {
        this.form.modify_sql = this.tableData.map(i => i.restoreSql);
        exeSQL(this.form).then(data => {
          console.log(data);
          this.active++;
        });
      } else if (this.active === 3) {
        this.$alert('这是一段内容', '标题名称', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'info',
              message: `action: ${ action }`
            });
          }
        });
      }
    },
    // 查询数据库名称
    query_db(instanceId) {
      let params = {};
      params.id = instanceId;
      params.name = this.instance_list.find(i => i.instance_id === instanceId).instance_name;
      this.form.instance_name = params.name
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
    // 执行还原程序
    writeSql(data) {
      this.dialogVisible = true;
      this.writeForm = data;
    },
    getBackType() {
      const obj = this.file_type.find(
        item => item.value === this.form.back_type
      );
      return obj ? obj.label : "";
    },
    handleChange() {},
  }
};
</script>
<style lang="">
.empty {
  height: 1px;
}
.mt10 {
  margin-top: 10px;
}
.steps {
  margin-left: 100px;
  margin-right:200px;
  margin-top: 50px;
  margin-bottom: 50px;
}
.steps_btn {
  margin-top: 50px;
  margin-left: 100px;
  margin-bottom: 50px;
}
.exesql {
  margin-left: 30px;
  margin-right: 30px;
}
</style>
