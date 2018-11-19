## Local setup

### Prerequisites:

1. Download [DynamoDB (Downloadable version)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)

1. Install virtualenv: `pip install virtualenv`

1. Install dependencies `pip install -r requirements.txt`

### Setup environment

1. Run DynamoDB Local
   `java -D"java.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar -port 8000`

1. Configure AWS `aws configure`

```
AWS Access Key ID [None]: fakeMyKeyId
AWS Secret Access Key [None]: fakeSecretAccessKey
Default region name [None]: us-west-2
Default output format [None]: json
```

[The full list of default region ids is here](https://docs.aws.amazon.com/general/latest/gr/rande.html)

Config files are here: `C:\\Users\\UserName\\.aws`

3. See tables:

`aws dynamodb list-tables --endpoint-url http://localhost:8000`

## Guide

### Working with virtualenv

1. Install `pip install virtualenv`
1. Activate `./env/Scripts/activate`
1. Deactivate `./env/Scripts/deactivate`
1. Freeze `pip freeze > requirements.txt`
1. Install from virtualenv `pip install -r requirements.txt`

### Resources:

- [Boto3 DynamoDB docs](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)
- [DynamoDb docs](https://docs.aws.amazon.com/en_us/amazondynamodb/latest/developerguide/Introduction.html)
