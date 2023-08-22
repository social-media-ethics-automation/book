#!/usr/bin/env python
# coding: utf-8

# # Demo: Sentiment Analysis on Reddit
# 
# Now let's try using sentiment analysis (and loop variables) on Reddit:
# 
# We'll start by doing our normal steps to load Reddit PRAW (or fake praw)
# 
# ## Reddit PRAW Setup

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


# ## Sentiment Analysis
# ### load sentiment analysis library and make analyzer

# In[5]:


import nltk
nltk.download(["vader_lexicon"])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# ### loop through submissions, finding average sentiment
# We can now combine our previous examples of looping through reddit submissions with what we just learned of sentiment analysis and looping variables to find the average sentiment of a set of submission titles.

# In[6]:


num_submissions = 0
total_sentiment = 0

# Look up the subreddit "cuteanimals", then find the "hot" list, getting up to 10 submission
submissions = reddit.subreddit("cuteanimals").hot(limit=10)

# Turn the submission results into a Python List
submissions_list = list(submissions)

for submission in submissions_list:
    #calculate sentiment
    submission_sentiment = sia.polarity_scores(submission.title)["compound"]
    num_submissions += 1
    total_sentiment += submission_sentiment

    print("Sentiment: " + str(submission_sentiment))
    print("   Submission Title: " + submission.title)
    print()



average_sentiment = total_sentiment / num_submissions
print("Average sentiment was " + str(average_sentiment))


# We can now see the average sentiment of a set of reddit post titles based on our search of a subreddit! 
# 
# If you use your reddit bot keys, you can change the `subreddit` to be whatever one you want and see whether people are posting positively or negatively in it. 
# 
# _note: You can change `limit=10` to go up higher to get more submissions at a time to find the average of_
