import boto3
import tweepy

dynamodb = boto3.resource('dynamodb')
postsTable = dynamodb.Table('posts')


def tweet(message):
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    api.update_status(message)


def putPost(post):
    postsTable.put_item(Item=post)


def lambda_handler(event, context):
    for record in event['Records']:
        id = record['dynamodb']['NewImage']['id']['S']
        msg = record['dynamodb']['NewImage']['message']['S']
        putPost({'id': id, 'message': msg, 'status': 'OK'})
        tweet(msg)
