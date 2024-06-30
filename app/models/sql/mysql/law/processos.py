from app.models.bases.law.processos import BaseProcessos


class Processos(BaseProcessos):
    __bind_key__ = 'mysql'