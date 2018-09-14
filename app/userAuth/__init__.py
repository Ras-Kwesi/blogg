from flask import Blueprint

userAuth = Blueprint('userAuth',__name__)

from . import views,forms