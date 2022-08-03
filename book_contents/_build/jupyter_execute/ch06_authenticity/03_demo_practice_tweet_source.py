#!/usr/bin/env python
# coding: utf-8

# # Demo & Practice: Tweet Sources
# ### Set-up steps
# * Install the variable inspector!pip install lckr-jupyterlab-variableinspector
# * Install and import tweepy
# * Load login keys
# * Log in

# In[1]:


get_ipython().system('pip install lckr-jupyterlab-variableinspector')


# In[ ]:


get_ipython().system('pip install tweepy')
import tweepy


# In[ ]:


import my_bot_keys


# In[ ]:


client = tweepy.Client(
    bearer_token=my_bot_keys.bearer_token,
    consumer_key=my_bot_keys.consumer_key, consumer_secret=my_bot_keys.consumer_secret,                   
    access_token=my_bot_keys.access_token, access_token_secret=my_bot_keys.access_token_secret
)


# ## Load tweets with the source (what device they were posted on)
# Try different accounts, like: BarackObama, JoeBiden, MarkRuffalo, selenagomez, cnn

# In[ ]:


# choose account to search from (save in query variable)
query = 'from:cnn'

# search tweets with the query, also include the "source" info, and allow up to 20 results
# note: "search_recent_tweets" searches tweets from the last 7 days
tweets = client.search_recent_tweets(query=query, tweet_fields=["source"], max_results=20)

# loop through each of the tweets (saved in tweets.data)
for tweet in tweets.data:
    print(tweet.source) # print the source publishing the tweet
    print("   " + tweet.text) # print the text of the tweet
    print() # print a blank line

