import json, boto3

client = boto3.client('dynamodb')
TableName = 'cloudresumesam'

def lambda_handler(event, context):
    response = client.update_item(
        TableName='cloudresumesam',
        Key = {
            'visits': {'S': 'view-count'}
        },
        UpdateExpression = 'ADD Quantity :inc',
        ExpressionAttributeValues = {":inc" : {"N": "1"}},
        ReturnValues = 'UPDATED_NEW'
        )
        
    value = response['Attributes']['Quantity']['N']
    
    return {      
            'statusCode': 200,
            'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET' },
            'body': value }