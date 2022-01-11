import app.utils.LogHandler as logging
import app.constants.constants as const


class UserEntity(object):
    def __init__(self, payload):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.payload = payload

    def get_user_id(self):
        try:
            return self.getPayload()[const.USER_ID]
        except:
            self.logger.error('Error getting USER_ID')
            return None

    def get_user_code(self):
        try:
            return self.getPayload()[const.USER_CODE]
        except:
            self.logger.error('Error getting USER_CODE')
            return None

    def get_user_name(self):
        try:
            return self.getPayload()[const.USER_NAME]
        except:
            self.logger.error('Error getting USER_NAME')
            return None

    def get_partner_id(self):
        try:
            return self.getPayload()[const.PARTNER_ID]
        except:
            self.logger.error('Error getting PARTNER_ID')
            return None

    def set_user_password(self, data):
        try:
            self.payload[const.USER_PASSWORD] = data
        except:
            self.logger.error('Error set USER_PASSWORD')

    def set_user_token(self, data):
        try:
            self.payload[const.USER_TOKEN] = data
        except:
            self.logger.error('Error set USER_TOKEN')

    def set_user_type_id(self, data):
        try:
            self.payload[const.USER_TYPE_ID] = data
        except:
            self.logger.error('Error set USER_TYPE_ID')

    def set_user_api_key(self, data):
        try:
            self.payload[const.USER_API_KEY] = data
        except:
            self.logger.error('Error setS USER_API_KEY')

    def set_user_status(self, data):
        try:
            self.payload[const.USER_STATUS] = data
        except:
            self.logger.error('Error set USER_STATUS')

    def set_user_auth_type(self, data):
        try:
            self.payload[const.USER_AUTH_TYPE] = data
        except:
            self.logger.error('Error set USER_AUTH_TYPE')

    def set_user_save_session(self, data):
        try:
            self.payload[const.USER_SAVE_SESSION] = data
        except:
            self.logger.error('Error set USER_SAVE_SESSION')

    def set_create_user(self, data):
        try:
            self.payload[const.CREATE_USER] = data
        except:
            self.logger.error('Error set CREATE_USER')

    def set_update_user(self, data):
        try:
            self.payload[const.UPDATE_USER] = data
        except:
            self.logger.error('Error set UPDATE_USER')

    def set_last_session(self, data):
        try:
            self.payload[const.LAST_SESSION] = data
        except:
            self.logger.error('Error set LAST_SESSION')

    def set_user_id(self, data):
        try:
            self.payload[const.USER_ID] = data
        except:
            self.logger.error('Error set USER_ID')

    def getPayload(self):
        return self.payload
