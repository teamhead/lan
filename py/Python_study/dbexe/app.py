from flask import request,render_template,Flask,redirect,url_for
from test1 import *
import time
import datetime
import pymysql
from flask_sqlalchemy import SQLAlchemy
import datetime

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://db_mng_user:X2rePFHQaY-mGEdFcCM9n@rm-wz9954fkn5h96zerz.mysql.rds.aliyuncs.com:3306/db_manage_pfm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Instance_info(db.Model):
    '''初始化实例信息数据表'''
    __tablename__ = 'instance_info'
    created_user_id = db.Column(db.Integer,nullable = False,default = 0)                         # 创建人
    created_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)    # 创建时间
    modified_user_id = db.Column(db.Integer,nullable = False,default = 0)                        # 修改人
    modified_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)   # 修改时间
    isvalid = db.Column(db.Integer,nullable = False,default = 1)                                 # 是否有效，1:有效;0:无效
    instance_id = db.Column(db.Integer,nullable = False,autoincrement = True,primary_key = True) # 主键ID
    instance_name = db.Column(db.String(80),nullable = False)                                    # 实例名称'
    instance_ip_addr = db.Column(db.String(255),nullable = False)                     # 实例IP地址
    instance_db_port = db.Column(db.String(32),nullable = False)                   # 实例端口
    instance_user_name = db.Column(db.String(32),nullable = False)                               # 实例登录名
    instance_passwd = db.Column(db.String(32),nullable = False)                                  # 实例登录密码
    db_name = db.relationship("DB_info", backref="instance_info", lazy="dynamic")

    def __repr__(self):
        return "<User '{:s}'>".format(self.instance_name)

class DB_info(db.Model):
    '''初始化数据库信息表'''
    __tablename__ = 'db_info'
    created_user_id = db.Column(db.Integer,nullable = False,default = 0)                         # 创建人
    created_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)    # 创建时间
    modified_user_id = db.Column(db.Integer,nullable = False,default =0)                         # 修改人
    modified_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)   # 修改时间
    isvalid = db.Column(db.Integer,nullable = False,default = 1)                                 # 是否有效，1:有效;0:无效
    db_id = db.Column(db.Integer,nullable = False,autoincrement = True,primary_key = True)       # 主键ID
    db_name = db.Column(db.String(80),nullable = False,unique = True)                            # 数据库ID
    db_backup_path = db.Column(db.String(255),nullable = False,default='/')                                  # 备份路径
    instance_id = db.Column(db.Integer, db.ForeignKey('instance_info.instance_id'))

    def __repr__(self):
        return "<User '{:s}'>".format(self.db_name)

class User_info(db.Model):
    '''初始化用户信息表'''
    __tablename__ = 'user_info'
    created_user_id = db.Column(db.Integer,nullable = False,default = 0)                         # 创建人
    created_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)    # 创建时间
    modified_user_id = db.Column(db.Integer,nullable = False,default = 0)                        # 修改人
    modified_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)   # 修改时间
    isvalid = db.Column(db.Integer,nullable = False,default = 1)                                 # 是否有效，1:有效;0:无效
    user_id = db.Column(db.Integer,nullable = False,autoincrement = True,primary_key = True)     # 主键ID
    user_name = db.Column(db.String(32),nullable = False)                     # 用户名
    user_passwd = db.Column(db.String(32),nullable = False)                                      # 用户密码

    def __repr__(self):
        return "<User '{:s}'>".format(self.dbname)

class Zabbix_monitor_config(db.Model):
    '''初始化自动发现数据表'''
    __tablename__ = 'zabbix_monitor_config'
    monitorkey = db.Column(db.String(255),nullable = False,primary_key=True)
    sql_content = db.Column(db.Text,nullable = False)
    mon_interval = db.Column(db.Integer,nullable = False)
    type = db.Column(db.String(20),nullable = False)
    db_id = db.Column(db.Integer,nullable = False)
    create_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)
    creator = db.Column(db.String(255),nullable = False )
    update_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)
    updator = db.Column(db.String(255),nullable = False)
    description = db.Column(db.String(255),nullable = False)


    def __repr__(self):
        return "<User '{:s}'>".format(self.dbname)
#
db.create_all()

# 添加实例页
@app.route('/insert_instance',methods=['GET','POST'])
def insert():
    # 判断请求，如果是get请求返回页面，如果是post请求，将参数写入数据库
    if request.method == 'GET':
        return render_template('insertdb.html')
    if request.method == 'POST':
        # 从模板获取用户输入的信息
        instance_name = request.form.get('easname')
        instance_ip_addr = request.form.get('ipaddr')
        instance_db_port = request.form.get('db_port')
        instance_user_name = request.form.get('username')
        instance_passwd = request.form.get('passwd')
        # 查询数据库已存在的实例
        instance_ip_addrs = db.session.query(Instance_info).filter(Instance_info.instance_ip_addr == instance_ip_addr).all()
        print('获取数据')
        if instance_ip_addrs:
            for i in instance_ip_addrs:
                # 判断IP和端口是否存在
                if i.instance_ip_addr == instance_ip_addr and i.instance_db_port == instance_db_port:
                    return '此实例已存在'
        else:
            # 连接msqlserver 并将sqlserver中的所有数据库信息插入DB_info
            print('连接msqlserver 并将sqlserver中的所有数据库信息插入DB_info')
            data = Instance_info(instance_name=instance_name,instance_ip_addr=instance_ip_addr,instance_db_port=instance_db_port,instance_user_name=instance_user_name, instance_passwd = instance_passwd )
            try:
                print('添加实例')
                db.session.add(data)
                db.session.commit()
                return render_template('insertdb.html')
            except:
                return '添加失败'


