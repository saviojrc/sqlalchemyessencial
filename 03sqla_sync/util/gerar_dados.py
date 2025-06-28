import random

from faker import Faker

faker = Faker('pt_BR')

class GeradorDados:
    ## Gera nomes em português do brasil

    @staticmethod
    def gerar_nome():
        return faker.name()

    @staticmethod
    def gera_cnpj_sem_pontuacao():
        return faker.cnpj().replace('.', '').replace('-', '').replace('/', '')

    @staticmethod
    def gerar_razao_social():
        return faker.company()

    @staticmethod
    def gerar_contato():
        return faker.phone_number()

    @staticmethod
    def gera_sabores_de_picole():
        sabores = [
            'Calabresa', 'Mussarela', 'Portuguesa', 'Frango com Catupiry',
            'Quatro Queijos', 'Margherita', 'Pepperoni', 'Vegetariana',
            'Atum', 'Bacon', 'Coração', 'Palmito'
        ]
        return random.choice(sabores)


    @staticmethod
    def gerar_vitaminas():
        vitaminas = [
            {
                "nome": "Vitamina A",
                "formula_quimica": "C20H30O"
            },
            {
                "nome": "Vitamina B1",
                "formula_quimica": "C12H17N4OS"
            },
            {
                "nome": "Vitamina B2",
                "formula_quimica": "C17H20N4O6"
            },
            {
                "nome": "Vitamina C",
                "formula_quimica": "C6H8O6"
            },
            {
                "nome": "Vitamina D",
                "formula_quimica": "C27H44"
            },
            {
                "nome": "Vitamina E",
                "formula_quimica": "C29H50O2"
            },
            {
                "nome": "Vitamina K",
                "formula_quimica": "C31H46O2"
            },
            {
                "nome": "Vitamina B3",
                "formula_quimica": "C6H5NO2"
            },
            {
                "nome": "Vitamina B5",
                "formula_quimica": "C9H17NO5"
            },
            {
                "nome": "Vitamina B6",
                "formula_quimica": "C8H11NO3"
            },
            {
                "nome": "Vitamina B7",
                "formula_quimica": "C10H16N2O3S"
            },
            {
                "nome": "Vitamina B9",
                "formula_quimica": "C19H19N7O6"
            },
            {
                "nome": "Vitamina B12",
                "formula_quimica": "C63H88CoN14O14P"
            }
        ]
        return random.choice(vitaminas)

    @staticmethod
    def gerar_tipo_embalagem_faker():
        adjetivo = faker.word().capitalize()
        embalagem = random.choice([
            "caixa", "saco", "envelope", "frasco", "lata", "pote",
            "garrafa", "pacote", "tubo", "barril", "caixote", "balde",
            "saco plástico", "saco de papel", "caixa de papelão", "caixa de madeira",
            "caixa de plástico", "caixa de metal", "caixa de vidro", "caixa de isopor",
            "caixa de alumínio", "caixa de papel kraft", "caixa de papelão ondulado",
            "caixa de papelão reciclado", "caixa de papelão ondulado reciclado", "caixa de papelão liso",
            "caixa de papelão micro ondulado", "caixa de papelão triplex", "caixa de papelão duplex",
            "caixa de papelão kraft", "caixa de papelão cinza", "caixa de papelão branco",
            "caixa de papelão marrom", "caixa de papelão colorido", "caixa de papelão estampado",
            "caixa de papelão liso colorido", "caixa de papelão liso estampado", "caixa de papelão ondulado colorido",
            "caixa de papelão ondulado estampado", "caixa de papelão micro ondulado colorido", "caixa de papelão micro ondulado estampado"
        ])
        return f"{embalagem} {adjetivo}"

