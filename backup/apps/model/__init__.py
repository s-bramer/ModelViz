from flask import Blueprint

model_bp = Blueprint(
    'model',
    __name__,
    url_prefix='',
    template_folder="../templates", 
    static_folder="../static", 
    static_url_path='/apps/static'
)
from . import routes