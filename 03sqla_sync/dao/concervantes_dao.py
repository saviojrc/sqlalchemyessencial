from dao.generic_dao import GenericDAO
from models.conservantes import Conservante
from services.db_service import DBService


class ConcervanteDAO(GenericDAO):
    """
    Classe para gerenciar operações de CRUD para o modelo Concervante.
    Herda de GenericDAO para reutilizar métodos comuns de acesso ao banco de dados.
    Esta classe fornece métodos específicos para consultar, inserir, atualizar e apagar concervantes.
    Uso:
    concervante_dao = ConcervanteDAO()
    concervante_dao.inserir_concervante(nome='Nome do Concervante', descricao='Descrição do Concervante')
    concervante_dao.consultar_por_id(identificador=1)
    concervante_dao.atualizar_concervante(concervante_obj)
    """

    def __init__(self, db_service: DBService):
        super().__init__(db_service=db_service)

    def consultar_por_id(self, identificador: int):
        try:
            concervante = self.select_by_id(
                type_obj=Conservante,
                id=identificador
            )
            return concervante
        except Exception as e:
            print(f'Erro ao consultar Concervante por ID {identificador}: {e}')
            raise e
        finally:
            self.close_session()

    def inserir_concervante(self, nome: str , descricao: str):
        """
        Insere um novo concervante no banco de dados.
        :param nome:
        :param descricao:
        :return: None
        """
        try:
            concervante = Conservante(nome=nome, descricao=descricao)
            self.insert(concervante)
            return concervante
        except Exception as e:
            print(f'Erro ao inserir Concervante {nome}: {e}')
            raise e
        finally:
            self.close_session()

    def atualizar_concervante(self, concervante: Conservante):
        """
        Atualiza um concervante existente no banco de dados.
        :param concervante: Objeto Concervante a ser atualizado.
        :return: None
        """
        try:
            self.update(concervante)
        except Exception as e:
            print(f'Erro ao atualizar Concervante {concervante.nome}: {e}')
            raise e
        finally:
            self.close_session()

    def apagar_concervante(self, concervante: Conservante):
        """
        Apaga um concervante do banco de dados.
        :param concervante: Objeto Concervante a ser apagado.
        :return: None
        """
        try:
            self.delete(concervante)
        except Exception as e:
            print(f'Erro ao apagar Concervante {concervante.nome}: {e}')
            raise e
        finally:
            self.close_session()
