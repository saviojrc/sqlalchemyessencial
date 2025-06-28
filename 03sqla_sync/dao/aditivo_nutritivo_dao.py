from services.db_service import DBService
from models.aditivo_nutritivo import AditivoNutritivo
from dao.generic_dao import GenericDAO

class AditivoNutritivoDAO(GenericDAO):

    def __init__(self , db_service: DBService):
        super().__init__(db_service=db_service)

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