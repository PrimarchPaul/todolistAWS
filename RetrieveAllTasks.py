import json
import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'TodoList'  # Update this with your DynamoDB table name

def lambda_handler(event, context):
    # Retrieve all to-do items from the DynamoDB table
    table = dynamodb.Table(table_name)
    response = table.scan()
    
    # Return the list of to-do items
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }
