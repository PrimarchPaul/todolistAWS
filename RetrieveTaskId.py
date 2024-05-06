import json
import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'TodoList'  # Update this with your DynamoDB table name

def retrieve_task_by_id(task_id):
    # Retrieve the task with the specified ID from the DynamoDB table
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={'ID': task_id})
    
    return response.get('Item')

def lambda_handler(event, context):
    # Parse the task ID from the request
    task_id = event['pathParameters']['id']
    
    # Retrieve the task by its ID
    task = retrieve_task_by_id(task_id)
    
    # Return the task if found, or an error message if not found
    if task:
        return {
            'statusCode': 200,
            'body': json.dumps(task)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Task not found')
        }
