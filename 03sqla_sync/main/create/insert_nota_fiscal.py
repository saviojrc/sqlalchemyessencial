from dao.nota_fiscal_dao import NotaFiscalDAO
from services.db_service import DBService
from main.create.insert_lote import insert_lote
from util.logger import Logger

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Este campo não pode ser vazio.")

def collect_lotes(qtd_lotes):
    lotes = []
    for i in range(qtd_lotes):
        Logger.info(f'Inserindo lote {i+1} de {qtd_lotes}')
        lotes.append(insert_lote())
    return lotes

def inserir_nota_fiscal():
    db_service = DBService()
    nota_fiscal_dao = NotaFiscalDAO(db_service)

    valor = get_float_input("Digite o valor da nota fiscal: ")
    numero_serie = get_non_empty_input("Digite o número de série da nota fiscal: ")
    descricao = get_non_empty_input("Digite a descrição da nota fiscal: ")
    id_revendedor = get_int_input("Digite o ID do revendedor associado à nota fiscal: ")
    quantidade_lotes = get_int_input("Digite a quantidade de lotes a serem inseridos: ")

    lotes = collect_lotes(quantidade_lotes)

    try:
        nota_fiscal = nota_fiscal_dao.inserir_nota_fiscal(
            valor=valor,
            numero_serie=numero_serie,
            descricao=descricao,
            id_revendedor=id_revendedor,
            lotes=lotes
        )
        Logger.info(f'Nota fiscal inserida com sucesso: {nota_fiscal}')
    except Exception as e:
        Logger.error(f'Erro ao inserir nota fiscal: {e}')

if __name__ == "__main__":
    inserir_nota_fiscal()