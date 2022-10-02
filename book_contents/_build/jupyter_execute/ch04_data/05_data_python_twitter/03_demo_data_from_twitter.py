#!/usr/bin/env python
# coding: utf-8

# # Demo: Data from a Tweet
# Let's see what the data actually looks like from a Tweet!
# 
# First we need to do our normal twitter login steps (and optional fake tweepy step)
# ## Log into tweepy (or fake tweepy)
# ### 

# In[1]:


# Load some code called "tweepy" that will help us work with twitter
import tweepy


# ### (optional) make a fake twitter connection with the fake_tweepy library
# For testing purposes, we've added this line of code, which loads a fake version of tweepy, so it wont actually connect to twitter. __If you want to try to actually connect to twitter, don't run this line of code.__

# In[2]:


get_ipython().run_line_magic('run', '../../fake_tweepy/fake_tweepy.ipynb')


# ### load your developer access passwords
# To use this on your real twitter account, copy your [developer access passwords](../../prefaces/making_twitter_account.md) into the code below, replacing our fake passwords.

# In[3]:


# Load all your developer access passwords into Python
# TODO: Put your twitter account's special developer access passwords below:
bearer_token = "n4tossfgsafs_fake_bearer_token_isa53#$%$"
consumer_key = "sa@#4@fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"


# In[8]:





# ### give tweepy (or fake_tweepy) your developer access passwords

# In[4]:


# Give the tweepy code your developer access passwords so
# it can perform twitter actions
client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)


# ## Find a tweet
# Below I have the code to find a recent tweet that has the words "cute" and "cat". 
# 
# Don't worry if you don't understand this part yet, We are
# just doing this, so we can get to the point of seeing what tweet data looks like.
# 
# _Note: If you run this on real twitter, we can't gurantee anything about how offensive what you might find is. We don't know of any word search We could guarantee would be safe._

# In[5]:


# Choose a search to run
query = 'cute cat'

#Run the search and request some additional info
tweets = client.search_recent_tweets(query=query, tweet_fields=["author_id", "conversation_id", "created_at", "geo", "id", "in_reply_to_user_id", "lang", "public_metrics", "source", "text"])

# Find the first tweet returned
recent_tweet = tweets.data[0]


# ## Look at data in tweet
# 
# Now we will look at some of the data that came back!
# 
# Again, don't worry too much about the code, we want to look at the data and data types.
# 
# ### tweet text:

# In[22]:


display("The data type of the tweet text is: " + type(recent_tweet.text).__name__)
display("The tweet text is: " + recent_tweet.text)


# ### tweet id

# In[26]:


display("The data type of the tweet id is: " + type(recent_tweet.id).__name__)
display("The tweet tweet id is: " + str(recent_tweet.id))


# ### tweet author id

# In[25]:


display("The data type of the author id is: " + type(recent_tweet.author_id).__name__)
display("The tweet author id is: " + str(recent_tweet.author_id))


# ### tweet created at

# In[27]:


display("The data type of the tweet created at is: " + type(recent_tweet.created_at).__name__)
display("The tweet tweet created at is: " + str(recent_tweet.created_at))


# ### tweet lang (language)

# In[28]:


display("The data type of the tweet lang is: " + type(recent_tweet.lang).__name__)
display("The tweet tweet lang is: " + str(recent_tweet.lang))


# In[ ]:


### tweet source (device that made the tweet)


# In[29]:


display("The data type of the tweet source is: " + type(recent_tweet.source).__name__)
display("The tweet tweet source is: " + str(recent_tweet.source))


# ### TODO: public metrics
"author_id", "conversation_id", "created_at", "geo", "id", "in_reply_to_user_id", "lang", "public_metrics", "source", "text"