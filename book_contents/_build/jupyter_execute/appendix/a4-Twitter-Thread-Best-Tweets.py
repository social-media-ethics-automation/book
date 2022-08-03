#!/usr/bin/env python
# coding: utf-8

# # A4: Twitter Thread Best Tweets

# In this assignment you will be modifying a recursive function that prints a twitter thread. Your goal will be to only show the best tweets in the thread. It will be up to you to decide what rules you use to decide which tweets are the best tweets.

# ### normal tweepy set-up code

# In[1]:


# make sure tweepy library is installed
get_ipython().system('pip install tweepy')
import tweepy


# In[2]:


# load my twitter keys
import my_bot_keys


# In[3]:


# log into tweepy
client = tweepy.Client(
    bearer_token=my_bot_keys.bearer_token,
    consumer_key=my_bot_keys.consumer_key, consumer_secret=my_bot_keys.consumer_secret,                   
    access_token=my_bot_keys.access_token, access_token_secret=my_bot_keys.access_token_secret
)


# ### Helper function to display text in an indented box

# In[4]:


from IPython.display import HTML, Image, display
import html
def display_indented(text, left_margin=0, color="white"):
    display(
        HTML(
            "<pre style='border:solid 1px;padding:3px;margin-left:"+str(left_margin)+"px;background-color:"+color+"'>" + 
            html.escape(text) + 
            "</pre>"
        )
    )


# ### Demo of using the display_with_left_margin function

# In[5]:


display_indented("A no indent text")
display_indented("A 10px indent text", left_margin=10)
display_indented("A 20px indent text \n with a newline!", left_margin=20)
display_indented("You can change the 'color' of the box too, like make it red", color='red', left_margin=10)


# ### Helper code for getting a twitter conversation (that is a tweet and a bunch of its replies)
# You don't need to know how this code works, but you can look through it if you want.
# 
# Also, if you want to use more includes or something, you can add them to the client.get_tweet() call and the client.search_recent_tweets() call. You might also need to do extra work to include them like I did with the author/users info

# In[6]:


# Given a tweetId, create a datastructure with the tweet and replies
# Each "tweet" is dictionary with keys for:
#    "tweet_info" (from the tweet.data), "author", "replies", "previous_tweet", and "first_tweet"
#
# When searching for tweets in the conversation, it looks for groups of 100
# tweets at a time. You can set how many groups of 100 tweets it looks for with
# max_conversation_searches
def get_tweets_with_replies(tweetId, max_conversation_searches=1):
    (starting_tweet, all_conversation_tweets, users_lookup) = get_tweet_and_conversation(tweetId, max_conversation_searches)
    tweets_by_referenced_tweet = organize_tweets_by_referenced_tweets(all_conversation_tweets)
    tweet_with_replies = organize_tweets_with_replies(starting_tweet, tweets_by_referenced_tweet, users_lookup)
    return tweet_with_replies

# the function above uses the helper functions below

# Given a tweet id, find the tweet and other tweets in the same conversation
def get_tweet_and_conversation(tweetId, max_conversation_searches=1):
    starting_tweet = client.get_tweet(tweetId, tweet_fields=['conversation_id', 'public_metrics'], expansions=['author_id'])
    conversation_id = starting_tweet.data.conversation_id
    
    all_conversation_tweets = get_conversation_tweets(conversation_id, max_conversation_searches)
    all_users = starting_tweet.includes['users']
    for conversation_tweets in all_conversation_tweets:
        all_users += conversation_tweets.includes['users']
    users_lookup = {str(u["id"]): u for u in all_users}
    return (starting_tweet, all_conversation_tweets, users_lookup)

# Get tweets in a conversation (given the conversation id)
def get_conversation_tweets(conversation_id, max_conversation_searches):
    query = "conversation_id:" + str(conversation_id)
    all_conversation_tweets = []
    num_searches=0
    is_done = False
    next_token = None
    while not is_done and num_searches < max_conversation_searches:
        conversation_tweets = client.search_recent_tweets(query=query, next_token=next_token, tweet_fields = 'public_metrics', expansions=['referenced_tweets.id','author_id'], max_results=100)
        num_searches += 1
        all_conversation_tweets.append(conversation_tweets)
        print("loaded a set of tweets: " + str(conversation_tweets.meta))
        if 'next_token' in conversation_tweets.meta:
            next_token = conversation_tweets.meta['next_token']
        else:
            is_done = True
    return all_conversation_tweets

# Given a list of tweets, group them all based on what tweet they are replying to
def organize_tweets_by_referenced_tweets(list_of_tweet_results):
    tweets_by_referenced_tweet = {}
    for tweets in list_of_tweet_results:
        for tweet in tweets.data:
            for referenced_tweet in tweet.referenced_tweets:
                if(referenced_tweet.type == "replied_to"):
                    referenced_tweet_id = str(referenced_tweet.id)
                    if(referenced_tweet_id not in tweets_by_referenced_tweet):
                        tweets_by_referenced_tweet[referenced_tweet_id] = []
                    tweets_by_referenced_tweet[referenced_tweet_id].append(tweet)
                    break

    return tweets_by_referenced_tweet

