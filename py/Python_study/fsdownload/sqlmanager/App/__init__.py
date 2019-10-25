from App.BackupAndRestory.views import BkAndRs
from App.QueryInstance.views import QItance
from App.InsertInstance.views import IIstance
from App.Zabbix.views import Zbx
from flask import Flask
from flask_script import Manager
from flask_cors import *
from App.setting import *



app = Flask(__name__)
app.config.from_object(Config)
CORS(app, supports_credentials=True)
manager = Manager(app=app)
app.register_blueprint(blueprint=BkAndRs)
app.register_blueprint(blueprint=QItance)
app.register_blueprint(blueprint=IIstance)
app.register_blueprint(blueprint=Zbx)

