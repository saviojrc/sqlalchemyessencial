from models.tipos_picoles import TipoPicole
from dao.tipos_picoles_dao import TipoPicoleDAO
from services.db_service import DBService

db_service = DBService()

tipo_picole_dao = TipoPicoleDAO(db_service=db_service)

def inserir_tipos_picoles():
    ## Imput do nome do picole
    nome = input("Digite o nome do picole: ")

    ## Cria o objeto TipoPicole
    tipo_picole = TipoPicole(nome=nome)




    ## Insere o tipo de picole no banco de dados
    try:
        tipo_picole_dao.inserir_tipo_picole(tipo_picole)
        print({
            'id': tipo_picole.id,
            'nome': tipo_picole.nome,
            'data_criacao': tipo_picole.data_criacao
        })
    except Exception as e:
        print(f'Erro ao inserir tipo de picole: {e}')

if __name__ == "__main__":
    inserir_tipos_picoles()