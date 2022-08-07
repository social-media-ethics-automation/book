#!/usr/bin/env python
# coding: utf-8

# # Practice: Get info from twitter

# The purpose of this lab is to try running a program yourself and get an idea of things you can do with twitter, we aren't going to explain each detail of the code today, that will be covered in the future

# ## Install and import the "tweepy" library of code that gives us twitter functions

# In[1]:


get_ipython().system('pip install tweepy')
import tweepy


# ## Log into the Instructors' twitter with read only access

# In[2]:


import teacher_bot_read_keys
client = tweepy.Client(teacher_bot_read_keys.bearer_token)


# ## You can't post tweets (since you have read only access)
# If you try to run the command to post a tweet, it will have a long error message in a red box, ending with:
# > TypeError: Consumer key must be string or bytes, not NoneType
# 
# This means that in order to post a tweet, it needs the twitter accounts' "Consumer Key." But since we didn't provide it with the login info above, it showed up as "NoneType" which means the code to post a tweet couldn't continue.
# 
# _Note: You can get rid of the long error message by right-clicking on the red error message box and selecting "Clear Outputs"_

# In[ ]:


client.create_tweet(text="Trying to post this tweet won't work")


# ## You can search for tweets

# In[ ]:


query = 'from:KSeattleWeather'

tweets = client.search_recent_tweets(query=query)

display(tweets.data)


# ## You can get user IDs from usernames 

# In[ ]:


username = "BillNye"
user_id = client.get_user(username=username).data.id
user_id


# ## You can get user mentions from ID

# In[ ]:


client.get_users_mentions(id=user_id).data


# ## You can get who the user follows from the ID

# In[ ]:


following = client.get_users_following(user_id).data
following


# ## You can manipulate the output

# In[ ]:


for user in following:
    print('Bill Nye the Science Guy follows ' + user.name + '!')


# ## YOU TRY:

# ## 1) Modify the "query" variable to search for someone else's tweets.

# In[ ]:


query = 'from:???'    # replace the "???" with the username of the account you want

tweets = client.search_recent_tweets(query=query)

display(tweets.data)


# ## 2) Modify the username to get the ID from a twitter user of your choice

# In[ ]:


username = "???"
user_id = client.get_user(username=username).data.id
user_id


# ## 3) Get user mentions from the ID

# In[ ]:


# Try it yourself by copying code from above and pasting it here:


# ## 4) Get who the user follows from the ID

# In[ ]:


# Try it yourself by copying code from above and pasting it here:


# ## Optional bonus challenge (not for credit): 
# 
# Try using a method we haven't tried in the demos! Refer to: https://docs.tweepy.org/en/stable/client.html#

# In[ ]:


# Write your answer here:

