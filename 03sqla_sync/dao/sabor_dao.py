from dao.generic_dao import GenericDAO
from models.sabores import Sabor
from services.db_service import DBService


### Classe que gerencia as operações de CRUD para a entidade Sabor

class SaborDAO(GenericDAO):

    def __init__(self, db_service: DBService):
        super().__init__(db_service=db_service)

    def consultar_por_id(self, id_sabor: int):
        try:
            sabor: Sabor
            with self.session as session:
                sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

            return sabor


        except Exception as e:
            print(f'Erro ao consultar Sabor por ID {id_sabor}: {e}')
            raise e
        finally:
            self.close_session()

    def inserir_sabor(self, sabor: Sabor):
        try:
            self.insert(sabor)
            return sabor
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