from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo

## Insert a new AditivoNutritivo record
def insert_aditivo_nutritivo():

    ## Recebe os valores com input do usuário
    nome : str = input("Digite o nome do aditivo nutritivo: ")
    formula_quimica: str = input("Digite a fórmula química do aditivo nutritivo: ")

    an : AditivoNutritivo = AditivoNutritivo(
        nome = nome,
        formula_quimica = formula_quimica
    )

    with create_session() as session:
        session.add(an)
        session.commit()

    print(f'Aditivo Nutritivo {an} adicionado com sucesso!')


if __name__  == "__main__":
    insert_aditivo_nutritivo()