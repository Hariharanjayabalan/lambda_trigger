import time
from datetime import  datetime,timedelta
from github_archive.conf.github_archive_conf import GithubArchiveConf



def generate_path(previous_date):
    base_url=GithubArchiveConf.SOURCE_URL
    current_batch = (datetime.strptime(previous_date, '%Y-%m-%d')+timedelta(days=1)).strftime('%Y-%m-%d')
    path_list=[base_url+current_batch+'-'+str(i)+'.json.gz' for i in range(1,24)]
    return path_list
    
generate_path('2021-10-11')