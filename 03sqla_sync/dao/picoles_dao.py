from services.db_service import DBService
from models.picole import Picole
from dao.generic_dao import GenericDAO
from typing import Optional

class PicoleDAO(GenericDAO):

    def __init__(self, db_service: DBService):
        super().__init__(db_service)
        self.db_service = db_service

    def consultar_por_id(self,identificador) -> Picole:

        try:

            return self.select_by_id(
                id=identificador,
                type_obj=Picole

            )
        except Exception as e:
            print("Erro ao consultar picole por ID:", str(e))
            raise e
        finally:
            self.close_session()

    def inserir_picole(self, preco : float , id_sabor : int , id_tipo_embalagem : int , id_tipo_picole : int , ingredientes : list , conservantes : Optional[list] , aditivos_nutritivos : Optional[list] ) -> Picole:
        """
        Insere um novo picole no banco de dados.
        :param preco:
        :param id_sabor:
        :param id_tipo_embalagem:
        :param id_tipo_picole:
        :param ingredientes:
        :param conservantes:
        :param aditivos_nutritivos:
        :return:
        Instância de Picole inserida.
        """
        try:
            picole = Picole(
                preco=preco,
                id_sabor=id_sabor,
                id_tipo_embalagem=id_tipo_embalagem,
                id_tipo_picole=id_tipo_picole,
                ingredientes=ingredientes,
                conservantes=conservantes,
                aditivos_nutritivos=aditivos_nutritivos
            )

            self.insert(picole)
            return picole
        except Exception as e:
            print(f'Erro ao inserir picole: {e}')
            raise e
        finally:
            self.close_session()