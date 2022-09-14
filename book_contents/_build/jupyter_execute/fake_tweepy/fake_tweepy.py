#!/usr/bin/env python
# coding: utf-8

# # Fake Tweepy Library
# This library is intended to mimic Tweepy so that the book demoes can be run without actually needing twitter credentials, and not actually posting to twitter

# In[1]:


from types import SimpleNamespace

from IPython.display import HTML, Image, display
import html



# In[2]:


def print_info(text):
    display(
        HTML(
            "<strong style='color:darkred'>" + 
            html.escape(text) + 
            "</strong>"
        )
    )


# In[3]:


print_info("Fake tweepy is replacing the tweepy library. Fake Tweepy doesn't need real passwords, and prevents you from accessing real twitter")

def print_tweet(text=""):
    print_info("Fake Tweepy is pretending to post this tweet (note: real tweepy shows no output here when a tweet is posted): ")
    print(text)

def client_creator(bearer_token="", consumer_key="", consumer_secret="", access_token="", access_token_secret="" ):
    print_info("Fake Tweepy is pretending to log in to twitter")
    return SimpleNamespace(
      create_tweet = print_tweet
    )


tweepy = SimpleNamespace(
    Client = client_creator
)


# In[ ]:




