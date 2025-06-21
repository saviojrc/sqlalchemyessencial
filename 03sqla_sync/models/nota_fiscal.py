from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from models.model_base import ModelBase

## Nota fiscal pode ter varios lotes
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.Integer, sa.ForeignKey('notas_fiscais.id'), primary_key=True),
    sa.Column('id_lote', sa.Integer, sa.ForeignKey('lotes.id'), primary_key=True)
)


class NotaFiscal(ModelBase):
    __tablename__ = 'notas_fiscais'

    id = sa.Column(sa.Integer, primary_key=True,autoincrement=True)
    data_criacao = sa.Column(sa.DateTime, default=datetime.now, index = True, nullable=False)
    valor = sa.Column(sa.DECIMAL(8,2), nullable=False)
    numero_serie = sa.Column(sa.String(45), nullable=False, unique=True)
    descricao = sa.Column(sa.String(200), nullable=True)
    id_revendedor = sa.Column(sa.Integer, sa.ForeignKey('revendedores.id'), nullable=False)
    revendedor  = orm.relationship('Revendedor',lazy='joined')
    ## Uma nota pode ter varios lotes
    ## E um lote esta ligado a uma nota fiscal
    lotes = orm.relationship(
        'Lote',
        secondary=lotes_nota_fiscal,
        backref='lote',
        lazy='dynamic'
    )

    def __repr__(self):
        return f'<NotaFiscal(numero_serie={self.numero_serie})>'
