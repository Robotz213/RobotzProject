from datetime import datetime
import bcrypt
from app import db
from app.misc.gen_id import generate_id



salt = bcrypt.gensalt()

class BaseUsers(db.Model):
    
    """
    Classe responsável por gerenciar o banco de dados do sistema.
    Essa Model é fixa, só deve ser alterada caso seja alterado algo de 
    configuração no database MySQL
    """
    
    __abstract__ = True
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(length=30), nullable=False, unique=True)
    nome_usuario = db.Column(db.String(length=32), nullable=False, unique=True)
    type_user = db.Column(db.String(length=15), nullable=False)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    license_key = db.Column(db.Integer, nullable=False, default=5000)
    login_time = db.Column(db.DateTime, default=datetime.strptime(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "%d/%m/%Y %H:%M:%S"))
    verification_code = db.Column(db.String(length=45),unique=True)
    login_id = db.Column(db.String, nullable=False, unique=True, default=generate_id())

    @property
    def senhacrip(self):
        return self.senhacrip
    
    @senhacrip.setter
    def senhacrip(self, senha_texto):
        self.password = bcrypt.hashpw(senha_texto.encode(), salt).decode("utf-8")

    def converte_senha(self, senha_texto_claro) -> bool:
        return bcrypt.checkpw(senha_texto_claro.encode("utf-8"), self.password.encode("utf-8"))  
