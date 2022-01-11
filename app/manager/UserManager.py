import os
import app.constants.constants as const
from app.entities.UserEntity import UserEntity
from app.repository.DBManager import DBManager
from app.repository.UserRepository import UserRepository
import app.utils.LogHandler as logging
import csv


class UserManager(object):

    def __init__(self, dbManager: DBManager):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.dbManager = dbManager

    def execute(self):
        self.dbManager.connect()
        userRepository = UserRepository(self.dbManager)
        users_to_insert = self.readCSV()
        userRepository.insert_many(users_to_insert)
        

        self.dbManager.close()

    def readCSV(self):
        try:
            self.logger.info('Looking for user file...')
            users_to_insert: list[UserEntity] = []
            
            with open(f'{const.ROOT_PATH}/app/input/users.csv') as f:
                resultDict = [{k: str(v) for k, v in row.items()}
                     for row in csv.DictReader(f, skipinitialspace=True, delimiter=';')]

            for result in resultDict:
                newUser = UserEntity(result)
                users_to_insert.append(newUser)

            return users_to_insert
        except Exception as e:
            self.logger.warning('There are not files to read')
            print(e)
            return []
