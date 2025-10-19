from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from models.model_base import ModelBase
from models.revendedores import Revendedores
from models.lotes import Lotes

## Nota fiscal pode ter varios lotes
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.Integer, sa.ForeignKey('notas_fiscais.id'), primary_key=True),
    sa.Column('id_lote', sa.Integer, sa.ForeignKey('lotes.id'), primary_key=True)
)


class NotasFiscais(ModelBase):
    """
    Modelo de Nota Fiscal
    Representa uma nota fiscal emitida por um revendedor, contendo informações como
    data de criação, valor, número de série e descrição. Cada nota fiscal pode estar associada
    a um revendedor e pode conter vários lotes de produtos.
    Atributos:
        id (int): Identificador único da nota fiscal.
        data_criacao (datetime): Data e hora de criação da nota fiscal.
        valor (decimal): Valor total da nota fiscal.
        numero_serie (str): Número de série da nota fiscal, deve ser único.
        descricao (str): Descrição opcional da nota fiscal.
        id_revendedor (int): Identificador do revendedor associado à nota fiscal.
        revendedor (Revendedor): Relação com o modelo Revendedor.
        lotes (list[Lote]): Lista de lotes associados a esta nota fiscal.
    Métodos:
        __repr__(): Retorna uma representação em string da nota fiscal.
    """

    __tablename__ = 'notas_fiscais'

    id = sa.Column(sa.Integer, primary_key=True,autoincrement=True)
    data_criacao = sa.Column(sa.DateTime, default=datetime.now, index = True, nullable=False)
    valor = sa.Column(sa.DECIMAL(8,2), nullable=False)
    numero_serie = sa.Column(sa.String(45), nullable=False, unique=True)
    descricao = sa.Column(sa.String(200), nullable=True)
    id_revendedor = sa.Column(sa.Integer, sa.ForeignKey('revendedores.id'), nullable=False)
    revendedor  = orm.relationship(Revendedores,lazy='joined')
    lotes = orm.relationship(
        Lotes,
        secondary=lotes_nota_fiscal,
        backref='lotes',
        lazy='dynamic'
    )
