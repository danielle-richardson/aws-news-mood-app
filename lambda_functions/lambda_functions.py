import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    table = dynamodb.Table('news')
    inputSentiment=event['sentiment']
    try:
        # Querying the table using Primary key
        response = table.query(
            KeyConditionExpression=Key('sentiment').eq(inputSentiment),
            Limit=10, #limits returned news to 10
            ScanIndexForward=False) #descending order of timestamp, most recent news first
        return response
    except:
        raise