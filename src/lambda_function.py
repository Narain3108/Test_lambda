import json
import os
import boto3

sfn = boto3.client("stepfunctions")

def lambda_handler(event, context):

    value = event.get("value")

    if value == 1:

        response = sfn.start_execution(
            stateMachineArn=os.environ["STEP_FUNCTION_1_ARN"],
            input=json.dumps(event)
        )

        return {
            "message": "Workflow 1 started",
            "executionArn": response["executionArn"]
        }

    elif value == 2:

        response = sfn.start_execution(
            stateMachineArn=os.environ["STEP_FUNCTION_2_ARN"],
            input=json.dumps(event)
        )

        return {
            "message": "Workflow 2 started",
            "executionArn": response["executionArn"]
        }

    return {
        "message": "Provide value 1 or 2"
    }