import os

# Serverless
# ==================================================
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE")

UNSUBSCRIBE_SECRET = os.environ.get("UNSUBSCRIBE_SECRET")

MARKETING_S3_BUCKET = os.environ.get("MARKETING_S3_BUCKET")
