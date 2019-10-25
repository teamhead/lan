from flask import request,json
from App.Zabbix.zabbix_handle import *
from . import Zbx

# 添加监控信息
@Zbx.route('/ins_zabbix/',methods=["GET","POST"])
def ins_zabbix():
    '''自动发现页添加数据'''
    if request.method == "GET":
        pass
    elif request.method == "POST":
        zabbix_list = request.json
        print(zabbix_list)
        zbx = Zabbix(zabbix_list)
        message = zbx.add()
        # second = '*/1'
        # exe = Exec_func(second)
        # exe.exe_fun()
        return json.dumps(message)

# 查询监控信息
@Zbx.route('/query_data/',methods=["GET","POST"])
def query_data():
    '''自动发现页查询数据信息'''
    if request.method=="GET":
        pass
    elif request.method == "POST":
        zabbix_list = request.json
        zbx = Zabbix(zabbix_list)
        results = zbx.query()
        return json.dumps(results)

# 调用接口，生成发现监控项json字符串
@Zbx.route('/sql_api/',methods=["POST","GET"])
def sql_api():
    if request.method=="GET":
        pass
    elif request.method=="POST":
        datas = request.get_data(request.form).decode()
        data = json.loads(datas)
        print(data['type'])
        if datas:
            zbx = Zabbix()
            result = zbx.parse_str(data['type'])
        return json.dumps(result,ensure_ascii=False)
