# cw-logs-to-chime

This serverless app publishes AWS CloudWatch logs to AWS Chime based on a subscription filter.

## App Architecture

![App Architecture](https://github.com/keetonian/cw-logs-to-chime/raw/master/images/cw-logs-to-chime.png)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login
1. Go to the app's page on the [Serverless Application Repository](TODO) and click "Deploy"
1. Provide the required app parameters (see parameter details below) and click "Deploy"

## App Parameters

1. `ChimeUrl` (required) - Webhook URL for integration with Chime
1. `LogGroupName` (required) - Log group to listen to (has to be in same account and region)
1. `FilterPattern` (optional) - Pattern for filtering log events. Default: ERROR
1. `LogLevel` (optional) - Log level for Lambda function logging, e.g., ERROR, INFO, DEBUG, etc. Default: INFO

## App Outputs

1. `LogsToChimeName` - Lambda function name.
1. `LogsToChimeArn` - Lambda function ARN.

## License Summary

This code is made available under the MIT license. See the LICENSE file.