from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relationship

from models.model_base import ModelBase

## Classe AdictivoNutritivo

class Sabores(ModelBase):
    __tablename__ = "sabores"


    id = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao = Column(DateTime, default=datetime.now, index = True, nullable=False)
    nome = Column(String(45),unique = True,  nullable=False)

    picoles = relationship("Picole", back_populates="sabor")

    def __repr__(self):
        return f"Sabor(id={self.id}, nome={self.nome})"