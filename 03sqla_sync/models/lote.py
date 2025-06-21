import sqlalchemy as sa
import sqlalchemy.orm as orm

from models.model_base import ModelBase


## Classe lote contendo os dados do lote
## Campo id é a chave primária do tipo Integer
## id_tipo_picole referenciando o tipo de picolé
## quantidade inteiro

class Lote(ModelBase):
    __tablename__ = 'lotes'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    id_tipo_picole = sa.Column(sa.Integer, sa.ForeignKey('tipos_picole.id'), nullable=False)
    tipo_picole = orm.relationship("TipoPicole", lazy='joined')
    quantidade = sa.Column(sa.Integer, nullable=False)


    def __repr__(self):
        return f'<Lote(id={self.id})>'
