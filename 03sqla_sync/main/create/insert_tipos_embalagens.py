from models.tipos_embalagens import TiposEmbalagens
from dao.tipos_embalagens_dao import TipoEmbalagemDAO
from services.db_service import DBService

db_service = DBService()

tipo_embalagem_dao = TipoEmbalagemDAO(db_service=db_service)
def inserir_tipos_embalagens():

    ## Imput do nome da embalagem
    nome = input("Digite o nome da embalagem: ")

    ## Cria o objeto TipoEmbalagem
    tipo_embalagem = TiposEmbalagens(nome=nome)

    ## Insere o tipo de embalagem no banco de dados
    try:
        tipo_embalagem_dao.inserir_tipo_embalagem(tipo_embalagem)
        print({
            'id': tipo_embalagem.id,
            'nome': tipo_embalagem.nome,
            'data_criacao': tipo_embalagem.data_criacao
        })
    except Exception as e:
        print(f'Erro ao inserir tipo de embalagem: {e}')

if __name__ == "__main__":
    inserir_tipos_embalagens()





