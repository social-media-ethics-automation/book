#!/usr/bin/env python
# coding: utf-8

# # Demo: Track Tweepy Use
# In this code demo, we will take the `create_tweet` function that we've used several times earlier in this book, but now we will use the "wrapping function" trick from "Demo: Writing Functions" and track the uses of `create_tweet`. 
# 
# If we were being malicious we could track all the other Tweepy functions, hide the code we are using to wrap `create_tweet`, and send the results to some other account. In doing this we would violate the privacy of anyone who used tweepy with our malicious code.

# ## Normal Tweepy Set-Up

# In[1]:


import tweepy


#  (optional) use the fake version of tweepy, so you don't have to use real twitter developer access passwords

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


# ## Tracking the create_tweet function use

# In[5]:


# list to hold the information we are tracking
tweets_created = []

# save the original create_tweet function
old_create_tweet = client.create_tweet

# make a new create tweet function that will track information,
# then call the original create_tweet function
def new_create_tweet(text=""):
    tweets_created.append(text)
    
    old_create_tweet(text=text) 
    
# replace client.create_tweet with our new version, which also is tracking use
client.create_tweet = new_create_tweet


# In[6]:


client.create_tweet(text="I am using the tweepy library like normal")
client.create_tweet(text="There is no indication that anything is working differntly")
client.create_tweet(text="I might not realize these tweets are being tracked")


# So, our calls to `client.create_tweet` worked like normal.
# 
# But if I look at the `tweets_created` variable I can see all the tweets there

# In[7]:


display(tweets_created)


# Now, if we were being malicious, we would hide this code in some other code library we would try to convince you to use, that way you wouldn't notice the code. And instead of just saving those tweets to a variable, we would send it to ourselves, perhaps by putting code into our new_create_tweet to log into a different twitter account and private messaged that info to ourselves.

# ## How can we trust code libraries?
# If people can make code libraries track us and violate our privacy, how can we trust them? We could try looking at the [source code for tweepy](https://github.com/tweepy/tweepy/blob/ad5e31be58965d67e353128f711857a47f8d45d0/tweepy/client.py#L714) to try and make sure the library we are using isn't doing anything bad, but no programmer can be expected to read through all the libraries they use. There is unfortunately no simple answer to this.
# 
# In fact, there are cases where people have messed with code libraries:
# - The United States National Security Agency "[paid massive computer security firm RSA $10 million to promote a flawed encryption system so that the surveillance organization could wiggle its way around security.](https://gizmodo.com/nsa-paid-security-firm-10-million-bribe-to-keep-encryp-1487442397)"
#   - Does US national security outweigh global computer security? 
# - Shortly after the Russian invasion of Ukraine in 2022, someone modified a popular NodeJS code library so that it would [automatically destroy files if it was run on a computer in Russia or Belarus](https://arstechnica.com/information-technology/2022/03/sabotage-code-added-to-popular-npm-package-wiped-files-in-russia-and-belarus/).
#   - Does opposing a military invasion justify sabatoging a code library? 
#   
# And those are just the intentional problems with code libraries. All sorts of code libraries and computer programs are full of security flaws, which are regularly discovered and fixed (though who knows how much the flaws were exploited first).
# 
