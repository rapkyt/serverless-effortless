import hashlib
import logging

import boto3

from serverless import settings
from serverless.project.utils import format_response

logger = logging.getLogger(__name__)
dynamodb = boto3.resource("dynamodb")


def handler(event, context):
    params = event.get("queryStringParameters", {})
    email = params.get("email", "")
    token = params.get("token", "")
    secret = settings.UNSUBSCRIBE_SECRET
    email_and_secret = f"{email}{secret}".encode()
    hashed_email_and_secret = hashlib.md5(email_and_secret).hexdigest()
    if token != hashed_email_and_secret:
        logger.error("Token is not valid.")
        return format_response({"message": "Token is not valid."}, 400)

    table = dynamodb.Table(settings.DYNAMODB_TABLE)
    table.delete_item(Key={"email": email})
    return format_response(result=None, status_code=204)
