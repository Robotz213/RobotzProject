from flask import Flask

from app.dashboard import dashboard_blueprint
from app.home import home_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(dashboard_blueprint, url_prefix= "/dashboard")

