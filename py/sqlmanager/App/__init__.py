from App.BackupAndRestory.views import BkAndRs
from App.InsertDb.views import QItance
from App.InsertInstance.views import IIstance
from App.Zabbix.views import Zbx
from App.setting import *
from App.BigData.views import *
from flask import Flask
from flask_script import Manager
from flask_cors import *




app = Flask(__name__)
app.config.from_object(Config)
CORS(app, supports_credentials=True)
manage = Manager(app)
app.register_blueprint(blueprint=BkAndRs)
app.register_blueprint(blueprint=QItance)
app.register_blueprint(blueprint=IIstance)
app.register_blueprint(blueprint=Zbx)
app.register_blueprint(blueprint=BData)
