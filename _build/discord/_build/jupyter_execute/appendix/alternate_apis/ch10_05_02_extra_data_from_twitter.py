#!/usr/bin/env python
# coding: utf-8

# # Ch10.5.2: Demo: Extra Data From Twitter
# 
# In order to get alt-text data from images in Tweets, we're going to have to look at how to get extra data from Twitter.
# 
# _Note: You don't really need to undestand this whole process, you can just take the final code pieces and copy/paste them to use them yourself. We are including this explanation in case you want to know how it is working._
# 
# The examples here are based on examples from [this website](https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9)
# 
# But first let's do our normal tweepy set-up

# ## Normal Tweepy Set-Up

# In[1]:


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


# ## Get media (including image) data
# 
# If we want to get media (including image) data from tweets, when we are using search_recent_tweets, then we have to include:
# - `expansions='attachments.media_keys'` which tells Tweepy to get the media information for the tweet
# - `media_fields=['preview_image_url', 'height', 'width']` which tells Tweepy which information to get for each piece of media.
# 
# Let's do a search for tweets that include the word dog, and have an image, and are not retweets (so we don't just get the same tweet for all the times it was retweeted):

# In[5]:


query = "dog -is:retweet has:images"

tweet_search_results = client.search_recent_tweets(
                                    query=query,
                                    expansions='attachments.media_keys', #tell twitter to download the media related to this tweet
                                    media_fields=['preview_image_url', 'height', 'width']  # when getting the media, make sure to include this info
                                    )


# Now, when our search comes back, it has both the Tweet information and the information about media (including images) in those Tweets. 
# 
# Unfortunately the Tweet info and the media info come back in two separate parts of the tweet_search_results:
# - `tweet_search_results.data` has the list of tweets
# - `tweet_search_results.includes['media']` has a list of the pieces of media in the tweets
# 
# 

# In[6]:


display(tweet_search_results.data)


# In[7]:


display(tweet_search_results.includes['media'])


# The way this comes back doesn't directly tell us which piece of media is part of which tweet. Instead, for each piece of media, there is a special id number called the `media_key`, and for each tweet there is a list of `media_key`s that are part of the tweet. 
# - for a `tweet` in `tweets.data`, the media_keys are in `tweet.data['attachments']['media_keys']`
# - for a piece of `media` in the `tweets.includes['media']`, the media_id is in `media['media_key']`
# 
# So, if we are looking at a tweet, and look at the media keys, we will want to look up the media information that goes with that key. Looking up something based on a key is easiest to do with a dictionary in Python. So, what we will do is make a dictionary where the keys are media_keys, and the values are the media information. It will look something like this:
# 
# Below is the code to do this (using several Python short hand tricks at once):

# In[8]:


media_lookup = {m.media_key: m for m in tweet_search_results.includes['media']}

display(media_lookup)


# Now we can choose a tweet, find the media_keys for that tweet, and then look up the media information on each of those tweets

# In[9]:


# get the first tweet
first_tweet = tweet_search_results.data[0]

print("displaying info for tweet: " + first_tweet.text)

# get the media keys for the first tweet
first_tweet_media_keys = first_tweet.data['attachments']['media_keys']

# loop through the media keys
for media_key in first_tweet_media_keys:
    # lookup the info about this particular media_key
    media_info = media_lookup[media_key]
    
    # print out some info about this piece of media
    print("  type: " + media_info.type)
    print("  height: " + str(media_info.height))
    print("  width: " + str(media_info.width))
    print()


# ## Get user information
# User information works the same way that media information did, though there will only be one author per tweet. We have to set an expansion and tell what user fields to download:

# In[10]:


query = "dog -is:retweet has:images"

tweet_search_results = client.search_recent_tweets(
                                    query=query,
                                    expansions='author_id', #tell twitter to download the author related to this tweet
                                    user_fields=['profile_image_url']  # when getting the author, make sure to include this info
                                    )


# Then we make a lookup dictionary for the user information

# In[11]:


user_lookup = {u.id: u for u in tweet_search_results.includes['users']}

display(user_lookup)


# Then we can find the `author_id` of a tweet in tweet.author_id, and look it up in the `user_lookup` dictionary

# In[12]:


first_tweet = tweet_search_results.data[0]

print("displaying info for tweet: " + first_tweet.text)

# get the author id for the first tweet
first_tweet_author_id = first_tweet.author_id

author = user_lookup[first_tweet_author_id]

# look up info about the author:
print("  author name: " + author.name)
print("  author username: " + author.username)
print("  author profile image: " + author.profile_image_url)



# In[ ]:




