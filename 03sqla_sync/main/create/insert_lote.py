from dao.lote_dao import LoteDAO
from services.db_service import DBService
from util.logger import Logger
db_service = DBService()
lote_dao = LoteDAO(db_service)


def insert_lote():

    ## Recebe os valores com input do usuário
    quantidade: int = int(input("Digite a quantidade do lote: "))
    identificador_tipo_picole: int = int(input("Digite o ID do tipo de picolé associado ao lote: "))



    try:
        lote = lote_dao.inserir_lote(
            quantidade=quantidade,
            identificador_tipo_picole=identificador_tipo_picole
        )
        Logger.info('Lote inserido com sucesso!')
        Logger.info({
            'id': lote.id,
            'data_criacao': lote.data_criacao,
            'quantidade': lote.quantidade,
            'id_tipo_picole': lote.id_tipo_picole,
            "tipo_picole": {
                'id': lote.tipo_picole.id,
                'nome': lote.tipo_picole.nome
            }
        })
        return lote

    except Exception as e:
        Logger.error({
            'message': 'Erro ao inserir lote',
            'error': str(e)
        })
        raise e


if __name__ == "__main__":
    insert_lote()