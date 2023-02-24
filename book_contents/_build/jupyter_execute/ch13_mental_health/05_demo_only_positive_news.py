#!/usr/bin/env python
# coding: utf-8

# # Demo: Only positive news
# 
# Let's look at something we could try to do to improve the mental health for our users: Only show positive news!
# 
# We'll use sentiment analysis again, but this time we'll get posts from the news subreddit, but only display the tweets with a positive sentiment.
# 
# Would this actually improve someone's mental health? It's hard to say! But we can see something that we might try out if we wanted to improve mental health of our users.

# ## Normal Reddit PRAW Setup

# In[1]:


import praw


# (optional) make a fake praw connection with the fake_praw library
# 
# For testing purposes, we've added this line of code, which loads a fake version of praw, so it wont actually connect to reddit. __If you want to try to actually connect to reddit, don't run this line of code.__

# In[2]:


get_ipython().run_line_magic('run', '../fake_apis/fake_praw.ipynb')


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


# ## Load sentiment analyis code

# In[5]:


import nltk
nltk.download(["vader_lexicon"])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# ## Code to search and display news
# Now let's make code that will get submissions from the news subreddit (or from a fake_news_site), and display all of them. We will then make a modified version below to compare the results.

# In[6]:


# Look up the subreddit "news", then find the "hot" list, getting up to 10 submission
submissions = reddit.subreddit("news").hot(limit=10)

# Turn the submission results into a Python List
submissions_list = list(submissions)

# go through each reddit submission
for submission in submissions_list:
    print(submission.title)
    print()


# ## Search through news submissions and only display good news
# Now we will make a different version of the code that computes the sentiment of each submission title and only displays the ones with positive sentiment.

# In[34]:


# Look up the subreddit "news", then find the "hot" list, getting up to 10 submission
submissions = reddit.subreddit("news").hot(limit=10)

# Turn the submission results into a Python List
submissions_list = list(submissions)

# go through each reddit submission
for submission in submissions_list:
    
    #calculate sentiment
    title_sentiment = sia.polarity_scores(submission.title)["compound"]
    
    if(title_sentiment > 0):
        print(submission.title)
        print()


# ## Try it out on real Reddit
# If you want, you can skip the fake_praw step and try it out on real Reddit, from whatever subreddit you want
# 
# Did it work like you expected?
# 
# You can also only show negative sentiment submissions (sentiment < 0) if you want to see only bad news.
