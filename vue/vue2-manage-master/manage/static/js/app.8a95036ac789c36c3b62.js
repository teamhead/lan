webpackJsonp([17],{101:function(n,t,e){"use strict";e.d(t,"p",function(){return u}),e.d(t,"q",function(){return i}),e.d(t,"t",function(){return o}),e.d(t,"r",function(){return a}),e.d(t,"s",function(){return c}),e.d(t,"u",function(){return f}),e.d(t,"w",function(){return d}),e.d(t,"y",function(){return s}),e.d(t,"g",function(){return p}),e.d(t,"x",function(){return l}),e.d(t,"v",function(){return h}),e.d(t,"o",function(){return m}),e.d(t,"b",function(){return b}),e.d(t,"l",function(){return v}),e.d(t,"m",function(){return g}),e.d(t,"n",function(){return T}),e.d(t,"d",function(){return O}),e.d(t,"f",function(){return P}),e.d(t,"h",function(){return S}),e.d(t,"e",function(){return w}),e.d(t,"c",function(){return _}),e.d(t,"a",function(){return q}),e.d(t,"k",function(){return y}),e.d(t,"j",function(){return x}),e.d(t,"i",function(){return k});var r=e(143),u=function(n){return e.i(r.a)("/queryDb/",n,"POST")},i=function(){return e.i(r.a)("/queryInstance/",{},"POST")},o=function(n){return e.i(r.a)("/backup/",n,"POST")},a=function(n){return e.i(r.a)("/restore/",n,"POST")},c=function(n){return e.i(r.a)("/exe_sql/",n,"POST")},f=function(n){return e.i(r.a)("/queryInstanceAll/",n,"POST")},d=function(n){return e.i(r.a)("/updateInstance/",n,"POST")},s=function(n){return e.i(r.a)("/deleteInstance/",n,"POST")},p=function(n){return e.i(r.a)("/deleteConfig/",n,"POST")},l=function(n){return e.i(r.a)("/ins_instance/",n,"POST")},h=function(n){return e.i(r.a)("/insertDBInfo/",n,"POST")},m=function(n){return e.i(r.a)("/getUsersql/",n,"POST")},b=function(n){return e.i(r.a)("/insertBigData/",n,"POST")},v=function(n){return e.i(r.a)("/queryALLBigData/",n,"POST")},g=function(n){return e.i(r.a)("/updataBigData/",n,"POST")},T=function(){return e.i(r.a)("/deleteBigData/",{},"POST")},O=function(n){return e.i(r.a)("/queryAF/",n,"POST")},P=function(n){return e.i(r.a)("/updateAF/",n,"POST")},S=function(n){return e.i(r.a)("/queryAFCondition/",n,"POST")},w=function(n){return e.i(r.a)("/ins_zabbix/",n,"POST")},_=function(){return e.i(r.a)("/admin/signout")},q=function(n){return e.i(r.a)("/statis/"+n+"/count")},y=function(n){return e.i(r.a)("/admin/all",n)},x=function(){return e.i(r.a)("/admin/count")},k=function(){return e.i(r.a)("/v1/user/city/count")}},143:function(n,t,e){"use strict";e.d(t,"a",function(){return a});var r=e(68),u=e.n(r),i=e(127),o=e.n(i);o.a.interceptors.response.use(function(n){if(200===n.status)return n.data;console.log("请求错误")},function(n){return u.a.reject(n)}),o.a.interceptors.request.use(function(n){return n.headers={"Content-Type":"application/json;charset=UTF-8"},n},function(n){return u.a.reject(n)});var a=function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},e=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"get";return n="http://sqlmanager.e6gpshk.com/api"+n,"get"===e.toLowerCase()?o.a.get(n,t):"post"===e.toLowerCase()?o.a.post(n,t):void 0}},144:function(n,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=e(1),u=e(99),i=e.n(u),o=e(95),a=e(96),c=e(97),f=e.n(c),d=e(98);e.n(d);r.default.config.productionTip=!1,r.default.use(f.a),new r.default({el:"#app",router:o.a,store:a.a,template:"<App/>",components:{App:i.a}})},145:function(n,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={}},205:function(n,t){},218:function(n,t){n.exports={render:function(){var n=this,t=n.$createElement,e=n._self._c||t;return e("div",{staticClass:"fillcontain",attrs:{id:"app"}},[e("router-view")],1)},staticRenderFns:[]}},95:function(n,t,e){"use strict";var r=e(1),u=e(219);r.default.use(u.a);var i=function(n){return e.e(14).then(function(){return n(e(230))}.bind(null,e)).catch(e.oe)},o=function(n){return e.e(15).then(function(){return n(e(231))}.bind(null,e)).catch(e.oe)},a=function(n){return e.e(9).then(function(){return n(e(225))}.bind(null,e)).catch(e.oe)},c=function(n){return e.e(10).then(function(){return n(e(224))}.bind(null,e)).catch(e.oe)},f=function(n){return e.e(6).then(function(){return n(e(233))}.bind(null,e)).catch(e.oe)},d=function(n){return e.e(2).then(function(){return n(e(234))}.bind(null,e)).catch(e.oe)},s=function(n){return e.e(5).then(function(){return n(e(236))}.bind(null,e)).catch(e.oe)},p=function(n){return e.e(7).then(function(){return n(e(229))}.bind(null,e)).catch(e.oe)},l=function(n){return e.e(8).then(function(){return n(e(226))}.bind(null,e)).catch(e.oe)},h=function(n){return e.e(0).then(function(){return n(e(237))}.bind(null,e)).catch(e.oe)},m=function(n){return e.e(13).then(function(){return n(e(232))}.bind(null,e)).catch(e.oe)},b=function(n){return e.e(12).then(function(){return n(e(235))}.bind(null,e)).catch(e.oe)},v=function(n){return e.e(1).then(function(){return n(e(238))}.bind(null,e)).catch(e.oe)},g=function(n){return e.e(4).then(function(){return n(e(227))}.bind(null,e)).catch(e.oe)},T=function(n){return e.e(11).then(function(){return n(e(223))}.bind(null,e)).catch(e.oe)},O=function(n){return e.e(3).then(function(){return n(e(228))}.bind(null,e)).catch(e.oe)},P=[{path:"/",component:i},{path:"/manage",component:o,name:"",children:[{path:"/addinstance",component:a,meta:["实例信息管理","添加实例"]},{path:"/add_dbname",component:c,meta:["实例信息管理","实例信息管理"]},{path:"/sqlbackup",component:f,meta:["备份还原","数据库备份"]},{path:"/sqlrestore",component:d,meta:["备份还原","数据库还原"]},{path:"/userhandle",component:s,meta:["备份还原","数据库用户问题处理"]},{path:"/big_data_show",component:p,meta:["大数据同步","大数据信息页"]},{path:"/adminList",component:l,meta:["数据管理","管理员列表"]},{path:"/visitor",component:h,meta:["图表","用户分布"]},{path:"/newMember",component:m,meta:["图表","用户数据"]},{path:"/uploadImg",component:b,meta:["文本编辑","MarkDown"]},{path:"/vueEdit",component:v,meta:["编辑","文本编辑"]},{path:"/autofind",component:g,meta:["自动发现配置","查询自动发现配置"]},{path:"/add_autofind",component:T,meta:["自动发现配置","添加自动发现配置"]},{path:"/big_data",component:O,meta:["大数据同步","大数据添加页"]},{path:"/",redirect:"/addinstance"}]}];t.a=new u.a({routes:P,strict:!1})},96:function(n,t,e){"use strict";var r=e(103),u=e.n(r),i=e(102),o=e.n(i),a=e(1),c=e(104),f=e(101);a.default.use(c.a);var d={adminInfo:{avatar:"default.jpg"}},s={saveAdminInfo:function(n,t){n.adminInfo=t}},p={getAdminData:function(n){var t=this,r=n.commit;return o()(u.a.mark(function n(){var i;return u.a.wrap(function(n){for(;;)switch(n.prev=n.next){case 0:return n.prev=0,n.next=3,e.i(f.a)();case 3:if(i=n.sent,1!=i.status){n.next=8;break}r("saveAdminInfo",i.data),n.next=9;break;case 8:throw new Error(i.type);case 9:n.next=13;break;case 11:n.prev=11,n.t0=n.catch(0);case 13:case"end":return n.stop()}},n,t,[[0,11]])}))()}};t.a=new c.a.Store({state:d,actions:p,mutations:s})},98:function(n,t){},99:function(n,t,e){e(205);var r=e(100)(e(145),e(218),null,null);n.exports=r.exports}},[144]);