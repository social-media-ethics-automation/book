#!/usr/bin/env python
# coding: utf-8

# # Demo: Recommend a Friend

# In[1]:


# Demo: refactor recommendation through writing Functions
## Install variable inspector (then reload browser tab)
get_ipython().system('pip install lckr-jupyterlab-variableinspector')


# ## Default and named parameters

# In[2]:


def say_hello(name = ""):
    print("Hello " + name)


# In[3]:


say_hello()


# In[4]:


say_hello(name = "Kyle")


# In[5]:


import time

def pause_before_saying_hello(name = "", pause_time = 1):
    time.sleep(pause_time)
    print("Hello " + name)


# In[6]:


pause_before_saying_hello()


# In[7]:


pause_before_saying_hello(name = "Kyle")


# In[8]:


pause_before_saying_hello(pause_time = 3)


# In[9]:


pause_before_saying_hello(name = "Kyle", pause_time = 3)


# ## Returns

# In[10]:


def mult(num1, num2):
    return num1 * num2


# In[11]:


num_val = mult(3, 4)


# In[12]:


def make_hello_message(name):
    message = "Hello " + name + "! How are you today?"
    return message


# In[13]:


hi_kyle_message = make_hello_message("Kyle")


# ## Update recommendation algorithm from last time

# In[ ]:


# make sure tweepy library is installed
get_ipython().system('pip install tweepy')
import tweepy


# In[15]:


# load my twitter keys
import my_bot_keys


# In[16]:


# log into tweepy
client = tweepy.Client(
    bearer_token=my_bot_keys.bearer_token,
    consumer_key=my_bot_keys.consumer_key, consumer_secret=my_bot_keys.consumer_secret,                   
    access_token=my_bot_keys.access_token, access_token_secret=my_bot_keys.access_token_secret
)


# In[19]:


def id_from_username(username):
    user_info = client.get_user(username=username)
    user_id = user_info.data.id
    return user_id


# In[20]:


# Changes from 09 lecture: 
#
#  - I have taken the code to get from a username to a user id and 
#    put it in its own function above (id_from_username), which 
#    makes my code below slightly shorter and easier to read
#
#  - I have made an optional parameter num_followers_to_check, with
#    a default of 3, so I can change how many users the person is 
#    following to start with, so I can change that value when I 
#    call the function


def get_follow_suggestions(username, num_followers_to_check=3):
    # for a given user, I need to user id
    user_id = id_from_username(username)

    # find the people that user currently follows
    follow_users = client.get_users_following(id=user_id, max_results=num_followers_to_check)

    # dictionary to track who my follow follows are, as possible suggestions
    # The keys will be the username, and the values will be how often they
    # appeared as follow follows
    possible_suggestion_counts = {}

    # for each of those people, see who they follow
    for follow_user in follow_users.data:
        print("looking for followings of user: " + follow_user.username)
        follow_follow_users = client.get_users_following(id=follow_user.id)

        for follow_follow_user in follow_follow_users.data:
            possible_suggestion = follow_follow_user.username

            # If this possible suggestion is not yet in the dictionary,
            # add it with a count of one
            if possible_suggestion not in possible_suggestion_counts:
                possible_suggestion_counts[possible_suggestion] = 1
            else: #otherwise, update the count in the dictionary
                possible_suggestion_counts[possible_suggestion] += 1


    # recommend that I follow the people who those people follow most
    ordered_suggestions = sorted(possible_suggestion_counts.items(), key=lambda x: -x[1])
    display(ordered_suggestions)


# In[21]:


get_follow_suggestions("UW", num_followers_to_check=5)


# In[ ]:




