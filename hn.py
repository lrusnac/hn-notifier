import requests
import json
from google.oauth2 import service_account
from fs.googledrivefs import GoogleDriveFS
import os

GOOGLE_DRIVE_SERVICE_ACCOUNT = json.loads(os.environ.get('GOOGLE_DRIVE_SERVICE_ACCOUNT', ''))
NUM_STORIES = 10
BASE_URL_HN_API = 'https://hacker-news.firebaseio.com'

READ_STORIES = 'read_stories'
NEW_STORIES = 'new_stories'

BASE_PATH_GOOGLE_DRIVE = 'datastores/hn/'

g_credentials = service_account.Credentials.from_service_account_info(GOOGLE_DRIVE_SERVICE_ACCOUNT)
fs = GoogleDriveFS(credentials=g_credentials)

response = requests.get(f'{BASE_URL_HN_API}/v0/topstories.json')
response.raise_for_status()
top_stories = response.json()[:NUM_STORIES]

with fs.open(f'{BASE_PATH_GOOGLE_DRIVE}{READ_STORIES}') as f:
    read_stories = f.read().splitlines()[:100]

new_top_stories = [str(story) for story in top_stories if str(story) not in read_stories]

if len(new_top_stories) > 0:
    with fs.open(f'{BASE_PATH_GOOGLE_DRIVE}{READ_STORIES}', 'w') as f:
        f.write('\n'.join(read_stories + new_top_stories))

    with fs.open(f'{BASE_PATH_GOOGLE_DRIVE}{NEW_STORIES}', 'a') as f:
        f.write('\n'.join(new_top_stories) + '\n')
