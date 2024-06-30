from flask import Flask
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_talisman import Talisman

from app.config import MySQL

app = Flask(__name__)
sqlite = "sqlite:///dev.db"

database_uri = f"mysql://{MySQL()['DBLogin']}:{MySQL()['DBPassword']}@{MySQL()['DBHost']}/{MySQL()['Database']}"
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite
app.config['SQLALCHEMY_BINDS'] = { 'sqlite': sqlite, 'mysql': database_uri }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configurações recomendadas para o Flask-Talisman
csp = {
    'default-src': [
        "'self'",
        'https://trusted-cdn.com'
    ],
    'img-src': [
        "'self'",
        'data:'
    ],
    'style-src': [
        "'self'",
        'https://cdn.jsdelivr.net',
        'https://use.fontawesome.com',
        'https://cdnjs.cloudflare.com',
        "'unsafe-inline'"
    ],
    'script-src': [
        "'self'",
        'https://cdn.jsdelivr.net',
        'https://use.fontawesome.com',
        'https://cdnjs.cloudflare.com',
        "'unsafe-inline'"
    ]
}

# Configurando Permissions-Policy sem 'browsing-topics'
# Configurando Permissions-Policy sem recursos não reconhecidos e com valores válidos
# Configurando Permissions-Policy corretamente
permissions_policy = {
    'accelerometer': '()',
    'autoplay': 'self',
    'camera': '()',
    'clipboard-read': 'self',
    'clipboard-write': 'self',
    'display-capture': '()',
    'encrypted-media': 'self',
    'fullscreen': 'self',
    'geolocation': 'self',
    'gyroscope': '()',
    'magnetometer': '()',
    'microphone': '()',
    'midi': '()',
    'payment': '()',
    'picture-in-picture': 'self',
    'publickey-credentials-get': 'self',
    'sync-xhr': 'self',
    'usb': '()',
    'xr-spatial-tracking': '()',
}


talisman = Talisman(app,
                    content_security_policy=csp,
                    force_https=True,
                    session_cookie_secure=True,
                    session_cookie_http_only=True,
                    frame_options='DENY',
                    strict_transport_security=True,
                    strict_transport_security_max_age=31536000,
                    strict_transport_security_include_subdomains=True,
                    referrer_policy='no-referrer',
                    permissions_policy=permissions_policy)

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


