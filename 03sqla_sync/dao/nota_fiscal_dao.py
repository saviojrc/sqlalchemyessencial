from services.db_service import DBService
from models.notas_fiscais import NotaFiscal
from dao.generic_dao import GenericDAO


class NotaFiscalDAO(GenericDAO):

    def __init__(self, db_service: DBService):
        super().__init__(db_service)
        self.db_service = db_service

    def consultar_por_id(self,identificador) -> NotaFiscal:

        try:

            return self.select_by_id(
                id=identificador,
                type_obj=NotaFiscal

            )
        except Exception as e:
            print("Erro ao consultar nota fiscal por ID:", str(e))
            raise e
        finally:
            self.close_session()

    def inserir_nota_fiscal(self, id_revendedor : int ,descricao : str ,numero_serie : str ,valor : float , lotes : list ) -> NotaFiscal:
        """
        Insere uma nova nota fiscal no banco de dados.
        :param lotes:
        :param id_revendedor:
        :param descricao:
        :param numero_serie:
        :param valor:
        :return:
        Instância de NotaFiscal inserida.
        """
        try:
            nota_fiscal = NotaFiscal(
                valor=valor,
                numero_serie=numero_serie,
                descricao=descricao,
                id_revendedor=id_revendedor,
                lotes= lotes
            )

            self.insert(nota_fiscal)
            return nota_fiscal
        except Exception as e:
            print(f'Erro ao inserir nota fiscal: {e}')
            raise e
        finally:
            self.close_session()



