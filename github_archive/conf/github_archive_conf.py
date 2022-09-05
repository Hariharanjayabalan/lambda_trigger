from datetime import datetime
import time


class GithubArchiveConf:
    BUCKET_NAME = "hari-learn"
    FILE_NAME = "github_archive"
    HOME_PATH = "github/download/"
    SOURCE_URL = "https://data.gharchive.org/"
    INITIAL_LOAD_START_DT = "2015-09-01-01"
    DYNAMODB_TABLE_NAME = "gharchive"
    DYNAMODB_PARAM = {
        "TABLE_ID": {"N": "HASH"},
        "FILE_NAME": {"S": "HASH"},
        "FILE_CYLE_DT": {"N": "RANGE"},
        "LAST_MODIFIED_DATE": {"N": "RANGE"},
    }
    DYNAMODB_KEY_TYPE = [
        {"AttributeName": "TABLE_ID", "KeyType": "HASH"},
        {"AttributeName": "FILE_NAME", "KeyType": "RANGE"},
    ]

    DYNAMODB_ATTRIBUTE_TYPE = [
        {"AttributeName": "TABLE_ID", "AttributeType": "N"},
        {"AttributeName": "FILE_NAME", "AttributeType": "S"},
    ]

    DYNAMODB_FILTER_CONDITION = {
        "TABLE_ID": {"N": "1"},
        "FILE_NAME": {"S": "gharchive"},
    }

    DYNAMODB_WRITE_CONDITION = {
        "TABLE_ID": {"N": "1"},
        "FILE_NAME": {"S": "gharchive"}
    }

    @staticmethod
    def epoch_time():
        pattern = "%Y-%m-%d %H:%M:%S"
        ts = datetime.strftime(datetime.now(), pattern)
        return int(time.mktime(time.strptime(ts, pattern)))
