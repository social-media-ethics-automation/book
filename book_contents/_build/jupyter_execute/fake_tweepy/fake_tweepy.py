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


# In[4]:


def print_tweet(text="", in_reply_to_tweet_id=0):
    print_info("Fake Tweepy is pretending to post this tweet (note: real tweepy shows no output here when a tweet is posted): ")
    print(text)
    if(in_reply_to_tweet_id > 0):
        print("Tweet in reply to: " + str(in_reply_to_tweet_id))


# In[5]:


def search_recent_tweets(query="", tweet_fields=[], max_results=10):
    print_info("Fake Tweepy is pretending to search for '"+query+"' and is returning some fake tweets.")
    if(query == '"cute cat"'):
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
    if(query == "from:fake_celebrity"):
        return SimpleNamespace(
          data = [
              SimpleNamespace(
                  text = "Why is the line at the grocery store taking so long???",
                  id = 129308937494,
                  source = 'Twitter for iPhone'
              ),
              SimpleNamespace(
                  text = "Remember, my show tonight starts at 7:00pm!",
                  id = 93298432,
                  source = 'Fake Social Media Manager',
              ),
              SimpleNamespace(
                  text = "Hope all my followers are having a lovely day!",
                  id = 321923,
                  source = 'Fake Social Media Manager',
              )
          ]
        )


# In[6]:


def get_user(id="", user_auth=False):
    if(id == "me"):
        return SimpleNamespace(
            data = SimpleNamespace(
                id = 123456789,
                username = "fake_user"
            )
        )


# In[7]:


mentions_counter = 0

def get_users_mentions(id=0):
    global mentions_counter
    if(id == 123456789):
        mentions_counter += 1
        if(mentions_counter == 1):
            return SimpleNamespace(
              data = [
                  SimpleNamespace(
                      text = "Hi @fake_user, please jump",
                      id = 232434,
                  )
              ]
            )
        elif(mentions_counter == 2):
            return SimpleNamespace(
              data = [
                  SimpleNamespace(
                      text = "Hi @fake_user, please do something horrible!",
                      id = 234356,
                  )
              ]
            )
        elif(mentions_counter == 3):
            return SimpleNamespace(
              data = [
                  SimpleNamespace(
                      text = "Hi @fake_user, please fly",
                      id = 245454,
                  )
              ]
            )
        elif(mentions_counter == 4):
            return SimpleNamespace(
              data = [
                  SimpleNamespace(
                      text = "Hi @fake_user, please do something horrible!",
                      id = 245454,
                  )
              ]
            )
        elif(mentions_counter == 5):
            return SimpleNamespace(
              data = [
                  SimpleNamespace(
                      text = "Hi @fake_user, please stop talking. But that doesn't mean I won't say horrible things like: I hate everybody!",
                      id = 245454,
                  )
              ]
            )


# In[8]:


def client_creator(bearer_token="", consumer_key="", consumer_secret="", access_token="", access_token_secret="" ):
    print_info("Fake Tweepy is pretending to log in to twitter")
    return SimpleNamespace(
      create_tweet = print_tweet,
      search_recent_tweets = search_recent_tweets,
      get_user = get_user,
      get_users_mentions = get_users_mentions
    )


# In[9]:


tweepy = SimpleNamespace(
    Client = client_creator
)


# In[ ]:




