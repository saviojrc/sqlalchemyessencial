from services.db_service import DBService
from models.revendedor import Revendedor
from dao.generic_dao import GenericDAO

class RevendedorDAO(GenericDAO):
    def __init__(self, db_service: DBService):
        super().__init__(db_service)

    def consultar_por_id(self , indentificador: int) -> Revendedor:
        """
        Consulta um revendedor pelo ID.
        :param indentificador: ID do revendedor a ser consultado.
        :return: Instância de Revendedor ou None se não encontrado.
        """
        try:
            return self.select_by_id(
                id=indentificador,
                type_obj=Revendedor
            )
        except Exception as e:
            print(f'Erro ao consultar revendedor por ID {indentificador}: {e}')
            raise e
        finally:
            self.close_session()

    def inserir_revendedor(self, cnpj: str, razao_social: str, contato: str) -> Revendedor:

        """
        Insere um novo revendedor no banco de dados.
        :param nome:
        :param cnpj:
        :param razao_social:
        :param contato:
        :return:
            Instância de Revendedor inserida.
        """

        try:
            revendedor = Revendedor(
                cnpj=cnpj,
                razao_social=razao_social,
                contato=contato
            )
            self.insert(revendedor)
            return revendedor
        except Exception as e:
            print(f'Erro ao inserir revendedor: {e}')
            raise e

    def atualizar_revendedor(self, revendedor: Revendedor):
        try:
            self.update(revendedor)
        except Exception as e:
            print(f'Erro ao atualizar revendedor {revendedor.nome}: {e}')
            raise e
        finally:
            self.close_session()

    def apagar_revendedor(self, revendedor: Revendedor):
        try:
            self.delete(revendedor)
        except Exception as e:
            print(f'Erro ao apagar revendedor {revendedor.nome}: {e}')
            raise e
        finally:
            self.close_session()
