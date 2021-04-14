import requests
import json
from github import Github

main = int(input('1.username 2.country 3. language > '))

if main == 1:
	username = input('Enter username > ')
	g = Github()
	user = g.get_user('dimagamera')
	for repo in user.get_repos():
	    print(repo)
elif main == 2:
	name_country = input('Enter name country > ')
	r = requests.get('https://api.github.com/search/users?q=location:'+ name_country).json()
	for item in r['items']:
		print("https://github.com/"+item['login'])
elif main == 3:
	language = input('Enter language > ')
	r = requests.get('https://api.github.com/search/repositories?q=language:'+language+'&per_page=100').json()
	i = 0
	while i < 100:
		i+=1
		print(r['items'][i]['html_url'])
