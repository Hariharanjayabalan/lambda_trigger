import boto3
import subprocess
import os

class S3:
    def __init__(self):
        os.environ.setdefault('AWS_PROFILE','lambda_profile')
        self.s3_client=boto3.client('s3', verify=False)
    
    def s3_list_buckets(self):
        bucket=self.s3_client.list_buckets()
        print(os.environ.get('bucket'))

    def s3_write_content(self,bucket_name,content):
        pass


    

a=S3()
a.s3_list_buckets()
