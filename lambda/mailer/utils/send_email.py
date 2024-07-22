#from mypy_boto3_ses import SESClient
from ..models.models import SendEmailRequest

def send_email(client: SESClient, request: SendEmailRequest) -> str: # type: ignore
    """Send e-mail using SES.

    :param client: An instantiated Boto3 SES client.
    :param request: The request parsed from the Lambda event.
    :returns: The ID of the message upon a successful call to SES.
    """
    
    response = client.send_email(
        Source="david.enthoven.python@gmail.com",
        Destination={
            "BccAddresses": request.bcc_addresses,
            "CcAddresses": request.cc_addresses,
            "ToAddresses": request.to_addresses,
        },
        Message={
            "Body": {
                "Html": {
                    "Charset": "UTF-8",
                    "Data": request.body_html,
                },
                "Text": {
                    "Charset": "UTF-8",
                    "Data": request.body_txt,
                },
            },
            "Subject": {
                "Charset": "UTF-8",
                "Data": request.subject,
            },
        },
    )
    
    print(f"Got the following response from SES: {response}")
    return response["MessageId"]
