from flask import Flask, request
import boto3
import json

app = Flask(__name__)

@app.route('/api', methods=["POST"])
def post():
    sqs_client = boto3.client("sqs", region_name="us-east-1")
    message = request.get_json(silent=True)
    print(message)
    response = sqs_client.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/393952290553/MyQueue",
        MessageBody=json.dumps(message)
    )
    print(response)
    return "200"

app.run(host='0.0.0.0', port=80)