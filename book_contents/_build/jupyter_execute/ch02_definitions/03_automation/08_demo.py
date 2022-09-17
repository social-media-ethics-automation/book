#!/usr/bin/env python
# coding: utf-8

# # Demo: Try Running the Twitter Bot!

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
# Our demo Twitter bot code is below, broken up into different sections. 
# 
# You can select each section of the code below and run it to see what it does.
# 
# By default this code uses a fake version of our twitter connection so it doesn't connect to a real twitter account.
# 
# If you want to actually connect to your twitter account, you can put your special developer access passwords in the right code section below, and then when you run the code make sure to skip the code section that makes a fake twitter connection with "fake_tweepy".

# ### Step 1: Load Tweepy code

# In[1]:


# Load some code called "tweepy" that will help us work with twitter
import tweepy


# ### (Optional) Step 1b: Make a fake twitter connection with the fake_tweepy library
# For testing purposes, we've added this line of code, which loads a fake version of tweepy, so it wont actually connect to twitter. __If you want to try to actually connect to twitter, don't run this line of code.__

# In[2]:


get_ipython().run_line_magic('run', '../../fake_tweepy/fake_tweepy.ipynb')


# ### Step 2: Load your developer access passwords
# To use this on your real twitter account, copy your [developer access passwords](../../prefaces/making_twitter_account.md) into the code below, replacing our fake passwords.

# In[3]:


# Load all your developer access passwords into Python
# TODO: Put your twitter account's special developer access passwords below:
bearer_token = "n4tossfgsafs_fake_bearer_token_isa53#$%$"
consumer_key = "sa@#4@fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"


# ### Step 4: Give tweepy (or fake_tweepy) your developer access passwords

# In[4]:


# Give the tweepy code your developer access passwords so
# it can perform twitter actions
client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)


# ### Step 5: Post a tweet

# In[5]:


# Post a tweet
# TODO: modify the text in the quotes below to change what this bot tweets:
client.create_tweet(text="This tweet was posted by a computer program!")


# ### Step 6: Modify the code above to post a different tweet
# Note: If you try to post the same exact tweet twice in a row on real twitter, you will get an error message (it will be a lot of red text, which can be intimidating, but it just means you aren't allowed to post the same tweet twice in a row).

# In[ ]:




