import csv, tweepy, os
from textblob import TextBlob
import new_file 

#script by A. Ablazo, © 2017

#modifications done by A. Timajo.

def tweetscraper(filename, query): #required: .csv for filename
    class Conn:
        '''
            twitter credentials class
        '''
        def __init__(self, *args):
            self.ck =     #consumer key
            self.cs =     #consumer secret
            self.at =     #access token
            self.ats =    #access token secret
    
        def tweep_creds(self):
            auth = tweepy.OAuthHandler(self.ck, self.cs)
            auth.set_access_token(self.at, self.ats)
            return tweepy.API(auth, wait_on_rate_limit=True)

    #initialize api w/ twitter api credentials object
    api = Conn().tweep_creds()

    #function to add language to csv row
    def add_language(query_word, twt_lmt):
        for tweet in list(tweepy.Cursor(api.search, q=query_word).items(twt_lmt)):
        
            tweet = TextBlob(tweet.text)
        
            language = tweet.detect_language()

        return language

    #function to gather polarity of a specific tweet to estimate sentiments
    def add_sentiment(query_word,twt_lmt):
        for tweet in list(tweepy.Cursor(api.search, q=query_word).items(twt_lmt)):
        
            tweet = TextBlob(tweet.text)
        
            if tweet.sentiment.polarity > 0:
                sentiment = str("Positive_Tweet")

            elif tweet.sentiment.polarity < 0:
                sentiment = str("Negative_Tweet")

            else:
                sentiment = str("Neutral_Tweet")

        return sentiment

    # gather tweets using the initialized twitter api. 
    def gather_tweets_sentiments(query_word,twt_lmt, sentiment, language):
        counter = 0
        for tweet in list(tweepy.Cursor(api.search, q=query_word).items(twt_lmt)):
            csvWriter.writerow([tweet.text, tweet.user.screen_name, tweet.created_at, tweet.user.location, tweet.retweet_count, tweet.favorite_count, sentiment, language])
            counter = counter + 1
        return counter


    # tweet filename
    global csvWriter
    new_file.create_file(filename)
    namefile = filename
    dir_name = os.path.dirname(os.path.abspath(__file__))
    file_dir = open(dir_name+"/"+namefile,'r', encoding='ISO-8859-1')
    csvFile = open(dir_name+"/"+namefile,'a')
    csvreader = csv.reader(file_dir)
    csvWriter = csv.writer(csvFile)
    row_cnt = sum(1 for row in file_dir)


    q_words = query # enter query words here (separate by spaces)
    q_words = q_words.split()

    t_lmt = tweet_limit = 100 #adjust tweet limit accordingly
    limit_num = tweet_limit * len(q_words)
    new_rc = row_cnt

    for q in q_words:
        new_rc += gather_tweets_sentiments(q, t_lmt, add_sentiment(q, t_lmt), add_language(q, t_lmt))


    print("initial rows: %s\ngathered rows: %s"%(row_cnt,new_rc-row_cnt))
    csvFile.close()

    return
