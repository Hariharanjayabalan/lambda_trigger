import requests
import sys


def read_data(path):
    response = requests.request("GET", path, verify=False)
    if response.status_code == 200:
        print(f"File present in the {path} has been downloaded sucessfully")
        return response.content
    else:
        print("Issue in downloading the file")
        sys.exit(1)


read_data("https://data.gharchive.org/2015-01-01-15.json.gz")
