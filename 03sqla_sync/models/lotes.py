from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from models.model_base import ModelBase
from models.tipos_picoles import TiposPicoles


## Classe lote contendo os dados do lote
## Campo id é a chave primária do tipo Integer
## id_tipo_picole referenciando o tipo de picolé
## quantidade inteiro


class Lotes(ModelBase):
    __tablename__ = 'lotes'

    id : int = sa.Column(sa.Integer, primary_key=True)
    data_criacao = sa.Column(sa.DateTime, default=datetime.now, index=True, nullable=False)
    id_tipo_picole = sa.Column(sa.Integer,
                               sa.ForeignKey(TiposPicoles.id),
                               nullable=False)
    tipo_picole = orm.relationship(TiposPicoles,lazy="joined")
    quantidade : int = sa.Column(sa.Integer, nullable=False)


    def __repr__(self):
        return f'<Lote(id={self.id})>'
