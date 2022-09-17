#!/usr/bin/env python
# coding: utf-8

# # Demo: Try Running the Twitter Bot!

# This page is called a "Jupyter Notebook" which it is a text page that has runnable Python code in it.
# 
# TODO: Explain how to run the Jupyter Notebook (rocket button at top of page, etc.)

# ## Sections of bot code
# We will put each section of code in its own separate code block. We also are adding a piece of code to load a fake version of the tweepy code so that it wont actually connect to twitter (just skip or delete that section if you have your developer access passwords and want to actually post on twitter).

# ### Load Tweepy code

# In[1]:


# Load some code called "tweepy" that will help us work with twitter
import tweepy


# ### Make a fake twitter connection (fake_tweepy library)
# For testing purposes, we've added this line of code, which loads a fake version of tweepy, so it wont actually connect to twitter. If you want to try to actually connect to twitter, don't run this line of code.

# In[2]:


get_ipython().run_line_magic('run', '../../fake_tweepy/fake_tweepy.ipynb')


# ### Load your developer access passwords
# To use this on your real twitter account, copy your [developer access passwords](../../prefaces/making_twitter_account.md) into the code below.

# In[3]:


# Load all your developer access passwords into Python
# TODO: Put your twitter account's special developer access passwords below:
bearer_token = "n4tossfgsafs_fake_bearer_token_isa53#$%$"
consumer_key = "sa@#4@fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"


# ### Give tweepy (or fake_tweepy) your developer access passwords

# In[4]:


# Give the tweepy code your developer access passwords so
# it can perform twitter actions
client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)


# ### Post a tweet

# In[5]:


# Post a tweet
# TODO: modify the text in the quotes below to change what this bot tweets:
client.create_tweet(text="This tweet was posted by a computer program!")


# In[ ]:




