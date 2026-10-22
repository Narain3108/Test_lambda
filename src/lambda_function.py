import json
import boto3
import os

sfn = boto3.client("stepfunctions")

def lambda_handler(event, context):

    # Called by Step Function
    if event.get("source") == "stepfunction":
        return {
            "message": "Hello Narain"
        }

    # Called directly
    value = event.get("value")

    if value == 1:
        response = sfn.start_execution(
            stateMachineArn=os.environ["STEP_FUNCTION_ARN"],
            input=json.dumps({
                "source": "stepfunction"
            })
        )

        return {
            "message": "Step Function started",
            "executionArn": response["executionArn"]
        }

    return {
        "message": "Invalid input"
    }
