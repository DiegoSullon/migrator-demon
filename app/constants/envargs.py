import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.


def get_env_var(key, default=''):
    value = os.getenv(key, default)
    if value == '':
        raise Exception(f'Environment variable not found: {key}')
    return value

DB_HOST = get_env_var('DB_HOST', '')
DB_NAME = get_env_var('DB_NAME', '')
DB_USER= get_env_var('DB_USER', '')
DB_PASSWORD = get_env_var('DB_PASSWORD', '')

S3_BUCKET_AUTH = get_env_var('S3_BUCKET_AUTH', '')
S3_BUCKET_LIVE = get_env_var('S3_BUCKET_LIVE', '')
S3_FOLDER_ROOT = get_env_var('S3_FOLDER_ROOT', '')
S3_FOLDER_DELETED = get_env_var('S3_FOLDER_DELETED', '')
TASK_ARN = get_env_var('TASK_ARN', '')