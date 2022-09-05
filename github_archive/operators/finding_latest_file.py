from datetime import datetime, timedelta
from github_archive.conf.github_archive_conf import GithubArchiveConf


def generate_path(previous_date_hr):
    base_url = GithubArchiveConf.SOURCE_URL
    previous_date = "-".join(previous_date_hr.split("-")[:-1])
    current_batch = (
        datetime.strptime(previous_date, "%Y-%m-%d") + timedelta(days=1)
    ).strftime("%Y-%m-%d")
    path_list = [
        base_url + current_batch + "-" + str(i) + ".json.gz" for i in range(1, 2)
    ]
    return path_list


if __name__ == "__main__":
    generate_path("2021-10-11")
