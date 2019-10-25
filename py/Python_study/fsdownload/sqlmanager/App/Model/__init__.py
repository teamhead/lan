# import datetime
# import pymysql
# from flask_sqlalchemy import SQLAlchemy
#
# pymysql.install_as_MySQLdb()
# db = SQLAlchemy()
#
# class Instance_info(db.Model):
#     '''初始化实例信息数据表'''
#     __tablename__ = 'instance_info'
#     created_user_id = db.Column(db.Integer,nullable = False,default = 0)                         # 创建人
#     created_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)    # 创建时间
#     modified_user_id = db.Column(db.Integer,nullable = False,default = 0)                        # 修改人
#     modified_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)   # 修改时间
#     isvalid = db.Column(db.Integer,nullable = False,default = 1)                                 # 是否有效，1:有效;0:无效
#     instance_id = db.Column(db.Integer,nullable = False,autoincrement = True,primary_key = True) # 主键ID
#     instance_name = db.Column(db.String(80),nullable = False)                                    # 实例名称'
#     instance_ip_addr = db.Column(db.String(255),nullable = False,unique = True)                  # 实例IP地址
#     instance_db_port = db.Column(db.String(32),nullable = False,unique = True)                   # 实例端口
#     instance_user_name = db.Column(db.String(32),nullable = False)                               # 实例登录名
#     instance_passwd = db.Column(db.String(32),nullable = False)                                  # 实例登录密码
#     db_name = db.relationship("DB_info", backref="instance_info", lazy="dynamic")
#
#     def __repr__(self):
#         return "<User '{:s}'>".format(self.instance_name)
#
# class DB_info(db.Model):
#     '''初始化数据库信息表'''
#     __tablename__ = 'db_info'
#     created_user_id = db.Column(db.Integer,nullable = False,default = 0)                         # 创建人
#     created_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)    # 创建时间
#     modified_user_id = db.Column(db.Integer,nullable = False,default =0)                         # 修改人
#     modified_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)   # 修改时间
#     isvalid = db.Column(db.Integer,nullable = False,default = 1)                                 # 是否有效，1:有效;0:无效
#     db_id = db.Column(db.Integer,nullable = False,autoincrement = True,primary_key = True)       # 主键ID
#     db_name = db.Column(db.String(80),nullable = False,unique = True)                            # 数据库ID
#     db_backup_path = db.Column(db.String(255),nullable = False,default='/')                                  # 备份路径
#     instance_id = db.Column(db.Integer, db.ForeignKey('instance_info.instance_id'))
#
#     def __repr__(self):
#         return "<User '{:s}'>".format(self.db_name)
#
# class User_info(db.Model):
#     '''初始化用户信息表'''
#     __tablename__ = 'user_info'
#     created_user_id = db.Column(db.Integer,nullable = False,default = 0)                         # 创建人
#     created_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)    # 创建时间
#     modified_user_id = db.Column(db.Integer,nullable = False,default = 0)                        # 修改人
#     modified_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)   # 修改时间
#     isvalid = db.Column(db.Integer,nullable = False,default = 1)                                 # 是否有效，1:有效;0:无效
#     user_id = db.Column(db.Integer,nullable = False,autoincrement = True,primary_key = True)     # 主键ID
#     user_name = db.Column(db.String(32),nullable = False)                     # 用户名
#     user_passwd = db.Column(db.String(32),nullable = False)                                      # 用户密码
#
#     def __repr__(self):
#         return "<User '{:s}'>".format(self.dbname)
#
# class Zabbix_monitor_config(db.Model):
#     '''初始化自动发现数据表'''
#     __tablename__ = 'zabbix_monitor_config'
#     monitorkey = db.Column(db.String(255),nullable = False,primary_key=True)
#     sql_content = db.Column(db.Text,nullable = False)
#     mon_interval = db.Column(db.Integer,nullable = False)
#     type = db.Column(db.String(20),nullable = False)
#     db_id = db.Column(db.Integer,nullable = False)
#     create_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)
#     creator = db.Column(db.String(255),nullable = False )
#     update_time = db.Column(db.DateTime,nullable = False,default = datetime.datetime.utcnow)
#     updator = db.Column(db.String(255),nullable = False)
#     description = db.Column(db.String(255),nullable = False)
#
#
#     def __repr__(self):
#         return "<User '{:s}'>".format(self.dbname)
#
#
# if __name__=="__main__":
#     db.create_all()