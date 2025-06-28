from dao.sabor_dao import SaborDAO
from models.sabor import Sabor


## Insert a new Sabor record

def insert_sabor():
    sabor_dao = SaborDAO()
    ## Recebe os valores com input do usuário
    nome: str = input("Digite o nome do sabor: ")

    sabor = Sabor(
        nome=nome
    )

    try:
        sabor_dao.inserir_sabor(sabor)
        print('Sabor inserido com sucesso!')
        ## Exibe os atributos do sabor inserido
        print(f'ID: {sabor.id}')
        print(f'Data de criação: {sabor.data_criacao}')
        print(f'nome: {sabor.nome}')

    except Exception as e:
        print(f'Erro ao inserir Sabor: {e}')


if __name__ == "__main__":
    insert_sabor()
