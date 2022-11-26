import tweepy


def TWEET(
    TWEET_TEXT="", CONSUMER_KEY="", CONSUMER_SECRET="", ACCESS_KEY="", ACCESS_SECRET=""
):

    if TWEET_TEXT == "":
        print("No text to tweet")
    if CONSUMER_KEY == "":
        print("No consumer key")
    if CONSUMER_SECRET == "":
        print("No consumer secret")
    if ACCESS_KEY == "":
        print("No access key")
    if ACCESS_SECRET == "":
        print("No access secret")
    else:
        CLIENT = tweepy.Client(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_KEY,
            access_token_secret=ACCESS_SECRET,
        )

        MESSAGE = CLIENT.create_tweet(text=TWEET_TEXT)
        print("Tweeted Successfully with id : ", MESSAGE.data["id"])
