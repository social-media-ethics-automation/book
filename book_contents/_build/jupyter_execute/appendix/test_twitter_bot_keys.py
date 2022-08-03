#!/usr/bin/env python
# coding: utf-8

# # Test Twitter Bot Keys
# This is to test and make sure your twitter keys are working correctly.
# 
# Just run the code here one section at a time, and make sure you don't get errors (red) and that you get the expected output.

# ### Install and import tweepy
# First, make sure the tweepy library is installed and loaded

# In[1]:


get_ipython().system('pip install tweepy')
import tweepy


# ### Load your keys
# 
# Now try loading your keys from the my_bot_keys.py file

# In[2]:


import my_bot_keys


# ### Provide the tweepy library with the keys from your my_bot_keys.py file

# In[3]:


client = tweepy.Client(
    bearer_token=my_bot_keys.bearer_token,
    consumer_key=my_bot_keys.consumer_key, consumer_secret=my_bot_keys.consumer_secret,                   
    access_token=my_bot_keys.access_token, access_token_secret=my_bot_keys.access_token_secret
)


# ### Test loading info for a user
# If this works, it should display the user info for @KSeattleWeather. It should look like this:
# ```
# Response(data=<User id=34379755 name=Seattle Weather Blog username=KSeattleWeather>, includes={}, errors=[], meta={})
# ```

# In[4]:


userInfo = client.get_user(username="KSeattleWeather")
display(userInfo)


# ### Test posting a tweet
# If this works, it should post a tweet with your account (you can go to the twitter page for your account and make sure the tweet shows up)
# 
# **Note: You can't post the same tweet twice, so change the text inside the double quote marks each time you try running this. If you try posting the same tweet again, you'll get an error message that says "Forbidden"**

# In[ ]:


client.create_tweet(text="Posting a tweet from a computer program worked!")

