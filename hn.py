#!/usr/bin/env python
# -*- coding: utf-8 0*0

import requests

number_of_stories = 5
base_url = 'https://hacker-news.firebaseio.com'
passed_stories_file = 'old_stories.txt'

with open(passed_stories_file) as f:
    passed_stories = f.read().splitlines()

response = requests.get(base_url + '/v0/topstories.json')
best_x_stories =  response.json()[0:number_of_stories]

for s in best_x_stories:
    if str(s) not in passed_stories:
        passed_stories.append(s)
        
        with open(passed_stories_file, 'a') as f:
            f.write(str(s) + '\n')

