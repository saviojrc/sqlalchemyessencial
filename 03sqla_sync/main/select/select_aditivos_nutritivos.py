from util.logger import Logger
from dao.aditivo_nutritivo_dao import AditivoNutritivoDAO
from services.db_service import DBService

db_service = DBService()
aditivo_nutritivo_dao = AditivoNutritivoDAO(db_service=db_service)


def selecionar_aditivos_nutritivos():

    try:
        aditivo_nutritivos = aditivo_nutritivo_dao.consultar_todos()
        if aditivo_nutritivos:
            Logger.info({
                'message': 'Aditivos nutritivos selecionados com sucesso.',
                'aditivos_nutritivos': [aditivo.__dict__ for aditivo in aditivo_nutritivos]
            })

        Logger.warning({
            'message': 'Nenhum aditivo nutritivo encontrado.'
        })


    except Exception as e:
        Logger.error(f'Erro ao selecionar aditivos nutritivos: {e}')


if __name__ == "__main__":
    selecionar_aditivos_nutritivos()