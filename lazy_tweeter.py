# Generate a tweet based on a user's previous tweets

from twython import Twython
from markov import Markov
import ConfigParser, re

config = ConfigParser.RawConfigParser()
config.read('lazy_tweeter.cfg')

KEY = config.get('appinfo', 'key')
TOKEN = config.get('appinfo', 'token')

def main():
    twitter = Twython(KEY, access_token=TOKEN)
    try:
        tweets = twitter.get_user_timeline(screen_name=raw_input("twitter username: "), count=200)
    except:
        print "User does not exist."
        return
    try:
        count = int(raw_input("number of tweets to generate: "))
        text = ""
        for tw in tweets:
            text += re.sub("https?:\/\/([^\s]+)", "", tw['text']) + ". "
        mk = Markov(text)
        sentences = ""
        for i in range(0, count):
            print mk.sentence()

    except:
        print "Please enter a valid number."

if __name__ == '__main__':
    main()