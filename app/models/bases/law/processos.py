from datetime import datetime
from app import db

class BaseProcessos(db.Model):
    
    """
    Classe responsável por gerenciar o banco de dados do sistema.
    Essa Model é fixa, só deve ser alterada caso seja alterado algo de 
    configuração no database MySQL
    """
    
    __abstract__ = True
    __tablename__ = 'processos'
    id = db.Column(db.Integer, primary_key=True)
    processo = db.Column(db.String(length=26), nullable=False, unique=True)
    autor = db.Column(db.String(length=64), nullable=False)
    reu = db.Column(db.String(length=64), nullable=False)
    status = db.Column(db.String(length=64), nullable=False)
    distribuicao_data = db.Column(db.DateTime, default=datetime.strptime(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "%d/%m/%Y %H:%M:%S"))
    valor_causa = db.Column(db.Numeric(precision=10, scale=2))
