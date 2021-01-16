from twitter import Twitter, OAuth
import config

auth = OAuth(
    consumer_key=config.API_KEY,
    consumer_secret=config.API_SECRET,
    token=config.ACCESS_TOKEN,
    token_secret=config.ACCESS_TOKEN_SECRET
)
# twitter_stream = TwitterStream(auth=auth)
# stream=twitter_stream.statuses.sample()
# for msg in stream:
#     print(msg)

t = Twitter(auth=auth)

# first tweet
print(t.statuses.home_timeline()[0]["text"])
