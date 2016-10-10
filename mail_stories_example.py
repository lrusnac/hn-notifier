#!/usr/bin/env python
# -*- coding: utf-8 0*0

import requests

base_url = 'https://hacker-news.firebaseio.com'
stories_file = 'stories.txt'

with open(stories_file) as f:
    meanwhile_stories = f.read().splitlines()

mail = ""

for s in meanwhile_stories:
	story = requests.get(base_url + '/v0/item/'+str(s)+'.json').json()

	if 'url' in story:
			msg = str(s) + '  -  ' + story['title'] + '  -  ' + story['url'] + '\n'
	else:
			msg = str(s) + ' - ' + story['title'] + '\n'
	msg = msg.encode('utf-8')

	mail = mail + msg

if mail is not "":
	# send the mail
	pass
 
with open(stories_file, 'w') as f:
	f.write('')

