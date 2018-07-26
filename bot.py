import tweepy, time

REPLIED_TO = 'replied_to_log.txt'

# Create a config.ini file and save your Twitter API keys on lines 1-4
with open('config.ini','r') as config:
  tokens = config.readlines()
  TW_CONSUMER_KEY = tokens[0].rstrip()
  TW_CONSUMER_SECRET = tokens[1].rstrip()
  TW_ACCESS_KEY = tokens[2].rstrip()
  TW_ACCESS_SECRET = tokens[3].rstrip()

def authenticate_twitter():
  print('Authenticating twitter...')
  auth = tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
  auth.set_access_token(TW_ACCESS_KEY, TW_ACCESS_SECRET)
  twitter = tweepy.API(auth)
  print('Twitter authenticated.\n')
  return twitter

# Helper functions you may or may not need depending on what your bot does

  # If your bot replies to tweets you may want to record that you've replied to a paticular tweet in a local log so you don't reply to that tweet again
def record_replied_to(tweet):
    with open(replied_to, 'a') as f:
        f.write(str(tweet.id) + '\n')

  # Checks your logs to see if you've already replied to this tweet.
def is_replied_to(tweet):
     with open(REPLIED_TO, 'r') as f:
        if str(tweet.id) in f.read():
            return True
        else:
            return False


# Define some functions here to do whatever the heck it is your bot is supposed to do.


def tweet(twitter, text):
  #you can tweet with a photo or just text by using one of the two following lines
  twitter.update_with_media("photo.png", text)
  twitter.update_status(text)

def main():
    twitter = authenticate_twitter()
    while True:
        # Call your functions here to make your bot do its bot thing


        # You don't want your bot to do anything non-stop because it's spammy and Twitter will lock your account so this sleeps for an hour.
        time.sleep(1200)

if __name__ == '__main__':
  main()
