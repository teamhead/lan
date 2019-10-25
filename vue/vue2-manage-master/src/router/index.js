import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const login = r => require.ensure([], () => r(require('@/page/login')), 'login');
const manage = r => require.ensure([], () => r(require('@/page/manage')), 'manage');
// const home = r => require.ensure([], () => r(require('@/page/home')), 'home');


// 添加实例
const addinstance = r => require.ensure([], () => r(require('@/page/addinstance')), 'addinstance');
// 添加数据库
const add_dbname = r => require.ensure([], () => r(require('@/page/add_dbname')), 'add_dbname');
//数据库备份
const sqlbackup = r => require.ensure([], () => r(require('@/page/sqlbackup')), 'sqlbackup');
// 数据库还原
const sqlrestore = r => require.ensure([], () => r(require('@/page/sqlrestore')), 'sqlrestore');
// 用户权限操作
const userhandle = r => require.ensure([], () => r(require('@/page/userhandle')), 'userhandle');
//大数据展示
const big_data_show = r => require.ensure([], () => r(require("@/page/big_data_show")), "big_data_show");


const adminList = r => require.ensure([], () => r(require('@/page/adminList')), 'adminList');
const visitor = r => require.ensure([], () => r(require('@/page/visitor')), 'visitor');
const newMember = r => require.ensure([], () => r(require('@/page/newMember')), 'newMember');
const uploadImg = r => require.ensure([], () => r(require('@/page/uploadImg')), 'uploadImg');
const vueEdit = r => require.ensure([], () => r(require('@/page/vueEdit')), 'vueEdit');
// 查询自动发现
const autofind = r => require.ensure([], () => r(require('@/page/autofind')), 'autofind');
// 添加自动发现
const add_autofind = r => require.ensure([], () => r(require('@/page/add_autofind')), 'add_autofind');
// 大数据同步页
const big_data = r => require.ensure([], () => r(require('@/page/big_data')), 'big_data');

const routes = [
    {
        path: "/",
        component: login
    },
    {
        path: "/manage",
        component: manage,
        name: "",
        children: [
            // {
            //     path: "",
            //     component: home,
            //     meta: []
            // },
            {
                // 添加实例
                path: "/addinstance",
                component: addinstance,
                meta: ["实例信息管理", "添加实例"]
            },
            {
                path: "/add_dbname",
                component: add_dbname,
                meta: ["实例信息管理", "实例信息管理"]
            },
            {
                //数据库备份
                path: "/sqlbackup",
                component: sqlbackup,
                meta: ["备份还原", "数据库备份"]
            },
            {
                //数据库还原
                path: "/sqlrestore",
                component: sqlrestore,
                meta: ["备份还原", "数据库还原"]
            },
            {
                // 用户处理
                path: "/userhandle",
                component: userhandle,
                meta: ["备份还原", "数据库用户问题处理"]
            },
            {
                path: "/big_data_show",
                component: big_data_show,
                meta: ["大数据同步", "大数据信息页"]
            },
            {
                path: "/adminList",
                component: adminList,
                meta: ["数据管理", "管理员列表"]
            },
            {
                path: "/visitor",
                component: visitor,
                meta: ["图表", "用户分布"]
            },
            {
                path: "/newMember",
                component: newMember,
                meta: ["图表", "用户数据"]
            },
            {
                path: "/uploadImg",
                component: uploadImg,
                meta: ["文本编辑", "MarkDown"]
            },
            {
                path: "/vueEdit",
                component: vueEdit,
                meta: ["编辑", "文本编辑"]
            },
            {
                // 查询自动发现
                path: "/autofind",
                component: autofind,
                meta: ["自动发现配置", "查询自动发现配置"]
            },
            {
                // 添加自动发现
                path: "/add_autofind",
                component: add_autofind,
                meta: ["自动发现配置", "添加自动发现配置"]
            },
            {
                path: "/big_data",
                component: big_data,
                meta: ["大数据同步", "大数据添加页"]
            },
            {
                path: '/',
                redirect: '/addinstance'
            }
        ]
    }
];

export default new Router({
	routes,
	strict: process.env.NODE_ENV !== 'production',
})
