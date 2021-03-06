# cw-logs-to-chime

This serverless app publishes AWS CloudWatch logs to AWS Chime based on a subscription filter.

## App Architecture

![App Architecture](https://github.com/keetonian/cw-logs-to-chime/raw/master/images/cw-logs-to-chime.png)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login
1. Go to the app's page on the [Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:289559741701:applications~cw-logs-to-chime) and click "Deploy"
1. Provide the required app parameters (see parameter details below) and click "Deploy"

### Chime Url
To get a webhook URL for this application:
* Navigate to Settings -> Manage webhooks
* Select "Add Webhooks"
* Name your webhook (this will be the display name in the chat room)
* Copy the Url and paste it into the template parameter

### Log Group Name
You can find the name of the log group by navigating to CloudWatch logs on the AWS console. You can also pass it in as a parameter from another stack or another resource (e.g. default lambda log group names are `/aws/lambda/{lambda-function-name}`).

### Filter Pattern
CloudWatch logs allow you to filter logs based on a pattern. For more information, see the [AWS Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

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