# organize the tweets so that author info and replies to tweets are included
# with it in a convenient data structure
def organize_tweets_with_replies(tweet, tweets_by_referenced_tweet, users_lookup, previous_tweet=None, first_tweet=None):
    tweet_with_replies = {
        "tweet_info": tweet.data,
        "author": users_lookup[str(tweet.data["author_id"])].data,
        "replies": [],
        "previous_tweet": previous_tweet
    }
    if first_tweet == None:
        first_tweet = tweet_with_replies
    tweet_with_replies["first_tweet"] = first_tweet

    tweet_id = str(tweet.data["id"])
    if tweet_id in tweets_by_referenced_tweet:
        reply_tweets = tweets_by_referenced_tweet[tweet_id]
        for reply_tweet in reply_tweets:
            tweet_with_replies["replies"].append(
                organize_tweets_with_replies(reply_tweet, tweets_by_referenced_tweet, users_lookup, previous_tweet=tweet_with_replies, first_tweet=first_tweet)
            )
    return tweet_with_replies



# ### Code to print all tweets and replies
# I am providing this function that prints all tweets and replies with nothing hidder. You can use this to compare with what your function will print

# In[7]:


def print_all_tweet_and_replies(tweet_with_replies, num_indents=0):
    tweet_info = tweet_with_replies["tweet_info"]
    replies = tweet_with_replies["replies"]
    author_info = tweet_with_replies["author"]
    public_metrics = tweet_info["public_metrics"]

    display_text = (
        tweet_info['text'] + "\n" +
        "-- " + author_info["name"] + " (@" + author_info["username"] + ")" + "\n" +
        str(public_metrics)
    )
    
    display_indented(display_text, num_indents*20)

    #print replies (and the replies of those, etc.)
    for reply in replies:
        print_all_tweet_and_replies(reply, num_indents = num_indents + 1)


# # Your Code!

# ### TODO: Modify this function to include your own rule for displaying best tweets
# 
# The `print_best_tweet_and_replies()` function below currently prints all tweets and replies that have at least 1 like. (For more information on this, see the code demo and lecture for lecture 16.)
# 
# Your job is to invent and implement your own rule for what tweets count as the "best tweets" and therefore should be displayed. The rule can be complicated or simple, it just can't be the same as the current rule. You can aim for focusing on removing a few tweets that you judge are bad, or for only showing a few tweets you judge are the very best, or a combination of those.
# 
# When you are making your rule you may want to use different comparison operators (like == for equals, > for greater than, etc.) and different logical operators (like `and` for both things must be true, `or` for at least one thing must be true, etc.). See a list of operators here: https://www.w3schools.com/python/python_operators.asp
# 
# Some things you can use when you are deciding whether to display a tweet or not:
# 
# * The text of the tweet: `tweet_info['text']`
# * The author info of the tweet: saved in `author_info`
# * The public metrics of the tweet (likes, replies, etc.): saved in `public_metrics`
# * Information from the initial tweet: saved in `tweet_with_replies["first_tweet"]`
#    * To get the public metrics of the initial tweet, you can use 
#       * `tweet_with_replies["first_tweet"]["tweet_info"]["public_metrics"]`. 
#    *For example you could decide your rule is, it must have at least 1/10th the likes of the initial tweet.
# * Information from the previous tweet (that this tweet is in reply to): saved in `tweet_with_replies["previous_tweet"]`
#    * Note, for the initial tweet, `tweet_with_replies["previous_tweet"]` will be `None`
#    * To get the public metrics of the previous tweet, you can use
#       * `tweet_with_replies["previous_tweet"]["tweet_info"]["public_metrics"]`
# * You can use any other information you can figure out about the tweet as well, such as the sentiment analysis that was demoed in lecture 12.
# 
# #### Testing:
# You'll probably want to test out different versions of your rule with different twitter threads (which you'll be adding below) to see what you like best.
# 
# Also, if you want to see what tweets you are hiding, you can make an else to go with your if statement, and in there for tweets that you would be hiding, you can instead display them the color set to "red".

# In[8]:


def print_best_tweet_and_replies(tweet_with_replies, num_indents=0):
    tweet_info = tweet_with_replies["tweet_info"]
    replies = tweet_with_replies["replies"]
    author_info = tweet_with_replies["author"]
    public_metrics = tweet_info["public_metrics"]

    display_text = (
        tweet_info['text'] + "\n" +
        "-- " + author_info["name"] + " (@" + author_info["username"] + ")" + "\n" +
        str(public_metrics)
    )
    
    if public_metrics["like_count"] > 1:
        display_indented(display_text, num_indents*20)

        #print replies (and the replies of those, etc.)
        for reply in replies:
            print_best_tweet_and_replies(reply, num_indents = num_indents + 1)


# ### Test your code with a KSeattleWeather tweet

# In[9]:


# Get tweets and replies from a tweet by KSeattleWeather (https://twitter.com/KSeattleWeather)
# Feel free to look up a new tweet id if the search doesn't work well anymore, since it only searches
# for tweets from the last seven days (see lab 15.5 for how to find a tweet id).
weather_tweets_and_replies = get_tweets_with_replies(1496559168702099456)


# In[ ]:


# print the weather_tweets_and_replies tweets found above
print_best_tweet_and_replies(weather_tweets_and_replies)


# # Your Code! Test it with 3 tweet threads

# Now you will find your own three tweets that start a twitter thread and test out your function on those (no need to copy the function again, just replace the `?????`s in the code below with a tweet id (see lab 15.5 for getting the id of a tweet):
# 
# To find tweets with lots of replies, you can search trending topics, look at news organization, or look for users/organizations that get a lot of feedback, like the reddit "Am I the Asshole?": https://twitter.com/AITA_online, "web3 is going just great" https://twitter.com/web3isgreat, or anyone on this list: https://en.wikipedia.org/wiki/List_of_most-followed_Twitter_accounts
# 
# Note: I've started these all with `max_conversation_searches = 10` in order to load very large twitter threads (up to 1000 tweets), though you can modify this to get more or less

# ### TODO: Print twitter thread 1

# In[ ]:


tweet_with_replies_1 = get_tweets_with_replies(?????, max_conversation_searches = 10)


# In[ ]:


print_all_tweet_and_replies(tweet_with_replies_1)


# In[ ]:


print_best_tweet_and_replies(tweet_with_replies_1)


# ### Twitter thread 1 follow-up questions
# Write an answer in response to each of these questions (you can edit this text by double clicking it):
# 
# Look through the output of printing all tweets (`print_all_tweet_and_replies()`) and your version of printing the best tweets (`print_best_tweet_and_replies()`). 
# 
# * Did your function tend to keep most tweets or tend to hide most tweets?
# 
# * Do you see any pattern to the contents of the tweets you showed versus hid (e.g., did it actually select better quality or more interesting tweets)?

# ### TODO: Print twitter thread 2

# In[ ]:


tweet_with_replies_2 = get_tweets_with_replies(?????, max_conversation_searches = 10)


# In[ ]:


print_all_tweet_and_replies(tweet_with_replies_2)


# In[ ]:


print_best_tweet_and_replies(tweet_with_replies_2)


# ### Twitter thread 2 follow-up questions
# Write an answer in response to each of these questions (you can edit this text by double clicking it):
# 
# Look through the output of printing all tweets (`print_all_tweet_and_replies()`) and your version of printing the best tweets (`print_best_tweet_and_replies()`). 
# 
# * Did your function tend to keep most tweets or tend to hide most tweets?
# 
# * Do you see any pattern to the contents of the tweets you showed versus hid (e.g., did it actually select better quality or more interesting tweets)?

# ### TODO: Print twitter thread 3

# In[ ]:


tweet_with_replies_3 = get_tweets_with_replies(?????, max_conversation_searches = 10)


# In[ ]:


print_all_tweet_and_replies(tweet_with_replies_3)


# In[ ]:


print_best_tweet_and_replies(tweet_with_replies_3)


# ### Twitter thread 3 follow-up questions
# Write an answer in response in response to each of these questions (you can edit this text by double clicking it):
# 
# Look through the output of printing all tweets (`print_all_tweet_and_replies()`) and your version of printing the best tweets (`print_best_tweet_and_replies()`). 
# 
# * Did your function tend to keep most tweets or tend to hide most tweets?
# 
# * Do you see any pattern to the contents of the tweets you showed versus hid (e.g., did it actually select better quality or more interesting tweets)?

# # TODO: Final Reflection questions

# Write an answer in response in response to each of these questions (you can edit this by double clicking it):
# 
# * Explain why you chose the rules you did for selecting the best tweets?
# 
# * What was most challenging about coming up with your rules?
# 
# * What additional information or rules do you wish you could have used?
# 
# * If someone or some group wanted to make sure their tweets was shown by your function, what would they do? How hard would this be?
# 
# * If someone or some group wanted to make sure someone else's tweets were NOT shown by your function, what would they do? How hard would this be?
# 
# * If Twitter adopted this rule as a universal rule for which tweets to display, what do you think would happen (e.g., in the initial "at least one like" rule I provided, maybe no tweets would ever get shown since they start with no likes, and no one else would see it to like it)?
# 
