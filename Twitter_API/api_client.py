import tweepy
import time
import webbrowser
import json

secrets = json.load(open('C:/Users/lenovo/Documents/GitHub/Hello-World/Twitter_API/secrets.json', 'r'))

consumer_key = secrets['CONSUMER_KEY']
consumer_secret = secrets['CONSUMER_SECRET']
callback_uri = 'oob' #

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()

webbrowser.open(redirect_url)

user_pin_input = input('What\'s The Pin Code ? ')
print(user_pin_input)

auth.get_access_token(user_pin_input)
print(auth.access_token, auth.access_token_secret)

api = tweepy.API(auth)
me = api.me()

print(me.screen_name) # username :> codewithlenny
