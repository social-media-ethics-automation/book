#!/usr/bin/env python
# coding: utf-8

# # Fake Tweepy Library
# This library is intended to mimic Tweepy so that the book demoes can be run without actually needing twitter credentials, and not actually posting to twitter

# In[1]:


from types import SimpleNamespace


# In[2]:


tweepy = SimpleNamespace(
    Client = lambda bearer_token="", consumer_key="", consumer_secret="", access_token="", access_token_secret="" : SimpleNamespace(
      create_tweet = lambda text="" : print(text)
    )
)


# In[ ]:




