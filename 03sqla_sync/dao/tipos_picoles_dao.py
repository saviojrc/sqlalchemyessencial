from dao.generic_dao import GenericDAO
from models.tipos_picoles import TipoPicole
from services.db_service import DBService


### Classe que gerencia as operações de CRUD para a entidade TipoPicole

class TipoPicoleDAO(GenericDAO):
    def __init__(self, db_service: DBService):
        super().__init__(db_service=db_service)

    def consultar_por_id(self, identificador: int) -> TipoPicole:
        try:
            tipo_picole: TipoPicole = self.select_by_id(identificador, TipoPicole)
            return tipo_picole
        except Exception as e:
            print(f'Erro ao consultar TipoPicole por ID {identificador}: {e}')
            raise e
        finally:
            self.close_session()

    def inserir_tipo_picole(self, tipo_picole: TipoPicole):
        try:
            self.insert(tipo_picole)
        except Exception as e:
            print(f'Erro ao inserir TipoPicole {tipo_picole.nome}: {e}')
            raise e
        finally:
            self.close_session()

    def atualizar_tipo_picole(self, tipo_picole: TipoPicole):
        try:
            self.update(tipo_picole)
        except Exception as e:
            print(f'Erro ao atualizar TipoPicole {tipo_picole.nome}: {e}')
            raise e
        finally:
            self.close_session()

    def apagar_tipo_picole(self, tipo_picole: TipoPicole):
        try:
            self.delete(tipo_picole)
        except Exception as e:
            print(f'Erro ao apagar TipoPicole {tipo_picole.nome}: {e}')
            raise e
        finally:
            self.close_session()