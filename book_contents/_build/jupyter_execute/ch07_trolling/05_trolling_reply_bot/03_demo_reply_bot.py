#!/usr/bin/env python
# coding: utf-8

# # Demo: Trolling a Reply Bot
# 
# We are later going to build a bot that, if you tweet at it: 
# - "Hi @mybotname, please ___" (where the ___ is some action)
# - then the bot will reply, "I will now ____" (where the ___ is that same action).
# 
# Then we will try trolling it, and fixing it, and trolling it again.
# 
# First though we need to do our Redddit PRAW setup:
# 
# ## Log into Reddit (PRAW)

# In[1]:


import praw


# (optional) make a fake praw connection with the fake_praw library
# 
# For testing purposes, we've added this line of code, which loads a fake version of praw, so it wont actually connect to reddit. __If you want to try to actually connect to reddit, don't run this line of code.__

# In[2]:


get_ipython().run_line_magic('run', '../../fake_apis/fake_praw.ipynb')


# In[3]:


# Load all your developer access passwords into Python
# TODO: Put your reddit username, password, and special developer access passwords below:
username="fake_reddit_username"
password="sa@#4*fdf_fake_password_$%DSG#%DG"
client_id="45adf$TW_fake_client_id_JESdsg1O"
client_secret="56sd_fake_client_secret_%Yh%"


# In[5]:





# In[4]:


# Give the praw code your reddit account info so
# it can perform reddit actions
reddit = praw.Reddit(
    username=username, password=password,
    client_id=client_id, client_secret=client_secret,
    user_agent="a custom python script"
)


# https://www.reddit.com/message/compose/?to=kthayer_teacher_bot
# "Wanting bot response"
# 

# In[5]:


for m in reddit.inbox.messages(limit=20):
    print(m.subject)


# ## Finding my twitter bot name
# We are going to be looking for people tweeting at us "Hi @mybotname, please ___", except we will need to get our actual twitter handle instead of "@mybotname". We'll need our twitter id number as well to find tweets that mention us.
# 
# We do this by asking twitter for our user info, then getting the id and username from it:

# In[14]:


# Ask twitter for my user info
my_user_info = client.get_user(id="me", user_auth=True)

# Get my id number and username from the user info
my_id = my_user_info.data.id
my_username = my_user_info.data.username

display("my user id number is: " + str(my_id))
display("my username is: " + my_username)


# ## Bot 1: do whatever we are told
# our first bot will find our latest mention, and then do whatever it is told

# ### find my latest mention
# Next we need to find the latest tweet that mentioned us. 
# 
# We do this by asking twitter for tweets that mention our user id, then pulling the first thing out of the list (index 0).
# 
# Then we get the tweet id and the text of the tweet.
# 
# _Note: This code will crash, showing error messages if there are no recent tweets mentioning us_

# In[15]:


# Ask twitter for tweets that mention my id
my_mentions = client.get_users_mentions(id=my_id)

# Get the first tweet from the list (latest tweet)
latest_mention = my_mentions.data[0]

latest_mention_id = latest_mention.id
latest_mention_text = latest_mention.text

display("the latest mention of us is tweet id: " + str(latest_mention_id))
display("the text of latest mention of us is: " + latest_mention_text)


# ### If tweet matches our pattern, reply
# 
# We will now see if our tweet matches our pattern of "Hi @mybotname, please ___" and then we will reply.
# 
# First we will create a string with the correct pattern, but with our actual bot name

# In[16]:


expected_pattern = "Hi @" + my_username + ", please "


# Now, if the mention text starts with that expected pattern, then we will find the action from the end of the mention text (based on the expected_pattern length), and reply using that action:

# In[17]:


# check if the mention text starts with our set phrase
if latest_mention_text.startswith(expected_pattern):
    # get the action, which should be the end of the string after the expected pattern
    action = latest_mention_text[len(expected_pattern) :]
    
    # make a new tweet message which says we will do the action
    message = "I will now " + action
    
    # tweet our message in reply to the mention tweet
    client.create_tweet(
        text=message, 
        in_reply_to_tweet_id=latest_mention_id
    )


# Yay! It worked! But there is a problem!

# ## Trolling bot 1
# This bot is really easy to troll, so if I repeat my steps and get a new mention:

# In[18]:


# Ask twitter for tweets that mention my id
my_mentions = client.get_users_mentions(id=my_id)

# Get the first tweet from the list (latest tweet)
latest_mention = my_mentions.data[0]

latest_mention_id = latest_mention.id
latest_mention_text = latest_mention.text

display("the latest mention of us is tweet id: " + str(latest_mention_id))
display("the thext of latest mention of us is: " + latest_mention_text)

expected_pattern = "Hi @" + my_username + ", please "

# check if the mention text starts with our set phrase
if latest_mention_text.startswith(expected_pattern):
    # get the action, which should be the end of the string after the expected pattern
    action = latest_mention_text[len(expected_pattern) :]
    
    # make a new tweet message which says we will do the action
    message = "I will now " + action
    
    # tweet our message in reply to the mention tweet
    client.create_tweet(
        text=message, 
        in_reply_to_tweet_id=latest_mention_id
    )


# Someone tweeted at us: `Hi @fake_user, please do something horrible!`, and we replied `I will now do something horrible!`. 
# 
# They could have made us tweet much worse!

