import boto3
from github_archive.conf.github_archive_conf import GithubArchiveConf
from github_archive.operators.request_data import read_data
import warnings

warnings.filterwarnings("ignore")


class S3:
    def __init__(self):
        self.s3_client = boto3.client("s3", verify=False)

    def s3_list_buckets(self):
        bucket = self.s3_client.list_buckets()
        print(bucket)

    def s3_write_content(self, content, key):
        print(f"Starting to write {GithubArchiveConf.HOME_PATH + key}")
        self.s3_client.put_object(
            Bucket=GithubArchiveConf.BUCKET_NAME,
            Body=content,
            Key=GithubArchiveConf.HOME_PATH + key,
        )


if __name__ == "__main__":
    s3_object = S3()
    s3_object.s3_list_buckets()
    response = read_data("https://data.gharchive.org/2022-09-02-1.json.gz")
