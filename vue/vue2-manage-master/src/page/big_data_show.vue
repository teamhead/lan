<template>
    <div>
        <head-top></head-top>
        <el-form ref="form" :model="form" label-width="80px" class="row">
            <!--            <el-row :gutter="24" class='row'>-->
            <!--                <el-col :span="6">-->
            <!--                    <el-form-item label="源服务器地址">-->
            <!--                        <el-input v-model="form.SourceServerIP" placeholder="请输入实例名"></el-input>-->
            <!--                    </el-form-item>-->
            <!--                </el-col>-->
            <!--                <el-col :span="6">-->
            <!--                    <el-form-item label="源数据库名">-->
            <!--                        <el-input v-model="form.SyncDBName" placeholder="请输入IP地址"></el-input>-->
            <!--                    </el-form-item>-->
            <!--                </el-col>-->
            <!--                <el-col :span="6">-->
            <!--                    <el-form-item label="源表名">-->
            <!--                        <el-input v-model="form.SyncSchemaName" placeholder="请输入端口号"></el-input>-->
            <!--                    </el-form-item>-->
            <!--                </el-col>-->
            <!--            </el-row>-->
            <el-row :gutter="20">
                <el-col :span="6">
                    <el-form-item label="源数据库">
                        <el-input v-model="form.SyncDBName" placeholder="请输入源数据库"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="6">
                    <el-form-item label="备注">
                        <el-input v-model="form.Remark" placeholder="请输入备注信息"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item>
                        <el-button type="primary" @click="queryRecord()">查询</el-button>
                    </el-form-item>
                </el-col>
            </el-row>
        </el-form>
        <el-table :data="tableData" style="width: 100%" max-height="250">
            <el-table-column fixed prop="SourceServerIP" label="源服务器地址" width="250">
            </el-table-column>
            <el-table-column prop="SyncDBName" label="源数据库名" width="200">
            </el-table-column>
            <el-table-column prop="SyncSchemaName" label="源表名" width="200">
            </el-table-column>
            <el-table-column prop="SyncType" label="源数据库类型" width="200">
            </el-table-column>
            <el-table-column prop="Remark" label="备注" width="200">
            </el-table-column>
            <el-table-column fixed="right" label="操作" width="220">
                <template slot-scope="scope">
                    <el-button @click="edit(scope.row)" type="text" size="small">修改</el-button>
                    <!--                    <el-button @click="dialog = true" type="text" size="small">修改</el-button>-->
                    <el-button type="text" size="small" @click="del(scope.row)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page.sync="currentPage"
            :page-size="pageSize"
            layout="prev, pager, next, jumper"
            :total="total">
        </el-pagination>
        <el-dialog title="修改" :visible.sync="dialogVisible" width="50%">
            <el-form :model="editform" label-width="80px">
                <el-form-item label="源服务器地址" prop="SourceServerIP">
                    <el-input v-model="editform.SourceServerIP"></el-input>
                </el-form-item>
                <el-form-item label="源数据库名" prop="SyncDBName">
                    <el-input v-model="editform.SyncDBName"></el-input>
                </el-form-item>
                <el-form-item label="源表名" prop="SyncSchemaName">
                    <el-input v-model="editform.SyncSchemaName"></el-input>
                </el-form-item>
                <el-form-item label="源数据库类型" prop="SyncType">
                    <el-input v-model="editform.SyncType"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="SyncType">
                    <el-input v-model="editform.SourcePW" type="password"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
      <el-button @click="dialogVisible = false">取 消</el-button>
      <el-button type="primary" @click="handlerEdit('editForm')">确 定</el-button>
    </span>
        </el-dialog>
    </div>
</template>

<script>
	import headTop from "../components/headTop";
	import {
		queryALLBG,
		updateBG,
		deleteBG
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
				queryALLBG(this.form).then(data => {
					console.log(data)
					this.tableData = data;
				})
			},
			queryRecord() {
				this.init();
			},
			edit(row) {
				this.editform = {
					...row
				};

				this.dialogVisible = true;
			},
			deleteRow(index, rows) {
				rows.splice(index, 1);
			},
			handlerEdit() {
				updateBG(this.editform).then((data) => {
					this.init();
				}).finally(() => {
					this.dialogVisible = false;
				})
			},
			del(row) {
				this.$confirm('是否禁用该实例?', '提示', {
					confirmButtonText: '确定',
					cancelButtonText: '取消',
					type: 'warning'
				}).then(() => {
					console.log(row.id);
					deleteBG(row.id).then(() => {
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
		},
		data() {
			return {
				editform: {},
				tableData: [],
				dialogVisible: false,
				form: {}
			}
		}
	}
</script>
<style>
    .row {
        margin-top: 60px;
    }
</style>
