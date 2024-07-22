from typing import Any
from ..models.models import SendEmailRequest

class EventValidationError(Exception):
    """Indicates that the Lambda event was not successfully validated."""

    pass

def parse_event(event: dict[str, Any]) -> SendEmailRequest:
    """Parse the incoming request."""
    print('start parse event')
    request = SendEmailRequest(**event)
    recipients = request.to_addresses + request.cc_addresses + request.bcc_addresses

    if not request.to_addresses:
        raise EventValidationError("At least one To: address should be specified!")

    if len(recipients) > 50:
        raise EventValidationError("Too many recipients specified, max is 50!")

    if not request.body_html and not request.body_txt:
        raise EventValidationError("At least one message body should be specified!")

    return request