import json
import logging

logger = logging.getLogger(__name__)


def format_response(result, status_code=200):
    if result is not None:
        result = json.dumps(result)
    return {"statusCode": status_code, "body": result}


def send_email(emails, image):
    """Open the image and send the email."""
    logger.setLevel(logging.INFO)
    logger.info(f"Send image {image} to emails {emails}")
    # TODO: Handle email sending.
