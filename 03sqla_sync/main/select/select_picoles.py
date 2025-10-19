from dao.picoles_dao import PicoleDAO
from util.logger import Logger

from services.db_service import DBService
db_service = DBService()
picole_dao = PicoleDAO(db_service=db_service)

from models.picoles import Picole
from models.sabores import Sabor


def consultar_todos_os_picoles():
    try:
        picoles = picole_dao.motrar_todos_picoles()

        if len(picoles) >0:
            Logger.info({
                "mensagem": "Picoles encontrados",
                "quantidade": len(picoles),
                "picoles": [
                    {
                        'id': picole.id,
                        'preco': picole.preco,
                        'sabor_id': picole.sabor_id,
                        'tipo_embalagem_id': picole.tipo_embalagem_id,
                        'tipo_picole_id': picole.tipo_picole_id
                    } for picole in picoles
                ]
            })
        else:
            Logger.info({
                "mensagem": "Nenhum picole encontrado"
            })
    except Exception as e:
        Logger.error({
            'message': 'Erro ao consultar todos os picoles',
            'error': str(e)
        })
        raise e

if __name__  == "__main__":
    consultar_todos_os_picoles()
