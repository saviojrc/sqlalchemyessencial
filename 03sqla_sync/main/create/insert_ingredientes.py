from time import process_time_ns

from models.ingredientes import Ingrediente
from dao.ingredientes_dao import IngredientesDAO
from services.db_service import DBService

db_service = DBService()
## Insert a new Ingrediente record
def insert_ingrediente():
    ingredientes_dao = IngredientesDAO(db_service)
    ## Recebe os valores com input do usuário
    nome: str = input("Digite o nome do ingrediente: ")

    ingrediente = Ingrediente(
        nome=nome
    )

    try:
        ingredientes_dao.inserir_ingrediente(ingrediente)
        print('Ingrediente inserido com sucesso!')
        print({
            'id': str(ingrediente.id),
            'data_de_criacao': str(ingrediente.data_criacao),
            'nome': str(ingrediente.nome)
        })

    except Exception as e:
        print(f'Erro ao inserir Ingrediente: {e}')

if __name__ == "__main__":
    start_time = process_time_ns()
    insert_ingrediente()
    end_time = process_time_ns()
    print(f"Tempo de execução: {(end_time - start_time) / 1_000_000} ms")