#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk.stack import EmailerStack

app = cdk.App()
EmailerStack(
    app,
    "AWSEmailer",
)
app.synth()