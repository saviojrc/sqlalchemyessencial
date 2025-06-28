import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase

class Revendedor(ModelBase):
    __tablename__ = 'revendedores'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao = sa.Column(sa.DateTime, default=datetime.now, index = True, nullable=False)
    cnpj = sa.Column(sa.String(14), nullable=False, unique=True)
    razao_social = sa.Column(sa.String(100), nullable=False)
    contato = sa.Column(sa.String(100), nullable=False)


    def __repr__(self):
        return f"<Revendedor(nome={self.razao_social}')>"
