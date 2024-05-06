import json
import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'TodoList'  # Update this with your DynamoDB table name

def delete_todo(task_id):
    print("Task ID:", task_id)  # Add this line for debugging
    # Delete the specified to-do item from the DynamoDB table
    table = dynamodb.Table(table_name)
    response = table.delete_item(
        Key={'ID': task_id}
    )
    return response


def lambda_handler(event, context):
    # Parse the task ID from the request
    task_id = str(event['pathParameters']['id'])  # Extract the ID from the URL path and convert to string
    
    # Delete the to-do item
    response = delete_todo(task_id)
    
    # Return a response indicating success or failure
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Todo item deleted successfully')
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to delete todo item')
        }
