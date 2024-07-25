import pytest

from mailer.utils.parse_event import parse_event, EventValidationError
from mailer.models.models import SendEmailRequest

def test_parse_event_good():
    dummy_event = {
        "subject": "Hello world",
        "to_addresses": ["hello.world@gmail.com"],
        "body_txt": "Hello, world"
    }
    expected = SendEmailRequest(
        subject = "Hello world",
        body_txt = "Hello, world",
        to_addresses = ["hello.world@gmail.com"],
        sender = "david.enthoven.python@gmail.com"
    )

    assert parse_event(dummy_event) == expected

def test_parse_event_bad():
    dummy_event = {
        "subject": "Hello world",
        "to_addresses": [],
        "cc_addresses": ["hello.world@gmail.com"],
        "body_txt": "Hello, world"
    }

    with pytest.raises(EventValidationError):
        assert parse_event(dummy_event)

