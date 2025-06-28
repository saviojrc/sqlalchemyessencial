from models.sabor import Sabor
from dao.generic_dao import GenericDAO
from services.db_service import DBService


### Classe que gerencia as operações de CRUD para a entidade Sabor

class SaborDAO(GenericDAO):

    def __init__(self, db_service: DBService):
        super().__init__(db_service=db_service)

    def consultar_por_id(self, identificador: int) -> Sabor:
        try:
            sabor: Sabor = self.select_by_id(identificador, Sabor)
            return sabor
        except Exception as e:
            print(f'Erro ao consultar Sabor por ID {identificador}: {e}')
            raise e
        finally:
            self.close_session()

    def inserir_sabor(self, sabor: Sabor):
        try:
            self.insert(sabor)
        except Exception as e:
            print(f'Erro ao inserir Sabor {sabor.nome}: {e}')
            raise e
        finally:
            self.close_session()

    def atualizar_sabor(self, sabor: Sabor):
        try:
            self.update(sabor)
        except Exception as e:
            print(f'Erro ao atualizar Sabor {sabor.nome}: {e}')
            raise e
        finally:
            self.close_session()

    def apagar_sabor(self, sabor: Sabor):
        try:
            self.delete(sabor)
        except Exception as e:
            print(f'Erro ao apagar Sabor {sabor.nome}: {e}')
            raise e
        finally:
            self.close_session()