from datetime import datetime

import sqlalchemy as sa

from models.model_base import ModelBase


class TipoPicole(ModelBase):
    __tablename__ = "tipos_picole"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao = sa.Column(sa.DateTime,
                             default=datetime.now,
                             index=True,
                             nullable=False)
    nome = sa.Column(sa.String(45), unique=True, nullable=False)


    def __repr__(self):
        return f"<TipoPicole(id={self.id})>"