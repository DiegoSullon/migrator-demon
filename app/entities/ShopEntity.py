import app.utils.LogHandler as logging
import app.constants.constants as const
from datetime import date

class ShopEntity(object):
    def __init__(self, payload):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.payload = payload

    # User
    def get_user_id(self):
        try:
            return self.getPayload()[const.USER_ID]
        except:
            self.logger.error('Error getting USER_ID')
            return None

    def get_user_email(self):
        try:
            return self.getPayload()[const.USER_EMAIL]
        except:
            self.logger.error('Error getting USER_EMAIL')
            return None

    def get_user_name(self):
        try:
            return self.getPayload()[const.USER_EMAIL]
        except:
            self.logger.error('Error getting USER_USERNAME')
            return None

    def get_user_roleId(self):
        try:
            return 2
        except:
            self.logger.error('Error getting user_roleId')
            return None
            
    def get_user_status_id(self):
        try:
            return 1
        except:
            self.logger.error('Error getting user_status_id')
            return None

    def get_user_save_session(self):
        try:
            return False
        except:
            self.logger.error('Error getting user_save_session')
            return False

    def get_user_first_names(self):
        try:
            return self.getPayload()[const.USER_FIRSTNAME]
        except:
            self.logger.error('Error getting user_first_names')
            return None

    def get_user_last_names(self):
        try:
            return self.getPayload()[const.USER_LASTNAME]
        except:
            self.logger.error('Error getting user_last_names')
            return None

    # Shop
    def get_shop_id(self):
        try:
            return self.getPayload()[const.SHOP_ID]
        except:
            self.logger.error('Error getting SHOP_ID')
            return None

    def get_shop_name(self):
        try:
            return self.getPayload()[const.SHOP_NAME]
        except:
            self.logger.error('Error getting SHOP_NAME')
            return None

    def get_shop_type(self):
        try:
            # S: Seller
            # P: Provider
            return 'S'
        except:
            self.logger.error('Error getting SHOP_type')
            return None

    def get_shop_state(self):
        try:
            # 1: INACTIVO| CERRADO
            # 2: ACTIVO|ABIERTO
            # 3: ELIMINADO
            return '2' if self.getPayload()[const.SHOP_STATE][0] == 'A' else '1'
        except:
            self.logger.error('Error getting SHOP_STATE')
            return None
    
    def get_web_site(self):
        try:
            return self.getPayload()[const.SHOP_WEB_SITE]
        except:
            self.logger.error('Error getting SHOP_WEB_SITE')
            return None

    def get_shop_logo(self):
        try:
            return self.getPayload()[const.SHOP_LOGO]
        except:
            self.logger.error('Error getting SHOP_LOGO')
            return None

    def get_shop_logo(self):
        try:
            return self.getPayload()[const.SHOP_DESCRIPTION]
        except:
            self.logger.error('Error getting SHOP_DESCRIPTION')
            return None

    def get_mrkl_shop_id(self):
        try:
            return self.getPayload()[const.SHOP_ID]
        except:
            self.logger.error('Error getting mrkl_shop_id')
            return None

    def get_business_name(self):
        try:
            return self.getPayload()[const.SHOP_BUSINESS_NAME]
        except:
            self.logger.error('Error getting SHOP_BUSINESS_NAME')
            return None

    def get_shop_ruc(self):
        try:
            return self.getPayload()[const.SHOP_RUC]
        except:
            self.logger.error('Error getting SHOP_RUC')
            return None

    def get_shop_address(self):
        try:
            return self.getPayload()[const.SHOP_ADDRESS]
        except:
            self.logger.error('Error getting SHOP_ADDRESS')
            return None

    def get_shop_address_ref(self):
        try:
            return self.getPayload()[const.SHOP_ADDRESS_REF]
        except:
            self.logger.error('Error getting SHOP_ADDRESS_REF')
            return None

    def get_shop_country_id(self):
        try:
            return '051'
        except:
            self.logger.error('Error getting country_id')
            return None

    def get_shop_state_id(self):
        try:
            return '15'
        except:
            self.logger.error('Error getting state_id')
            return None

    def get_shop_city_id(self):
        try:
            return '150101'
        except:
            self.logger.error('Error getting city_id')
            return None
            
    def get_shop_county_id(self):
        try:
            return '1501'
        except:
            self.logger.error('Error getting county_id')
            return None

    def get_shop_phone(self):
        try:
            return self.getPayload()[const.SHOP_PHONE]
        except:
            self.logger.error('Error getting phone')
            return None

    def get_shop_email(self):
        try:
            return self.getPayload()[const.SHOP_EMAIL]
        except:
            self.logger.error('Error getting email')
            return None

    def get_shop_created_at(self):
        try:
            return self.getPayload()[const.SHOP_CREATED_AT]
        except:
            self.logger.error('Error getting SHOP_CREATED_AT')
            return None

    def get_shop_updated_at(self):
        try:
            today = date.today().strftime("%d-%m-%Y")
            return today
        except:
            self.logger.error('Error getting updated_at')
            return None

    def get_shop_branch(self):
        try:
            return self.getPayload()[const.SHOP_BRANCH]
        except:
            self.logger.error('Error getting branch')
            return None

    def get_shop_trade_name(self):
        try:
            return self.getPayload()[const.SHOP_TRADE_NAME]
        except:
            self.logger.error('Error getting trade_name')
            return None

    def getPayload(self):
        return self.payload
