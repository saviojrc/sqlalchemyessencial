from dao.concervantes_dao import ConcervanteDAO
from services.db_service import DBService
db_service = DBService()
concervante_dao = ConcervanteDAO(db_service=db_service)

def insert_concervante():

    ## Insere o tipo de embalagem no banco de dados
    try:
        ## Imput do nome da concervante
        nome = input("Digite o nome do concervante: ")
        descricao = input("Digite a descrição do concervante: ")

        concervante_dao.inserir_concervante(
            nome=nome,
            descricao=descricao

        )
        print('Concervante inserido com sucesso!')

        concervante = concervante_dao.consultar_por_id(
            identificador=1
        )
        print({
            "id": concervante.id,
            "nome": concervante.nome,
            "descricao": concervante.descricao,
            "data_criacao": concervante.data_criacao

        })
    except Exception as e:
        print(f'Erro ao inserir tipo de embalagem: {e}')

if __name__ == "__main__":
    insert_concervante()