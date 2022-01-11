import app.utils.LogHandler as logging
import boto3
from botocore.exceptions import ClientError
import app.constants.envargs as env
import os


class AmazonUtils(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def uploadS3File(self, filename, bucketAuth=None, bucketLive=None, path=None):
        try:
            if not path:
                path = os.path.basename(path)

            objectName = f'{env.S3_FOLDER_ROOT}/{path}'
            s3_client = boto3.client('s3')

            if bucketAuth:
                self.logger.info(f'Loading file to {bucketAuth}: {objectName}')
                s3_client.upload_file(filename, bucketAuth, objectName)

            if bucketLive:
                self.logger.info(f'Reloading file to {bucketLive}: {path}')
                s3_client.upload_file(filename, bucketLive, path)

        except ClientError as e:
            self.logger.error(f'Error: {e}')
            return False
        except Exception as e:
            self.logger.error(f'Error: {e}')
            return False
        return True

    def runDataSync(self):
        self.logger.info('Calling datasync')
        try:
            client = boto3.client('datasync')
            response = client.start_task_execution(
                TaskArn=env.TASK_ARN
            )
            self.logger.info(f'Data sync response: {response}')
            return True
        except Exception as e:
            self.logger.warning(e)
            return False

    def downloadS3File(self, bucket, key: str):
        try:
            #item_uuid = str(uuid.uuid4())
            #os.mkdir(os.path.join(['tmp', item_uuid]))
            #download_path = os.path.join(['tmp', item_uuid, key])
            self.logger.info(f"key : {key}")
            download_path = f"/tmp/{key.split('/')[-1]}"
            self.logger.info(f"download_path : {download_path}")

            s3_client = boto3.client('s3')
            s3_client.download_file(bucket, key, download_path)
            return download_path
        except Exception as ex:
            self.logger.error("Error downloading file S3.")
            self.logger.exception(ex)
        return None

    def deleteS3File(self, bucket, key: str):
        try:
            self.logger.info(f'Deleting file: {key} - bucket: {bucket}')
            s3_client = boto3.client('s3')
            s3_client.delete_object(Bucket=bucket, Key=key)
            return True
        except Exception as ex:
            self.logger.error("Error deleting file S3.")
            self.logger.exception(ex)
        return False

    def copyS3File(self, bucket, key: str, newBucket, newKey: str):
        try:
            self.logger.info(
                f'Copying file: {key} - bucket: {bucket} to {newKey} - newBucket: {newBucket}')
            s3 = boto3.resource('s3')
            copy_source = {
                'Bucket': bucket,
                'Key': key
            }
            s3.meta.client.copy(copy_source, newBucket, newKey)
            return True
        except Exception as ex:
            self.logger.error("Error copying file S3.")
            self.logger.error(ex)
        return False
