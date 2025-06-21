import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase


## Classe AdictivoNutritivo

class Sabor(ModelBase):
    __tablename__ = "sabores"


    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao = sa.Column(sa.DateTime, default=datetime.now, index = True, nullable=False)
    nome = sa.Column(sa.String(45),unique = True,  nullable=False)

    def __repr__(self):
        return  f'<Sabor(nome={self.nome})>'