#!/usr/bin/env python
# coding: utf-8

# # Demo: Dictionaries
# 
# We've talked about lists, but the other data organization we need to work with social media data is `dictionaries`.
# 
# As we mentioned in chapter 4, dictionaries allow us to combine pieces of information by naming them (sort of like variables).
# 
# So for example, the information about a user might have the following pieces of data:
# - Username
# - Twitter handle
# - Profile Picture:
# - Follows
# 
# Python has two ways of doing these types of dictionaries: `dict` and objects

# ## Dictionaries (`dict`)
# We can create dictionaries in Python by storing values into `key`s inside of curly braces `{` `}`, like this:

# In[1]:


user_1 = {
    "username": "kylethayer",
    "twitter_handle": "@kylemthayer",
    "profile_picture": "kylethayer.jpg",
    "follows": ["@SusanNotess", "@UW", "@UW_iSchool", "@ajlunited"]
}


# In the code above, inside of the curly braces are a set of lines. Each line has a string (the `key`, or name of the value), followed by a colon (`:`), followed by a value that is to be saved for the key. At the end of all but the last line is a comma (`,`) which indicates that another `key` and value will come next.
# 
# Now that we've saved some values for some keys in the dictionary now saved in user_1, we can look up the values by using square brackets (`[`, `]`) with the key name inside, like this:

# In[2]:


user_1_username = user_1["username"]
display(user_1_username)


# In[3]:


user_1_handle = user_1["twitter_handle"]
display(user_1_handle)


# In[4]:


user_1_picture = user_1["profile_picture"]
display(user_1_picture)


# In[5]:


user_1_follows = user_1["follows"]
display(user_1_follows)


# ## Objects
# The other way of saving information that works similarly in Python is through an object. We won't be creating any in this book, but we will have to get data from some.
# 
# The main difference from what we will need is that while in dictionaries we use square brackets and put the key name in quotes as a string (e.g., `user_1["profile_picture"]`), in an object you use a period (`.`) and don't put they key name (called a `field`) in quotes (e.g., `user_1.profile_picture`)
# 
# We have already seen code that used this period to get something from an object a few times, specifically getting functions from them, like:
# - `client.create_tweet(...`
# - `normal_message.upper()`
# 
# When we go through data from twitter, sometimes we will need to use `.` to get parts of the information out of objects, and sometimes we will need to use `[" "]` to get information out of dictionaries.

# ## Looping through lists of dictionaries
# Now that we've seen loops, lists, and dictionaries, we can go to Reddit, run a search and look through multiple submissions:

# ### load praw library

# In[6]:


# Load some code called "praw" that will help us work with reddit
import praw


# ### (Optional) make a fake praw connection with the fake_praw library
# For testing purposes, we've added this line of code, which loads a fake version of praw, so it wont actually connect to reddit. __If you want to try to actually connect to reddit, don't run this line of code.__

# For testing purposes, we’ve added this line of code, which loads a fake version of tweepy, so it wont actually connect to twitter. __If you want to try to actually connect to twitter, don’t run this line of code.__

# In[7]:


get_ipython().run_line_magic('run', '../../fake_apis/fake_praw.ipynb')


# ### load your developer access passwords

# In[8]:


# Load all your developer access passwords into Python
# TODO: Put your reddit username, password, and special developer access passwords below:
username="fake_reddit_username"
password="sa@#4*fdf_fake_password_$%DSG#%DG"
client_id="45adf$TW_fake_client_id_JESdsg1O"
client_secret="56sd_fake_client_secret_%Yh%"


# ### give praw (or fake_praw) your developer access passwords

# In[9]:


# Give the praw code your reddit account info so
# it can perform reddit actions
reddit = praw.Reddit(
    username=username, password=password,
    client_id=client_id, client_secret=client_secret,
    user_agent="a custom python script"
)


# ### find a list of submissions
# We can now do a search and find a list of submissions.
# 
# _Note: If you run this on real reddit, we can’t gurantee anything about how offensive what you might find is._

# In[10]:


# Look up the subreddit "cuteanimals", then find the "hot" list, getting up to 10 submission
submissions = reddit.subreddit("cuteanimals").hot(limit=10)

# Note: The submissions come back from Reddit as an
# "iterator" instead of a "list." We can write our
# normal for loops with it as an iterator, but we will
# turn it into a list, since we are using those in this class

submissions_list = list(submissions)


# ## Loop through the list of submissions
# The variable `submissions_list` now has a list of Reddit submissions. So we can use a for loop to go through each submission, and then use `.` to access info from each tweet (other pieces of information would need `[" "]` to access).
# 
# For each of the tweets, we will use `print` to display information about the tweet

# In[11]:


for submission in submissions_list:
    print("Info for submission with id: " + str(submission.id))
    print("  title: " + str(submission.title))
    print("  author: " + str(submission.author))
    print("  created_utc: " + str(submission.created_utc))
    print("  selftext: " + str(submission.selftext))
    print("  url: " + str(submission.url))
    print("  score (upvotes): " + str(submission.score))
    print()

