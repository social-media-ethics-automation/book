#!/usr/bin/env python
# coding: utf-8

# # Demo of getting image data 2

# ## Set up

# In[1]:


# Install variable inspector (then reload browser tab)
get_ipython().system('pip install lckr-jupyterlab-variableinspector')


# In[ ]:


# make sure tweepy library is installed
get_ipython().system('pip install tweepy')
import tweepy


# In[5]:


# load my twitter keys
import my_bot_keys


# In[6]:


# log into tweepy
client = tweepy.Client(
    bearer_token=my_bot_keys.bearer_token,
    consumer_key=my_bot_keys.consumer_key, consumer_secret=my_bot_keys.consumer_secret,                   
    access_token=my_bot_keys.access_token, access_token_secret=my_bot_keys.access_token_secret
)


# ## Find tweets with images
# Resources: 
# * Tweepy documentation (for Twitter API v2): https://docs.tweepy.org/en/stable/client.html
# * Some examples of how to use Tweepy: https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9 

# In[12]:


#query = "from:KSeattleWeather -is:retweet has:images"
query = "dog -is:retweet has:images"

tweets = client.search_recent_tweets(query=query,
                                    expansions='attachments.media_keys', #tell twitter to download the media related to this tweet
                                    media_fields=['preview_image_url', 'height', 'width']  # when getting the media, make sure to include this info
                                    )

# print the infromation from the "media" includes 
# Note: the media information is stored separately in the results
print(tweets.includes['media'])
for media in tweets.includes['media']:
    print(media)
    print(media.preview_image_url)
    print(media.height)
    print(media.width)
    print()
    

# clever trick to make lookup table for media_keys saved in the variable "media"
media = {m["media_key"]: m for m in tweets.includes['media']}

# go through each tweet
for tweet in tweets.data:
    # use the tweet id to make a link to this specific tweet
    print('https://twitter.com/twitter/statuses/' + str(tweet.id))
    
    # print the contents of the tweet
    print(tweet)
    
    #get the media keys for this tweet
    attachments = tweet.data['attachments']
    media_keys = attachments['media_keys']
    
    # go through each of the photos (or other media)
    for media_key in media_keys:
        # find that media object using the media lookup table
        media_info = media[media_key]
        print(media_info.type)
        print("  media_key: " + media_info.media_key)
        print("  height: " + str(media_info.height))
        print("  width: " + str(media_info.width))
        
    print()


# In[14]:


#query = "from:KSeattleWeather -is:retweet has:images"
query = "dog -is:retweet has:images"

tweets = client.search_recent_tweets(query=query,
                                    expansions='author_id', #tell twitter to download the author related to this tweet
                                    user_fields=['profile_image_url']  # when getting the author, make sure to include this info
                                    )

   

# clever trick to make lookup table for user ids saved in the variable "users"
users = {u["id"]: u for u in tweets.includes['users']}

# go through each tweet
for tweet in tweets.data:
    # use the tweet id to make a link to this specific tweet
    print('https://twitter.com/twitter/statuses/' + str(tweet.id))
    
    # print the contents of the tweet
    print(tweet)
    
    #get the authorid for this tweet
    author_id = tweet.author_id
    
    # get the author info
    author = users[tweet.author_id]
    
    print(author)
    print("author profile image: " + author.profile_image_url)
        
    print()


# In[ ]:




