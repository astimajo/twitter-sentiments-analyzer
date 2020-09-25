import tweepy
from textblob import TextBlob

def execute(topic): #topic #return

    #API key and API secret key
    auth = tweepy.OAuthHandler("fUEl1vqhD3FO37I12c0mXfQpo","THQXyMK5YZQ66sGPizhM3tFOCETRhQg8Rm1AChPOQGntMo5A1g")

    #Acess Token and Access token secret
    auth.set_access_token("1149663947676479488-Fj02BUZShgRBJbPkkw2hFHKj4BvRmk","FsUFTot9IaDRPmGPmO4jPsStMSKJT8dv980GgfatOW1k3")

    #calling the accessed twitter API
    api = tweepy.API(auth)
    #Fetching tweets which contain machine learning keyword
    tweets = api.search(topic, count=5, tweet_mode='extended') 

    for item in tweets:
        tweet = TextBlob(item.text)
        if tweet.sentiment.polarity > 0:
            return ("Positive Tweet" + "\n" + str(tweet) +"\n"+ "— — — — — — — — — — \n")
        
        elif tweet.sentiment.polarity < 0:
            return ("Negative Tweet" + "\n" + str(tweet) + "\n" + "— — — — — — — — — — \n") 
        else:
            return ("Neutral Tweet" + "\n" + str(tweet) + "\n" + "— — — — — — — — — — \n")

    

    



