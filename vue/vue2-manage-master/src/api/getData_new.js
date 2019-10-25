import {$http} from '@/config/fetch'

/**
 * 获取数据库信息
 */
export const getDBInfo = (instance_name) => $http('/queryDb/',instance_name,'POST');
/**
 * 获取实例信息
 */
export const getInstanceInfo = () => $http("/queryInstance/", {}, "POST");

/**
 * 执行备份程序
 */
export const exeBackup = (data)=> $http('/backup/',data,'POST')
/**
 * 执行还原程序
 */
export const exeRestore = data => $http("/restore/", data, "POST");
/**
 * 生成还原语句
 */
export const exeDetection = (data) => $http('/backup/',data,'POST')
/**
 * 执行SQL语句程序
 */
export const exeSQL = data => $http("/exe_sql/", data, "POST");
/**
 * 查询所有实例信息
 */
export const exeAllInstanceInfo = data => $http("/queryInstanceAll/",data,"POST")
/**
 * 修改实例信息
 */
export const editInstanceInfo = data => $http("/updateInstance/",data,"POST");
/**
 * 禁用实例信息
 */
export const deleteInstance = data => $http("/deleteInstance/",data,"POST");

export const editConfig = data => $http("/editConfig/",data,"POST");

export const deleteConfig = data => $http("/deleteConfig/",data,"POST");

export const insertInstance = data => $http("/ins_instance/", data, "POST");
/**
 * 添加数据库名
 */
export const insertDB = data => $http("/insertDBInfo/",data,"POST");
/**
 * 处理用户
 */
export const userHeadle = data => $http("/getUsersql/", data, "POST");
/**
 * 大数据插入
 */
export const insertBG = data => $http("/insertBigData/",data,"POST");
/**
 * 大数据记录查询
 */
export const queryBG = data => $http("/queryBigData/",data,"POST");
/**
 * 查询所有大数据配置
 */
export const queryALLBG = data => $http("/queryALLBigData/",data,"POST");
/**
 * 修改大数据配置
 */
export const updateBG = data => $http("/updataBigData/",data,"POST");
/**
 * 删除大数据配置
 */
export const deleteBG = () => $http("/deleteBigData/",{},"POST");
/**
 * 自动发现查询
 */
export const queryAF = data => $http("/queryAF/",data,"POST")
/**
 * 修改自动发现配置
 */
export const updateAF = data => $http("/updateAF/",data,"POST")
/**
 * 按照条件查询自动发现配置
 */
export const queryAFC = data => $http("/queryAFCondition/",data,"POST")
/**
 * 添加自动发现
 */
export const insertAF = data => $http("/ins_zabbix/",data,"POST")

//============================================================以下请求不可用=====================================================================================
/**
 * 登陆
 */
export const login = data => $http('/admin/login', data, 'POST');
/**
 * 退出
 */
export const signout = () => $http('/admin/signout');
//这个函数没传参数
export const getAdminInfo = date => $http('/statis/' + date + '/count');
export const apiAllCount = () => $http('/statis/count');
/**
 * 用户注册量
 */
export const adminList = data => $http('/admin/all', data);
export const adminCount = () => $http('/admin/count');
export const searchplace = (cityid, value) => $http('/v1/pois', {
    type: 'search',
    city_id: cityid,
    keyword: value
});
export const getUserCity = () => $http('/v1/user/city/count');
