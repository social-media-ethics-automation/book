#!/usr/bin/env python
# coding: utf-8

# # Demo: Trolling a Reply Bot
# 
# We are later going to build a bot that, if you tweet at it: 
# - Subject: "Wanting bot response", body: "I want you to ___" (where the ___ is some action)
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


# In[4]:


# Give the praw code your reddit account info so
# it can perform reddit actions
reddit = praw.Reddit(
    username=username, password=password,
    client_id=client_id, client_secret=client_secret,
    user_agent="a custom python script"
)


# https://www.reddit.com/message/compose/
# "Wanting bot response"
# 

# ## Bot 1: do whatever we are told
# Our first bot will find our latest inbox message, and then reply with whatever it is told to do

# ### find my latest message
# We need to find our latest message in our inbox
# 
# We do this by looking in our reddit inbox for messages (we limit it to one, since we just want the latest).
# 
# It doesn't directly give us the one message (instead it is in something called an "iterator"), but we can use the `next` function to get the message out.
# 
# We then display the subject of the message just so we can see that it found something..

# In[5]:


# Look up the subreddit "cuteanimals", then find the "hot" list, getting up to 1 submission
messages = reddit.inbox.messages(limit=1)

# get the first submission off the list (should only be one anyway)
latest_message = next(messages) 

# display the subject and body of the message, so we can see what we found
display("latest message subject: " + str(latest_message.subject))
display("latest message body: " + str(latest_message.body))


# ### If tweet matches our pattern, reply
# 
# We will now see if our tweet matches our pattern of a message subject of "Wanting bot response" with a message body of "I want you to ___" and then we will reply.
# 
# First we will create strings with the patterns we are looking for and save them into variables.

# In[6]:


expected_subject = "Wanting bot response"
expected_body_pattern = "I want you to "


# We will check if the message has the subject we are expecting. If it does it will check if the essage body starts with the expected pattern. If it does, then we will find the action from the end of the message body text (based on the expected_pattern length), and reply using that action. 
# 
# We also add "else" cases for when we didn't match the patter, and display a message saying what didn't match.

# In[7]:


# check if the mention text starts with our set phrase
if latest_message.subject == expected_subject:
    
    if latest_message.body.startswith(expected_body_pattern):
        # get the action, which should be the end of the string after the expected pattern
        action = latest_message.body[len(expected_body_pattern) :]

        # make a new message which says we will do the action
        message = "I will now " + action

        # send our message in reply
        latest_message.reply(message)
        
    else: # else code for if the message body didn't match
        display("The message body (" + body + ") didn't match our pattern (" + expected_pattern + ")")
        
else: # else code for if the message subject didn't match
    display("The message subject (" + latest_message.subject + ") didn't match our expected subject (" + expected_subject + ")" )


# Yay! It worked! But there is a problem!

# ## Trolling bot 1
# This bot is really easy to troll, so if I repeat my steps and get a new mention (this code is just a duplication of the code above):

# In[8]:


# Look up the subreddit "cuteanimals", then find the "hot" list, getting up to 1 submission
messages = reddit.inbox.messages(limit=1)

# get the first submission off the list (should only be one anyway)
latest_message = next(messages) 

# display the subject and body of the message, so we can see what we found
display("latest message subject: " + str(latest_message.subject))
display("latest message body: " + str(latest_message.body))

expected_subject = "Wanting bot response"
expected_body_pattern = "I want you to "

# check if the mention text starts with our set phrase
if latest_message.subject == expected_subject:
    
    if latest_message.body.startswith(expected_body_pattern):
        # get the action, which should be the end of the string after the expected pattern
        action = latest_message.body[len(expected_body_pattern) :]

        # make a new message which says we will do the action
        message = "I will now " + action

        # sen our message in reply
        latest_message.reply(message)
        
    else: # else code for if the message body didn't match
        display("The message body (" + body + ") didn't match our pattern (" + expected_pattern + ")")
        
else: # else code for if the message subject didn't match
    display("The message subject (" + latest_message.subject + ") didn't match our expected subject (" + expected_subject + ")" )


# Someone messaged us saying at us: `I want you to do something horrible!`, and we replied `I will now do something horrible!`. 
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

# In[9]:


# Look up the subreddit "cuteanimals", then find the "hot" list, getting up to 1 submission
messages = reddit.inbox.messages(limit=1)

# get the first submission off the list (should only be one anyway)
latest_message = next(messages) 

# display the subject and body of the message, so we can see what we found
display("latest message subject: " + str(latest_message.subject))
display("latest message body: " + str(latest_message.body))


# ### If tweet matches our pattern, reply
# We do the same code for this as before, but after we get the action we are told to do, we put another `if`/`else` to either do the action if we recognize it, or say we didn't recognize the action.
# 
# We will use `in` to see if the action is in our list of allowed actions (called an allow_list)

# In[10]:


expected_subject = "Wanting bot response"
expected_body_pattern = "I want you to "

actions_allow_list = ["run", "jump", "fly"]

# check if the mention text starts with our set phrase
if latest_message.subject == expected_subject:
    
    if latest_message.body.startswith(expected_body_pattern):
        # get the action, which should be the end of the string after the expected pattern
        action = latest_message.body[len(expected_body_pattern) :]
        
        # See if it is one of our recognized actions
        if(action in actions_allow_list):
            # make a new message which says we will do the action
            message = "I will now " + action

            # send our message in reply
            latest_message.reply(message)
            
        else: # we didn't recognize the action
            # make a new message which says we will NOT do the action
            message = "I do not recognize the command " + action

            # send our message in reply
            latest_message.reply(message)
        
    else: # else code for if the message body didn't match
        display("The message body (" + body + ") didn't match our pattern (" + expected_pattern + ")")
        
else: # else code for if the message subject didn't match
    display("The message subject (" + latest_message.subject + ") didn't match our expected subject (" + expected_subject + ")" )



# That one was in our allow list so it worked. Let's do it all again, with the tweet that caused us problems last time
# 
# _Note: the code below is just copied from the code sections above_

# In[11]:


# Look up the subreddit "cuteanimals", then find the "hot" list, getting up to 1 submission
messages = reddit.inbox.messages(limit=1)

# get the first submission off the list (should only be one anyway)
latest_message = next(messages) 

# display the subject and body of the message, so we can see what we found
display("latest message subject: " + str(latest_message.subject))
display("latest message body: " + str(latest_message.body))

expected_subject = "Wanting bot response"
expected_body_pattern = "I want you to "

actions_allow_list = ["run", "jump", "fly"]

# check if the mention text starts with our set phrase
if latest_message.subject == expected_subject:
    
    if latest_message.body.startswith(expected_body_pattern):
        # get the action, which should be the end of the string after the expected pattern
        action = latest_message.body[len(expected_body_pattern) :]
        
        # See if it is one of our recognized actions
        if(action in actions_allow_list):
            # make a new message which says we will do the action
            message = "I will now " + action

            # send our message in reply
            latest_message.reply(message)
            
        else: # we didn't recognize the action
            # make a new message which says we will NOT do the action
            message = "I do not recognize the command " + action

            # send our message in reply
            latest_message.reply(message)
        
    else: # else code for if the message body didn't match
        display("The message body (" + body + ") didn't match our pattern (" + expected_pattern + ")")
        
else: # else code for if the message subject didn't match
    display("The message subject (" + latest_message.subject + ") didn't match our expected subject (" + expected_subject + ")" )


# Ok, this time we said `I do not recognize the command do something horrible!`. 
# 
# That looks a little better! Are we safe now?

# ## Trolling bot 2
# No, it turns out we are not safe.
# 
# Let's find the latest mention again and see what happens

# In[12]:


# Look up the subreddit "cuteanimals", then find the "hot" list, getting up to 1 submission
messages = reddit.inbox.messages(limit=1)

# get the first submission off the list (should only be one anyway)
latest_message = next(messages) 

# display the subject and body of the message, so we can see what we found
display("latest message subject: " + str(latest_message.subject))
display("latest message body: " + str(latest_message.body))

expected_subject = "Wanting bot response"
expected_body_pattern = "I want you to "

actions_allow_list = ["run", "jump", "fly"]

# check if the mention text starts with our set phrase
if latest_message.subject == expected_subject:
    
    if latest_message.body.startswith(expected_body_pattern):
        # get the action, which should be the end of the string after the expected pattern
        action = latest_message.body[len(expected_body_pattern) :]
        
        # See if it is one of our recognized actions
        if(action in actions_allow_list):
            # make a new message which says we will do the action
            message = "I will now " + action

            # send our message in reply
            latest_message.reply(message)
            
        else: # we didn't recognize the action
            # make a new message which says we will NOT do the action
            message = "I do not recognize the command " + action

            # send our message in reply
            latest_message.reply(message)
        
    else: # else code for if the message body didn't match
        display("The message body (" + body + ") didn't match our pattern (" + expected_pattern + ")")
        
else: # else code for if the message subject didn't match
    display("The message subject (" + latest_message.subject + ") didn't match our expected subject (" + expected_subject + ")" )


# Oh no! Someone tweeted at us:
# - `I want you to stop talking. But that doesn't mean I won't say horrible things like: I hate everybody!`
# 
# And we replied:
# - `I do not recognize the command stop talking. But that doesn't mean I won't say horrible things like: I hate everybody!`
# 
# Making a bot that is troll proof is very difficult! You either need to severely limit how your bot engages with people, or do a ton of work trying to prevent trolling and fix problems when people find a new way of trolling you.
# 
# If you want to learn more, you can revisit the story of what went wrong with the Microsoft Tay bot: [How to Make a Bot That Isn't Racist](https://www.vice.com/en_us/article/mg7g3y/how-to-make-a-not-racist-bot)
