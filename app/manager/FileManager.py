import os
from time import sleep
import app.constants.constants as const
from app.entities.ShopEntity import ShopEntity
from app.repository.DBManager import DBManager
from app.repository.ShopRepository import ShopRepository
from app.repository.UserRepository import UserRepository
import app.utils.LogHandler as logging
import csv


class FileManager(object):

    def __init__(self, dbManager: DBManager):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.dbManager = dbManager

    def execute(self):
        self.dbManager.connect()

        userRepository = UserRepository(self.dbManager)
        shopRepository = ShopRepository(self.dbManager)

        users_to_insert, users_to_relation = self.readUsersCSV()
        shops_to_insert = self.readShopsCSV()
        
        userRepository.insert_many(users_to_insert)
        shopRepository.insert_many(shops_to_insert)
        shopRepository.insert_shops_users(users_to_relation)

        self.dbManager.close()

    def readShopsCSV(self):
        shops_to_insert: list[ShopEntity] = []
        try:
            self.logger.info('Looking for shops file...')

            filePath = f'{const.ROOT_PATH}/app/input/shops.csv'
            
            resultDictShops = []
            shop_ids = []

            with open(filePath) as f:
                for row in csv.DictReader(f, skipinitialspace=True, delimiter=';'):
                    newDict = {}
                    for k, v in row.items():
                        newDict[k] = str(v)

                    # not append duplicate mrkl_shop_id
                    if const.SHOP_ID in newDict and newDict[const.SHOP_ID] not in shop_ids:
                        resultDictShops.append(newDict)
                    if const.SHOP_ID in newDict:
                        shop_ids.append(newDict[const.SHOP_ID])

            for result in resultDictShops:
                newShop = ShopEntity(result)
                shops_to_insert.append(newShop)

            sleep(1)
            if os.path.exists(filePath):
                os.remove(filePath)
            return shops_to_insert
        except Exception as e:
            self.logger.warning('There is not shops file to read')
            print(e)
            return shops_to_insert
        
    def readUsersCSV(self):
        users_to_insert: list[ShopEntity] = []
        users_to_relation: list[ShopEntity] = []
        try:
            self.logger.info('Looking for users file...')

            filePath = f'{const.ROOT_PATH}/app/input/users.csv'
            
            resultDictUsers = []
            resultDictRelation = []
            user_emails = []

            with open(filePath) as f:
                for row in csv.DictReader(f, skipinitialspace=True, delimiter=';'):
                    newDict = {}
                    for k, v in row.items():
                        newDict[k] = str(v)

                    resultDictRelation.append(newDict)

                    # not append duplicate user_codes
                    if const.USER_EMAIL in newDict and newDict[const.USER_EMAIL] not in user_emails:
                        resultDictUsers.append(newDict)
                    if const.USER_EMAIL in newDict:
                        user_emails.append(newDict[const.USER_EMAIL])

            for result in resultDictUsers:
                newUser = ShopEntity(result)
                users_to_insert.append(newUser)

            for result in resultDictRelation:
                newShop = ShopEntity(result)
                users_to_relation.append(newShop)

            sleep(1)
            if os.path.exists(filePath):
                os.remove(filePath)
            return users_to_insert, users_to_relation
        except Exception as e:
            self.logger.warning('There is not users file to read')
            print(e)
            return users_to_insert, users_to_relation
