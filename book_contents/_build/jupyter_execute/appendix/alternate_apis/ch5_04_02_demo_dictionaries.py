#!/usr/bin/env python
# coding: utf-8

# # Ch 5.4.2 Demo: Dictionaries (Twitter)
# 
# We've talked about lists, but the other data organization we need to work with social media data is `dictionaries`.
# 
# As we mentioned in chapter 4, dictionaries allow us to combine pieces of information by naming them (sort of like variables).
# 
# So for example, the information about a user might have the following pieces of data:
# - Username
# - Twitter handle
# - Profile Picture:
# - Follows
# 
# Python has two ways of doing these types of dictionaries: `dict` and objects

# ## Dictionaries (`dict`)
# We can create dictionaries in Python by storing values into `key`s inside of curly braces `{` `}`, like this:

# In[1]:


user_1 = {
    "username": "kylethayer",
    "twitter_handle": "@kylemthayer",
    "profile_picture": "kylethayer.jpg",
    "follows": ["@SusanNotess", "@UW", "@UW_iSchool", "@ajlunited"]
}


# In the code above, inside of the curly braces are a set of lines. Each line has a string (the `key`, or name of the value), followed by a colon (`:`), followed by a value that is to be saved for the key. At the end of all but the last line is a comma (`,`) which indicates that another `key` and value will come next.
# 
# Now that we've saved some values for some keys in the dictionary now saved in user_1, we can look up the values by using square brackets (`[`, `]`) with the key name inside, like this:

# In[2]:


user_1_username = user_1["username"]
display(user_1_username)


# In[3]:


user_1_handle = user_1["twitter_handle"]
display(user_1_handle)


# In[4]:


user_1_picture = user_1["profile_picture"]
display(user_1_picture)


# In[5]:


user_1_follows = user_1["follows"]
display(user_1_follows)


# ## Objects
# The other way of saving information that works similarly in Python is through an object. We won't be creating any in this book, but we will have to get data from some.
# 
# The main difference from what we will need is that while in dictionaries we use square brackets and put the key name in quotes as a string (e.g., `user_1["profile_picture"]`), in an object you use a period (`.`) and don't put they key name (called a `field`) in quotes (e.g., `user_1.profile_picture`)
# 
# We have already seen code that used this period to get something from an object a few times, specifically getting functions from them, like:
# - `client.create_tweet(...`
# - `normal_message.upper()`
# 
# When we go through data from twitter, sometimes we will need to use `.` to get parts of the information out of objects, and sometimes we will need to use `[" "]` to get information out of dictionaries.

# ## Looping through lists of dictionaries
# Now that we've seen loops, lists, and dictionaries, we can go back to Twitter, run a search and look through multiple tweets:

# ### load tweepy library

# In[6]:


# Load some code called "tweepy" that will help us work with twitter
import tweepy


# ### (optional) make a fake twitter connection with the fake_tweepy library

# For testing purposes, we’ve added this line of code, which loads a fake version of tweepy, so it wont actually connect to twitter. __If you want to try to actually connect to twitter, don’t run this line of code.__

# In[7]:


get_ipython().run_line_magic('run', '../../fake_tweepy/fake_tweepy.ipynb')


# ### load your developer access passwords

# In[8]:


# Load all your developer access passwords into Python
# TODO: Put your twitter account's special developer access passwords below:
bearer_token = "n4tossfgsafs_fake_bearer_token_isa53#$%$"
consumer_key = "sa@#4@fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"


# ### give tweepy (or fake_tweepy) your developer access passwords

# In[9]:


# Give the tweepy code your developer access passwords so
# it can perform twitter actions
client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)


# ### find a list of tweets
# We can now do a search and find a list of tweets.
# 
# _Note: If you run this on real twitter, we can’t gurantee anything about how offensive what you might find is. We don’t know of any word search we could guarantee would be safe._

# In[10]:


# Choose a search to run
query = '"cute cat"'

#Run the search and request some additional info
tweets_info = client.search_recent_tweets(query=query, tweet_fields=["author_id", "created_at", "id", "lang", "public_metrics", "source", "text"])

# Get the actual list of tweets out of the data field (tweets_info also has metadata about our search)
tweets_list = tweets_info.data


# ## Loop through the list of tweets
# The variable `tweets_list` now has a list of tweet. So we can use a for loop to go through each tweet, and then use `.` to access info from each tweet (other pieces of information would need `[" "]` to access).
# 
# For each of the tweets, we will use `print` to display information about the tweet

# In[11]:


for tweet in tweets_list:
    print("Info for tweet with id: " + str(tweet.id))
    print("  author_id: " + str(tweet.author_id))
    print("  created_at: " + str(tweet.created_at))
    print("  source: " + str(tweet.source))
    print("  text: " + str(tweet.text))
    print()

