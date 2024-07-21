from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_source,
    aws_iam as iam,
)
from constructs import Construct


class EmailerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the SQS queue resource
        queue = sqs.Queue(
            self, 
            "SQS_Queue",
            queue_name = "emails-to-send-out"
        )

        # Define the Lambda function resource
        lambda_function = _lambda.Function(
            self,
            "Lambda_Function",
            runtime=_lambda.Runtime.PYTHON_3_10,
            code=_lambda.Code.from_asset(
                "lambda"
            ),  # Points to the lambda directory,
            handler="emailer.handler",  # Points to the file and function in the lambda directory
        )

        # Add policy to the lambda function to enable sending emails.
        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["ses:SendEmail", "ses:SendRawEmail"],
                resources=["*"],
            )
        )

        # Create an SQS event source for Lambda
        sqs_event_source = lambda_event_source.SqsEventSource(queue)

        # Add SQS event source to the Lambda function
        lambda_function.add_event_source(sqs_event_source)
