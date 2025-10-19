import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase


## Classe AdictivoNutritivo

class AditivosNutritivos(ModelBase):
    __tablename__ = "aditivos_nutritivos"


    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    data_criacao = sa.Column(sa.DateTime, default=datetime.now, index = True, nullable=False)
    nome = sa.Column(sa.String(45),unique = True,  nullable=False)
    formula_quimica = sa.Column(sa.String(45),unique = True, nullable=False)