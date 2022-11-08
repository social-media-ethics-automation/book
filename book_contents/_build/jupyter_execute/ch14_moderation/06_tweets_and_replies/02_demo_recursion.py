#!/usr/bin/env python
# coding: utf-8

# # Demo: Navigating Trees (recursion)

# ## Structure of Tweets & Replies
# Let's look at our example from before of comments and replies:
# ![Initial tweet: "That last exam in sure was hard!" Two main replies, the first is "It sure was hard, what score did you get?" and that replies has two replies: "I got a 67% :(" and "I got a 73%". The second main reply is "I didn't think it was that bad". That second main reply has two replies, the first is "how was that not a super hard exam?" and the second is "of course you didn't", which has a reply "what's that supposed to mean?" which has a reply "you're an overacheiver" which has a reply "and that's bad how?"](comments_replies_trees.png)
# 
# When we want to represent Trees (like comments and replies) in code, one way of doing so is by using dictionaries.
# 
# Our initial tweet will be a dictionary with `text` (the comment text), and `replies` (a list of dictionaries).
# 
# Each of those replies will in turn be a dictioary with `text` (the reply text), and `replies` to that reply (a list of dictionaries). 
# 
# And so on.
# 
# Below is code to store that in a variable (though it looks kind of messy):

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


# We'll also make a function that will help us display a message in a box that is indented over. Don't worry about the details, but this uses HTML display styling, which is how websites do styling.

# In[2]:


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


# The function above takes the `text` to be displayed, and optionally the `left_margin` for how much to indent the text box. 
# 
# Below are some examples of how it works:

# In[3]:


display_indented("Here is an example")


# In[4]:


display_indented("Here is an example with an left_margin of 20", left_margin=20)


# ## Navigating tree
# 
# Now let's consider how we can navigate this tree of comments and replies.
# 
# First, we can just print out the initial tweet (the root):

# In[5]:


display_indented(tweet_about_exam['text'])


# ### Navigate with for loops
# 
# If we want to print the initial tweet, and just the replies to that tweet, we can use a for loop, like this:

# In[6]:


display_indented(tweet_about_exam['text'])

for reply in tweet_about_exam['replies']:
    display_indented(reply['text'], left_margin=20)


# If we also want to include the replies to those initial replies, we can put another for loop inside of there:

# In[7]:


display_indented(tweet_about_exam['text'])

for reply in tweet_about_exam['replies']:
    display_indented(reply['text'], left_margin=20)
    
    for reply_reply in reply['replies']:
        display_indented(reply_reply['text'], left_margin=40)


# If we want to get all of the replies in our example though, we'll need to have a for loop for each level, but the code is going to be getting messy:

# In[8]:


display_indented(tweet_about_exam['text'])

for reply in tweet_about_exam['replies']:
    display_indented(reply['text'], left_margin=20)
    
    for reply_reply in reply['replies']:
        display_indented(reply_reply['text'], left_margin=40)
        
        for reply_reply_reply in reply_reply['replies']:
            display_indented(reply_reply_reply['text'], left_margin=60)
            
            for reply_reply_reply_reply in reply_reply_reply['replies']:
                display_indented(reply_reply_reply_reply['text'], left_margin=80)
                
                for reply_reply_reply_reply_reply in reply_reply_reply_reply['replies']:
                    display_indented(reply_reply_reply_reply_reply['text'], left_margin=100)


# #### for loops didn't work great
# Our code was messy, and if there were even more levels, we'd need even more for loops. This could go on endlessly.

# ### Navigate with recursion: a function that calls itself
# We can use a clever programming trick that will work better.
# 
# We make a function that prints a tweet and all the replies (`print_tweet_and_replies`). So our function will first print the text of the tweet, and then it will go through each reply, but instead of printing the reply directly, there is a function that will print that tweet and all replies to it: `print_tweet_and_replies` (which is the function we are writing).
# 
# This trick can be confusing to understand (and it's ok if you don't), but let's look at it again in psuedocode:
# 
# The function `print_tweet_and_replies` does the following
# 1. Print the text of the tweet
# 2. For each of the replies to that tweet, use the `print_tweet_and_replies` function to print it out
# 
# So, we will call `print_tweet_and_replies` with our initial tweet, and that function will then call `print_tweet_and_replies` for each of the replys to that tweet, and then those new calls to `print_tweet_and_replies` will call `print_tweet_and_replies` for all the replies to those tweets, and so on, until all the tweets are printed out.
# 
# _Note: In computer science terms, this is called a "depth-first search" algorithm_
# 
# The actual code for `print_tweet_and_replies` is here:

# In[9]:


def print_tweet_and_replies(tweet):
    # print tweet
    display_indented(tweet['text'])
    
    #print replies (and the replies of those, etc.)
    for reply in tweet['replies']:
        print_tweet_and_replies(reply)


# And we can test it out on our tweet and see it work

# In[10]:


print_tweet_and_replies(tweet_about_exam)


# In the above result, there were no indents, but we can use another trick (getting more confusing) where we track how many indents to make when the function is called (by default, it starts at 0). When the function calls itself to print the replies, we adde:

# In[11]:


def print_tweet_and_replies(tweet, num_indents=0):
    # print indented tweet
    display_indented(tweet['text'], left_margin=num_indents*20)
    
    #print replies (and the replies of those, etc.)
    for reply in tweet['replies']:
        print_tweet_and_replies(reply, num_indents = num_indents + 1)


# And when we test this out, we can see the result

# In[12]:


print_tweet_and_replies(tweet_about_exam)


# In[ ]:




