from util.logger import Logger
from dao.sabor_dao import SaborDAO
from services.db_service import DBService
from util.helpers import formata_data
db_service = DBService()
sabor_dao = SaborDAO(db_service=db_service)

def select_filtro_sabor(id : int):
    try:
        if not id:
            raise ValueError("ID do sabor não fornecido.")

        sabor = sabor_dao.consultar_por_id(id)

        if not sabor:
            Logger.info(f'Sabor com ID {id} não encontrado.')

        Logger.info({
            "id": sabor.id,
            "nome": sabor.nome,
            "data_criacao": formata_data(sabor.data_criacao)
        })
    except Exception as e:
        Logger.error(f'Erro ao selecionar sabor: {e}')


if __name__ == "__main__":
    id = int(input("Digite o ID do sabor que deseja consultar: "))
    select_filtro_sabor(id)