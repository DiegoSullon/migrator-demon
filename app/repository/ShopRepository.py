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
        try:
            if len(shops) >= 1:
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
                isInserted = self.dbManager.insertMany(
                    const.SHOP_TABLE, columns, inserts)
                return isInserted
        except:
            return False

    def insert_shops_users(self, shops: list[ShopEntity]):
        try:
            if len(shops) >= 1:
                inserts: list[tuple] = []
                dictUserOrder: dict[list[int]] = {}
                for shop in shops:
                    currentShopList = dictUserOrder[shop.get_user_email(
                    )] if shop.get_user_email() in dictUserOrder else []
                    dictUserOrder[shop.get_user_email(
                    )] = currentShopList + [int(shop.get_shop_id())]
                for shop in shops:
                    # Get users id
                    UserColumns = [const.USER_ID]
                    res = self.dbManager.getMany(const.USER_TABLE, UserColumns, equalParams={
                                                 const.USER_EMAIL: shop.get_user_email()})
                    user_id = res[0][0] if len(res) >= 1 else None

                    order = 0
                    for shopId in dictUserOrder[shop.get_user_email()]:
                        if int(shop.get_shop_id()) < shopId:
                            order += 1

                    if user_id:
                        # Insert relation
                        self.logger.info(
                            f'shop: {shop.get_shop_id()} - user_id: {user_id}')
                        columns = [const.USER_SHOPS_USER_ID, const.USER_SHOPS_SELLER_ID, const.USER_SHOPS_STATE,
                                   const.USER_SHOPS_CREATED_AT, const.USER_SHOPS_UPDATED_AT, const.USER_SHOPS_ORDER, const.USER_SHOPS_UPDATE_USER]
                        dt = datetime.now(timezone.utc)

                        inserts.append(
                            (user_id, shop.get_shop_id(), 1, dt, dt, order, 0))
                if len(inserts) >= 1:
                    self.dbManager.insertMany(
                        const.USER_SHOPS_TABLE, columns, inserts)
        except Exception as e:
            self.logger.error(f'Error insert_shops_users: {e}')

    def insert_shops_categories(self, shops: list[ShopEntity]):
        try:
            if len(shops) >= 1:
                inserts: list[tuple] = []
                dictCategoryOrder = {}
                for shop in shops:
                    # Get users id
                    CategoryColumns = [const.CATEGORY_ID]
                    res = self.dbManager.getMany(const.CATEGORY_TABLE, CategoryColumns, equalParams={
                                                 const.CATEGORY_NAME: shop.get_shop_category()})
                    category_id = res[0][0] if len(res) >= 1 else None

                    order = dictCategoryOrder[category_id] if category_id in dictCategoryOrder else 0
                    dictCategoryOrder[category_id] = order + 1

                    if category_id:
                        # Insert relation
                        self.logger.info(
                            f'shop: {shop.get_shop_id()} - category_id: {category_id}')
                        columns = [const.PARTNER_CATEGORY_PARTNER_ID, const.PARTNER_CATEGORY_CATEGORY_ID,
                                   const.PARTNER_CATEGORY_ORDER, const.PARTNER_CATEGORY_UPDATE_USER, const.PARTNER_CATEGORY_LAST_UPDATE]
                        dt = datetime.now(timezone.utc)

                        inserts.append(
                            (shop.get_shop_id(), category_id, order, 0, dt))

                if len(inserts) >= 1:
                    self.dbManager.insertMany(
                        const.PARTNER_CATEGORY_TABLE, columns, inserts)

        except Exception as e:
            self.logger.error(f'Error insert_shops_categories: {e}')

    def insert_shops_root_directory(self, shops: list[ShopEntity]):
        try:
            print(0)
            if len(shops) >= 1:
                print(1)
                inserts: list[tuple] = []
                print(2)
                for shop in shops:
                    print(3)

                    columns = [const.DIRECTORY_SHOP_PARTNER_ID, const.DIRECTORY_SHOP_IDENTIFIER,
                               const.DIRECTORY_SHOP_PATH, const.DIRECTORY_SHOP_CREATED_USER, const.DIRECTORY_SHOP_CREATED_DATE, const.DIRECTORY_SHOP_LAST_UPDATE]
                    dt = datetime.now(timezone.utc)

                    inserts.append(
                        (shop.get_shop_id(), shop.get_shop_id(), '/', 0, dt, dt))

                print(4)
                if len(inserts) >= 1:
                    self.dbManager.insertMany(
                        const.DIRECTORY_SHOP_TABLE, columns, inserts)

        except Exception as e:
            self.logger.error(f'Error insert_shops_root_directory: {e}')
