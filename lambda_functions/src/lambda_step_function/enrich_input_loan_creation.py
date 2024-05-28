import json

import boto3


def handle(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])
        print(f'body: {body}')
        task_token = body["TaskToken"]
        response = {
            'taskToken': task_token,
            'retryCount': 1,
            'loanId': "123Loan"
        }
        client = boto3.client('stepfunctions')
        client.send_task_success(
            taskToken=task_token,
            output=json.dumps(response)
        )
