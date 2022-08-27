import sys
import boto3
import os
from github_archive.conf.github_archive_conf import GithubArchiveConf  

class S3:
    def __init__(self):
        os.environ.setdefault('AWS_PROFILE','lambda_profile')
        self.s3_client=boto3.client('s3', verify=False)
    
    def s3_list_buckets(self):
        bucket=self.s3_client.list_buckets()
        print(bucket)

    def s3_write_content(self,content,key):
        self.s3_client.put_object(Bucket=GithubArchiveConf.BUCKET_NAME,Body=content.encode('utf-8'),Key=GithubArchiveConf.HOME_PATH+key)

if __name__== '__main__': 
    a=S3()
    a.s3_write_content('hari','test.txt')
