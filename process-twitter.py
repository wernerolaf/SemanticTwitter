from twitter import *
try:
    f=open("/home/olaf/twitter2","r")
    f.readline()
    API_KEY = f.readline().strip()
    f.readline()
    API_SECRET = f.readline().strip()
    f.readline()
    ACCESS_TOKEN = f.readline().strip()
    f.readline()
    ACCESS_TOKEN_SECRET = f.readline().strip()
    f.readline()
    BEARER_TOKEN= f.readline().strip()
except:
    print("no file found")
finally:
    f.close()

auth = OAuth(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    token=ACCESS_TOKEN,
    token_secret=ACCESS_TOKEN_SECRET
)
# twitter_stream = TwitterStream(auth=auth)
# stream=twitter_stream.statuses.sample()
# for msg in stream:
#     print(msg)

t = Twitter(auth=auth)

# first tweet
print(t.statuses.home_timeline()[0]["text"])