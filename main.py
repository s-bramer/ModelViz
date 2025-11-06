from flask import Flask
from apps.home import home_bp
from apps.model import model_bp
from apps.report import report_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(model_bp)
app.register_blueprint(report_bp)

if __name__ == "__main__":
    app.run(debug=True)