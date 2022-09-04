from github_archive.services.s3_service import S3
from github_archive.services.dynamodb import Dynamodb
from github_archive.conf.github_archive_conf import GithubArchiveConf



def run():
    db_set=Dynamodb()
    print(type([GithubArchiveConf.DYNAMODB_KEY_TYPE]))
    print('hato')
    print(GithubArchiveConf.DYNAMODB_ATTRIBUTE_TYPE)
    db_set.create_table(table_name=GithubArchiveConf.DYNAMODB_TABLE_NAME,
    key_schema=[GithubArchiveConf.DYNAMODB_KEY_TYPE],
    attribute_definition=[GithubArchiveConf.DYNAMODB_ATTRIBUTE_TYPE],billing_mode="PAY_PER_REQUEST")

run()