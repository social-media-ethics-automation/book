#!/usr/bin/env python
# coding: utf-8

# # Demo: Statements and Variables

# ## Variables and assignment (single "=")
# Variables are a place in the computer where a piece of information is saved with a particular name.
# 
# To store something in a variable, put it on the left of a single "=" symbol, with the right side of the symbol being the thing (or formula) whose value you want to save in it. For example:
# 
# ```
# num_days = 3
# ```
# 
# The code above saves the number 3 into the variable called "num_days"
# 
# Variables can then be referred to by just typing their name. You can even make a formula with their name
# 
# ```
# num_days * 3
# ```
# 
# The code above will give the number 9 (3 times the number of days, which was 3)
# 
# Note: Variable names can't have spaces in them, and can't start with a number

# In[1]:


num_days = 3
num_days * 3


# In[2]:


# TODO: More demos: (saving, seeing result, using to save new variable)
years = 3
days = years * 365
hours = days * 24
minutes = hours * 60


# In[3]:


# try updating years
years = 4
# it doesn't update previous variables 
# that were made based on years


# In[4]:


years = years + 1


# In[5]:


minutes


# ## Calling Functions
# 
# A function is a named section of pre-written code. 
# 
# Functions can take inputs
# * Inputs go in parenthese after the function name
# * These inputs are called "parameters" or "arguments"
# * If there are multiple inputs, they are separated by commas
# * You can also specify which input you are giving within the parenthesis by putting parameter_name=value
# 
# Functions can also make outputs. 
# * Also called "returns" or "results"
# * When the code intepreter sees the function call, it runs the code in the function wiht the inputs, and then puts the output in the place where that function call was
# * The results of the function can be stored in a variable, used in a formula, or used as an argument for another function

# In[6]:


# I need to load the time library in order to use sleep
import time

# TODO: Demo functions with no returns (display, print, sleep)
message = "Hello World!"
display(message)

time.sleep(2)

display(3)

time.sleep(5)

display(pi * 2)
print(message)


# In[ ]:


import string
import math

# TODO: Demo functions with returns (upper, isupper, sqrt, range, type)
message2 = message.upper()
message3 = message.lower()

sqrt_years = math.sqrt(years)

example_range = range(10)

print( type(message2) )

# TODO: Demo a useful trick with functions (str)
first_name = "Kyle"
last_name = "Thayer"

combined_name = first_name + " " + last_name

kyle_age = first_name + " is " + str(38) + " years old"


# ## for loops
# For loops allow you to repeat an action multiple times.
# 
# ```
# for loop_value in thing_to_loop_over:
#     # Put actions to repeat here
# ```
# 
# For loops have to have something to loop over, which goes after "in".
# * You can use it with the function range to repeat an action a given number of times.
# * You can use it on a list, though we'll cover that more later.
# 
# As the loop goes, it saves the current thing it is looking at in the temporary variable you list before the in.
# 
# The commands you want to repeat need to be tabbed in one more level than the for statement to indicate they go inside the for loop.

# In[ ]:


# TODO: Demo some for loops, including the one below

for x in range(10):
    print("<<<<< " + str(x*4 + 1) + "/40")
    print("^^^^^ " + str(x*4 + 2) + "/40")
    print(">>>>> " + str(x*4 + 3) + "/40")
    print("vvvvv " + str(x*4 + 4) + "/40")


# In[5]:


#TODO: For loop "are we there yet?"


# ## Error demos
# 

# In[3]:


my_num = 5 / 0


# In[4]:


#TODO Make code run out of order


# ## Last lecture's code
# Now let's look at some of the code from last lecture and see if we understand it better

# In[ ]:


get_ipython().system('pip install tweepy')
import tweepy
import bot_keys

client = tweepy.Client(consumer_key=bot_keys.consumer_key, consumer_secret=bot_keys.consumer_secret,
                       access_token=bot_keys.access_token, access_token_secret=bot_keys.access_token_secret)

client.create_tweet(text="This is tweet was posted by a computer program!")

for x in range(10):
      client.create_tweet(text="test Computer program posting tweet " + str(x))


# In[ ]:




