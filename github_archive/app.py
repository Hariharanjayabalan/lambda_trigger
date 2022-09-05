from github_archive.services.s3_service import S3
from github_archive.conf.github_archive_conf import GithubArchiveConf
from github_archive.operators.bookmarking_file import (
    run_db_create,
    read_latest_file,
    update_latest_file,
)
from github_archive.operators.finding_latest_file import generate_path
from botocore.errorfactory import ClientError
from github_archive.operators.request_data import read_data
import sys
import time
import warnings

warnings.filterwarnings("ignore")


def run(event=None, context=None):

    s3_obj = S3()
    # Calling create table
    try:
        run_db_create()
        print("Waiting to create table")
        time.sleep(10)
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceInUseException":
            print("Table already existing")
        else:
            print(e)
            sys.exit()

    # Reading dynamodb table
    response_date = read_latest_file()

    # passing the value to find path
    if "FILE_CYLE_DT" not in response_date:
        print("Running for Initial Date")
        download_path = generate_path(GithubArchiveConf.INITIAL_LOAD_START_DT)
    else:
        print("Running for Delta batch ", response_date["FILE_CYLE_DT"]["S"])
        download_path = generate_path(response_date["FILE_CYLE_DT"]["S"])

    # Passing value to download path
    for path in download_path:
        print(f"Downloading the file for the date {path}")
        response_down = read_data(path)
        s3_obj.s3_write_content(response_down, path.split("/")[3])

    # Updating the dynamodb
    update_latest_file(path.split("/")[3])


if __name__ == "__main__":
    print(run(None, None))
