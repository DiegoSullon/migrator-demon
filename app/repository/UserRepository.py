from app.entities.UserEntity import UserEntity
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

    # (id, username, "password", role_id, user_status_id, email, seller_id, save_session) 
    def insert_many(self, users: list[UserEntity]):

        inserts: list[tuple] = []
        columns: list = [const.USER_ID ,const.USER_USERNAME, const.USER_PASSWORD, const.USER_ROLE_ID, const.USER_STATUS_ID,
                         const.USER_EMAIL, const.USER_SELLER_ID, const.USER_SAVE_SESSION ]
        
        userRoleId = 1
        userStatusId = 1
        dt = datetime.now(timezone.utc)
        saltRounds = 10


        usersLength = len(users)
        self.logger.info(f'Generating password hash to {usersLength} records...')
        
        printProgressBar(0, usersLength, prefix = 'Progress:', suffix = 'Complete', length = 50)
        i=0
        for u in users:
            passw = f'Ripley{u.get_partner_id()}@$'
            hashed = bcrypt.hashpw(bytes(passw, encoding='utf-8'), bcrypt.gensalt(saltRounds))
            decodehash = hashed.decode("utf-8")

            newTuple = tuple([i+7,u.get_user_email(), decodehash, userRoleId, userStatusId, u.get_user_email(), u.get_partner_id(), True])

            inserts.append(newTuple)
            printProgressBar(i + 1, usersLength, prefix = 'Progress:', suffix = 'Complete', length = 50)
            i+=1


        self.logger.info(f'Inserting {len(inserts)} users....')
        print('----')
        self.dbManager.insertMany(const.USER_TABLE, columns, inserts)
