from github_archive.services.s3_service import S3


def run():
    s3 = S3()
    s3.s3_write_content("hari", "test.txt")
