import json
import random

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'random_number': random.randint(1, 10)})
    }
