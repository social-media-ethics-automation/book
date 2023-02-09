#!/usr/bin/env python
# coding: utf-8

# # Demo: Only positive news
# 
# Let's look at something we could try to do to improve the mental health for our users: Only show positive news!
# 
# We'll use sentiment analysis again, but this time we'll do a search for news from a news account, but only display the tweets with a positive sentiment.
# 
# Would this actually improve someone's mental health? It's hard to say! But we can see something that we might try out if we wanted to improve mental health of our users.

# ## Normal Tweepy Set-Up

# In[1]:


# make sure tweepy library is installed
import tweepy


# (optional) use the fake version of tweepy, so you don’t have to use real twitter developer access passwords

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


# ## Load sentiment analyis code

# In[5]:


import nltk
nltk.download(["vader_lexicon"])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# ## Code to search and display news tweets
# Now let's make code that will do a search for news tweets (tweets from a fake_news_site), and display all of them. We will then make a modified version below to compare the results.

# In[6]:


query = 'from:fake_news_site'
tweets = client.search_recent_tweets(query=query, max_results=10)

# go through each tweet
for tweet in tweets.data:
    print(tweet.text)
    print()


# ## Search through tweets and only display good news
# Now we will make a different version of the code that computes the sentiment of each tweet and only displays the ones with positive sentiment.

# In[7]:


query = 'from:fake_news_site'
tweets = client.search_recent_tweets(query=query, max_results=20)

# go through each tweet
for tweet in tweets.data:
    
    #calculate sentiment
    tweet_sentiment = sia.polarity_scores(tweet.text)["compound"]

    if(tweet_sentiment > 0):
        print(tweet.text)
        print()


# ## Try it out on real twitter
# If you want, you can skip the fake_tweepy step and try it out on real twitter with a query like "from:npr", "from:msnbc", "from:cnn", etc.
# 
# Did it work like you expected?
# 
# You can also only show negative sentiment tweets (sentiment < 0) if you want to see only bad news.
