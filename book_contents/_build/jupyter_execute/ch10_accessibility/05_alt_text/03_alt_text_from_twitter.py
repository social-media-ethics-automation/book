#!/usr/bin/env python
# coding: utf-8

# # Demo: Alt-text From Twitter
# Now that we've seen how to select additional information about Tweet images and data, let's search for images and look up some alt-text:

# ## Normal Tweepy Set-Up

# In[1]:


import tweepy


# (optional) use the fake version of tweepy, so you don’t have to use real twitter developer access passwords

# In[ ]:





# In[2]:


# Load all your developer access passwords into Python
# TODO: Put your twitter account's special developer access passwords below:
bearer_token = "n4tossfgsafs_fake_bearer_token_isa53#$%$"
consumer_key = "sa@#4@fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"


# In[3]:


# Give the tweepy code your developer access passwords so
# it can perform twitter actions
client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)


# ## Do a search for tweets, loop through the tweets and display the alt-text information

# In[4]:


query = "dog -is:retweet has:images"

tweet_search_results = client.search_recent_tweets(
                                    query=query,
                                    expansions='attachments.media_keys', #tell twitter to download the media related to this tweet
                                    media_fields=['alt_text', 'url'],  # when getting the media, make sure to include this info
                                    max_results=100
                                    )


# make media_lookup dictionary
media_lookup = {m["media_key"]: m for m in tweet_search_results.includes['media']}

# go through each tweet
for tweet in tweet_search_results.data:
    
    # use the tweet id to make a link to this specific tweet
    print('https://twitter.com/twitter/statuses/' + str(tweet.id))
    
    # print the contents of the tweet
    print(tweet)
    
    # print the info on "attachments" for this tweet
    #  in this case, it will be the media_keys
    
    #get the media keys for this tweet
    media_keys = tweet.data['attachments']['media_keys']
    
    for media_key in media_keys:
        # lookup the info about this particular media_key
        media_info = media_lookup[media_key]

        # print out some info about this piece of media
        print("  type: " + media_info.type)
        print("  alt_text: " + str(media_info.alt_text))
        print("  url: " + str(media_info.url))
        print()
       
    # display a clear divider so we can more easily see each tweet
    print()
    print("------------------------")
    print()


# In[ ]:




