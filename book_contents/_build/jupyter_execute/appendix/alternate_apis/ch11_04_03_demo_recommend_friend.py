#!/usr/bin/env python
# coding: utf-8

# # Ch 11.4.3: Demo: Recommend a User to Follow
# 
# Now let's look at a recommendation algorithm for a new person to friend or follow. Our algorithm will be
# 
# For a given user:
# 1. Look at the people this user follows
# 2. For each of those follows, look at who they follow
# 3. While doing this, keep track of what accounts showed up most 
# 4. Recommend the accounts that showed up the most (the users most followed by people followed by our given user)

# ## Normal Tweepy Set-Up

# In[1]:


# make sure tweepy library is installed
import tweepy


# (optional) use the fake version of tweepy, so you don’t have to use real twitter developer access passwords

# In[2]:


get_ipython().run_line_magic('run', '../../fake_tweepy/fake_tweepy.ipynb')


# In[3]:


# Load all your developer access passwords into Python
# TODO: Put your twitter account's special developer access passwords below:
bearer_token = "n4tossfgsafs_fake_bearer_token_isa53#$%$"
consumer_key = "sa@#4@fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"


# In[4]:


# Give the tweepy code your developer access passwords so
# it can perform twitter actions
client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)


# ## Make a helper function (id_from_username
# Now that we've learned functions, we will be putting much of our code in functions. 
# 
# So in order to simplify our code later, we will make a function that, when given a username, looks up the user and gets their id number (since we'll need to use that id later)

# In[5]:


def id_from_username(username):
    user_info = client.get_user(username=username)
    user_id = user_info.data.id
    return user_id


# ## Make a function to get follow suggestions
# Now we make a function that will generate follow suggestions.
# 
# The function takes a username (who we are making suggestions for), and a num_followers_to_check, which limits how many follows of our user we check (since Twitter limits how many requests we can make)
# 
# We then get a list of the follows for our user, and we create a dictionary counter (`possible_suggestion_counts`).
# 
# For each of our user's follows, we get a list of who they follow (the follow-follows). Then for each of the follow_follows, we see if that user is in the `possible_suggestion_counts` dictionary, and add it if it wasn't there (starting with 1), or add 1 to it if it was already there.
# 
# After the for loop we have counts for our possible suggestions (how often the follow-follows appeared). So we sort the list to put the most common ones at the top, and we return the results.

# In[6]:


def get_follow_suggestions(username, num_followers_to_check=3):
    # for a given user, I need to user id
    user_id = id_from_username(username)

    # find the people that user currently follows
    follow_users = client.get_users_following(id=user_id, max_results=num_followers_to_check)

    # dictionary to track who my follow follows are, as possible suggestions
    # The keys will be the username, and the values will be how often they
    # appeared as follow follows
    possible_suggestion_counts = {}

    # for each of those people, see who they follow
    for follow_user in follow_users.data:
        print("looking for followings of user: " + follow_user.username)
        follow_follow_users = client.get_users_following(id=follow_user.id)
        
        # print out the follow-follows (using some python tricks to make it display nicer)
        print("  the follow-follows are: " + str(list(map(lambda x: x.username, follow_follow_users.data))))

        for follow_follow_user in follow_follow_users.data:
            possible_suggestion = follow_follow_user.username

            # If this possible suggestion is not yet in the dictionary,
            # add it with a count of one
            if possible_suggestion not in possible_suggestion_counts:
                possible_suggestion_counts[possible_suggestion] = 1
            else: #otherwise, update the count in the dictionary
                possible_suggestion_counts[possible_suggestion] += 1

        print()

    # sort the suggestions by who appeared the most
    ordered_suggestions = sorted(possible_suggestion_counts.items(), key=lambda x: -x[1])
    # recommend that I follow the people who those people follow most
    return ordered_suggestions


# ## Test our function (suggest follows)
# Now that our function is ready, we can test it out and see who we suggest our "fake_user" should follow (if you skip fake_tweepy and log into real twitter, you can do this for real users)

# In[7]:


suggestions = get_follow_suggestions("fake_user", num_followers_to_check=5)

display(suggestions)


# If you skip the fake_tweepy step and run this on real Twitter, you might see some issues with the suggestions that we haven't accounted for, such as:
# - it might suggest the user follow themself, or someone they already follow
# - the follow lists can be very long and you might not be getting the whole list in the `client.get_users_following()` function call (you could use [pagination](https://docs.tweepy.org/en/stable/v2_pagination.html) to get more)
# 
# We could of course add more code to deal with those issues, but hopefully you can at least get the idea of how this recommendation algorithm works :)
