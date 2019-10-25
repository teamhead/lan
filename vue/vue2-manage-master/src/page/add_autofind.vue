<template>
    <div>
        <head-top></head-top>
        <el-form ref="form" :model="form" label-width="80px">
            <el-row :gutter="24" class='row'>
                <el-col :span="4">
                    <el-form-item label="键值">
                        <el-input v-model="form.monitorkey" placeholder="请输入键值"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="数据库名称">
                        <el-input v-model="form.db_name" placeholder="请输入数据库名称"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="4">
                    <el-form-item label="SQL语句">
                        <el-input v-model="form.sql_content" placeholder="请输入SQL语句"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row :gutter="20">
                <el-col :span="4">
                    <el-form-item label="描述">
                        <el-input v-model="form.description" placeholder="请输入描述"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="4">
                    <el-form-item label="查询间隔">
                        <el-select v-model="form.mon_interval" placeholder="请选择时间间隔">
                            <el-option v-for="item in time_select" :key="item.value" :label="item.label"
                                       :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="4">
                    <el-form-item label="类型">
                        <el-select v-model="form.TYPE" placeholder="请选择类型">
                            <el-option v-for="item in type" :key="item.value" :label="item.label" :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item>
                        <el-button type="primary" @click="insertAFZ">添加</el-button>
                    </el-form-item>
                </el-col>
            </el-row>
        </el-form>
        <el-table :data="tableData" border style="width: 100%" class='table'>
            <el-table-column prop="tableData.instace_name" label="实例名" width="200">
            </el-table-column>
            <el-table-column prop="tableData.ipaddress" label="IP地址" width="200">
            </el-table-column>
            <el-table-column prop="tableData.port" label="端口" width="200">
            </el-table-column>
            <el-table-column prop="tableData.username" label="用户" width="200">
            </el-table-column>
            <el-table-column prop="tableData.dbname_count" label="数据库">
            </el-table-column>
            <el-table-column prop="tableData.date" label="同步时间" width="200">
            </el-table-column>
            <el-table-column fixed="right" label="操作" width="100">
                <template slot-scope="scope">
                    <el-button @click="handleClick(scope.row)" type="text" size="small">删除</el-button>
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
    </div>
</template>
<script>
	import headTop from "../components/headTop";
	import {deleteConfig, queryAF, updateAF, queryAFC,insertAF} from './../api/getData_new'

	export default {
		components: {
			headTop
		},
		created() {
			this.init()
		},
		methods: {
			handleClick(row) {
				console.log(row);
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
			handleSizeChange(val) {
				console.log(`每页 ${val} 条`);
				this.pageSize = '${val}';
				this.init();

			},
			handleCurrentChange(val) {
				console.log(`当前页: ${val}`);
				this.currentPage = "${val}";
			},
			insertAFZ(){
                insertAF(this.form).then(data =>{
                	console.log(data)
                })
            }
		},
		data() {
			return {
				key: "",
				db_name: "",
				time_select: [
					{
						value: 60,
						label: "60s"
					},
					{
						value: 300,
						label: "300s"
					},
					{
						value: 600,
						label: "600s"
					}
				],
				auto_type: "",
				type: [
					{
						value: "int",
						label: "INT"
					},
					{
						value: "str",
						label: "STR"
					}
				],
				interval: "",
				tableData:[],
				form: {
					key:'',
					db_name:'',
					interval:''
				},
				pageSize: 10,
				currentPage: 1,
				total: 0,
			};
		}
	};
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
