from app.entities.ShopEntity import ShopEntity
from app.repository.DBManager import DBManager
from app.utils.Console import printProgressBar
import app.utils.LogHandler as logging
import app.constants.constants as const
from datetime import datetime, timezone
import bcrypt


class UserRepository(object):

    def __init__(self, dbManager: DBManager):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.dbManager = dbManager

    # Requiered (id, username, "password", role_id, user_status_id, save_session, seller_id, email)
    # Obtained (id, username, "password", role_id, user_status_id, save_session, seller_id, email, first_names, last_names, created_at)
    def insert_many(self, users: list[ShopEntity], allUsersRecord: list[ShopEntity], shops_to_relation: list[ShopEntity]):
        try:
            if len(users) >=1:

                dictUserShop: dict[list[int]] = {}
                for user in allUsersRecord:
                    currentShopList = dictUserShop[user.get_user_email(
                    )] if user.get_user_email() in dictUserShop else []
                    dictUserShop[user.get_user_email(
                    )] = currentShopList + [int(user.get_shop_id())]
                
                dictUserName: dict[list[int]] = {}
                dictUserLastName: dict[list[int]] = {}
                for user in shops_to_relation:
                    uEmail = user.get_user_email()
                    dictUserName[uEmail] = user.get_user_first_names()
                    dictUserLastName[uEmail] = user.get_user_last_names()

                inserts: list[tuple] = []
                columns: list = [const.USER_USERNAME, const.USER_PASSWORD, const.USER_ROLE_ID, const.USER_STATUS_ID,
                                const.USER_SAVE_SESSION, const.USER_SELLER_ID, const.USER_EMAIL, const.USER_FIRSTNAME, const.USER_LASTNAME, const.USER_CREATED_AT]

                dt = datetime.now(timezone.utc)
                saltRounds = 10

                usersLength = len(users)
                self.logger.info(
                    f'Generating password hash to {usersLength} records...')

                printProgressBar(0, usersLength, prefix='Progress:',
                                suffix='Complete', length=50)
                i = 0
                for u in users:
                    userEmail = u.get_user_email()
                    # Get lower shopId
                    shopId = int(u.get_shop_id())
                    shopList = dictUserShop[userEmail] if userEmail in dictUserShop else None

                    if shopList:
                        shopId = min(shopList)

                    # Generating encrypt password
                    passw = f'Ripley{shopId}@$'
                    hashed = bcrypt.hashpw(
                        bytes(passw, encoding='utf-8'), bcrypt.gensalt(saltRounds))
                    decodehash = hashed.decode("utf-8")

                    # Get names
                    firstNames = dictUserName[userEmail] if userEmail in dictUserName else None
                    lastNames = dictUserLastName[userEmail] if userEmail in dictUserLastName else None

                    newTuple = tuple([userEmail, decodehash, u.get_user_roleId(), u.get_user_status_id(),
                                    u.get_user_save_session(), shopId, userEmail, firstNames, lastNames, dt])

                    inserts.append(newTuple)
                    printProgressBar(i + 1, usersLength,
                                    prefix='Progress:', suffix='Complete', length=50)
                    i += 1

                self.logger.info(f'Inserting {len(inserts)} users....')
                print('----')
                isInserted = self.dbManager.insertMany(const.USER_TABLE, columns, inserts)
                return isInserted
        except:
            return False
