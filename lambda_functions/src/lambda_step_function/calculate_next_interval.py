import json

import boto3


def handle(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])
        print(f'body: {body}')
        task_token = body["TaskToken"]
        retryCount = body["retryCount"]
        response = {
            'taskToken': task_token,
            'retryCount': retryCount
        }
        client = boto3.client('stepfunctions')
        client.send_task_success(
            taskToken=task_token,
            output=json.dumps(response)
        )
