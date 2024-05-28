import json
import random
import boto3


def handle(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])
        print(f'body: {body}')
        task_token = body["TaskToken"]
        random_number = random.randrange(1, 10)
        isRetry = False
        if random_number % 2 == 0:
            isRetry = True
        response = {
            'taskToken': task_token,
            'retryCount': 1
        }
        client = boto3.client('stepfunctions')
        client.send_task_success(
            taskToken=task_token,
            output=json.dumps(response)
        )
