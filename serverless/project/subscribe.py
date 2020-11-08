import json
import logging
import time

import boto3

from serverless import settings
from serverless.project.utils import format_response

dynamodb = boto3.resource("dynamodb")


def handler(event, context):
    data = json.loads(event["body"])
    if "email" not in data:
        logging.error("Validation Failed")
        return format_response(
            {"message": "Couldn't add the email to the newsletter."}, 400
        )
    table = dynamodb.Table(settings.DYNAMODB_TABLE)

    timestamp = str(time.time())
    item = {
        "email": data["email"],
        "createdAt": timestamp,
        "updatedAt": timestamp,
    }
    # write the email to the database
    table.put_item(Item=item)
    # create a response
    return format_response(item)
