#!/usr/bin/env python
# coding: utf-8

# # Lab: Nested Loops Review

# #### 1. Use single for loop to access each LIST
# 
# Below we have a list of lists. Use a single for loop to go through the main list and print out each of the lists inside of it.
# 
# Your output should look like this: 
# 
# ```
# ['fish', 'squid', 'starfish']
# ['shark', 'whale', 'turtle']
# ```

# In[1]:


ocean_animals = [['fish', 'squid', 'starfish'], ['shark', 'whale', 'turtle']]
# your code goes here 


# #### 2. Use nested loops to access each ANIMAL
# 
# Below we have the same list of lists. Use one for loop to go through the main list and then have inside of that another for loop to go through all the inside list and print out each animal
# 
# Your output should look like this:
# 
# ```
# fish
# squid
# starfish
# shark
# whale
# turtle
# ```

# In[2]:


ocean_animals = [['fish', 'squid', 'starfish'], ['shark', 'whale', 'turtle']]
# your code goes here 


# #### 3. Print the following output:
# 
# ```
# 1
# 22
# 333
# 4444
# 55555
# ```
# Hints: 
#  * you can print a character without it going to the next line by setting end='': print("test", end=' ')
#  * Use one for loop to choose a number 1-6, and another for loop to print the number the right number of times
#  * refer to the previous lab for help

# In[3]:


# your code goes here 


# #### 4. Create a function called `read`. Your goal is to read out the novel one word at a time until you find the word "Waldo".
# 
# The `novel` is a list of strings, where each string is a sentence
# 
# In the `read` function, go through each sentence and in each sentence print each word, waiting one second in between each print. If the word you printed was "Waldo", return the string, "Waldo found!" (note: the `return` will stop the function from reading any more of the novel).
# 
# #### Make sure to call the function to check the result.

# In[4]:


import time

novel = ['There once was a boy.', 'He had a particular style',
         'A red and white shirt Waldo wore', 'Can\'t forget the glasses']

# your code goes here


# ## Code Structures for replies

# #### Comments and replies
# 
# Let's imagine I made a post on a social media site and people were able to make comments on it, and people were also able to make replies to those comments.
# 
# Below is code to save some comments and replies in a variable `post_comments`. The posta nd comments are saved as a list of dictionaries (where each dictionary has a 'text"'and a list of 'replies').

# In[5]:


post_comments = [
    { 
        'text': 'Great article!',
        'replies': ['Thanks!']
    }, { 
        'text': 'I actually preferred the 1994 Little Women movie',
        'replies': [
            'Really? Why is that?',
            "Because they had an actual kid playing young Amy"
        ]
    }, { 
        'text': 'I really liked the ending of the new one too!',
        'replies': []
    }
]

display(post_comments)


# #### 5. Print out all comments. Write a for loop to go through all the post_comments and just print out the 'text' for each one
# 
# Your output should look like this:
# 
# ```
# Great article!
# I actually preferred the 1994 Little Women movie
# I really liked the ending of the new one too!
# ```

# In[6]:


# your code goes here 


# #### 6. Print out all comments and replies. Copy the for loop above, but add a for loop inside to loop over each of the replies and print those out too.
# 
# Your output should look like this:
# 
# ```
# Great article!
# Thanks!
# I actually preferred the 1994 Little Women movie
# Really? Why is that?
# Because they had an actual kid playing young Amy
# I really liked the ending of the new one too!
# ```

# In[7]:


# your code goes here 


# #### 7. Print out comments and replies, but add 3 spaces and a dash ("   -") to the start of each reply
# 
# Your output should look like this:
# ```
# Great article!
#    - Thanks!
# I actually preferred the 1994 Little Women movie
#    - Really? Why is that?
#    - Because they had an actual kid playing young Amy
# I really liked the ending of the new one too!
# ```

# In[8]:


# your code goes here 


# ## Structure of Tweets & Replies

# Lets say we want to search through the replies of tweets. Visualized, the structure may look something like this:
# 
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

# #### Breaking it down:
#     
# - TWEET #1 is the original tweet tweet. It is NOT a reply to any tweet. In programming terms, we call it the "root."
# - TWEET #2 AND TWEET #3 are both replies to TWEET #1
# - TWEET #4 AND TWEET #5 are both replies to TWEET #2
# - TWEET #6 AND TWEET #7 are both replies to TWEET #3
# - The ellipsis means that there might be an infinite number of layers with replies to tweets & replies to replies
# 
# The pseudo-code below (not real code to run) shows one way we might try to go through all of the tweets:

# In[9]:


# pseudo-code 
# do not run this code block:

for each_reply in TWEET_1:                    # represents going through layer #1
    for next_replies1 in each_reply:              # layer #2
        for next_replies2 in next_replies1:          # layer #3
            for next_replies3 in next_replies2:         # layer 4
                for next_replies3 in next_replies2:        
                    etc..........
                    
                    print(The text of the tweet)


# #### 8. Reflect on the psuedo-code above. How practical is it going to be to write code like this for large twitter threads?

# In[ ]:




