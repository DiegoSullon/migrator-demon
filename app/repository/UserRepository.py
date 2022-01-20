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
    def insert_many(self, users: list[ShopEntity]):
        if len(users) >=1:
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
                passw = f'Ripley{u.get_shop_id()}@$'
                hashed = bcrypt.hashpw(
                    bytes(passw, encoding='utf-8'), bcrypt.gensalt(saltRounds))
                decodehash = hashed.decode("utf-8")

                newTuple = tuple([u.get_user_email(), decodehash, u.get_user_roleId(), u.get_user_status_id(),
                                u.get_user_save_session(), u.get_shop_id(), u.get_user_email(), u.get_user_first_names(), u.get_user_last_names(), dt])

                inserts.append(newTuple)
                printProgressBar(i + 1, usersLength,
                                prefix='Progress:', suffix='Complete', length=50)
                i += 1

            self.logger.info(f'Inserting {len(inserts)} users....')
            print('----')
            self.dbManager.insertMany(const.USER_TABLE, columns, inserts)
