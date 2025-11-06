from flask import Blueprint

report_bp = Blueprint(
    'report',
    __name__,
    url_prefix='',
    template_folder="../templates", 
    static_folder="../static", 
    static_url_path='/apps/static'
)
from . import routes