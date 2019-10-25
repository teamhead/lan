from flask import Blueprint

QItance = Blueprint("QueryInstance",__name__)
from . import views
