import requests
import json
from github import Github
g = Github()
user = g.get_user('dimagamera')
for repo in user.get_repos():
  print(repo)
r = requests.get('https://api.github.com/search/users?q=location:ukraine').json()
for item in r['items']:
  print("https://github.com/"+item['login'])
