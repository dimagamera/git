import requests
import json
from github import Github

main = int(input('1.username 2.country 3. language > '))

if main == 1:
	username = input('Enter username > ')
	g = Github()
	user = g.get_user('dimagamera')
	i = 0
	for repo in user.get_repos():
	    i +=1
	    print(repo)
	print('total count repositories: '+str(i))
elif main == 2:
	name_country = input('Enter name country > ')
	r = requests.get('https://api.github.com/search/users?q=location:'+ name_country).json()
	i = 0
	for item in r['items']:
		i +=1
		print("https://github.com/"+item['login'])
	print('total count users in '+name_country +': '+str(i))
elif main == 3:
	language = input('Enter language > ')
	r = requests.get('https://api.github.com/search/repositories?q=language:'+language+'&per_page=100').json()
	i = 0
	while i < 99:
		i+=1
		print(r['items'][i]['html_url'])
	i = i+1
	print('total count repositories '+language+': '+str(i))
