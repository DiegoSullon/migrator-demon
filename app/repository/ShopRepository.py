from app.entities.ShopEntity import ShopEntity
from app.repository.DBManager import DBManager
import app.utils.LogHandler as logging
import app.constants.constants as const
from datetime import datetime, timezone


class ShopRepository(object):

    def __init__(self, dbManager: DBManager):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.dbManager = dbManager

    #Requiered (id, ruc, business_name, shop_name, trade_name, phone, address, country_id, state_id, county_id, city_id, email, branch, created_at, updated_at, "type", create_user)
    #Obtained (id, shop_name, type, state, web_site, logo, description, mrkl_shop_id, business_name, ruc, address, address_ref, country_id, state_id, city_id, county_id, phone, email, created_at, updated_at, branch, trade_name, create_user)
    def insert_many(self, shops: list[ShopEntity]):
        if len(shops) >=1:
            inserts: list[tuple] = []
            columns: list = [const.SHOP_SERIAL, const.SHOP_NAME, const.SHOP_TYPE, const.SHOP_STATE, const.SHOP_WEB_SITE, const.SHOP_LOGO, const.SHOP_DESCRIPTION, const.SHOP_ID, const.SHOP_BUSINESS_NAME, const.SHOP_RUC,
                            const.SHOP_ADDRESS, const.SHOP_ADDRESS_REF, const.SHOP_COUNTRY_ID, const.SHOP_STATE_ID, const.SHOP_CITY_ID, const.SHOP_COUNTY_ID, const.SHOP_PHONE, const.SHOP_EMAIL,
                            const.SHOP_CREATED_AT, const.SHOP_UPDATED_AT, const.SHOP_BRANCH, const.SHOP_TRADE_NAME, const.SHOP_CREATE_USER]

            dt = datetime.now(timezone.utc)

            shopsLength = len(shops)

            i = 0
            for s in shops:
                newTuple = tuple([s.get_mrkl_shop_id(), s.get_shop_name(), s.get_shop_type(), s.get_shop_state(), s.get_web_site(), s.get_shop_logo(), s.get_shop_description(), s.get_mrkl_shop_id(), s.get_business_name(), s.get_shop_ruc(),
                                s.get_shop_address(), s.get_shop_address_ref(), s.get_shop_country_id(), s.get_shop_state_id(
                ), s.get_shop_city_id(), s.get_shop_county_id(), s.get_shop_phone(), s.get_shop_email(),
                    dt, dt, s.get_shop_branch(), s.get_shop_trade_name(), 0])
                i += 1
                self.logger.info(f'ruc: {len(s.get_shop_ruc())}')
                self.logger.info(f'phone: {len(s.get_shop_phone())}')
                inserts.append(newTuple)

            self.logger.info(f'Inserting {len(inserts)} shops....')
            print('----')
            self.dbManager.insertMany(const.SHOP_TABLE, columns, inserts)
