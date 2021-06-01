# AWS Lambda Rekognition

This Lambda function receives a payload with a AWS S3 Bucket + Id, send it to AWS Rekognition to process objects and scenes and show the process result of it.

"Amazon Rekognition makes it easy to add image and video analysis to your applications using proven, highly scalable, deep learning technology that requires no machine learning expertise to use. With Amazon Rekognition, you can identify objects, people, text, scenes, and activities in images and videos, as well as detect any inappropriate content. Amazon Rekognition also provides highly accurate facial analysis and facial search capabilities that you can use to detect, analyze, and compare faces for a wide variety of user verification, people counting, and public safety use cases.

With Amazon Rekognition Custom Labels, you can identify the objects and scenes in images that are specific to your business needs. For example, you can build a model to classify specific machine parts on your assembly line or to detect unhealthy plants. Amazon Rekognition Custom Labels takes care of the heavy lifting of model development for you, so no machine learning experience is required. You simply need to supply images of objects or scenes you want to identify, and the service handles the rest."

Documentation: https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html

## Requirements

In order to use, you need to install Serverless Framework, as below
```
sudo npm install -g serverless
```

You need to have an AWS account and correcty set the credentials, as showed in http://slss.io/aws-creds-setup

After checkout repository, you should install serverless-python-requirements plugin and serverless-ignore, as below:
```
serverless plugin install -n serverless-python-requirements
npm install --save-dev serverless-ignore
```

In order to execute locally, you need to install python dependencies, as below:
```
pip install -r requirements.txt
```

## Usage

Change `data.json` file with the information of S3 bucket and key of image that should be analyzed, as sample below:

```json
{
    "body": {
        "bucket":"your-bucket-name",
        "image":"path/to/image-s3-key"
    }
}
```

### Local development

You can invoke function locally by using the following command:

```bash
serverless invoke local --function imageAnalyze --path data.json 
```

Which should result in response similar to the following, with labels identified, level of confidence and bounding box, if present. You can check the documentation of each field in: https://docs.aws.amazon.com/rekognition/latest/dg/API_DetectLabels.html

```json
{
    "statusCode": 200,
    "labels": [
        {
            "Name": "Furniture",
            "Confidence": 98.66049194335938,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Person",
            "Confidence": 98.5416488647461,
            "Instances": [
                {
                    "BoundingBox": {
                        "Width": 0.2313053160905838,
                        "Height": 0.5046771764755249,
                        "Left": 0.6030175089836121,
                        "Top": 0.4853447675704956
                    },
                    "Confidence": 98.5416488647461
                }
            ],
            "Parents": []
        },
        {
            "Name": "Human",
            "Confidence": 98.5416488647461,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Desk",
            "Confidence": 97.4099349975586,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Table"
                },
                {
                    "Name": "Furniture"
                }
            ]
        },
        {
            "Name": "Table",
            "Confidence": 97.4099349975586,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Furniture"
                }
            ]
        },
        {
            "Name": "Electronics",
            "Confidence": 86.259765625,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Computer",
            "Confidence": 80.34059143066406,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Electronics"
                }
            ]
        },
        {
            "Name": "Indoors",
            "Confidence": 70.13545227050781,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Machine",
            "Confidence": 67.52073669433594,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Keyboard",
            "Confidence": 57.56290054321289,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Electronics"
                }
            ]
        }
    ]
}
```

### AWS Deployment

In order to deploy the example, you need to run the following command:

```
$ serverless deploy
```

After running deploy, you should see output similar to:

```bash
Serverless: Generated requirements from /home/talesviegas/git/aws-lambda-rekognition/requirements.txt in /home/talesviegas/git/aws-lambda-rekognition/.serverless/requirements.txt...
Serverless: Using static cache of requirements found at /home/talesviegas/.cache/serverless-python-requirements/30febf488d4670fb1e5e875ddd892de45fe6081b2b524b22ce22f18c464a1945_slspyc ...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service aws-lambda-rekognition.zip file to S3 (8.49 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.......
Serverless: Stack update finished...
Service Information
service: aws-lambda-rekognition
stage: dev
region: us-east-1
stack: aws-lambda-rekognition-dev
resources: 6
api keys:
  None
endpoints:
  None
functions:
  imageAnalyze: aws-lambda-rekognition-dev-imageAnalyze
layers:
  None

```

### Invocation

After successful deployment, you can invoke the deployed function by using the following command:

```bash
serverless invoke --function imageAnalyze --path data.json 
```

Which should result in response similar to the following:

```json
{
    "statusCode": 200,
    "labels": [
        {
            "Name": "Furniture",
            "Confidence": 98.66049194335938,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Person",
            "Confidence": 98.5416488647461,
            "Instances": [
                {
                    "BoundingBox": {
                        "Width": 0.2313053160905838,
                        "Height": 0.5046771764755249,
                        "Left": 0.6030175089836121,
                        "Top": 0.4853447675704956
                    },
                    "Confidence": 98.5416488647461
                }
            ],
            "Parents": []
        },
        {
            "Name": "Human",
            "Confidence": 98.5416488647461,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Desk",
            "Confidence": 97.4099349975586,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Table"
                },
                {
                    "Name": "Furniture"
                }
            ]
        },
        {
            "Name": "Table",
            "Confidence": 97.4099349975586,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Furniture"
                }
            ]
        },
        {
            "Name": "Electronics",
            "Confidence": 86.259765625,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Computer",
            "Confidence": 80.34059143066406,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Electronics"
                }
            ]
        },
        {
            "Name": "Indoors",
            "Confidence": 70.13545227050781,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Machine",
            "Confidence": 67.52073669433594,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Keyboard",
            "Confidence": 57.56290054321289,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Electronics"
                }
            ]
        }
    ]
}
```

If you prefer, you can access AWS Console in https://console.aws.amazon.com/lambda/ and test lambda directly in the testing tab.
You should create an event with the same payload that you have in [data.json](data.json)

### Undeployment

In order to undeploy the example and its resources, you need to run the following command:

```
serverless remove
```