# 数据库更新页
@app.route('/insert_db',methods=['GET','POST'])
def insert_a():
    if request.method=="GET":
        infos = db.session.query(Instance_info).all()
        return render_template('update_db.html',info = infos)
    elif request.method=="POST":
        # 需要的参数 db, instance_ip_addr
        args = request.form.get('instance')
        if db.session.query(Instance_info).filter(Instance_info.instance_name == args).all():
            infos = db.session.query(Instance_info).filter(Instance_info.instance_name == args).all()
            print(infos)
            for info in infos:
                host = info.instance_ip_addr
                username = info.instance_user_name
                passswd = info.instance_passwd
                datebase ='E6ManagerDB'
                port = info.instance_db_port
                DBsql = Data_SQLserver(host,username,passswd,datebase, port)
                sql = 'select name from sys.databases;'
                datas = DBsql.select_SQL_Db(sql)
                print(datas)
                for data in datas:
                    print(data[0])
                    time.sleep(0.1)
                    SQL_data = DB_info(db_name=data[0],instance_id=info.instance_id,db_backup_path='/admin')
                    if db.session.query(DB_info).filter(DB_info.db_name==data[0]):
                        try:
                            modify = db.session.query(DB_info).filter(DB_info.db_name==data).all()[0]
                            modify.modified_time = datetime.datetime.now()
                        except:
                            return '<script>alert("添加失败")</script>'
                        finally:
                            db.session.commit()
                    else:
                        try:
                                db.session.add(SQL_data)
                        except:
                            return '添加失败'
                        finally:
                            db.session.commit()
            return "<script>alert('同步成功')</script>"
        else:
            return '<script>alert("添加失败")</script>'

# 首页
@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == "GET":
        insts = db.session.query(Instance_info).all()
        dbs = db.session.query(DB_info).all()
        return render_template('index.html',insts = insts,dbs=dbs)
    # if request.method == "POST":
    #     ECSName = request.form.get('EASName')
    #     if db.session.query(Instance_info).filter():
    #         return redirect('/insert_instance')

@app.route('/index_instance/<instance_name>',methods=["GET",'POST'])
def instance_name_l(instance_name):
    if request.method == "GET":
        instance_num=int(instance_name)
        instance_name = db.session.query(DB_info).filter(DB_info.instance_id==instance_num).all()
        insts = db.session.query(Instance_info).all()
        return render_template('index.html',insts=insts,dbs = instance_name)
    elif request.method == "POST":
        DatabaseNames = request.values.getlist('db_name')
        BKFileUrl = request.form.get('BKFileUrl')
        BKDBKey = request.form.get('BKDBKey')
        OperType = request.form.get('OperType')
        BKMode = request.form.get('BKMode')
        RSMode = request.form.get('RSMode')
        RSOper = request.form.get('RSOper')
        DBFileUrl = request.form.get('DBFileUrl')
        LogFileUrl = request.form.get('LogFileUrl')
        UserName = request.form.get('UserName')
        PassWD = request.form.get('PassWD')
        OperMode = request.form.get('OperMode')
        OperT = {'MD:创建目录':'MD','BK:备份':'BK','RS:还原':'RS','CU:创建账户':'CU'}
        BKMo = {'0:全备':0,'1:差异':1,'2:日志':2}
        RSOp = {'0:完全还原':0,'1:不完全还原':1}
        OperM={'0:处理孤立用户':0,'1:新建用户授权':1}


        Instance_ids = db.session.query(DB_info).filter(DB_info.db_name == db_name).all()[0].instance_id
        instance = db.session.query(Instance_info).filter(Instance_info.instance_id == Instance_ids).all()[0]
        host = instance.instance_ip_addr
        user = instance.instance_user_name
        passswd = instance.instance_passwd
        port = instance.instance_db_port
        DBsql = Data_SQLserver(host, user, passswd, 'E6ManagerDB', port)
        for db_name in DatabaseNames:
            # print(db_name,BKFileUrl,BKDBKey,OperType,BKMode,RSMode,RSOper,DBFileUrl,LogFileUrl,UserName,PassWD,OperMode)
            sql =   r"exec BR.prBKandRestoreDBAll @DatabaseNames = N'{0}',@BKFileUrl = N'{1}',@BKDBKey = N'{2}',@OperType = N'{3}',@BKMode={4},@RSMode= {5},@RSOper= {6}, @DBFileUrl= N'{7}',@LogFileUrl= N'{8}',@UserName='{9}',@PassWD='{10}',@OperMode={11}".format(db_name,BKFileUrl,BKDBKey,OperT[OperType],BKMo[BKMode],BKMo[RSMode],RSOp[RSOper],DBFileUrl,LogFileUrl,UserName,PassWD,OperM[OperMode])
            print(sql)

            DBsql.select_SQL_Db(sql)

        return 'ok'

#切换镜像页面
@app.route('/faildb',methods=["GET","POST"])
def faildb():
    if request.method=="GET":
        return render_template('faildb.html')


# 大数据配置管理页
@app.route('/bigdata')
def bigdata():
    return render_template('bigdata.html')

# 自动发现页
@app.route('/autodiscovery')
def autodiscovery():
    
    return render_template('autodiscovery.html')

#短信功能页
@app.route('/message')
def message():
    return render_template('message.html')

# 分区管理页
@app.route('/table')
def table():
    return render_template('table.html')




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
