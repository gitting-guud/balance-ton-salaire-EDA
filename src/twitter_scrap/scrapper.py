import os
from pathlib import Path

import tweepy

from config import settings
from utils import write_jsonlines

limit = 100
Path(settings.OUTPUTDIR).mkdir(exist_ok=True, parents=True)

query = "#balancetonsalaire -is:retweet lang:fr"
client = tweepy.Client(bearer_token=settings.BEARER_TOKEN)
tweets = tweepy.Paginator(
    client.search_recent_tweets,
    query=query,
    tweet_fields=["context_annotations", "created_at", "geo", "author_id", "source"],
    max_results=100,
).flatten(limit=10000)

data = []
for tweet in tweets:
    data.append(
        {
            "id": tweet.id,
            "text": tweet.text,
            "created_at": str(tweet.created_at),
            "geo": tweet.geo,
            "author_id": tweet.author_id,
            "source": tweet.source,
        }
    )
write_jsonlines(data=data, path=os.path.join(settings.OUTPUTDIR, "tweets.jsonlines"))
