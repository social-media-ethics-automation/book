#!/usr/bin/env python
# coding: utf-8

# # Demo: Recommend a Subreddit
# 
# Now let's look at a recommendation algorithm for a new subreddit to follow. Our algorithm will be
# 
# For a given subreddit:
# 1. Make a list of the accounts who made the most recent posts to the subreddit
# 2. For each of those accounts, look up what subreddits they also follow
# 3. While doing this, keep track of what subreddits showed up most 
# 4. Recommend the subreddits that showed up the most (the subreddits followed by people posting in a given subreddit)

# ## Normal Reddit PRAW Setup

# In[1]:


import praw


# (optional) use the fake version of Reddit praw, so you don't have to use real Reddit developer access passwords

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


# ## Make a function to get subreddit suggestions
# Now we make a function that will generate subreddit suggestions.
# 
# The function takes a subreddit name to start with, and also two optional arguments: `num_subreddit_posts` for how many posts it should look through in the starting subreddit, and `num_author_posts` for how many other posts by the post authors it should look through.
# 
# We first get a list of submissions to the given starting subreddit. Then we create a dictionary counter (`possible_suggestion_counts`).
# 
# For each of the submissions to the starting subreddit, we find the author. Then for the author we look at their recent submissions and see what subreddit that submission was on. We make sure it isn't an over18 (NSFW) subreddit, and then call it a `possible_suggestion`
# 
# We then check and see if our `possible_suggestion` subreddit is already in the `possible_suggestion_counts` dictionary. If it wasn't already in the dictionary we add it (starting with a count of 1), otherwise add 1 to the count if it was already there.
# 
# After the for loop we have counts for our possible suggestion subreddits. So we sort the list to put the most commonly appearing ones at the top, and we return the results.

# In[5]:


def get_follow_suggestions(subreddit_name, num_subreddit_posts=10, num_author_posts=10):
    
    # Look up the given subreddit, then find the "hot" list, getting up to 10 submission
    submissions = reddit.subreddit(subreddit_name).hot(limit=num_subreddit_posts)

    # Turn the submission results into a Python List
    submissions_list = list(submissions)
    
    # dictionary to track subreddits posted to by the authors of those submissions
    # which will be possible suggestions
    # The keys will be the username, and the values will be how often they
    # appeared as post subreddits for authors of the subreddit we are starting with
    possible_suggestion_counts = {}

    # Go through each of the posts on the subreddit we are starting with
    for submission in submissions_list:
        
        # display some information about the post we are looking at
        print("Getting info for submission: " + str(submission.title))
        print("  author: " + str(submission.author))
        
        # Get the latest submissions from the author of that post
        latest_author_submissions = submission.author.submissions.new(limit=num_author_posts)
        
        # For each of those posts by that author, we'll look at what subreddit it was on
        for author_submission in latest_author_submissions:

            # A lot of subreddits are not safe for work, so we'll skip those...
            if(not author_submission.subreddit.over18):
                
                # Get the name of the subreddit that post was made in
                possible_suggestion = author_submission.subreddit.display_name
                
                # If this possible suggestion is not yet in the dictionary,
                # add it with a count of one
                if possible_suggestion not in possible_suggestion_counts:
                    possible_suggestion_counts[possible_suggestion] = 1
                else: #otherwise, update the count in the dictionary
                    possible_suggestion_counts[possible_suggestion] += 1

    # sort the suggestions by who appeared the most
    ordered_suggestions = sorted(possible_suggestion_counts.items(), key=lambda x: -x[1])

    # return our recommendations for subreddits to follow
    return ordered_suggestions


# ## Test our function (suggest follows)
# Now that our function is ready, we can test it out and see who we suggest our "fake_user" should follow (if you skip fake_tweepy and log into real twitter, you can do this for real users)

# In[6]:


suggestions = get_follow_suggestions("cuteanimals")

display("suggested subreddits:")
display(suggestions)


# ## Try it youself!
# If you skip the fake_praw step and run this on real Reddit, you might notice:
# - The top suggestion is often the subreddit you are already looking at
# - If the same author posted multiple times in our starting subreddit, we count all the places they posted again (double counting)
# - There might still be some offensive subreddits even after we tried to filter out specifically labeled NSFW ones
# - the suggestion lists can be very long, even if you are only looking at the default num_subreddit_posts=10 and num_author_posts=10
# 
# We could of course add more code to deal with those issues, but hopefully you can at least get the idea of how this recommendation algorithm works :)

# In[ ]:




