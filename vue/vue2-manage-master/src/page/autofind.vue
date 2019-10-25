<template>
    <div>
        <head-top></head-top>
        <el-row :gutter="24" class='row'>
            <el-form ref="form" :model="form" label-width="80px">
                <el-col :span="4">
                    <el-form-item label="键值">
                        <el-input v-model="form.key" placeholder="请输入键值"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="6">
                    <el-form-item label="库名">
                        <el-input v-model="form.db_name" placeholder="请输入数据库名称"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="6">
                    <el-form-item label="查询间隔">
                        <el-select v-model="form.interval" placeholder="请选择时间间隔">
                            <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="2">
                    <el-form-item>
                        <el-button type="primary" @click="queryAFCondition">查询</el-button>
                    </el-form-item>
                </el-col>
            </el-form>
        </el-row>
        <el-table :data="tableData" border style="width: 100%" class='table'>
            <el-table-column
                show-overflow-tooltip
                prop="tableData.key"
                label="键值"
                width="120">
            </el-table-column>
            <el-table-column
                show-overflow-tooltip
                prop="tableData.db_name"
                label="库名"
                width="180">
            </el-table-column>
            <el-table-column
                show-overflow-tooltip
                prop="tableData.sql_content"
                label="SQL语句">
            </el-table-column>
            <el-table-column
                prop="tableData.type"
                label="类型"
                width="120">
            </el-table-column>
            <el-table-column
                prop="tableData.interval"
                label="时间间隔"
                width="120">
            </el-table-column>
            <el-table-column
                show-overflow-tooltip
                prop="tableData.description"
                label="描述"
                width="300">
            </el-table-column>
            <el-table-column
                fixed="right"
                label="操作"
                width="100">
                <template slot-scope="scope">
                    <el-button @click="edit(scope.row)" type="text" size="small">修改</el-button>
                    <el-button @click="deleteItem(scope.row)" type="text" size="small">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page.sync="currentPage"
            :page-size="pageSize"
            layout="total, prev, pager, next"
            :total="total">
        </el-pagination>
        <el-dialog
            title="修改"
            :visible.sync="dialogVisible"
            width="50%"
        >
            <el-form ref="form" :model="editForm" label-width="80px">
                <el-form-item label="键值">
                    <el-input v-model="editForm.key" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="库名">
                    <el-input v-model="editForm.db_name"></el-input>
                </el-form-item>
                <el-form-item label="SQL语句">
                    <el-input v-model="editForm.sql_content"></el-input>
                </el-form-item>
                <el-form-item label="类型">
                    <el-input v-model="editForm.type"></el-input>
                </el-form-item>
                <el-form-item label="时间间隔">
                    <el-select v-model="editForm.interval" placeholder="请选择时间间隔">
                        <el-option
                            v-for="item in options"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="handlerEdit">确 定</el-button>
          </span>
        </el-dialog>
    </div>
</template>

<script>
	import headTop from '../components/headTop'
	import {deleteConfig, queryAF,updateAF,queryAFC} from './../api/getData_new'
	export default {
		components: {
			headTop
		},
		created() {
			this.init()
		},
		methods: {
			handleCurrentChange() {
				this.search()
			},
			init() {
				const params = {
					pageSize: this.pageSize,
					currentPage: this.currentPage
				};
				queryAF(params).then(data => {
					console.log(data);
					this.tableData = data['msg'];
                    this.total = data['count']
				})
			},
			edit(row) {
				this.editForm = row;
				this.dialogVisible = true;
			},
			handlerEdit() {
				updateAF(this.editForm).then((data) => {
					this.init();
				}).finally(() => {
					this.dialogVisible = false;
				})
			},
			deleteItem(row) {
				this.$confirm('是否删除该配置?', '提示', {
					confirmButtonText: '确定',
					cancelButtonText: '取消',
					type: 'warning'
				}).then(() => {
					deleteConfig(row.id).then(() => {
						this.$message({
							type: 'success',
							message: '删除成功!'
						});
					})
				}).catch(() => {
					this.$message({
						type: 'info',
						message: '已取消删除'
					});
				});
			},
			handleSizeChange(val) {
				console.log(`每页 ${val} 条`);
				this.pageSize = '${val}';
				this.init();

			},
			handleCurrentChange(val) {
				console.log(`当前页: ${val}`);
				this.currentPage = "${val}";
			},
			queryAFCondition(){
				queryAFC(this.form).then(data =>{
					console.log(data)
                })
            }
		},

		data() {
			return {
				dialogVisible: false,
				editForm: {},
				key: '',
				db_name: '',
				options: [{
					value: 60,
					label: '60s'
				}, {
					value: 300,
					label: '300s'
				}, {
					value: 600,
					label: '600s'
				}],
				interval: '',
				tableData: [],
				form: {
					key:'',
					db_name:'',
					interval:''
                },
				editForm: {},
				pageSize: 10,
				currentPage: 1,
				total: 0,

			}
		}
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
