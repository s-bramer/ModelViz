from flask import render_template
from . import report_bp

@report_bp.route('/report')
def report():
    return render_template('home/manual.html')