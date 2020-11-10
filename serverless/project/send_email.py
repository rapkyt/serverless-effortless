import logging

import boto3

from serverless import settings
from serverless.project.utils import send_email

logger = logging.getLogger(__name__)
dynamodb = boto3.resource("dynamodb")


def handler(event, context):
    """Send email when an object is added to S3."""
    # Sample event:
    # _event = {
    #     "Records": [{"eventVersion": "2.1", "eventSource": "aws:s3",
    #                  "awsRegion": "us-west-2", "eventTime": "2020-11-09T14:36:33.112Z",
    #                  "eventName": "ObjectCreated:Put",
    #                  "userIdentity": {"principalId": "AWS:AIDASPFM7HJ64CSKPPI2K"},
    #                  "requestParameters": {"sourceIPAddress": "152.168.168.229"},
    #                  "responseElements": {"x-amz-request-id": "129F4B0ABD99B542",
    #                     "x-amz-id-2": "oo4N0cozEadasfasdasdasdfaspTqqGzRz6n4xi+A8lIewfYIcAEhAKQ3mK3wOvkv546qUbvZVz1htqe4Q8cK6iqNlYAJfpGmMysB",
    #                                       },
    #                  "s3": {
    #                      "s3SchemaVersion": "1.0", "configurationId": "3fasdd3a-9fd3-4asd0-9asd-e747fsd113ee",
    #                      "bucket": { "name": "newsletter-marketing", "ownerIdentity": {"principalId": "fasdf7LHV4EJA"},
    #                          "arn": "arn:aws:s3:::newsletter-marketing",
    #                                  },
    #                     "object": {"key": "5243756.jpg", "size": 20372,
    #                                "eTag": "b4fc88b74eee8dee4133e214e7e0a2a2",
    #                                "sequencer": "005FA953F5289361F0",
    #                                },
    #                  },
    #                 }]}
    key = event["Records"][0]["s3"]["object"]["key"]
    table = dynamodb.Table(settings.DYNAMODB_TABLE)
    # fetch all emails from the database
    result = table.scan()
    emails = [item["email"] for item in result["Items"]]
    image = f"{settings.MARKETING_S3_BUCKET}/{key}"
    send_email(emails, image)
