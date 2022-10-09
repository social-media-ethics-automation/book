#!/usr/bin/env python
# coding: utf-8

# # Demo & Practice: Tweet Sources
# 
# Let's now try out some code to see what device people are using to post their Tweets. We can't look at Donald Trump's Tweets, since his account was [suspended in January 2021 for inciting violence](https://blog.twitter.com/en_us/topics/company/2020/suspension), but we can look at other accounts and think about authenticity might mean for different types of accounts.

# ## Log into Twitter
# These are our normal steps get Tweepy loaded and logged into Twitter

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


# ## Load tweets with the source (what device they were posted on)
# 
# The code below searches for recent tweets from an account, and then does a loop though all the tweets, printing out the source device of the Tweet and then the tweet itself. Hopefully most of the code looks familiar from last chapter when we covered loops over social media data.
# 
# Try searching for recent tweets from different types of accounts, like: 
# - News organizations and other corporations, like: cnn
# - Politicians, like: BarackObama, JoeBiden, 
# - Other celebrities, like MarkRuffalo, selenagomez
# 
# To do this:
# - put in your special Twitter bot passwords
# - skip the fake_tweepy step above
# - take the first line of the code below and replace `'from:fake_celebrity'` with something like `'from:cnn'`

# In[5]:


# choose account to search from (save in query variable)
query = 'from:fake_celebrity'

# search tweets with the query, also include the "source" info, and allow up to 20 results
# note: "search_recent_tweets" searches tweets from the last 7 days
tweets = client.search_recent_tweets(query=query, tweet_fields=["source"], max_results=20)

# loop through each of the tweets (saved in tweets.data)
for tweet in tweets.data:
    print("Tweet Source: " + tweet.source) # print the source publishing the tweet
    print("   Tweet: " + tweet.text) # print the text of the tweet
    print() # print a blank line


# ## Reflecting on what you find
# In our fake_celebrity example, you will see that some of the tweets are posted from a Social Media Manager, a program that helps people schedule posts and otherwise manage their social media accounts. 
# 
# Reflect on what you feel that social media manager means for authenticity for different types of accounts.
