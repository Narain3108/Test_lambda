import json
import boto3
import os

sfn = boto3.client("stepfunctions")

def lambda_handler(event, context):

    response = sfn.start_execution(
        stateMachineArn=os.environ["STEP_FUNCTION_ARN"],
        input=json.dumps(event)
    )

    return {
        "statusCode": 200,
        "message": "Step Function started successfully",
        "executionArn": response["executionArn"]
    }
