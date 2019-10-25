<template>
<div>
  <head-top></head-top>
  <el-form ref="form" :model="form" label-width="80px" :rules="rules">
    <el-row :gutter="24" class='row'>
      <el-col :span="6">
        <el-form-item label="实例名" prop="instanceName">
          <el-input v-model="form.instanceName" placeholder="请输入实例名"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="6">
        <el-form-item label="IP地址" prop="instanceIp">
          <el-input v-model="form.instanceIp" placeholder="请输入IP地址"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="6">
        <el-form-item label="端口号" prop="instancePort">
          <el-input v-model="form.instancePort" placeholder="请输入端口号"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="6">
        <el-form-item label="账号" prop="instanceUser">
          <el-input v-model="form.instanceUser" placeholder="请输入账号"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="6">
        <el-form-item label="密码" prop="instancePasswd">
          <el-input v-model="form.instancePasswd" placeholder="请输入密码" type="password"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="8">
        <el-form-item>
          <el-button type="primary" @click="AddInstance('form')">添加</el-button>
        </el-form-item>
      </el-col>
    </el-row>
  </el-form>
  <el-table :data="tableData" border style="width: 100%" class='table'>
    <el-table-column prop="instanceName" label="实例名" width="300">
    </el-table-column>
    <el-table-column prop="instanceIp" label="IP地址" width="200">
    </el-table-column>
    <el-table-column prop="instancePort" label="端口" width="200">
    </el-table-column>
    <el-table-column prop="instanceUser" label="用户" width="200">
    </el-table-column>
    <el-table-column prop="instanceIsinsertdb" label="是否禁用" width="200">
    </el-table-column>
    <el-table-column label="修改时间" width="500">
      <template slot-scope="scope">
        {{(scope.row.instanceCreateTime + '000') | formatDate('yyyy-MM-dd hh:mm:ss')}}
      </template>
    </el-table-column>
    <el-table-column fixed="right" label="操作" width="200">
      <template slot-scope="scope">
        <el-button @click="edit(scope.row)" type="text" size="small">修改</el-button>
        <el-button @click="deleteItem(scope.row)" type="text" size="small">禁用</el-button>
      </template>
    </el-table-column>

  </el-table>
  <el-dialog title="修改" :visible.sync="dialogVisible" width="50%">
    <el-form ref="editForm" :model="editForm" label-width="80px" :rules="rules_update">
      <el-form-item label="实例名" prop="instanceName">
        <el-input v-model="editForm.instanceName"></el-input>
      </el-form-item>
      <el-form-item label="IP地址" prop="instanceIp">
        <el-input v-model="editForm.instanceIp"></el-input>
      </el-form-item>
      <el-form-item label="端口" prop="instancePort">
        <el-input v-model="editForm.instancePort"></el-input>
      </el-form-item>
      <el-form-item label="用户" prop="instanceUser">
        <el-input v-model="editForm.instanceUser"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="instancePasswd">
        <el-input v-model="editForm.instancePasswd" type="password"></el-input>
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
      <el-button @click="dialogVisible = false">取 消</el-button>
      <el-button type="primary" @click="handlerEdit('editForm')">确 定</el-button>
    </span>
  </el-dialog>
    <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        :page-size="pageSize"
        layout="prev, pager, next, jumper"
        :total="total">
    </el-pagination>
</div>
</template>

<script>
function padLeftZero(str) {
  return ('00' + str).substr(str.length)
}
import headTop from '../components/headTop'
import {
  editInstanceInfo,
  deleteInstance,
  insertInstance,
exeAllInstanceInfo
} from './../api/getData_new'
export default {
  components: {
    headTop
  },
  created() {
    this.init();
  },
  methods: {
    init() {
      exeAllInstanceInfo().then(data => {
        this.tableData = data
      })
    },
    deleteItem(row) {
      this.$confirm('是否禁用该实例?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteInstance(row.instanceId).then(() => {
          this.$message({
            type: 'success',
            message: '禁用成功!'
          });
          this.init();
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消禁用'
        });
      });

    },
    handlerEdit() {
      console.log(this.editForm);
      editInstanceInfo(this.editForm).then((data) => {
        this.init();
      }).finally(() => {
        this.dialogVisible = false;
      })
    },
    edit(row) {
      this.editForm = {
        ...row
      };
      this.dialogVisible = true;
    },
    AddInstance(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          insertInstance(this.form).then((data) => {
            this.init();
            if(data[0][0]===0){
              this.$notify({
               title: '成功',
               message: '添加实例成功',
               type: 'success'
            });
            }else{
              this.$notify.error({
              title: '添加失败',
              message: data[0][1],
            });
            }
          })
        } else {
          this.$notify.error({
            title: "错误",
            message: "请仔细核对输入"
          });
        }
      })
    },

  },
  filters: {
    formatDate(date, fmt) {

      if (!date) {
        return '';
      }
      var date = new Date(+date)
      if (/(y+)/.test(fmt)) {
        fmt = fmt.replace(RegExp.$1, (date.getFullYear() + '').substr(4 - RegExp.$1.length))
      }
      let o = {
        'M+': date.getMonth() + 1,
        'd+': date.getDate(),
        'h+': date.getHours(),
        'm+': date.getMinutes(),
        's+': date.getSeconds()
      }
      for (let k in o) {
        if (new RegExp(`(${k})`).test(fmt)) {
          let str = o[k] + ''
          fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? str : padLeftZero(str))
        }
      }
      return fmt
    }
  },
  data() {
    return {
      form: {},
      editForm: {},
      dialogVisible: false,
      tableData: [],
      rules: {
        instanceName: [{
          required: true,
          message: "请输入实例信息",
          trigger: "blur"
        }],
        instanceIp: [{
          required: true,
          message: "请输入实例IP地址",
          trigger: "blur"
        }],
        instancePort: [{
          required: true,
          message: "请输入实例端口",
          trigger: "blur"
        }],
        instanceUser: [{
          required: true,
          message: "请输入实例用户名",
          trigger: "blur"
        }],
        instancePasswd: [{
          required: true,
          message: "请输入实例密码",
          trigger: "blur"
        }]
      },
      rules_update: {
        instanceName: [{
          required: true,
          message: "请输入实例信息",
          trigger: "blur"
        }],
        instanceIp: [{
          required: true,
          message: "请输入实例IP地址",
          trigger: "blur"
        }],
        instancePort: [{
          required: true,
          message: "请输入实例端口",
          trigger: "blur"
        }],
        instanceUser: [{
          required: true,
          message: "请输入实例用户名",
          trigger: "blur"
        }],
      },
      options: [{
        value: '是',
        label: '是'
      }, {
        value: '否',
        label: '否'
      }, ],
    }
  },
}
</script>

<style lang="less" scoped>
.table {
  margin-top: 20px;
}

.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 20px;
  }
}

.el-col {
  border-radius: 40px;
}

.row-bg {
  padding: 40px 0;
  background-color: #ddd;
}

.row {
  margin-top: 40px;
}
</style>
