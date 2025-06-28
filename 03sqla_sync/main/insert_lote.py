from models.lote import Lote
from dao.lote_dao import LoteDAO
from services.db_service import DBService

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
        print('Lote inserido com sucesso!')
        print({
            'id': lote.id,
            'data_criacao': lote.data_criacao,
            'quantidade': lote.quantidade,
            'id_tipo_picole': lote.id_tipo_picole,
            "tipo_picole": {
                'id': lote.tipo_picole.id,
                'nome': lote.tipo_picole.nome
            }
        })

    except Exception as e:
        print(f'Erro ao inserir Lote: {e}')


if __name__ == "__main__":
    insert_lote()