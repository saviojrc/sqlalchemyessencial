from util.logger import Logger
from dao.sabor_dao import SaborDAO
from services.db_service import DBService
db_service = DBService()
sabor_dao = SaborDAO(db_service=db_service)


def select_filtro_sabor(id: int):
    try:
        sabor_dao.consultar_por_id(id_sabor=id)
    except Exception as e:
        Logger.error({
            'message': f'Erro ao consultar sabor com ID {id}',
            'error': str(e)
        })
        raise e

if __name__ == "__main__":
    id = int(input("Digite o ID do sabor que deseja consultar: "))
    select_filtro_sabor(id)