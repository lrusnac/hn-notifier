import requests
import json
from google.oauth2 import service_account
from fs.googledrivefs import GoogleDriveFS
import os

GOOGLE_DRIVE_SERVICE_ACCOUNT = json.loads(os.environ.get('GOOGLE_DRIVE_SERVICE_ACCOUNT', ''))
NUM_STORIES = 10
BASE_URL_HN_API = 'https://hacker-news.firebaseio.com'

NEW_STORIES = 'new_stories'

BASE_PATH_GOOGLE_DRIVE = 'datastores/hn/'

LEO_EMAIL = os.environ.get('LEO_EMAIL', '')
MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY', '')
MAILGUN_SANDBOX = os.environ.get('MAILGUN_SANDBOX', '')

g_credentials = service_account.Credentials.from_service_account_info(GOOGLE_DRIVE_SERVICE_ACCOUNT)
fs = GoogleDriveFS(credentials=g_credentials)

with fs.open(f'{BASE_PATH_GOOGLE_DRIVE}{NEW_STORIES}') as f:
    new_stories = f.read().splitlines()

mail_text = ''
for story in new_stories:
    full_story = requests.get(f'{BASE_URL_HN_API}/v0/item/{story}.json').json()
    if 'deleted' not in full_story and 'title' in full_story:
        if 'url' in full_story:
            entry = f'{story} - {full_story["title"]} - {full_story["url"]}\n'
        else:
            entry = f'{story} - {full_story["title"]} - https://news.ycombinator.com/item?id={story}\n'
        
        mail_text += entry

if mail_text != '':
    print(mail_text)
    
    response = requests.post(
        f'https://api.mailgun.net/v3/{MAILGUN_SANDBOX}.mailgun.org/messages',
        auth=('api', MAILGUN_API_KEY),
        data={
            'from': f'HN notifier <postmaster@{MAILGUN_SANDBOX}.mailgun.org>',
            'to': f'Leonid <{LEO_EMAIL}>',
            'subject': '[HN] new stories',
            'text': mail_text
        }
    )
    
    response.raise_for_status()

with fs.open(f'{BASE_PATH_GOOGLE_DRIVE}{NEW_STORIES}', 'w') as f:
    f.write('')
