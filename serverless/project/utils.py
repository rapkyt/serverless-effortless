import json


def format_response(result, status_code=200):
    result = json.dumps(result)
    return {"statusCode": status_code, "body": result}
