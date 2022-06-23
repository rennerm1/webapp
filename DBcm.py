import pymysql




class ConnectionError(Exception):
    pass

class CredentialsError(Exception):
    pass

class SQLError(Exception):
    pass

class UseDatabase:


    def __init__(self, config):
        self.configuration = config



    def __enter__(self):
        try:
            self.conn = pymysql.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except pymysql.OperationalError as er:
            raise ConnectionError(er)
        except pymysql.InternalError as err:
            raise CredentialsError(err)


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is pymysql.ProgrammingError:
            raise SQLError(exc_val)
        elif exc_type:
            raise exc_type(exc_val)