#!/usr/bin/env python
# coding: utf-8

# # Ch14 Demo: recursion with real tweets

# ## Normal Tweepy Set-Up

# In[1]:


# make sure tweepy library is installed
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


# ## (Just Run): Helper function to display text in an indented box

# In[5]:


from IPython.display import HTML, Image, display
import html
def display_indented(text, left_margin=0, color="white"):
    display(
        HTML(
            "<pre style='border:solid 1px;padding:3px;margin-left:"+str(left_margin)+"px;background-color:"+color+"'>" + 
            html.escape(text) + 
            "</pre>"
        )
    )


# ### Demo of using the display_with_left_margin function

# In[6]:


display_indented("A no indent text")
display_indented("A 10px indent text", left_margin=10)
display_indented("A 20px indent text \n with a newline!", left_margin=20)
display_indented("You can change the 'color' of the box too, like make it LightCoral", color='LightCoral', left_margin=10)


# ## (Just Run): Helper code for getting a twitter conversation (that is a tweet and a bunch of its replies)
# You don't need to know how this code works, but you can look through it if you want.
# 
# Also, if you want to use more includes or something, you can add them to the client.get_tweet() call and the client.search_recent_tweets() call. You might also need to do extra work to include them like I did with the author/users info

# In[7]:


# Given a tweetId, create a datastructure with the tweet and replies
# Each "tweet" is dictionary with keys for:
#    "tweet_info" (from the tweet.data), "author", "replies", "previous_tweet", and "first_tweet"
#
# When searching for tweets in the conversation, it looks for groups of 100
# tweets at a time. You can set how many groups of 100 tweets it looks for with
# max_conversation_searches
def get_tweets_with_replies(tweetId, max_conversation_searches=1):
    (starting_tweet, all_conversation_tweets, users_lookup) = get_tweet_and_conversation(tweetId, max_conversation_searches)
    tweets_by_referenced_tweet = organize_tweets_by_referenced_tweets(all_conversation_tweets)
    tweet_with_replies = organize_tweets_with_replies(starting_tweet, tweets_by_referenced_tweet, users_lookup)
    return tweet_with_replies

# the function above uses the helper functions below

# Given a tweet id, find the tweet and other tweets in the same conversation
def get_tweet_and_conversation(tweetId, max_conversation_searches=1):
    starting_tweet = client.get_tweet(tweetId, tweet_fields=['conversation_id', 'public_metrics'], expansions=['author_id'])
    conversation_id = starting_tweet.data.conversation_id
    
    all_conversation_tweets = get_conversation_tweets(conversation_id, max_conversation_searches)
    all_users = starting_tweet.includes['users']
    for conversation_tweets in all_conversation_tweets:
        all_users += conversation_tweets.includes['users']
    users_lookup = {str(u["id"]): u for u in all_users}
    return (starting_tweet, all_conversation_tweets, users_lookup)

# Get tweets in a conversation (given the conversation id)
def get_conversation_tweets(conversation_id, max_conversation_searches):
    query = "conversation_id:" + str(conversation_id)
    all_conversation_tweets = []
    num_searches=0
    is_done = False
    next_token = None
    while not is_done and num_searches < max_conversation_searches:
        conversation_tweets = client.search_recent_tweets(query=query, next_token=next_token, tweet_fields = 'public_metrics', expansions=['referenced_tweets.id','author_id'], max_results=100)
        num_searches += 1
        all_conversation_tweets.append(conversation_tweets)
        print("loaded a set of tweets: " + str(conversation_tweets.meta))
        if 'next_token' in conversation_tweets.meta:
            next_token = conversation_tweets.meta['next_token']
        else:
            is_done = True
    return all_conversation_tweets

# Given a list of tweets, group them all based on what tweet they are replying to
def organize_tweets_by_referenced_tweets(list_of_tweet_results):
    tweets_by_referenced_tweet = {}
    for tweets in list_of_tweet_results:
        for tweet in tweets.data:
            for referenced_tweet in tweet.referenced_tweets:
                if(referenced_tweet.type == "replied_to"):
                    referenced_tweet_id = str(referenced_tweet.id)
                    if(referenced_tweet_id not in tweets_by_referenced_tweet):
                        tweets_by_referenced_tweet[referenced_tweet_id] = []
                    tweets_by_referenced_tweet[referenced_tweet_id].append(tweet)
                    break

    return tweets_by_referenced_tweet

# organize the tweets so that author info and replies to tweets are included
# with it in a convenient data structure
def organize_tweets_with_replies(tweet, tweets_by_referenced_tweet, users_lookup, previous_tweet=None, first_tweet=None):
    tweet_with_replies = {
        "tweet_info": tweet.data,
        "author": users_lookup[str(tweet.data["author_id"])].data,
        "replies": [],
        "previous_tweet": previous_tweet
    }
    if first_tweet == None:
        first_tweet = tweet_with_replies
    tweet_with_replies["first_tweet"] = first_tweet

    tweet_id = str(tweet.data["id"])
    if tweet_id in tweets_by_referenced_tweet:
        reply_tweets = tweets_by_referenced_tweet[tweet_id]
        for reply_tweet in reply_tweets:
            tweet_with_replies["replies"].append(
                organize_tweets_with_replies(reply_tweet, tweets_by_referenced_tweet, users_lookup, previous_tweet=tweet_with_replies, first_tweet=first_tweet)
            )
    return tweet_with_replies


# ## Recursively printing the tweets and replies

# In[8]:


def print_tweet_and_replies(tweet_with_replies, num_indents=0):
    tweet_info = tweet_with_replies["tweet_info"]
    replies = tweet_with_replies["replies"]

    display_indented(tweet_info['text'], num_indents*20)
    
    #print replies (and the replies of those, etc.)
    for reply in replies:
        print_tweet_and_replies(reply, num_indents = num_indents + 1)


# In[9]:


loaded_tweets_and_replies = get_tweets_with_replies(98778587)


# In[10]:


print_tweet_and_replies(loaded_tweets_and_replies)


# ## Improved recursive print tweets and replies (more info)

# In[11]:


def print_tweet_and_replies(tweet_with_replies, num_indents=0):
    tweet_info = tweet_with_replies["tweet_info"]
    replies = tweet_with_replies["replies"]
    author_info = tweet_with_replies["author"]
    public_metrics = tweet_info["public_metrics"]

    display_text = (
        tweet_info['text'] + "\n" +
        "-- " + author_info["name"] + " (@" + author_info["username"] + ")" + "\n" +
        str(public_metrics)
    )
    
    display_indented(display_text, num_indents*20)
    
    #print replies (and the replies of those, etc.)
    for reply in replies:
        print_tweet_and_replies(reply, num_indents = num_indents + 1)


# In[12]:


print_tweet_and_replies(loaded_tweets_and_replies)


# In[13]:


# Note: to test for real, look for users who get a lot of engagement, 
#   like the reddit Am I the Asshole:
# https://twitter.com/AITA_online
# '1496516355931217926'

