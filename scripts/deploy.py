from utils.constants import (
    AWS_ACCESS_KEY,
    AWS_DEFAULT_REGION,
    AWS_SECRET_KEY,
    EC2_CFT_STACK_NAME,
    EC2_CFT_STACK_TEMPLATE_URL,
)
from utils.services.cft import CloudFormationClient, CloudFormationStack


def deploy():
    """Creating the CloudFormation client with aws credentials"""
    cf_client = CloudFormationClient(
        AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_DEFAULT_REGION
    ).get_cf_client()

    """ Deploying Cloud Formation stack """
    template_parameters = [
        {"ParameterKey": "VpcId", "ParameterValue": "vpc-064765778cdec343b"},
        {"ParameterKey": "Subnet1", "ParameterValue": "subnet-0c9607e9079cd9f66"},
        {"ParameterKey": "Subnet2", "ParameterValue": "	subnet-02eb2feff018c7c8b"},
    ]

    cf_stack = CloudFormationStack(
        stack_name=EC2_CFT_STACK_NAME,
        template_url=EC2_CFT_STACK_TEMPLATE_URL,
        parameters=template_parameters,
        cf_client=cf_client,
    )

    cf_stack.deploy()


if __name__ == "__main__":
    deploy()
