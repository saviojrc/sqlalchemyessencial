from dao.generic_dao import GenericDAO
from models.tipo_embalagem import TipoEmbalagem
from services.db_service import DBService


### Classe que gerencia as operações de CRUD para a entidade TipoEmbalagem


class TipoEmbalagemDAO(GenericDAO):

    def __init__(self, db_service: DBService):
        super().__init__(db_service=db_service)

    def consultar_por_id(self, identificador: int) -> TipoEmbalagem:
        try:
            tipo_embalagem: TipoEmbalagem = self.select_by_id(identificador, TipoEmbalagem)
            return tipo_embalagem
        except Exception as e:
            print(f'Erro ao consultar TipoEmbalagem por ID {identificador}: {e}')
            raise e
        finally:
            self.close_session()

    def inserir_tipo_embalagem(self, tipo_embalagem: TipoEmbalagem):
        try:
            self.insert(tipo_embalagem)
        except Exception as e:
            print(f'Erro ao inserir TipoEmbalagem {tipo_embalagem.nome}: {e}')
            raise e
        finally:
            self.close_session()

    def atualizar_tipo_embalagem(self, tipo_embalagem: TipoEmbalagem):
        try:
            self.update(tipo_embalagem)
        except Exception as e:
            print(f'Erro ao atualizar TipoEmbalagem {tipo_embalagem.nome}: {e}')
            raise e
        finally:
            self.close_session()

    def apagar_tipo_embalagem(self, tipo_embalagem: TipoEmbalagem):
        try:
            self.delete(tipo_embalagem)
        except Exception as e:
            print(f'Erro ao apagar TipoEmbalagem {tipo_embalagem.nome}: {e}')
            raise e
        finally:
            self.close_session()