# ## Bot 2: Trying to limit actions
# Let's try this again, but limit the actions we will do.
# - If someone asks us to "run", "jump", or "fly", we will do it
# - If someone asks us to do something else we will say:
#   - "I do not recognize the command ___" (with __ being whatever they said)
#   
# So, to go back through our steps:
# ### find my latest mention

# In[19]:


# Ask twitter for tweets that mention my id
my_mentions = client.get_users_mentions(id=my_id)

# Get the first tweet from the list (latest tweet)
latest_mention = my_mentions.data[0]

latest_mention_id = latest_mention.id
latest_mention_text = latest_mention.text

display("the latest mention of us is tweet id: " + str(latest_mention_id))
display("the text of latest mention of us is: " + latest_mention_text)


# ### If tweet matches our pattern, reply
# We do the same code for this as before, but after we get the action, we have another `if`/`else` to tweet back our two options.
# 
# We will use `in` to see if the action is in our list of allowed actions (called an allow_list)

# In[20]:


expected_pattern = "Hi @" + my_username + ", please "

actions_allow_list = ["run", "jump", "fly"]

# check if the mention text starts with our set phrase
if latest_mention_text.startswith(expected_pattern):
    # get the action, which should be the end of the string after the expected pattern
    action = latest_mention_text[len(expected_pattern) :]
    
    # See if it is one of our recognized actions
    if(action in actions_allow_list):
        # make a new tweet message which says we will do the action
        message = "I will now " + action

        # tweet our message in reply to the mention tweet
        client.create_tweet(
            text=message, 
            in_reply_to_tweet_id=latest_mention_id
        )
    else: # we didn't recognize the action
        # make a new tweet message which says we will do the action
        message = "I do not recognize the command " + action

        # tweet our message in reply to the mention tweet
        client.create_tweet(
            text=message, 
            in_reply_to_tweet_id=latest_mention_id
        )
        


# That one was in our allow list so it worked. Let's do it all again, with the tweet that caused us problems last time
# 
# _Note: the code below is just copied from the code sections above_

# In[21]:


# Ask twitter for tweets that mention my id
my_mentions = client.get_users_mentions(id=my_id)

# Get the first tweet from the list (latest tweet)
latest_mention = my_mentions.data[0]

latest_mention_id = latest_mention.id
latest_mention_text = latest_mention.text

display("the latest mention of us is tweet id: " + str(latest_mention_id))
display("the text of latest mention of us is: " + latest_mention_text)

expected_pattern = "Hi @" + my_username + ", please "

actions_allow_list = ["run", "jump", "fly"]

# check if the mention text starts with our set phrase
if latest_mention_text.startswith(expected_pattern):
    # get the action, which should be the end of the string after the expected pattern
    action = latest_mention_text[len(expected_pattern) :]
    
    # See if it is one of our recognized actions
    if(action in actions_allow_list):
        # make a new tweet message which says we will do the action
        message = "I will now " + action

        # tweet our message in reply to the mention tweet
        client.create_tweet(
            text=message, 
            in_reply_to_tweet_id=latest_mention_id
        )
    else: # we didn't recognize the action
        # make a new tweet message which says we will do the action
        message = "I do not recognize the command " + action

        # tweet our message in reply to the mention tweet
        client.create_tweet(
            text=message, 
            in_reply_to_tweet_id=latest_mention_id
        )


# Ok, this time we said `I do not recognize the command do something horrible!`. 
# 
# That looks a little better! Are we safe now?

# ## Trolling bot 2
# No, it turns out we are not safe.
# 
# Let's find the latest mention again and see what happens

# In[22]:


# Ask twitter for tweets that mention my id
my_mentions = client.get_users_mentions(id=my_id)

# Get the first tweet from the list (latest tweet)
latest_mention = my_mentions.data[0]

latest_mention_id = latest_mention.id
latest_mention_text = latest_mention.text

display("the latest mention of us is tweet id: " + str(latest_mention_id))
display("the text of latest mention of us is: " + latest_mention_text)

expected_pattern = "Hi @" + my_username + ", please "

actions_allow_list = ["run", "jump", "fly"]

# check if the mention text starts with our set phrase
if latest_mention_text.startswith(expected_pattern):
    # get the action, which should be the end of the string after the expected pattern
    action = latest_mention_text[len(expected_pattern) :]
    
    # See if it is one of our recognized actions
    if(action in actions_allow_list):
        # make a new tweet message which says we will do the action
        message = "I will now " + action

        # tweet our message in reply to the mention tweet
        client.create_tweet(
            text=message, 
            in_reply_to_tweet_id=latest_mention_id
        )
    else: # we didn't recognize the action
        # make a new tweet message which says we will do the action
        message = "I do not recognize the command " + action

        # tweet our message in reply to the mention tweet
        client.create_tweet(
            text=message, 
            in_reply_to_tweet_id=latest_mention_id
        )


# Oh no! Someone tweeted at us:
# - `Hi @fake_user, please stop talking. But that doesn't mean I won't say horrible things like: I hate everybody!`
# 
# And we replied:
# - `I do not recognize the command stop talking. But that doesn't mean I won't say horrible things like: I hate everybody!`
# 
# Making a bot that is troll proof is very difficult! You either need to severely limit how your bot engages with people, or do a ton of work trying to prevent trolling and fix problems when people find a new way of trolling you.
# 
# If you want to learn more, you can revisit the story of what went wrong with the Microsoft Tay bot: [How to Make a Bot That Isn't Racist](https://www.vice.com/en_us/article/mg7g3y/how-to-make-a-not-racist-bot)
