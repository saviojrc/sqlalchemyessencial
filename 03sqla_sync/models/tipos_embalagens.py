import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase


## Classe AdictivoNutritivo

class TiposEmbalagens(ModelBase):
    __tablename__ = "tipos_embalagens"


    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao = sa.Column(sa.DateTime, default=datetime.now, index = True, nullable=False)
    nome = sa.Column(sa.String(45),unique = True,  nullable=False)