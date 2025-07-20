import os
from dotenv import load_dotenv

# loading env variables
load_dotenv()


# env variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")



# constants
EXTERNAL_S3_DATA_BUCKET = "project-partials-1745563858222"
EC2_CFT_STACK_NAME = "ec2-instance-stack"
EC2_CFT_FILE_NAME = "ec2-instance.yml"
EC2_CFT_STACK_TEMPLATE_URL = f"https://{EXTERNAL_S3_DATA_BUCKET}.s3.{AWS_DEFAULT_REGION}.amazonaws.com/{EC2_CFT_FILE_NAME}"