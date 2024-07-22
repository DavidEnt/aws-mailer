"""
Send an e-mail with SES by events from an SQS queue.

Notes:
    - This Lambda can handle multiple requests in a single execution.
"""
import os
import boto3
from typing import Any
#from mypy_boto3_ses import SESClient

from .models.models import ExecutionSummary
from .utils.parse_event import parse_event
from .utils.send_email import send_email

def handle_email_request(client, event: dict[str, Any]) -> ExecutionSummary:
    """
    Handle the parsing of the Lambda event and sending of an e-mail via SES.

    :param client: An instantiated Boto3 SES client.
    :param event: The execution event from the Lambda service.
    :returns: A dictionary describing the status of the execution.
    """

    try:
        print(f"Got the following event: {event}")
        request = parse_event(event)
        message_id = send_email(client, request)
    except EventValidationError as err: # type: ignore
        result: ExecutionSummary = {
            "status": 400,
            "message": str(err),
            "message_id": None,
        }
    except ClientError as err: # type: ignore
        result: ExecutionSummary = {
            "status": 400,
            "message": err.response["Error"]["Message"],  # type: ignore
            "message_id": None,
        }
    else:
        result: ExecutionSummary = {
            "status": 200,
            "message": "E-mail successfully sent",
            "message_id": message_id,
        }
    return result


def handler(event: list[dict[str, Any]], context: dict[str, Any]) -> list[ExecutionSummary]:
    # We need to set a region for the boto3 client to work. We use the env var below.
    # This env var is automatically set by the Lambda service, we do not add it
    # ourselves during the deployment.

    region = os.environ.get("AWS_REGION", "eu-west-1")
    client = boto3.client("ses", region_name=region)

    results = [handle_email_request(client, e["body"]) for e in event]

    return results
