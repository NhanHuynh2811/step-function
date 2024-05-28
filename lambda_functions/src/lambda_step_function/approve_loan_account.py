import json

import boto3


def handle(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])
        task_token = body["TaskToken"]
        response = {
            'taskToken': task_token,
            'message': "close success"
        }
        print(f'body:{body}')
        client = boto3.client('stepfunctions')
        # client.send_task_success(
        #     taskToken=task_token,
        #     output=json.dumps(response)
        # )
        client.send_task_failure(
            taskToken=task_token,
            error='PROFILE_NOT_ELIGIBLE',
            cause=str("")
        )
