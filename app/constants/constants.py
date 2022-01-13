import os

# Path
ROOT_PATH = os.path.join(os.path.split(os.getcwd())[
                         0], os.path.split(os.getcwd())[1])

USER_TABLE = '"TAS_USER"'

# USER COLUMNS
# (id, username, "password", first_names, last_names, device_token, role_id, user_status_id,
# phone, email, mrkl_shop_name, mrkl_shop_contact, mrkl_shop_id, mrkl_shop_street, mrkl_shop_ruc,
# mrkl_shop_district, created_by, avatar, dni, created_at, updated_at, deleted_at,
# seller_id, password_changed, user_token, api_key, auth_type, save_session, update_user, last_session)
# --------------------------------------------------------------------------------------------------------------
# Required
# (id, username, "password", role_id, user_status_id, email, seller_id, save_session)
USER_ID = 'id'
USER_USERNAME = 'username'
USER_PASSWORD = 'password'
USER_ROLE_ID = 'role_id'
USER_STATUS_ID = 'user_status_id'
USER_EMAIL = 'email'
USER_SELLER_ID = 'seller_id'
USER_SAVE_SESSION = 'save_session'


# SHOP COLUMNS
# (id, ruc, business_name, shop_name, trade_name, phone, address, country_id, state_id, county_id, city_id, email, branch, commission, mrkl_shop_id,
# mrkl_shop_status, mrkl_shop_error, state, created_at, updated_at, deleted_at, "type", parent_partner, web_site, logo, description, address_ref,
# postal_code, contact_last_name, contact_name, enterprise_iva, create_user, update_user)
# --------------------------------------------------------------------------------------------------------------
# Required
# id, ruc, business_name, shop_name, trade_name, phone, address, country_id, state_id, county_id, city_id, email, branch, created_at, updated_at, "type", create_user
SHOP_ID = 'id'
SHOP_ruc = 'ruc'
SHOP_business_name = 'business_name'
SHOP_shop_name = 'shop_name'
SHOP_trade_name = 'trade_name'
SHOP_phone = 'phone'
SHOP_address = 'address'
SHOP_country_id = 'country_id'
SHOP_state_id = 'state_id'
SHOP_state_id = 'state_id'
SHOP_county_id = 'county_id'
SHOP_city_id = 'city_id'
SHOP_email = 'email'
SHOP_branch = 'branch'
SHOP_created_at = 'created_at'
SHOP_updated_at = 'updated_at'
SHOP_type = 'type'
SHOP_create_user = 'create_user'


# Monitores
CREATE_USER = 'create_user'
CREATE_DATE = 'create_date'
LAST_UPDATE = 'last_update'
LAST_SESSION = 'last_session'


PARTNER_ID = 'partner_id'
