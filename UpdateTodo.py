import json
import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'TodoList'  # Update this with your DynamoDB table name

def update_todo(task_id, new_task):
    # Update the specified to-do item in the DynamoDB table
    table = dynamodb.Table(table_name)
    try:
        response = table.update_item(
            Key={'ID': task_id},
            UpdateExpression='SET Task = :t',
            ExpressionAttributeValues={':t': new_task}
        )
        return response
    except Exception as e:
        print(f"Error updating todo item: {e}")
        return None

def lambda_handler(event, context):
    # Parse the task ID and new task data from the request
    task_id = event['pathParameters']['id']
    new_task = json.loads(event['body'])
    
    # Update the to-do item
    response = update_todo(task_id, new_task)
    
    # Return a response indicating success or failure
    if response and response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Todo item updated successfully')
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to update todo item')
        }