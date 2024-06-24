from flask import Flask
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail



app = Flask(__name__)
sqlite = "sqlite:///dev.db"

app.config['SQLALCHEMY_DATABASE_URI'] = sqlite
app.config['SQLALCHEMY_BINDS'] = { 'sqlite': sqlite}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy()
login_manager = LoginManager()
db.init_app(app)
mail = Mail(app)
csrf = CSRFProtect(app) 
login_manager.init_app(app)
app.secret_key = "5141951"

from app.dashboard import dashboard_blueprint
from app.home import home_blueprint
from app.auth import auth_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(dashboard_blueprint, url_prefix = "/dashboard")
app.register_blueprint(auth_blueprint, url_prefix = "")


