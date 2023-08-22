#!/usr/bin/env python
# coding: utf-8

# # Demo & Practice: Author Info
# 
# Though Reddit collects the device/program sources of submissions (like we saw from former President Trump), it unfortunately doesn't let us see them.
# 
# Instead we will look at other information about the author of posts on Reddit that can perhaps tell us something about their authenticity.

# ## Log into Reddit (PRAW)
# These are our normal steps get PRAW loaded and logged into Reddit

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


# ## Load a set of Reddit posts and look up author information
# 
# The code below searches for recent submissions from a subreddit, and then does a loop though all the tweets, printing out the information about the authors of the submissions, such as:
# - Link Karma (a measure of how much people like the links that person submits)
# - Comment Karma (a measure of how much people like the comments that person makes)
# 
# Try searching through other subreddits and see what you notice about the authors of posts in different subreddits.
# 
# To do this:
# - put in your special Reddit bot passwords
# - skip the fake_tweepy step above
# - take the first line of the code below and replace `cuteanimals` with a different subreddit name, like `movies`

# In[5]:


# Look up the subreddit "cuteanimals", then find the "hot" list, getting up to 10 submission
submissions = reddit.subreddit("cuteanimals").hot(limit=10)

# Turn the submission results into a Python List
submissions_list = list(submissions)

for submission in submissions_list:
    print("Info for submission: " + str(submission.title))
    print("  author: " + str(submission.author))
    print("  author's Link Karma: " + str(submission.author.link_karma))
    print("  author's Comment Karma: " + str(submission.author.comment_karma))
    print("  author has a verified email address? " + str(submission.author.has_verified_email))
    print("  author is a moderator of a subreddit? " + str(submission.author.is_mod))
    print("  author has active Reddit Premium status? " + str(submission.author.is_gold))
    print()


# In[ ]:




