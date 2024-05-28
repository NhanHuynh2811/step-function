import boto3
import json


def handle(event, context):
    for record in event["Records"]:
        print().info(record)
        # payload = json.loads(record["body"])
        # sf = boto3.client('stepfunctions', region_name='us-east-1')
        # response = sf.start_execution(
        #     stateMachineArn='arn:aws:states:us-east-1:477163241286:stateMachine:MoreTymeRepaymentWorkflow',
        #     input=json.dumps(payload))
        # logger.info(response)
