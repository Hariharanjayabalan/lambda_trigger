from inspect import Attribute


class GithubArchiveConf:
    BUCKET_NAME = "hari-redshift123"
    FILE_NAME = ""
    HOME_PATH = "github"
    SOURCE_URL = 'https://data.gharchive.org/'
    DYNAMODB_TABLE_NAME='gharchive'
    DYNAMODB_PARAM = {
        'TABLE_ID':{'N':'HASH'},
        'FILE_NAME':{'S':'HASH'},
        'FILE_CYLE_DT':{'N':'RANGE'},
        'LAST_MODIFIED_DATE':{'N':'RANGE'}
    }
    DYNAMODB_KEY_TYPE='{"AttributeName": "TABLE_ID", "KeyType": "HASH"},{"AttributeName": "FILE_NAME", "KeyType": "HASH"},{"AttributeName": "FILE_CYLE_DT", "KeyType": "RANGE"},{"AttributeName": "LAST_MODIFIED_DATE", "KeyType": "RANGE"},'

    DYNAMODB_ATTRIBUTE_TYPE='\
                {"AttributeName": "TABLE_ID", "AttributeType": "N"},\
                {"AttributeName": "FILE_NAME", "AttributeType": "S"},\
                {"AttributeName": "FILE_CYLE_DT", "AttributeType": "N"},\
                {"AttributeName": "LAST_MODIFIED_DATE", "AttributeType": "N"},'
    

