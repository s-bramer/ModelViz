from flask import render_template
from . import model_bp

@model_bp.route('/model')
def model():
    return render_template('home/manual.html')