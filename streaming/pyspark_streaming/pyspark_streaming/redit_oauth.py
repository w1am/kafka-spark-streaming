import requests
from requests.auth import HTTPBasicAuth
from rich import print
import pandas as pd
import reddit_streaming.config as config

# Get authentication info
client_auth = HTTPBasicAuth(config.REDDIT_CLIENT_ID, config.REDDIT_CLIENT_SECRET)
post_data = {"grant_type": "password", "username": config.REDDIT_USERNAME, "password": config.REDDIT_PASSWORD}

headers = {
    "User-Agent": "A reddit automation script 1.1 by William"
}

auth_response = requests.post(
    "https://www.reddit.com/api/v1/access_token",
    auth=client_auth,
    data=post_data,
    headers=headers
)

if (auth_response.status_code == 200):
    token = auth_response.json()['access_token']

    headers = { **headers, **{"Authorization": f'bearer {token}'} }

    # Get the websocket endpoint
    ws_response = requests.get("https://oauth.reddit.com/api/v1/live/thread/about", headers=headers)

    print(ws_response.json())

    # Get all new posts from reddit
    posts_response = requests.get("https://oauth.reddit.com/r/python/new", headers=headers)

    df = pd.DataFrame()

    rows = []

    for post in posts_response.json()['data']['children']:
        post = post['data']

        rows.append({
            'title': post['title'],
            'score': post['score'],
            'id': post['id'],
            'url': post['url'],
            'comms_num': post['num_comments'],
            'created': post['created'],
            'body': post['selftext']
        })

    df = pd.concat([pd.DataFrame(rows)], ignore_index=True)

    # Print all items in dataframe
    print(df)