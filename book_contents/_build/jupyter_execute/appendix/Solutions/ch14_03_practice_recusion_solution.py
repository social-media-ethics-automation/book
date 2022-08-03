#!/usr/bin/env python
# coding: utf-8

# # Recursion

# ## Twitter Practice

# #### Normal set up: run the following code block

# In[1]:


# Install variable inspector (then reload browser tab)
get_ipython().system('pip install lckr-jupyterlab-variableinspector')

# make sure tweepy library is installed
get_ipython().system('pip install tweepy')
import tweepy

# load my twitter keys
import my_bot_keys

# log into tweepy
client = tweepy.Client(
    bearer_token=my_bot_keys.bearer_token,
    consumer_key=my_bot_keys.consumer_key, consumer_secret=my_bot_keys.consumer_secret,                   
    access_token=my_bot_keys.access_token, access_token_secret=my_bot_keys.access_token_secret
)


# ### Getting Tweet Metrics

# Tweet metrics represent public information attached to any given tweet. This information incudes retweet count, reply count, like count, and quote count.

# #### To find the ID of a tweet:
# 
# The last number section of a tweet url is the ID of the tweet.
# 
# If you open a tweet on twitter, you can see the url in the menu bar:
# 
# &nbsp; &nbsp; &nbsp; <img src="tweet_url.jpg" alt="the url of a tweet highlighted, with the last number part circled" width="300" />
# 
# 
# or you can copy the link to the tweet and you can paste it in your browser to see the url
# 
# &nbsp; &nbsp; &nbsp; <img src="copy_link_to_tweet.jpg" alt="on a tweet the share button is circled and then the copy link to tweet option is circled" width="300"/>

# #### You can get tweet metrics by specifying "public_metrics" in the tweet_fields parameter:

# In[2]:


# This is the structure. Try running this code block:

tweet_id = 1130510065289404416

tweet_info = client.get_tweet(tweet_id, tweet_fields = "public_metrics")

tweet_metrics = tweet_info.data.public_metrics

print(tweet_metrics)


# #### 1. YOU TRY: Go on twitter and find your favorite tweet. Print the tweet metrics of that tweet using the structure from the example above. 
# 
# #### *NOTE: for this question, you can hard code the tweet ID

# In[3]:


tweet_id = 35767743634481152

tweet_info = client.get_tweet(tweet_id, tweet_fields = "public_metrics")

tweet_metrics = tweet_info.data.public_metrics

print(tweet_metrics)


# #### 2. Write a function that takes in a tweet ID as a paramter and returns the tweet metrics.

# In[4]:


def get_tweet_metrics(tweet_ID):
    tweet_info = client.get_tweet(tweet_ID, tweet_fields = "public_metrics")
    tweet_metrics = tweet_info.data.public_metrics
    return tweet_metrics


# #### 3. Call that function with a tweet ID of your choosing.

# In[5]:


tweet_ID = 35767743634481152
get_tweet_metrics(tweet_ID)


# #### 4. Search for recent tweets with the query "pike place" and save the list in the variable `pike_tweets`. Loop through the `pike_tweets` & print the text and the metrics of each tweet.

# In[6]:


query = "pike place"

pike_tweets = client.search_recent_tweets(query=query).data
#print(weather_tweets)

for tweet in pike_tweets:
    print(tweet.text)
    tweet_id = tweet.id
    metrics = get_tweet_metrics(tweet_id)
    print(metrics)
    print()


# #### 5. Write a function that takes in a tweet ID and returns "trending" if it has more than 10 replies, ELSE it returns "stagnant".

# In[7]:


def trend_machine(tweet_ID):
    metrics = get_tweet_metrics(tweet_ID)
    if metrics['reply_count'] > 10:
        return "trending"
    else:
        return "stagnant"


# #### 6. Call the function with a tweet ID of your chioce.

# In[8]:


tweet_id = 1234
trend_machine(tweet_id)


# ## Practice with recursion

# First we'll create a simplified tweet and reply structure like was demoed in lecture 14, though this time we'll include username information for each tweet.

# In[9]:


# run this code block
tweet_about_exam = {
    'text': 'That last exam in sure was hard!',
    'username': 'Emma',
    'replies':[{
        'text': 'It sure was hard, what score did you get? ',
        'username': 'Fatima',
        'replies': [{
            'text': 'I got a 67% :(',
            'username': 'Kwesi',
            'replies': []
        },{
            'text': 'I got a 73%',
            'username': 'Ying',
            'replies': []
        }]
    }, {
        'text': 'I didn\'t think it was that bad',
        'username': 'Maria',
        'replies': [{
            'text': 'how was that not a super hard exam?',
            'username': 'Dmitri',
            'replies': []
        }, {
            'text': 'of course you didn\'t',
            'username': 'Emma',
            'replies': [{
                'text': 'what\'s that supposed to mean?',
                'username': 'Maria',
                'replies': [{
                    'text': 'you\'re an overacheiver',
                    'username': 'Emma',
                    'replies': [{
                        'text': 'and that\'s bad how?',
                        'username': 'Maria',
                        'replies': []
                    }]
                }]
            }]
        }]
    }]
}

display(tweet_about_exam)


# ### This is the code form lecture 14 to print tweets and replies

# In[10]:


# try running this code block
def print_tweet_and_replies(tweet, num_indents=0):
    # print indent first
    for i in range(num_indents):
        print('   ', end='')
        
    # print tweet
    print('-' + tweet['text'])
    
    #print replies (and the replies of those, etc.)
    for reply in tweet['replies']:
        print_tweet_and_replies(reply, num_indents = num_indents + 1)

print_tweet_and_replies(tweet_about_exam)


# ### 7. Your turn: Make a copy of the code above and modify it so it also prints out the username of who made the tweet. Your output should have this exact structure:
# 
# ```
# "That last exam in sure was hard!"
#         -Emma
#    "It sure was hard, what score did you get?"
#            -Fatima
#    ...
# ```

# In[11]:


def print_tweet_and_replies(tweet, num_indents=0):
    # print indent first
    for i in range(num_indents):
        print('   ', end='')
        
    # print tweet
    print('"' + tweet['text'] + '"')
    
    # print indent before usernmae
    for i in range(num_indents):
        print('   ', end='')
    
    #print useraname
    print('        -' + tweet['username'])
    
    #print replies (and the replies of those, etc.)
    for reply in tweet['replies']:
        print_tweet_and_replies(reply, num_indents = num_indents + 1)

print_tweet_and_replies(tweet_about_exam)


# #### 8. Now, make a copy of your code from the previous question and modify it to only print out the tweet / username only if the length of the tweet is greater than 25.

# In[12]:


def print_tweet_and_replies(tweet, num_indents=0):
    length = len(tweet['text'])
    
    if length > 25:
        # print indent first
        for i in range(num_indents):
            print('   ', end='')

        # print tweet
        print('"' + tweet['text'] + '"')

        # print indent before usernmae
        for i in range(num_indents):
            print('   ', end='')

        #print useraname
        print('        -' + tweet['username'])

        #print replies (and the replies of those, etc.)
        for reply in tweet['replies']:
            print_tweet_and_replies(reply, num_indents = num_indents + 1)

print_tweet_and_replies(tweet_about_exam)

