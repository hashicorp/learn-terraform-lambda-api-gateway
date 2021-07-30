# Lambda function code
import json

def lambda_handler(event, context):
    print(f"[lambda_function] Received event: {json.dumps(event)}")
    print(f"[lambda_function] You can use this context: {context}")

    payload = {
        'message' : 'Hello Daniel',
        'details' : 'Lmk if you have questions'
    }

    """
    API Gateway expects an object with statusCode, headers, and body
    body must be a string
    """

    return { 
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': str(payload)
    }
