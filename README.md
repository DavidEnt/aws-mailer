# AWS emailer

The aim of this project is to provide the infrastructure and code to send emails from AWS. 

## HOW DOES IT WORK

This project contains the AWS CDK (IaC) infrastructure for the following components:

1. A SQS QUEUE to collect the messages to be send.
2. A Lambda function that collects the messages and calls the SES service. 

## PREREQUISITES

- Installed and setup the AWS CLI infrastucture.
- Installed python and poetry.
- Varified the email adresses to send emails from and to in the SES service.

## HOW TO GET STARTED

1. Open the folder 'aws-emailer' in your favorite IDE.
2. Setup a poetry virtual environment. 
3. Activate the poetry environment.
4. Run `cdk deploy' command in the cdk subfolder.
5. Validate the correct deployment of services in Cloudformation.
