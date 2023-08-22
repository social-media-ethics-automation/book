#!/usr/bin/env python
# coding: utf-8

# # Demo: Data from a Reddit Post
# Let's see what the data actually looks like from a Reddit Post!
# 
# First we need to do our normal Reddit login steps (and optional fake praw step)
# ## Log into Praw (or fake praw)
# ### Load Praw library

# In[1]:


# Load some code called "praw" that will help us work with reddit
import praw


# ### (Optional) Step 1b: Make a fake praw connection with the fake_praw library
# For testing purposes, we've added this line of code, which loads a fake version of praw, so it wont actually connect to reddit. __If you want to try to actually connect to reddit, don't run this line of code.__

# In[2]:


get_ipython().run_line_magic('run', '../../fake_apis/fake_praw.ipynb')


# ### Step 2: Load your developer access passwords
# To use this on your real Reddit account, copy your [developer access passwords](../../appendix/bot_set_ups/making_reddit_account.md) into the code below, replacing our fake passwords.

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


# ## Find a Reddit submission
# Below I have the code to find a recent Reddit submission on the subreddit "[cuteanimals](https://www.reddit.com/r/cuteanimals)" (we'll get the top post on the default reddit view, called "hot").. 
# 
# Don't worry if you don't understand this part yet. We are
# just doing this, so we can get to the point of seeing what tweet data looks like.
# 
# _Note: If you run this on real reddit, we can't gurantee anything about how offensive what you might find is._

# In[5]:


# Look up the subreddit "cuteanimals", then find the "hot" list, getting up to 1 submission
submissions = reddit.subreddit("cuteanimals").hot(limit=1)

# get the first submission off the list (should only be one anyway)
recent_submission = next(submissions) 


# ## Look at data in Reddit submission
# 
# Now we will look at some of the data that came back!
# 
# Again, don't worry too much about the code, we want to look at the data and data types.
# 
# ### submission title:

# In[6]:


display("The data type of the submission title is: " + type(recent_submission.title).__name__)
display("The submission title is: " + recent_submission.title)


# As you can see above, the title of a submission is a string (`str`) data type. 

# ### submission id

# In[7]:


display("The data type of the submission id is: " + type(recent_submission.id).__name__)
display("The submission id is: " + str(recent_submission.id))


# The submission id is a piece of text (`str`) that looks like random letters and numbers. This is how the submission is referred to inside Reddit's computers. So if someone is commenting on a submission, Reddit just puts uses submission ID they were commenting on to see where to display it.

# ### submission author name

# In[8]:


display("The data type of the author name is: " + type(recent_submission.author.name).__name__)
display("The author name is: " + str(recent_submission.author.name))


# The author name is an string (`str`). Note recent_submission.author has other information about the author as well as the name.

# ### submission edited

# In[9]:


display("The data type of edited is: " + type(recent_submission.edited).__name__)
display("The submission edited is: " + str(recent_submission.edited))


# The "edited" field represents whether a submission has been edited or not. It is a boolean true/false value (`bool`).

# ### tweet created at

# In[10]:


display("The data type of the tweet created_utc at is: " + type(recent_submission.created_utc).__name__)
display("The created_utc at is: " + str(recent_submission.created_utc))

# convert the utc to a different datetime
import datetime
converted_time = datetime.datetime.fromtimestamp(recent_submission.created_utc)
display("The data type of the converted_time at is: " + type(converted_time).__name__)
display("The converted_time at is: " + str(converted_time))


# The created at time for the submission is a floating point number (`float`), which is in [Unix Time](https://en.wikipedia.org/wiki/Unix_time), which is the number of seconds since Jan 1, 1970 in the [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) zone.
# 
# This is not a very useful number, so we use a python library called `datetime` to convert it into a more readable `datetime` data type, which we then can display and read easier.

# ### number of upvotes (score)

# In[11]:


display("The data type of the score is: " + type(recent_submission.score).__name__)
display("The submission score is: " + str(recent_submission.score))


# The number of upvotes is called `score` and it is a whole number (`int`). 

# ### upvote ratio

# In[12]:


display("The data type of the upvote ratio is: " + type(recent_submission.upvote_ratio).__name__)
display("The submission upvote ratio is: " + str(recent_submission.upvote_ratio))


# The upvote ratio (how many upvotes divided by total number of votes including downvotes) is a floating point number (`float`). 

# ### number of comments

# In[13]:


display("The data type of num_comments is: " + type(recent_submission.num_comments).__name__)
display("The submission number of comments is: " + str(recent_submission.num_comments))


# The number of comments is a whole number (`int`). Note: You can also get a data structure of all the comments, but we will look at that later.

# ### submission text (selftext)

# In[14]:


display("The data type of selftext is: " + type(recent_submission.selftext).__name__)
display("The submission selftext is: " + str(recent_submission.selftext))


# The submission selftext (the contents of the post if the post isn't a link url), is a string (`str`). Note that a submission can either be text saved as `selftext`, or a link (e.g., image or news story) saved as `url`. 

# ### submission url (link)

# In[15]:


display("The data type of url is: " + type(recent_submission.url).__name__)
display("The submission url is: " + str(recent_submission.url))


# The submission url is a string (`str`).

# ## Still more!
# In addition to the data we looked at above, there are even more options for reddit submissions, which you can see in the table of "attributes" at the top of the [PRAW library page on Submissions](https://praw.readthedocs.io/en/stable/code_overview/models/submission.html). You can also see the "attributes tables in the PRAW library pages for [Redditors](https://praw.readthedocs.io/en/stable/code_overview/models/redditor.html) and [Comments](https://praw.readthedocs.io/en/stable/code_overview/models/comment.html)
