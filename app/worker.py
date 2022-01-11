from app.manager.UserManager import UserManager
import app.utils.LogHandler as logging
from time import sleep
from app.repository.DBManager import DBManager
import app.constants.envargs as envargs
from app.utils.AmazonUtils import AmazonUtils
import app.constants.constants as const
import schedule


class Worker(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.amazonManager = AmazonUtils()
        self.dbManager = DBManager()

    def execute(self):
        self.dbManager.initPool()
        self.dbManager.connect()

        userManager = UserManager(self.dbManager)

        userCreateFrequency = 5
        sellerCreateFrequency = 5
        schedule.every(userCreateFrequency).seconds.do(userManager.execute)
        # schedule.every(sellerCreateFrequency).seconds.do(manager.execute)

        while True:
            schedule.run_pending()
            sleep(1)
