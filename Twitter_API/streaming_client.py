from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sys

secrets = json.load(open(
    'C:/Users/Lennylen/Documents/GitHub/Hello-World/Twitter_API/secrets.json', 'r'))


#consumer key, consumer secret, access token, access secret.
ckey = secrets['CONSUMER_KEY']
csecret = secrets['CONSUMER_SECRET']
atoken = secrets['ACCESS_TOKEN']
asecret = secrets['ACCESS_SECRET']


class listener(StreamListener):

    def __init__(self, output_file=sys.stdout):
        super().__init__()
        self.output_file = output_file
        self.counter = 0
        self.limit = 10
        # self.tweet_list = list()

    def on_data(self, data):
        # print(data)
        all_data = json.loads(data)
        # json.dump(all_data,open('sample_tweet.json','w'))
        tweet = all_data['text'].strip()
        # self.tweet_list.append(tweet)
        print(tweet, file=self.output_file)
        # print(all_data.keys())
        self.counter += 1
        if self.counter < self.limit:
            return True
        else:
            twitterStream.disconnect()
            # return self.tweet_list

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

output = open('stream_output.txt', 'w')
listen = listener(output_file=output)

twitterStream = Stream(auth, listen)
twitterStream.filter(track=["spacex"], languages=['en'])
