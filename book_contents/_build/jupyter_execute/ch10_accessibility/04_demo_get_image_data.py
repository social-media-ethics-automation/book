#!/usr/bin/env python
# coding: utf-8

# # Demo of getting image data

# ## Set up

# In[1]:


# Install variable inspector (then reload browser tab)
get_ipython().system('pip install lckr-jupyterlab-variableinspector')


# In[ ]:


# make sure tweepy library is installed
get_ipython().system('pip install tweepy')
import tweepy


# In[2]:


# load my twitter keys
import my_bot_keys


# In[3]:


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

# In[15]:


query = "from:KSeattleWeather -is:retweet has:images"

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
    
    # print the info on "attachments" for this tweet
    #  in this case, it will be the media_keys
    print(tweet.data.get('attachments'))
    
    #get the media keys for this tweet
    attachments = tweet.data['attachments']
    media_keys = attachments['media_keys']
    
    #look up first piece of media
    first_photo = media[media_keys[0]]
    
    #print the height and width of that first photo
    print(first_photo.height)
    print(first_photo.width)
    print()

