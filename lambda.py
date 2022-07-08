import json
import pandas
import boto3
from datetime import datetime

def lambda_handler(event, context):
    for record in event['Records']:
        try:
            #get message and convert into dataframe
            payload = record["body"]
            data = json.loads(payload)
            df = pandas.json_normalize(data)
            
            #generate file name base on the current time
            time = datetime.now()
            fileName = str(time)+"-product-list.csv"
            
            #convert dataframe into csv file
            filePath = "/tmp/" + fileName
            df.to_csv(filePath, index=False)
            
            #upload file into s3
            bucket_name = "roei-bucket"
            s3 = boto3.client('s3')
            s3.upload_file(filePath, bucket_name, fileName)
            
            #send message with SNS
            send_message()
        except:
            print("something went worng, please make sure you sent a valid JSON POST request")
            
            
def send_message():
    message = "Lambda function executed"
    client = boto3.client('sns')
    response = client.publish(
        TargetArn="arn:aws:sns:us-east-1:393952290553:lambda-execution",
        Subject="Email Alert",
        Message=message,
        MessageStructure='string'
    )
