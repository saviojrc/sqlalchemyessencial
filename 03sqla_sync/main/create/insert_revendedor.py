from dao.revendedor_dao import RevendedorDAO
from services.db_service import DBService

def inserir_revendedor():
    db_service = DBService()
    revendedor_dao = RevendedorDAO(db_service)

    cnpj = input("Digite o CNPJ do revendedor: ")
    razao_social = input("Digite a razão social do revendedor: ")
    contato = input("Digite o contato do revendedor: ")

    # Insere o revendedor no banco de dados
    try:
        revendedor = revendedor_dao.inserir_revendedor(
            cnpj=cnpj,
            razao_social=razao_social,
            contato=contato
        )
        print(f'Revendedor inserido com sucesso: {revendedor}')
    except Exception as e:
        print(f'Erro ao inserir revendedor: {e}')

if __name__== "__main__":
    inserir_revendedor()