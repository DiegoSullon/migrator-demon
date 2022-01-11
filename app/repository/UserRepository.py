from app.entities.UserEntity import UserEntity
from app.repository.DBManager import DBManager
import app.utils.LogHandler as logging
import app.constants.constants as const
from datetime import datetime, timezone
import bcrypt


class UserRepository(object):

    def __init__(self, dbManager: DBManager):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.dbManager = dbManager

    def insert_many(self, users: list[UserEntity]):
        inserts: list[tuple] = []
        columns: list = [const.USER_ID, const.USER_CODE, const.USER_NAME, const.USER_PASSWORD, const.USER_TYPE_ID,
                         const.USER_STATUS, const.USER_SAVE_SESSION, const.CREATE_USER, const.CREATE_DATE, const.LAST_UPDATE]

        dt = datetime.now(timezone.utc)

        saltRounds = 10

        for u in users:
            passw = f'Ripley{u.get_partner_id()}@$'
            print (passw)
            hashed = bcrypt.hashpw(bytes(passw, encoding='utf-8'), bcrypt.gensalt(saltRounds))
            decodehash = hashed.decode("utf-8")
            print (decodehash)
            newTuple = tuple([u.get_user_code(), u.get_user_code(
            ), u.get_user_code(), decodehash, '1', 1, True, 0, dt, dt])
            inserts.append(newTuple)

        self.dbManager.insertMany(const.USER_TABLE, columns, inserts)
