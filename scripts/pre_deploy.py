import os

from utils.constants import (
    AWS_ACCESS_KEY,
    AWS_DEFAULT_REGION,
    AWS_SECRET_KEY,
    EC2_CFT_FILE_NAME,
    EXTERNAL_S3_DATA_BUCKET,
)
from utils.services.s3_manager import S3Manager


def pre_deploy():
    s3_mgr = S3Manager(
        access_key=AWS_ACCESS_KEY, secret_key=AWS_SECRET_KEY, region=AWS_DEFAULT_REGION
    )

    # creating the bucket
    s3_mgr.create_bucket(EXTERNAL_S3_DATA_BUCKET)

    base_dir = os.getcwd()
    # upload cloud formation template
    ec2_template_file_path = os.path.join(base_dir, "templates", EC2_CFT_FILE_NAME)
    s3_mgr.upload_file(
        ec2_template_file_path, EXTERNAL_S3_DATA_BUCKET, EC2_CFT_FILE_NAME
    )



if __name__ == "__main__":
    pre_deploy()