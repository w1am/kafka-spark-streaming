import json
from data_ingestion.producer import ReviewProducer

def lambda_handler(event, context):
    producer = ReviewProducer()

    producer.run()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }