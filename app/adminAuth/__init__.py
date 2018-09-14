from flask import Blueprint

adminAuth = Blueprint('adminAuth',__name__)

from . import views,forms