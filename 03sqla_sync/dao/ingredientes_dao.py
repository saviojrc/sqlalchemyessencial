## Classe que representa o DAO (Data Access Object) para a tabela ingredientes

from dao.generic_dao import GenericDAO
from models.ingredientes import Ingrediente
from services.db_service import DBService


class IngredientesDAO(GenericDAO):
    """
    Classe que representa o DAO (Data Access Object) para a tabela ingredientes.
    Herda de GenericDAO para fornecer operações básicas de acesso a dados.
    """

    def __init__(self, db_service: DBService):
        super().__init__(db_service=db_service)

    def consultar_por_id(self, identificador: int):
        """
        Consulta um ingrediente pelo seu ID.

        :param identificador: ID do ingrediente a ser consultado.
        :return: Ingrediente correspondente ao ID fornecido.
        """
        try:
            ingrediente = self.select_by_id(identificador, Ingrediente)
            return ingrediente
        except Exception as e:
            print(f'Erro ao consultar Ingrediente por ID {identificador}: {e}')
            raise e
        finally:
            self.close_session()

    def inserir_ingrediente(self, ingrediente: Ingrediente):
        """
        Insere um novo ingrediente no banco de dados.

        :param ingrediente: Objeto Ingrediente a ser inserido.
        """
        try:
            self.insert(ingrediente)
            return ingrediente
        except Exception as e:
            print(f'Erro ao inserir Ingrediente {ingrediente.nome}: {e}')
            raise e
        finally:
            self.close_session()

    def atualizar_ingrediente(self, ingrediente: Ingrediente):
        """
        Atualiza um ingrediente existente no banco de dados.

        :param ingrediente: Objeto Ingrediente a ser atualizado.
        """
        try:
            self.update(ingrediente)
        except Exception as e:
            print(f'Erro ao atualizar Ingrediente {ingrediente.nome}: {e}')
            raise e
        finally:
            self.close_session()

    def apagar_ingrediente(self, ingrediente: Ingrediente):
        """
        Apaga um ingrediente do banco de dados.

        :param ingrediente: Objeto Ingrediente a ser apagado.
        """
        try:
            self.delete(ingrediente)
        except Exception as e:
            print(f'Erro ao apagar Ingrediente {ingrediente.nome}: {e}')
            raise e
        finally:
            self.close_session()

