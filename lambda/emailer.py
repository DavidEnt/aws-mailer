import json
import boto3

client = boto3.client("ses", region_name="eu-west-1")


def handler(event, context):
    print("> Hello, start sending email ...")

    record = event["Records"][0]
    body = json.loads(record["body"])

    response = client.send_email(
        Destination={"ToAddresses": body["to"]},
        Message={
            "Body": {
                "Text": {
                    "Charset": "UTF-8",
                    "Data": body["text"],
                }
            },
            "Subject": {
                "Charset": "UTF-8",
                "Data": body["subject"],
            },
        },
        Source="david.enthoven.python@gmail.com",
    )

    print(response)

    return {
        "statusCode": 200,
        "body": json.dumps(
            "Email Sent Successfully. MessageId is: " + response["MessageId"]
        ),
    }
