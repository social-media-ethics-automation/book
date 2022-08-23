#!/usr/bin/env python
# coding: utf-8

# # Demo: Trolling a Reply Bot
# ### Set-up steps
# * Install the variable inspector!pip install lckr-jupyterlab-variableinspector
# * Install and import tweepy
# * Load login keys
# * Log in

# In[1]:


get_ipython().system('pip install lckr-jupyterlab-variableinspector')


# In[ ]:


get_ipython().system('pip install tweepy')
import tweepy


# In[ ]:


import my_bot_keys


# In[ ]:


client = tweepy.Client(
    bearer_token=my_bot_keys.bearer_token,
    consumer_key=my_bot_keys.consumer_key, consumer_secret=my_bot_keys.consumer_secret,                   
    access_token=my_bot_keys.access_token, access_token_secret=my_bot_keys.access_token_secret
)


# ## A twitter bot that says hi back
# * The bot will first find my account and my twitter name.
# * The bot will then find the latest tweet that mentions me.
# * Then the bot will see if the tweet starts with "`Hi @mybotname, my name is `", and the bot will assume the rest of the tweet is their name.
# * Finally the bot will tweet back "`Hi [their name]! Nice to meet you!`"

# ### Find my twitter info

# In[ ]:


my_user_info = client.get_user(id="me", user_auth=True)

my_id = my_user_info.data.id
my_username = my_user_info.data.username


# ### Find the latest tweet that mentions me

# In[ ]:


my_mentions = client.get_users_mentions(id=my_id)

latest_mention = my_mentions.data[0]

latest_mention_id = latest_mention.id
latest_mention_text = latest_mention.text


# ### See if the mention matches our pattern

# In[ ]:


expected_pattern = "Hi @" + my_username + ", my name is "

does_match_pattern = latest_mention_text.startswith(expected_pattern)


# ### if it matched the pattern, get the name and send reply

# In[ ]:


if does_match_pattern:
    their_name = latest_mention_text[len(expected_pattern):]
    message = "Hi " + their_name + "! Nice to meet you!"
    client.create_tweet(
        text=message, 
        in_reply_to_tweet_id=latest_mention_id
    )


# In[ ]:




