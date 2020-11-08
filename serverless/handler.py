import json

from serverless.project.subscribe import handler as subscribe


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
    }
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response


__all__ = [
    "hello",
    "subscribe",
]
