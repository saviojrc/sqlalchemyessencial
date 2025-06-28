from services.db_service import DBService

class GenericDAO:

    def __init__(self , db_service: DBService):
        self.session = db_service.session

    ## Faz o crud básico de insert, update, delete e select com try cath , para o select não precisa fazer o try catch


    def close_session(self):
        try:
            self.session.close()
        except Exception as e:
            print(f'Erro ao fechar a sessão {e}')
            raise e

    def insert(self, obj):
        try:
            with self.session as session:
                session.add(obj)
                session.commit()

        except Exception as e:
            print(f'Erro ao inserir {e}')
            raise e
        finally:
           self.close_session()

    def update(self, obj):
        try:
            with self.session as session:
                session.merge(obj)
                session.commit()
        except Exception as e:
            print(f'Erro ao atualizar {e}')
            raise e
        finally:
            self.close_session()

    def delete(self, obj):
        try:
            with self.session as session:
                session.delete(obj)
                session.commit()

        except Exception as e:
            print(f'Erro ao apagar {e}')
            raise e
        finally:
            self.close_session()

    def select_by_id(self, id , type_obj):
        try:
            with self.session as session:
                instance = session.get(type_obj, id)
            return instance
        except Exception as e:
            print(f'Erro ao consultar {e}')
            raise e
        finally:
            self.close_session()

