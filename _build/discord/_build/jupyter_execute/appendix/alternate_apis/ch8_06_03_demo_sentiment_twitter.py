#!/usr/bin/env python
# coding: utf-8

# # Demo: Sentiment Analysis on Twitter
# 
# Now let's try using sentiment analysis (and loop variables) on Twitter:
# 
# We'll start by doing our normal steps to load tweepy (or fake tweepy)
# 
# ## Tweepy Setup

# In[1]:


import tweepy


# (optional) make a fake twitter connection with the fake_tweepy library
# 
# For testing purposes, we’ve added this line of code, which loads a fake version of tweepy, so it wont actually connect to twitter. If you want to try to actually connect to twitter, don’t run this line of code.

# In[2]:


get_ipython().run_line_magic('run', '../../fake_tweepy/fake_tweepy.ipynb')


# In[3]:


# Load all your developer access passwords into Python
# TODO: Put your twitter account's special developer access passwords below:
bearer_token = "n4tossfgsafs_fake_bearer_token_isa53#$%$"
consumer_key = "sa@#4@fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"


# In[4]:


# Give the tweepy code your developer access passwords so
# it can perform twitter actions
client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)


# ## Sentiment Analysis
# ### load sentiment analysis library and make analyzer

# In[5]:


import nltk
nltk.download(["vader_lexicon"])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# ### loop through tweets, finding average sentiment
# We can now combine our previous examples of looping through tweets with what we just learned of sentiment analysis and looping variables to find the average sentiment of a set of tweets.

# In[6]:


query = '"cute cat"'
tweets = client.search_recent_tweets(query=query, max_results=10)

num_tweets = 0
total_sentiment = 0

# go through each tweet
for tweet in tweets.data:
    
    #calculate sentiment
    tweet_sentiment = sia.polarity_scores(tweet.text)["compound"]
    num_tweets += 1
    total_sentiment += tweet_sentiment

    print("Sentiment: " + str(tweet_sentiment))
    print("   Tweet: " + tweet.text)
    print()


average_sentiment = total_sentiment / num_tweets
print("Average sentiment was " + str(average_sentiment))


# We can now see the average sentiment of a set of tweets based on our search of twitter! 
# 
# If you use your twitter bot keys, you can change the `query` to be whatever twitter search you want and see whether people are tweeting positively or negatively about it. 
# 
# _note: You can change `max_results=10` to go up to 100 to get more tweets at a time to find the average of_
