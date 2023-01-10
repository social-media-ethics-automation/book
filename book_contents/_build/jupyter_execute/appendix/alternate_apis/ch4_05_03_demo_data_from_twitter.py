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
# Below I have the code to find a recent tweet that has the phrase "cute cat". 
# 
# Don't worry if you don't understand this part yet, We are
# just doing this, so we can get to the point of seeing what tweet data looks like.
# 
# _Note: If you run this on real twitter, we can't gurantee anything about how offensive what you might find is. We don't know of any word search We could guarantee would be safe._

# In[5]:


# Choose a search to run
query = '"cute cat"'

#Run the search and request some additional info
tweets = client.search_recent_tweets(query=query, tweet_fields=["author_id", "created_at", "id", "lang", "public_metrics", "source", "text"])

# Find the first tweet returned
recent_tweet = tweets.data[0]


# ## Look at data in tweet
# 
# Now we will look at some of the data that came back!
# 
# Again, don't worry too much about the code, we want to look at the data and data types.
# 
# ### tweet text:

# In[6]:


display("The data type of the tweet text is: " + type(recent_tweet.text).__name__)
display("The tweet text is: " + recent_tweet.text)


# As you can see above, the tweet text is a string (`str`) data type. And while we can't see any indication here, we know from elsewhere that tweet text is limited to 280 characters in length.

# ### tweet id

# In[7]:


display("The data type of the tweet id is: " + type(recent_tweet.id).__name__)
display("The tweet tweet id is: " + str(recent_tweet.id))


# The tweet id is an integer number (`int`). This is how the tweet is referred to inside Twitter's computers. So if someone is replying to a tweet, Twitter just puts which tweet ID they were replying to, and then can look up that tweet if needed.

# ### tweet author id

# In[8]:


display("The data type of the author id is: " + type(recent_tweet.author_id).__name__)
display("The tweet author id is: " + str(recent_tweet.author_id))


# The author id is an integer number (int). This is how the user who posted the tweet is referred to inside Twitter's computers. So when twitter wants to display the tweet with the user info, it uses this number to look up the information on that user.

# ### tweet created at

# In[9]:


display("The data type of the tweet created at is: " + type(recent_tweet.created_at).__name__)
display("The tweet tweet created at is: " + str(recent_tweet.created_at))


# The created at time for the tweet is a special python datetime data type (`datetime`). As you can see, it has the year, month, and day, and then the time in hours, minutes and seconds. It then shows the timezone it is in, in this case: 00:00, which is in [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).

# ### tweet lang (language)

# In[10]:


display("The data type of the tweet lang is: " + type(recent_tweet.lang).__name__)
display("The tweet tweet lang is: " + str(recent_tweet.lang))


# The language the tweet is made in is a string (`str`). It comes from a set of [standard language abbreviations](https://en.wikipedia.org/wiki/IETF_language_tag#List_of_common_primary_language_subtags) and in this case it is "en" which is short for "English".

# ### tweet source (device that made the tweet)

# In[11]:


display("The data type of the tweet source is: " + type(recent_tweet.source).__name__)
display("The tweet tweet source is: " + str(recent_tweet.source))


# The tweet source is a string (`str`). In this case it is "Twitter for Android" meaning someone posted this tweet from the Twitter App on their Android phone.

# ### public metrics

# In[12]:


display("The data type of the tweet source is: " + type(recent_tweet.public_metrics).__name__)
display("The tweet tweet source is: " + str(recent_tweet.public_metrics))


# The public metrics of a tweet are saved in a dictionary (`dict`), which holds a group of values. So let's look at each of those:

# In[13]:


display("The data type of the retweet count is: " + type(recent_tweet.public_metrics['retweet_count']).__name__)
display("The retweet count is: " + str(recent_tweet.public_metrics['retweet_count']))

display("The data type of the reply count is: " + type(recent_tweet.public_metrics['reply_count']).__name__)
display("The reply count is: " + str(recent_tweet.public_metrics['reply_count']))

display("The data type of the like count is: " + type(recent_tweet.public_metrics['like_count']).__name__)
display("The like count is: " + str(recent_tweet.public_metrics['like_count']))

display("The data type of the quote count is: " + type(recent_tweet.public_metrics['quote_count']).__name__)
display("The quote count is: " + str(recent_tweet.public_metrics['quote_count']))


# The counts for retweets, replies, likes, and quotes are each integer numbers (`int`), indicating how many times the tweet has been retweeted, replied to, liked, or quoted.

# ## Still more!
# In addition to the data we looked at above, there are even more options for tweets such as:
# - conversation_id: For tracking which tweets are in the same conversation, like replies and threads)
# - geo: For the location where a tweet was posted (I think default privacy settings now leave this blank)
# - organic_metrics: For the account that made the tweet, they can see how many people looked at it, or clicked on the user profile
# 
# You can read more about all this data and more in the [official twitter API documentation](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) (which is admittedly, a little hard to read and make sense of).
