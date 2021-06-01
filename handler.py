import json
import logging
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

MAX_LABELS = int(os.getenv('MAX_LABELS'))

def image_analyze(event, context):

    client = boto3.client('rekognition')
    print(event)

    if not event['body']:
        return {'statusCode': 400, 'body': json.dumps({'message':'No body was found'})}

    if not event['body']['bucket']:
        return {'statusCode': 400, 'body': json.dumps({'message':'Bucket not informed'})}

    if not event['body']['image']:
        return {'statusCode': 400, 'body': json.dumps({'message':'Image not informed'})}

    bucket = event['body']['bucket']
    image = event['body']['image']

    response = client.detect_labels(Image={'S3Object':{'Bucket': bucket, 'Name': image}}, MaxLabels=MAX_LABELS)

    if not response['Labels']:
        return {'statusCode': 400, 'body': json.dumps({'message':'Could not get response labels', 'response': response})}

    body = response['Labels']

    return {"statusCode": 200, "labels": body}
