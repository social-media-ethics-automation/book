#!/usr/bin/env python
# coding: utf-8

# # Ch 14.6.3: Demo: Hide Some Tweets
# 
# Now we will use our code from before, but we will skip displaying some tweets, and we can make up whatever rule we want to do this.
# 
# First let's make our fake conversation data:

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


# We'll copy that function to help us display the tweets nicely again too

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


# ## Display everything
# 
# If we want to display everything, we can use the recursive function from the last section:

# In[3]:


def print_tweet_and_replies(tweet, num_indents=0):
    # print indented tweet
    display_indented(tweet['text'], left_margin=num_indents*20)
    
    #print replies (and the replies of those, etc.)
    for reply in tweet['replies']:
        print_tweet_and_replies(reply, num_indents = num_indents + 1)


# And when we test this out, we can see the result

# In[4]:


print_tweet_and_replies(tweet_about_exam)


# ## Display only some
# If we want to make a rule for what to display, we will first make a new function called `should_display` which will look at a comment/reply and return `True` if it should be displayed, or `False` if it should be hidden.
# 
# For our first rule, let's say we will display all messages that are more than 16 characters long. If a comment/reply is shorter than that, we won't display it or any of the replies to it.

# In[5]:


def should_display(comment):
    # only display if the length of the comment text is more than 20 characters long 
    if(len(comment["text"]) > 20):
        return True
    else:
        return False


# Now we will make a new version of our recursive `print_tweet_and_replies` with an added `if` statement that checks whether the `should_display` function says if we should display that comment and its replies:

# In[6]:


def print_tweet_and_replies(tweet, num_indents=0):
    if(should_display(tweet)):
        # print indented tweet
        display_indented(tweet['text'], left_margin=num_indents*20)

        #print replies (and the replies of those, etc.)
        for reply in tweet['replies']:
            print_tweet_and_replies(reply, num_indents = num_indents + 1)


# Now let's test it out and see that fewer of the messages were printed out (only the long ones)

# In[7]:


print_tweet_and_replies(tweet_about_exam)


# ## Making up new rules
# We can make up whatever rules we want for what to display. For example, we might search for offensive words and hide those, or we could hide ones with negative sentiment. 
# 
# As one more simple example here, we will make a new rule that only displays a message if it got replies (we will assume that if no one bothered to reply, than it isn't worth displaying).
# 
# To make this change we will redefine our `should_display` function with the new rule, and then re-run `print_tweet_and_replies`

# In[8]:


def should_display(comment):
    # only display if there are more than 0 replies
    if(len(comment["replies"]) > 0):
        return True
    else:
        return False


# In[9]:


print_tweet_and_replies(tweet_about_exam)

