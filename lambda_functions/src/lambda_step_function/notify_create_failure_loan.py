import json

import boto3


def handle(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])
        print(f'body:{body}')
        task_token = body["TaskToken"]
        response = {
            'taskToken': task_token,
            'message': "notify success"
        }
        print(f'taskToken:{task_token}')
        client = boto3.client('stepfunctions')
        client.send_task_success(
            taskToken=task_token,
            output=json.dumps(response)
        )
        # client.send_task_failure(
        #     taskToken=task_token,
        #     error='CLOSE_LOAN_ACCOUNT_ERROR',
        #     cause=str("")
        # )
