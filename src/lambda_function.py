import json
import boto3
import os

sfn = boto3.client("stepfunctions")

def lambda_handler(event, context):

    print(event)

    # Invoked by Step Function
    if event.get("source") == "stepfunction":
        return {
            "message": "Hello Narain"
        }

    # Initial invocation
    if event.get("value") == 1:
        response = sfn.start_execution(
            stateMachineArn=os.environ["STEP_FUNCTION_ARN"],
            input=json.dumps(event)
        )

        return {
            "message": "Step Function Started",
            "executionArn": response["executionArn"]
        }

    return {
        "message": "Invalid Input"
    }
