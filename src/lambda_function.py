import json
import boto3
import os

sfn = boto3.client("stepfunctions")

def lambda_handler(event, context):

    value = event.get("value")

    response = sfn.start_execution(
        stateMachineArn=os.environ["STEP_FUNCTION_ARN"],
        input=json.dumps({
            "value": value
        })
    )

    return {
        "statusCode": 200,
        "executionArn": response["executionArn"]
    }