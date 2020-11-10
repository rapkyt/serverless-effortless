import json

from serverless.project.send_email import handler as send_email
from serverless.project.subscribe import handler as subscribe
from serverless.project.unsubscribe import handler as unsubscribe


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
    "unsubscribe",
    "send_email",
]
