from dataclasses import dataclass, field
from typing import Literal, Optional, TypedDict

@dataclass
class SendEmailRequest:
    """
    Models a request for SES to send an e-mail.

    Based on:
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/client/send_email.html
    """

    subject: str
    sender: str
    to_addresses: list[str]
    cc_addresses: list[str] = field(default_factory=list)
    bcc_addresses: list[str] = field(default_factory=list)
    body_html: str = ""
    body_txt: str = ""

class ExecutionSummary(TypedDict):
    """The dictionary that the Lambda will return after an execution.

    Notes:
        - `message`: The error description when status is 400, or a success message when
            status is 200.
        - `message_id`: The ID of the response from SES, only sent when status is 200.
    """

    status: Literal[200, 400]
    message: str
    message_id: Optional[str]