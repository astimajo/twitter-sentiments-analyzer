import tweepy
from textblob import TextBlob

#def execute(topic): #topic #return

    #API key and API secret key
auth = tweepy.OAuthHandler("fUEl1vqhD3FO37I12c0mXfQpo","THQXyMK5YZQ66sGPizhM3tFOCETRhQg8Rm1AChPOQGntMo5A1g")

    #Acess Token and Access token secret
auth.set_access_token("1149663947676479488-Fj02BUZShgRBJbPkkw2hFHKj4BvRmk","FsUFTot9IaDRPmGPmO4jPsStMSKJT8dv980GgfatOW1k3")

    #calling the accessed twitter API
api = tweepy.API(auth)
    #Fetching tweets which contain machine learning keyword

tweets = api.search("machine learning")

for item in tweets:
    tweet = TextBlob(item.text)
        
    if tweet.sentiment.polarity > 0:
        results = str("Positive Tweet" + "\n" + str(tweet) +"\n"+ "— — — — — — — — — — \n")
            
        print(results)
        
    elif tweet.sentiment.polarity < 0:
        results = str("Negative Tweet" + "\n" + str(tweet) + "\n" + "— — — — — — — — — — \n") 
            
        print(results)
    else:
        results = str("Neutral Tweet" + "\n" + str(tweet) + "\n" + "— — — — — — — — — — \n")
            
        print(results)



    



