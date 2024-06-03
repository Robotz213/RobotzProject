from flask import Flask

from app.dashboard import dashboard_blueprint
from app.home import home_blueprint
from app.auth import auth_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(dashboard_blueprint, url_prefix = "/dashboard")
app.register_blueprint(auth_blueprint, url_prefix = "")

