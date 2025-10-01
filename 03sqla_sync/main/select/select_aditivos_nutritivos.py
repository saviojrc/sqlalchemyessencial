from util.logger import Logger
from dao.aditivo_nutritivo_dao import AditivoNutritivoDAO
from services.db_service import DBService

db_service = DBService()
aditivo_nutritivo_dao = AditivoNutritivoDAO(db_service=db_service)


def selecionar_aditivos_nutritivos():

    try:
        aditivo_nutritivo_dao.consultar_todos()

    except Exception as e:
        Logger.error(f'Erro ao selecionar aditivos nutritivos: {e}')


if __name__ == "__main__":
    selecionar_aditivos_nutritivos()