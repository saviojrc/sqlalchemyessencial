from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from models.model_base import ModelBase

## Picole pode ter varios ingredientes
ingredientes_picole = sa.Table(
    "ingredientes_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id"), primary_key=True),
    sa.Column("id_ingrediente", sa.Integer, sa.ForeignKey("ingredientes.id"), primary_key=True)
)

## Picole pode ter varios concervantes e picoles pode ter varios aditivos nutritivos

conservantes_picole = sa.Table(
    "conservantes_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id"), primary_key=True),
    sa.Column("id_conservante", sa.Integer, sa.ForeignKey("conservantes.id"), primary_key=True)
)

## Picole pode ter varios aditivos nutritivo

aditivos_nutritivos_picole = sa.Table(
    "aditivos_nutritivos_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id"), primary_key=True),
    sa.Column("id_aditivo_nutritivo", sa.Integer,
              sa.ForeignKey("aditivos_nutritivos.id"), primary_key=True)
)


class Picole(ModelBase):

    __tablename__ = "picoles"

    id  = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao= sa.Column(sa.DateTime, default=datetime.now, index = True)
    preco = sa.Column(sa.DECIMAL(8,2), nullable=False)

    id_sabor = sa.Column(sa.Integer, sa.ForeignKey("sabores.id"), nullable=False)
    sabor = orm.relationship("Sabor", lazy='joined')


    id_tipo_embalagem : int = sa.Column(sa.Integer, sa.ForeignKey("tipos_embalagem.id"), nullable=False)
    tipo_embalagem = orm.relationship("TipoEmbalagem", lazy='joined')

    id_tipo_picole : int = sa.Column(sa.Integer, sa.ForeignKey("tipos_picole.id"), nullable=False)
    tipo_picole = orm.relationship("TipoPicole", lazy='joined')

    ## Um picole pode ter varios ingredientes
    ingredientes = orm.relationship(
        "Ingrediente",
        secondary=ingredientes_picole,
        backref='ingrediente',
        lazy='joined'
    )

    ## Um picole pode ter varios conservantes ou nenhum
    conservantes = orm.relationship(
        "Conservante",
        secondary=conservantes_picole,
        backref='conservante',
        lazy='joined'
    )

    ## Um picole pode ter varios aditivos nutritivos ou nenhum
    aditivos_nutritivos = orm.relationship(
        "AditivoNutritivo",
        secondary=aditivos_nutritivos_picole,
        backref='aditivo_nutritivo',
        lazy='joined'
    )

    def __repr__(self):
        tipo = getattr(self.tipo_picole, 'nome', '')
        sabor = getattr(self.sabor, 'nome', '')
        return f"<Picole : {tipo} com sabor {sabor} e preço {self.preco}>"

