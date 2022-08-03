#!/usr/bin/env python
# coding: utf-8

# # Demo: recursion (simplified tweet data)

# ## Create a tweet structure
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

# In[1]:


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

# In[3]:


print(tweet_about_exam['text'])

for reply in tweet_about_exam['replies']:
    print('  -' + reply['text'])


# #### The root tweet and replies and replies to those replies

# In[4]:


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

# In[5]:


def print_tweet_and_replies(tweet):
    # print tweet
    print(tweet['text'])
    
    #print replies (and the replies of those, etc.)
    for reply in tweet['replies']:
        print_tweet_and_replies(reply)

print_tweet_and_replies(tweet_about_exam)


# ### Modify the function to add indents for replies

# In[6]:


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
