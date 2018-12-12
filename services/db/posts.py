import boto3
import datetime

dynamodb = boto3.resource(
    'dynamodb', region_name="us-west-2", endpoint_url="http://localhost:8001")


postsTable = dynamodb.Table('posts')


def putPost(post):
    postsTable.put_item(Item=post)


def getPost(id):
    response = postsTable.get_item(Key={
        'id': id
    })
    return response['Item']


def removePost(id):
    postsTable.delete_item(Key={
        'id': id
    })

# putPost({
#     'id': 'post1',
#     'user_id': 'user1',
#     'date_created': str(datetime.datetime.now())
# })

# print('getting item', getPost('post2'))


print(postsTable.creation_date_time)
