from services.db_service import DBService
from models.lote import  Lote
from dao.generic_dao import GenericDAO

class LoteDAO(GenericDAO):

    def __init__(self, db_service: DBService):
        super().__init__(db_service)

    def consultar_por_id(self, indentificador: int) -> Lote:
        """
        Consulta um lote pelo ID.
        :param indentificador: ID do lote a ser consultado.
        :return: Instância de Lote ou None se não encontrado.
        """
        try:
            return self.select_by_id(
                id=indentificador,
                type_obj=Lote
            )
        except Exception as e:
            print(f'Erro ao consultar lote por ID {indentificador}: {e}')
            raise e
        finally:
            self.close_session()

    def inserir_lote(self,quantidade: int , identificador_tipo_picole : int ) -> Lote:
        """
        Insere um novo lote no banco de dados.
        :param identificador_tipo_picole:  Identificador do tipo de picolé associado ao lote.
        :param quantidade: Quantidade de itens no lote.
        :return: Instância de Lote inserida.
        """
        try:
            lote = Lote(
                id_tipo_picole = identificador_tipo_picole,
                quantidade = quantidade,
            )
            self.insert(lote)
            return lote
        except Exception as e:
            print(f'Erro ao inserir lote: {e}')
            raise e