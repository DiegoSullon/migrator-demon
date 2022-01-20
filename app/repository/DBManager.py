
from distutils.sysconfig import customize_compiler
import app.utils.LogHandler as logging
import app.constants.envargs as env
import sys
import psycopg2
from psycopg2 import pool

class DBManager(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.postgreSQL_pool = None
        self.conn = None

    def initPool(self):
        self.logger.info('Connecting to the PostgreSQL database...')
        try:
            self.postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(1, 20,  #minConnection, maxConnection
                                                        host=env.DB_HOST,
                                                        database=env.DB_NAME,
                                                        user=env.DB_USER,
                                                        password=env.DB_PASSWORD)

            self.logger.info(f'Connect pool with the db successfully: {self.postgreSQL_pool}')
        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.error(f'Error connecting to DB: {error}')
            self.logger.info('Finishing execution .....')
            sys.exit()

    def connect(self):
        self.logger.info('Getting pool conection')
        try:
            self.conn = self.postgreSQL_pool.getconn()
            self.logger.info(f'Pool connetion obtained: {self.conn}')
        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.error(f'Error connecting to DB: {error}')

    def close(self):
        self.logger.info('Returning connection')
        self.postgreSQL_pool.putconn(self.conn)
    
    def getMany(self, table: str, columns:list[str] = [], equalParams: dict = {}):
        """Select many query\n
        Return:\n
        \tSelect many response -> list[list[str]]

        Parameters: \n
        \ttable -- table name \n
        \tcolumns -- select columns \n
        \tequalParams -- where params -> {'status': 'P', 'sync': 'P'} \n

        Exceptions:
        \tError db getMany
        """
        try:

            cursor = self.conn.cursor()

            query = self.selectQuery(table, columns, equalParams)
            cursor.execute(query)
            response = cursor.fetchall()

            cursor.close()
            self.logger.debug(f'First response: {response}')
            self.logger.debug(f'obtained rows: {len(response)}')
            return response
        except Exception as error:
            self.logger.error(f'Error db getMany: {error}')
            return None

    
    def cutomGetMany(self, customQuery: str):
        """Select many with customQuery
        """
        try:
            if(not customQuery or customQuery==''): return None

            cursor = self.conn.cursor()

            cursor.execute(customQuery)
            response = cursor.fetchall()

            cursor.close()

            self.logger.debug(f'First response: {response}')
            self.logger.info(f'obtained rows: {len(response)}')
            return response
        except Exception as error:
            self.logger.error(f'Error db getMany: {error}')
            return None


    def selectQuery(self, table: str, columns:list[str] = [], equalParams: dict = {}):
        columnsQuery = ','.join(columns) if columns else '*'
        equals = ''
        equalKeys = equalParams.keys()
        for p in equalKeys:
            if(p == list(equalKeys)[len(equalKeys)-1]):
                equals += f"{p} = '{equalParams[p]}' "
            else:
                equals += f"{p} = '{equalParams[p]}' AND "

        whereQuery = f'WHERE {equals}' if equalParams else ''
        query=f'SELECT {columnsQuery} FROM {table} {whereQuery}'
        return query
    
    def updateOne(self, table: str, idColumn: str, updates: dict = {}, id: str = ''):
        try:
            if(id==''): return None
            updatesQuery = ''
            updateKeys = updates.keys()
            for u in updateKeys:
                if(u == list(updateKeys)[len(updateKeys)-1]):
                    updatesQuery += f"{u} = '{updates[u]}'"
                else:
                    updatesQuery += f"{u} = '{updates[u]}', "

            query = f'update "{table}" set {updatesQuery} where {idColumn} = {id}'
            self.logger.debug(f'UPDATE: {query}')

            cursor = self.conn.cursor()

            cursor.execute(query, ())
            self.conn.commit()
            row_count = cursor.rowcount

            cursor.close()

            self.logger.info(f"Records Updated: {row_count}")
            return True
        except Exception as error:
            self.logger.info(f'Error db updateOne: {error}')
            return None

    def updateMany(self, table: str, idColumn: str, updates: dict = {}, ids: list[str] = []):
        try:
            if(ids==[]): return None
            updatesQuery = ''
            updateKeys = updates.keys()
            for u in updateKeys:
                if(u == list(updateKeys)[len(updateKeys)-1]):
                    updatesQuery += f"{u} = '{updates[u]}'"
                else:
                    updatesQuery += f"{u} = '{updates[u]}', "

            query = f'update "{table}" set {updatesQuery} where {idColumn} in ({",".join(ids)})'
            self.logger.debug(f'UPDATE: {query}')

            cursor = self.conn.cursor()

            cursor.execute(query, ())
            self.conn.commit()
            row_count = cursor.rowcount

            cursor.close()

            self.logger.info(f"Records Updated: {row_count}")
            return True
        except Exception as error:
            self.logger.info(f'Error db updateMany: {error}')
            return None
    def insertMany(self, table: str, columns: list = [], data: list[tuple] = []):
        cursor = None
        try:
            if(data==[]): return None

            records_list_template = ','.join(['%s'] * len(data))
            columnsJoin = ','.join(columns)
            insert_query = f'insert into {table} ({columnsJoin}) values {records_list_template}'

            cursor = self.conn.cursor()
            cursor.execute(insert_query, data)
            self.conn.commit()
            row_count = cursor.rowcount

            cursor.close()
            self.logger.info(f"Records Inserts: {row_count}")

        except Exception as error:
            self.logger.info(f'Error db insertMany: {error}')
            self.conn.commit()
            if(cursor):
                cursor.close()
            return None