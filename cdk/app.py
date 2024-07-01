#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_emailer import EmailerStack

app = cdk.App()
EmailerStack(
    app,
    "AWSEmailer",
)
app.synth()
