from services.db_service import DBService
from models.aditivo_nutritivo import AditivoNutritivo
from dao.generic_dao import GenericDAO
from util.logger import Logger
from util.helpers import formata_data
class AditivoNutritivoDAO(GenericDAO):

    def __init__(self , db_service: DBService):
        super().__init__(db_service=db_service)


    """
        Retorna todos os aditivos nutritivos cadastrados no banco de dados.
        :return: Lista de objetos AditivoNutritivo
        :rtype:None
    """
    def consultar_todos(self) -> None:
        try:
            with self.session as session:
                aditivos_nutritivos =session.query(AditivoNutritivo).all()

            Logger.info({
                'aditivos_nutritivos': [
                    {
                        'id': aditivo_nutritivo.id,
                        'nome': aditivo_nutritivo.nome,
                        'data_criacao': formata_data(aditivo_nutritivo.data_criacao)
                    } for aditivo_nutritivo in aditivos_nutritivos
                ]
            })

        except Exception as e:
            print(f'Erro ao consultar todos os Aditivos Nutritivos: {e}')
            raise e

    def consultar_por_id(self, identificador: int) -> AditivoNutritivo:
        try:
            aditivo_nutritivo : AditivoNutritivo = self.select_by_id(identificador, AditivoNutritivo)
            return aditivo_nutritivo
        except Exception as e:
            print(f'Erro ao consultar Aditivo Nutritivo por ID {identificador}: {e}')
            raise e

    def inserir_aditivo_nutritivo(self,aditivo_nutritivo: AditivoNutritivo):
        try:
            self.insert(aditivo_nutritivo)
        except Exception as e:
            print(f'Erro ao inserir Aditivo Nutritivo {aditivo_nutritivo.nome}: {e}')
            raise e

    def atualizar_aditivo_nutritivo(self, aditivo_nutritivo: AditivoNutritivo):
        try:
            self.update(aditivo_nutritivo)
        except Exception as e:
            print(f'Erro ao atualizar Aditivo Nutritivo {aditivo_nutritivo.nome}: {e}')
            raise e

    def apagar_aditivo_nutritivo(self, aditivo_nutritivo: AditivoNutritivo):
        try:
            self.delete(aditivo_nutritivo)
        except Exception as e:
            print(f'Erro ao apagar Aditivo Nutritivo {aditivo_nutritivo.nome}: {e}')
            raise e