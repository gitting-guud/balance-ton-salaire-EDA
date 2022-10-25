import os
from pathlib import Path

import tweepy

from config import settings
from utils import write_jsonlines

limit = 10000
Path(settings.OUTPUTDIR).mkdir(exist_ok=True, parents=True)

query = "#balancetonsalaire -is:retweet lang:fr"
client = tweepy.Client(bearer_token=settings.BEARER_TOKEN)
tweets = tweepy.Paginator(
    client.search_recent_tweets,
    query=query,
    tweet_fields=["context_annotations", "created_at", "geo", "author_id", "source"],
    max_results=100,
).flatten(limit=limit)

data = []
for tweet in tweets:
    data.append(
        {
            "id": tweet.id,
            "text": tweet.text,
            "created_at": str(tweet.created_at),
            "author_id": tweet.author_id,
            "source": tweet.source,
        }
    )

users = []
start_index = 0
chunks = 100
for i in range(0, len(data), chunks):
    users.extend(
        client.get_users(
            ids=[row["author_id"] for row in data[start_index : start_index + chunks]]
        ).data
    )
    start_index += chunks

data = [
    {**row, "location": user.location, "username": user.username} for row, user in zip(data, users)
]
write_jsonlines(data=data, path=os.path.join(settings.OUTPUTDIR, "tweets.jsonlines"))
