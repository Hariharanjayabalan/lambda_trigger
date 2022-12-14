from github_archive.services.dynamodb import Dynamodb
from github_archive.conf.github_archive_conf import GithubArchiveConf


def run_db_create():
    db_set = Dynamodb()
    response = db_set.create_table(
        table_name=GithubArchiveConf.DYNAMODB_TABLE_NAME,
        key_schema=GithubArchiveConf.DYNAMODB_KEY_TYPE,
        attribute_definition=GithubArchiveConf.DYNAMODB_ATTRIBUTE_TYPE,
        billing_mode="PAY_PER_REQUEST",
    )
    return response


def read_latest_file():
    db_set = Dynamodb()
    response = db_set.retrive_table_data_using_get(
        table_name=GithubArchiveConf.DYNAMODB_TABLE_NAME,
        filter_condition=GithubArchiveConf.DYNAMODB_FILTER_CONDITION,
    )
    return response


def update_latest_file(FILE_CYLE_DT):
    db_set = Dynamodb()
    filter_condition = GithubArchiveConf.DYNAMODB_WRITE_CONDITION
    filter_condition["FILE_CYLE_DT"] = {"S": FILE_CYLE_DT}
    filter_condition["LAST_MODIFIED_DATE"] = {"N": str(GithubArchiveConf.epoch_time())}
    print(f"Updating the Dynamodb value to {filter_condition}")
    response = db_set.write_to_table(
        table_name=GithubArchiveConf.DYNAMODB_TABLE_NAME, write_value=filter_condition
    )
    return response


if __name__ == "__main__":
    print(update_latest_file())
