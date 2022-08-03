#!/usr/bin/env python
# coding: utf-8

# # Demo: Sentiment Analysis

# ### Standard loading

# In[1]:


# Install variable inspector (then reload browser tab)
get_ipython().system('pip install lckr-jupyterlab-variableinspector')


# In[7]:


# make sure tweepy library is installed
get_ipython().system('pip install tweepy')
import tweepy


# In[8]:


# load my twitter keys
import my_bot_keys


# In[9]:


# log into tweepy
client = tweepy.Client(
    bearer_token=my_bot_keys.bearer_token,
    consumer_key=my_bot_keys.consumer_key, consumer_secret=my_bot_keys.consumer_secret,                   
    access_token=my_bot_keys.access_token, access_token_secret=my_bot_keys.access_token_secret
)


# ### Load Sentiment Analysis Library

# In[5]:


import nltk
nltk.download(["vader_lexicon"])


# In[ ]:


from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# ## Test Sentiment Analysis

# In[11]:


sia.polarity_scores("I really, really hate pizza!!!!!!!!")


# In[38]:


def get_sentiment_of_text(text):
    tweet_sentiment = sia.polarity_scores(text)
    tweet_compound_sentiment = tweet_sentiment['compound']
    return tweet_compound_sentiment

def get_sentiment(query, show_progress=False, max_results=10):
    tweets = client.search_recent_tweets(query=query, max_results=max_results)

    num_tweets = 0
    total_sentiment = 0

    # go through each tweet
    for tweet in tweets.data:
        if show_progress: 
            print(tweet.text)

        #calculate sentiment
        tweet_compound_sentiment = get_sentiment_of_text(tweet.text)

        if show_progress:
            print(tweet_compound_sentiment)

        num_tweets += 1
        total_sentiment += tweet_compound_sentiment

        if show_progress:
            print()

    if show_progress:
        print("num tweets: " + str(num_tweets))
        print("total_sentiment: " + str(total_sentiment))
        print("avg_sentiment: " + str(total_sentiment / num_tweets))
    
    return total_sentiment / num_tweets


# In[39]:


get_sentiment("football", max_results=10, show_progress=True)


# In[28]:


get_sentiment("Biden", max_results=100)


# In[29]:


get_sentiment("Trump", max_results=100)


# In[30]:


get_sentiment("Mitch McConnell", max_results=100)


# In[31]:


get_sentiment("AOC", max_results=100)


# In[33]:


get_sentiment("Harvard", max_results=100)


# In[ ]:


get_sentiment("UW", max_results=100, show_progress=True)


# In[35]:


get_sentiment("University of Washington", max_results=100)


# In[40]:


get_sentiment("@UW", max_results=100)


# In[ ]:




