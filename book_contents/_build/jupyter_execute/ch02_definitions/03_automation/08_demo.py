#!/usr/bin/env python
# coding: utf-8

# # Demo: Try Running the Reddit Bot!

# ## Running this Jupyter Notebook
# This page is called a "Jupyter Notebook" which it is a text page that has runnable Python code in it.
# 
# In order to run the code, you can look for the rocket button at the top which will give you an option to "launch binder"
# 
# ![screenshot of this page in the online textbook, with the launch binder link highlighted under the rocket button at the top.](binder_link.png)
# 
# If you launch binder, it will take a while to load, but eventually show you a version of this page Jupyter Notebook in a code editor called Jupyter Lab
# 
# ![a screenshot of this page viewed in jupyter_lab, with menus and options above the editable page](jupyter_lab.png)
# 
# In Jupyter Lab you can double click any section to edit it, and you can press the triangle "run" button to run the code (or display the text).
# 
# ![a screenshot of this page viewed in jupyter_lab,with the triangle "run" button circled. Next to it are a square "interrupt the kernal" button and other options](jupyter_run_code.png)
# 
# When the code runs, the little number to the left of the code block should change. There might also be some output from your action displyed below the code block.
# 
# So now you can go through the rest of this page and select and run each section of code.
# 

# ## Here is the bot code you can run!
# Our demo Reddit bot code is below, broken up into different sections. 
# 
# You can select each section of the code below and run it to see what it does.
# 
# By default this code uses a fake version of our reddit connection so it doesn't connect to a real reddit account.
# 
# If you want to actually connect to your reddit account, you can put your special developer access passwords in the right code section below, and then when you run the code make sure to skip the code section that makes a fake twitter connection with "fake_praw".

# ### Step 1: Load praw code

# In[1]:


# Load some code called "praw" that will help us work with reddit
import praw


# ### (Optional) Step 1b: Make a fake praw connection with the fake_praw library
# For testing purposes, we've added this line of code, which loads a fake version of praw, so it wont actually connect to reddit. __If you want to try to actually connect to reddit, don't run this line of code.__

# In[2]:


get_ipython().run_line_magic('run', '../../fake_apis/fake_praw.ipynb')


# ### Step 2: Load your developer access passwords
# To use this on your real twitter account, copy your [developer access passwords](../../appendix/bot_set_ups/making_reddit_account.md) into the code below, replacing our fake passwords.

# In[3]:


# Load all your developer access passwords into Python
# TODO: Put your reddit username, password, and special developer access passwords below:
username="fake_reddit_username"
password="sa@#4*fdf_fake_password_$%DSG#%DG"
client_id="45adf$TW_fake_client_id_JESdsg1O"
client_secret="56sd_fake_client_secret_%Yh%"


# ### Step 4: Give praw (or fake_praw) your developer access passwords

# In[4]:


# Give the praw code your reddit account info so
# it can perform reddit actions
reddit = praw.Reddit(
    username=username, password=password,
    client_id=client_id, client_secret=client_secret,
    user_agent="a custom python script"
)


# ### Step 5: Submit a post to reddit

# In[5]:


# Post a reddit post
# TODO: modify the text in the quotes below to change what and where this bot posts to reddit:
reddit.subreddit(
   "soc_media_ethics_auto"
).submit(
   "A bot post", 
   selftext = "This post was made by a computer program!"
)


# ### Step 6: Modify the code above to create a different reddit post
# 

# In[ ]:




