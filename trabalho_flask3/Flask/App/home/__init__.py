from flask import Blueprint

home = Blueprint('home', __name__)

from .menu import *

from .inscreva_se import * 
