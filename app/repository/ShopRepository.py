from app.repository.DBManager import DBManager
import app.utils.LogHandler as logging
import app.constants.constants as const
from datetime import datetime, timezone


class ShopRepository(object):

    def __init__(self, dbManager: DBManager):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.dbManager = dbManager

    #  id, ruc, business_name, shop_name, trade_name, phone, address, country_id, state_id, county_id, city_id, email, branch, created_at, updated_at, "type", create_user
    def insert_many(self, shops: list):

        inserts: list[tuple] = []
        columns: list = [const.SHOP_ID, const.SHOP_RUC, const.SHOP_BUSINESS_NAME, const.SHOP_SHOP_NAME, const.SHOP_TRADE_NAME, const.SHOP_PHONE, const.SHOP_ADDRESS,
                         const.SHOP_COUNTRY_ID, const.SHOP_STATE_ID, const.SHOP_COUNTY_ID, const.SHOP_CITY_ID, const.SHOP_EMAIL, const.SHOP_BRANCH, const.SHOP_CREATED_AT, const.SHOP_UPDATED_AT,
                         const.SHOP_TYPE, const.SHOP_CREATE_USER]

        dt = datetime.now(timezone.utc)

        shopsLength = len(shops)

        i=0
        for s in shops:
            newTuple = tuple([i+7, True])
            i+=1
            inserts.append(newTuple)

        self.logger.info(f'Inserting {len(inserts)} users....')
        print('----')
        self.dbManager.insertMany(const.SHOP_TABLE, columns, inserts)
