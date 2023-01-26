#!/usr/bin/env python
# coding: utf-8

# # Demo: Track Use of Sentiment Analysis Code
# In this code demo, we will take the sentiment analysis code we used in the last chapter (Data Mining), and we will turn it into a function which will make it easier to use.
# 
# After turning it into a function though, we will add code to that function to track how it is used. We could theoretically take this information we are tracking and send to results to some other account.
# 
# This sort of tracking can be part of tracking program [telemetry](https://en.wikipedia.org/wiki/Telemetry#Software), which can be useful in figure out where software is broken or where it is most or least useful. But it can also be violating the privacy of anyone using our funtion who doesn't know we are tracking its use, or used maliciously to steal user information.

# ## Reddit PRAW Setup

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


# ### load sentiment analysis library and make analyzer

# In[5]:


import nltk
nltk.download(["vader_lexicon"])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# ### original code to loop through submissions, finding average sentiment
# This is the code from chapter 8 that loops through submissions in the "cuteanimals" subreddit and calculates the average sentiment

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


# ## Make a function using the code above for finding the average sentiment
# We now make a function of that code above by doing the following:
# - Add a `def` line at the start to make a function called `find_average_sentiment`
# - Indent all the old code so that it becomes the contents of the function `find_average_sentiment`
# - Make the function take two arguments:
#   - `subreddit_name`, which takes place of "cuteanimals", so the person calling the function can choose which subreddit to search
#   - `display_progress` which defaults to False. This decides whether or not the print statements are run when the function is run, so we can see the progress if we want, or just get the answer by default
# - At the end of the function, return the average_sentiment as the result

# In[7]:


def find_average_sentiment(subreddit_name, display_progress = False):
   num_submissions = 0
   total_sentiment = 0

   # Look up the subreddit given as a parameter, then find the "hot" list, getting up to 10 submission
   submissions = reddit.subreddit(subreddit_name).hot(limit=10)

   # Turn the submission results into a Python List
   submissions_list = list(submissions)

   for submission in submissions_list:
       #calculate sentiment
       submission_sentiment = sia.polarity_scores(submission.title)["compound"]
       num_submissions += 1
       total_sentiment += submission_sentiment

       if(display_progress):
           print("Sentiment: " + str(submission_sentiment))
           print("   Submission Title: " + submission.title)
           print()



   average_sentiment = total_sentiment / num_submissions
   if(display_progress):
       print("Average sentiment was " + str(average_sentiment))
   
   return average_sentiment


# Now let's try using the function

# In[8]:


find_average_sentiment("cuteanimals")


# In[9]:


find_average_sentiment("science", display_progress=True)


# ## Modify the function so it tracks use
# Now we make another version of the same function, but with a small difference:
# - We make a list variable called `sentiment_searches` which exists outside the function.
# - At the start of the function we add the subreddit being searched to that list.
# This way, as the function gets used, we'll keep a history of its use in the `sentiment_searches` list

# In[10]:


# Make a list to save what subreddit was used for each time `find_average_sentiment` is run
sentiment_searches = []

def find_average_sentiment(subreddit_name, display_progress = False):
    
    # Add the current subreddit being searched to the sentiment_searches list
    sentiment_searches.append(subreddit_name)
    
    num_submissions = 0
    total_sentiment = 0

    # Look up the subreddit name given as a parameter, then find the "hot" list, getting up to 10 submission
    submissions = reddit.subreddit(subreddit_name).hot(limit=10)

    # Turn the submission results into a Python List
    submissions_list = list(submissions)

    for submission in submissions_list:
        #calculate sentiment
        submission_sentiment = sia.polarity_scores(submission.title)["compound"]
        num_submissions += 1
        total_sentiment += submission_sentiment

        if(display_progress):
            print("Sentiment: " + str(submission_sentiment))
            print("   Submission Title: " + submission.title)
            print()



    average_sentiment = total_sentiment / num_submissions
    if(display_progress):
        print("Average sentiment was " + str(average_sentiment))
    
    return average_sentiment


# Now let's run this version of the function

# In[11]:


find_average_sentiment("cuteanimals")


# In[12]:


find_average_sentiment("science")


# It looks like it works like normal, but our calls to the function have been tracked!

# In[13]:


display(sentiment_searches)


# Now, if we were being malicious, we would hide this code in some other code library we would try to convince you to use, that way you wouldn't notice the code. And instead of just saving those tweets to a variable, we would send it to ourselves, perhaps by putting code into our new_create_tweet to log into a different twitter account and private messaged that info to ourselves.

# ## How can we trust code libraries?
# If people can make code libraries track us and violate our privacy, how can we trust them? We could try looking at the [source code for the PRAW library](https://github.com/praw-dev/praw/) to try and make sure the library we are using isn't doing anything bad, but no programmer can be expected to read through all the libraries they use. There is unfortunately no simple answer to this.
# 
# In fact, there are cases where people have messed with code libraries:
# - The United States National Security Agency "[paid massive computer security firm RSA $10 million to promote a flawed encryption system so that the surveillance organization could wiggle its way around security.](https://gizmodo.com/nsa-paid-security-firm-10-million-bribe-to-keep-encryp-1487442397)"
#   - Does US national security outweigh global computer security? 
# - Shortly after the Russian invasion of Ukraine in 2022, someone modified a popular NodeJS code library so that it would [automatically destroy files if it was run on a computer in Russia or Belarus](https://arstechnica.com/information-technology/2022/03/sabotage-code-added-to-popular-npm-package-wiped-files-in-russia-and-belarus/).
#   - Does opposing a military invasion justify sabatoging a code library? 
#   
# And those are just the intentional problems with code libraries. All sorts of code libraries and computer programs are full of security flaws, which are regularly discovered and fixed (though who knows how much the flaws were exploited first).
# 
