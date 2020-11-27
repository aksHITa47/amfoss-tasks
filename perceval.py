import base64
from perceval.backends.core.git import Git
from github import Github
from pprint import pprint
import json
# Github username
username = input("Enter the organization name:")
# pygithub object
g = Github()
data = []
# get that user by username
user= g.get_user(username)
for repo in user.get_repos():
    print(repo)
    repo_url = 'https://github.com/amfoss/repo.git'#URL of one repo at a time 
    repo_dir = '/tmp/cms.git' #directory to clone the repo
    git= Git(uri=repo_url,gitpath=repo_dir)
    for commit in git.fetch():
        data.append(commit)
      # pyob=json.loads(commit)
with open("commits.json", "w") as write_file:
        json.dump(data, write_file)
       

       
