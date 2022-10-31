#!/usr/bin/env python
# coding: utf-8

# # Practice: Dictionary Counters

# ## Install Variable Inpsector

# In[1]:


# Install variable inspector (then reload browser tab)
get_ipython().system('pip install lckr-jupyterlab-variableinspector')


# ## Practice Writing Functions
# Read more here: https://www.w3schools.com/python/python_functions.asp

# In[1]:


def function_name():
  # do various actions, like this:
  print("This is a function!")


# In[2]:


function_name()


# In[3]:


def say_hello():
    print("Hello!")


# In[5]:


for x in range(5):
    say_hello()


# In[6]:


def say_hello(name):
    print("Hello " + name + "!")


# In[7]:


say_hello("Kyle")


# In[8]:


def say_hello(name):
    if(name == "Kyle"):
        print("I'm not saying hello to you!")
    else:
        print("Hello " + name + "!")


# In[9]:


say_hello("Emily")


# In[10]:


say_hello("Kyle")


# In[11]:


say_hello("Fred")


# ## Practice Using Dictionaries
# Read more here: https://www.w3schools.com/python/python_dictionaries.asp

# In[12]:


my_info = {
    "first_name": "Kyle",
    "last_name": "Thayer"
}


# In[13]:


print("The full name is: " + 
      my_info["first_name"] + 
      " " + 
      my_info["last_name"])


# In[14]:


my_info["age"] = 38


# In[15]:


favorite_ice_creams = {
    "Kyle": "Chocolate Chip Cookie Dough",
    "Emily": "Mint Chocolate Chip",
    "Sally": "Vanilla",
    "Maria": "Chocolate"
}


# In[16]:


names = favorite_ice_creams.keys()


# In[17]:


for name in names:
    favorite_ic = favorite_ice_creams[name]
    print(name + " likes the ice cream " + favorite_ic)


# ## Recommend new people to follow
# Resources: 
# * Tweepy documentation (for Twitter API v2): https://docs.tweepy.org/en/stable/client.html
# * Some examples of how to use Tweepy: https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9 
# 
# ## First, set-up

# In[18]:


# make sure tweepy library is installed
get_ipython().system('pip install tweepy')
import tweepy


# In[19]:


# load my twitter keys
import my_bot_keys


# In[20]:


# log into tweepy
client = tweepy.Client(
    bearer_token=my_bot_keys.bearer_token,
    consumer_key=my_bot_keys.consumer_key, consumer_secret=my_bot_keys.consumer_secret,                   
    access_token=my_bot_keys.access_token, access_token_secret=my_bot_keys.access_token_secret
)


# ## Write code to recommend new people to follow

# In[27]:


# for a given user, I need to user id
user_info = client.get_user(username="KSeattleWeather")
user_id = user_info.data.id

# find the people that user currently follows
follow_users = client.get_users_following(id=user_id, max_results=3)

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


# ## Now make that code into a function

# In[28]:


def get_follow_suggestions(username):
    # for a given user, I need to user id
    user_info = client.get_user(username=username)
    user_id = user_info.data.id

    # find the people that user currently follows
    follow_users = client.get_users_following(id=user_id, max_results=3)

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


# ## Use function to see follow recommendations

# In[31]:


get_follow_suggestions("UW")


# In[ ]:




