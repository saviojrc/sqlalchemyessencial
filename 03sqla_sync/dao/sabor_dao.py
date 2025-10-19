from models.sabor import Sabor
from dao.generic_dao import GenericDAO
from services.db_service import DBService
from util.logger import Logger
from util.helpers import formata_data

### Classe que gerencia as operações de CRUD para a entidade Sabor

class SaborDAO(GenericDAO):

    def __init__(self, db_service: DBService):
        super().__init__(db_service=db_service)

    def consultar_por_id(self, id_sabor: int) -> None:
        try:
            with self.session as session:
                sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()

                if not sabor:
                    Logger.warning(f'Sabor com ID {id_sabor} não encontrado.')

                Logger.info({
                    'id': sabor.id,
                    'nome': sabor.nome,
                    'data_criacao': formata_data(sabor.data_criacao)
                })
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