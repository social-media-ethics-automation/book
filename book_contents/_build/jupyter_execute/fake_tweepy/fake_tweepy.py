#!/usr/bin/env python
# coding: utf-8

# # Fake Tweepy Library
# This library is intended to mimic Tweepy so that the book demoes can be run without actually needing twitter credentials, and not actually posting to twitter

# In[1]:


from types import SimpleNamespace

from IPython.display import HTML, Image, display
import html

import datetime



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
    
def search_recent_tweets(query="", tweet_fields=[]):
    print_info("Fake Tweepy is pretending to search and is returning some fake tweets.")
    return SimpleNamespace(
      data = [
          SimpleNamespace(
              text = "While trying to tweet right now, I am being attacked by my cute cat! It's so hard to tpye wihsaoae as fesadf asd fssasaf sa",
              id = 129308937494,
              author_id = 239048094385,
              created_at = datetime.datetime(2022, 2, 22, 22, 22, 22, 0, datetime.timezone.utc),
              lang = 'en',
              source = 'Twitter for Android',
              public_metrics = {
                  'retweet_count': 7,
                  'reply_count': 3,
                  'like_count': 6,
                  'quote_count': 2                  
              }
          ),
          SimpleNamespace(
              text = "I wish I could be sleeping now like my cute cat is!",
              id = 93298432,
              author_id = 23409023,
              created_at = datetime.datetime(2022, 2, 22, 2, 2, 2, 0, datetime.timezone.utc),
              lang = 'en',
              source = 'Twitter for iPhone',
              public_metrics = {
                  'retweet_count': 2,
                  'reply_count': 1,
                  'like_count': 5,
                  'quote_count': 3                  
              }
          ),
          SimpleNamespace(
              text = "Why won't my cute cat stop scratching my face in the morning!",
              id = 321923,
              author_id = 32892394,
              created_at = datetime.datetime(2022, 2, 22, 3, 3, 3, 0, datetime.timezone.utc),
              lang = 'en',
              source = 'Twitter for iPhone',
              public_metrics = {
                  'retweet_count': 3,
                  'reply_count': 4,
                  'like_count': 2,
                  'quote_count': 3                  
              }
          )
      ]
    )


def client_creator(bearer_token="", consumer_key="", consumer_secret="", access_token="", access_token_secret="" ):
    print_info("Fake Tweepy is pretending to log in to twitter")
    return SimpleNamespace(
      create_tweet = print_tweet,
      search_recent_tweets = search_recent_tweets
    )


tweepy = SimpleNamespace(
    Client = client_creator
)


# In[ ]:




