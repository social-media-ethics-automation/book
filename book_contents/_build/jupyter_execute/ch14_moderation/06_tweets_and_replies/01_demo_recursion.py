#!/usr/bin/env python
# coding: utf-8

# # Demo: recursion (simplified tweet data)

# 

# ## Structure of Tweets & Replies
# Lets say we want to search through the replies of tweets. Visualized, the structure may look something like this:
# ```
#                             TWEET #1                         LAYER #1
#                           /          \
#                          /            \
#                  TWEET #2           TWEET #3                  LAYER #2
#                /         \        /         \
#               /           \      /           \
#        TWEET #4     TWEET #5    TWEET #6     TWEET #7         LAYER #3
#       /       \     /      \    /      \     /      \
#      /         \   /        \  /        \   /        \
#     
#     ...                                                     
#                  
# ```
# ### Breaking it down:
# - TWEET #1 is the original tweet tweet. It is NOT a reply to any tweet. In programming terms, we call it the "root."
# - TWEET #2 AND TWEET #3 are both replies to TWEET #1
# - TWEET #4 AND TWEET #5 are both replies to TWEET #2
# - TWEET #6 AND TWEET #7 are both replies to TWEET #3
# - The ellipsis means that there might be an infinite number of layers with replies to tweets & replies to replies
# 
# 
# The pseudo-code below (not real code to run) shows one way we might try to go through all of the tweets:

# In[1]:


# pseudo-code 
# do not run this code block:

for each_reply in TWEET_1:                    # represents going through layer #1
    for next_replies1 in each_reply:              # layer #2
        for next_replies2 in next_replies1:          # layer #3
            for next_replies3 in next_replies2:         # layer 4
                for next_replies3 in next_replies2:        
                    etc..........
                    
                    print(The text of the tweet)


# In[4]:


tweet_about_exam = {
    'text': 'That last exam in sure was hard!',
    'replies':[{
        'text': 'It sure was hard, what score did you get? ',
        'replies': [{
            'text': 'I got a 67% :(',
            'replies': []
        },{
            'text': 'I got a 73%',
            'replies': []
        }]
    }, {
        'text': 'I didn\'t think it was that bad',
        'replies': [{
            'text': 'how was that not a super hard exam?',
            'replies': []
        }, {
            'text': 'of course you didn\'t',
            'replies': [{
                'text': 'what\'s that supposed to mean?',
                'replies': [{
                    'text': 'you\'re an overacheiver',
                    'replies': [{
                        'text': 'and that\'s bad how?',
                        'replies': []
                    }]
                }]
            }]
        }]
    }]
}

display(tweet_about_exam)


# ### Try printing using for loops

# #### Just the root tweet

# In[2]:


print(tweet_about_exam['text'])


# #### The root tweet and replies

# In[4]:


print(tweet_about_exam['text'])

for reply in tweet_about_exam['replies']:
    print('  -' + reply['text'])


# #### The root tweet and replies and replies to those replies

# In[6]:


print(tweet_about_exam['text'])

for reply in tweet_about_exam['replies']:
    print('  -' + reply['text'])
    
    for reply_reply in reply['replies']:
        print('      -' + reply_reply['text'])


# ### for loops didn't work great
# We still didn't get all the replies. For every level of replies we need another for loop. This could go on endlessly.

# ### Now use recursion: a function that calls itself
# We make a function `print_tweet_and_replies` that prints a tweet and all its replies.
# 
# The way it does this is it prints the 'text' of a tweet and then for each reply it uses the `print_tweet_and_replies` to print that tweet and all its replies.

# In[7]:


def print_tweet_and_replies(tweet):
    # print tweet
    print(tweet['text'])
    
    #print replies (and the replies of those, etc.)
    for reply in tweet['replies']:
        print_tweet_and_replies(reply)

print_tweet_and_replies(tweet_about_exam)


# ### Modify the function to add indents for replies

# In[8]:


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


# ### What you say in computer science terms, was a "depth-first-search" on a "tree" data structure

# In[5]:


from IPython.display import HTML, Image, display
import html
def display_indented(text, left_margin=0):
    display(
        HTML(
            "<pre style='border:solid 1px;padding:3px;margin-left:"+ str(left_margin) + "px'>" + 
            html.escape(text) + 
            "</pre>"
        )
    )


# In[11]:


def print_tweet_and_replies(tweet, num_indents=0):
    display_indented(tweet['text'], num_indents*30)

    #print replies (and the replies of those, etc.)
    for reply in tweet['replies']:
        print_tweet_and_replies(reply, num_indents = num_indents + 1)

print_tweet_and_replies(tweet_about_exam)


# In[ ]:





# In[ ]:




