from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

secrets = json.load(open(
    'C:/Users/lenovo/Documents/GitHub/Hello-World/Twitter_API/secrets.json', 'r'))


#consumer key, consumer secret, access token, access secret.
ckey = secrets['CONSUMER_KEY']
csecret = secrets['CONSUMER_SECRET']
atoken = secrets['ACCESS_TOKEN']
asecret = secrets['ACCESS_SECRET']


class listener(StreamListener):

    def on_data(self, data):
        # print(data)
        all_data = json.loads(data)
        # json.dump(all_data,open('sample_tweet.json','w'))
        tweet = all_data['text']
        print(tweet)
        # print(all_data.keys())
        return(True)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["100DaysofCode"])
