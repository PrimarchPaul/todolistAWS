import json
import boto3
import uuid
from datetime import datetime

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'TodoList'  # Update this with your DynamoDB table name

def lambda_handler(event, context):
    # Extract task description from request body
    task_description = event.get('TaskDescription', '')
    
    # Generate unique ID using UUID
    todo_id = str(uuid.uuid4())
    
    # Generate current date and time
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Add the to-do item to the DynamoDB table
    table = dynamodb.Table(table_name)
    response = table.put_item(
        Item={
            'ID': todo_id,
            'CreationDate': current_date,
            'TaskDescription': task_description
        }
    )
    
    # Return a response indicating success or failure
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Todo item added successfully')
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to add todo item')
        }
