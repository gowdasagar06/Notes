Connect & Disconnect
---
import json

def lambda_handler(event, context):
    print(event)
    print("**Hello Sagar Connected**")
    print(context)
    return { "statusCode": 200  }

SendMessage - Needs AmazonAPIGatewayInvokeFullAccess IAM Policy
---
import json
import urllib3
import boto3

client = boto3.client('apigatewaymanagementapi', endpoint_url="https://lyazahf0i2.execute-api.ap-south-1.amazonaws.com/production")

def lambda_handler(event, context):
    print(event)
    connectionId = event["requestContext"]["connectionId"]
    responseMessage = "responding ..."
    response = client.post_to_connection(ConnectionId=connectionId, Data=json.dumps(responseMessage).encode('utf-8'))
    return { "statusCode": 200  }


Broadcast - Needs AmazonAPIGatewayInvokeFullAccess IAM Policy
---
import json
import urllib3
import boto3

client = boto3.client('apigatewaymanagementapi', endpoint_url="https://lyazahf0i2.execute-api.ap-south-1.amazonaws.com/production")

def lambda_handler(event, context):
    connectionId = event["connectionId"]
    message = event["message"]
    response = client.post_to_connection(ConnectionId=connectionId, Data=json.dumps(message).encode('utf-8'))
    print(response)
    
 Broadcast Lambda Input Event Example
 ---
{
  "connectionId": "FUVNdckkIAMCIZw=",
  "message": "Anyone out there?"
}
