#!/usr/bin/env python
# coding: utf-8

# # Practice: Statements and Variables

# ## Variable Inspector
# Before we begin, run the code below to install a helpful library, then refresh your browser tab.
# 
# Once you've done that, when you right click here, one of the bottom options should be "Variable Inspector." Open that and then drag it to the side to make two divided tabs (as was demonstrated in the lecture). 
# 

# In[1]:


get_ipython().system('pip install lckr-jupyterlab-variableinspector')


# ## Variables
# You will first practice saving values into variables. Remember, the way we save a value into a variable is like this:
# ```
# variable_name = value
# ```
# 
# First, save the value 5 into a variable named `number_of_pies`

# In[ ]:





# Now, save the value 12.5 into a variable named `cost_per_pie`

# In[ ]:





# Now make a new variable called `total_pie_cost` and save into the value of the number_of_pies multiplied by the cost_per_pie.
# 
# Note: In python (and many programming languages), the symbol for multiply is `*`

# In[ ]:





# Now, make a new variable called `name` and assign your first name to it

# In[ ]:





# Now, add your last name and save it back into the name variable

# In[ ]:





# Create a variable called `age` and assign your age to it.

# In[ ]:





# ~ A year goes by ~
# 
# Increase the `age` variable by 1. 

# In[ ]:





# Using both variables, create a new variable and assign the sentence "NAME is AGE years old!" to it. Think of your own variable name.
# 
# *hint: make sure to cast numbers as strings with the str() function when combining them with other strings.

# In[ ]:





# ## Indexing

# When we think of strings, we commonly think of them as a sequence of characters, where each character has an index in the string. Each character has its own spot in the sequence, and the spots are ordered starting at index 0 going up to the end of the string.
# 
# Python lets you access a character at a specific index using the [] notation
# 
# Note: You can use either "double quotes" or 'single quotes' to indicate a string

# In[ ]:


# try running the following examples:

wa = 'Washington'


# In[ ]:


wa[0]


# In[ ]:


wa[1]


# In[ ]:


wa[5:]


# In[ ]:


wa[:5]


# In[ ]:


wa[2:4]


# Return the first letter of your name

# In[ ]:





# Return all the letters of your name EXCEPT for the first.

# In[ ]:





# ## Calling Functions

# You can suspend execution of your code for the given number of seconds using the python function `time.sleep()`

# In[ ]:


# try running this example: 

import time  # you must load the time library in order to use 'sleep'

display('Monday was a sunny day.')
time.sleep(3)                              # waits 3 seconds
display('So I decided to go for a walk.')
time.sleep(4)                              # waits 4 seconds
display('The end!')


# You can also find out the length of a string using the python function `len()`. 

# In[ ]:


# try running this example:

weather = 'Today was a rainy day'
len(weather)


# Return the length of your name using the `len()` function and the `name` variable.

# In[ ]:





# Create a story using the `sleep()` function (at least 2 times).

# In[ ]:





# ## Loops

# For loops let you iterate over a sequence of values.

# In[ ]:


# try out this example:

for num in range(10):
    print(num)


# Create a loop of range 5, mutiplying each number by 2

# In[ ]:





# Create a loop of range 5, squaring each number

# In[ ]:





# ## Lists

# Variables can also store different data structures such as lists. Create a list of at least 3 food items and assign it to a variable called `favorite_foods`. 
# 
# Remember, lists have this structure:
# 
# ```
# [item1, item2, item3]
# ```
# 

# In[ ]:





# Just like strings, lists also have indexes.

# In[ ]:


# try out this example:

states = ['California', 'Washington', 'New York']
states[0]


# Return the second index in your list.

# In[ ]:





# Use the `len()` function to return the length of your list

# In[ ]:





# Loop through the list. For each iteration, print out the sentence: "NAME's favorite food is FOOD", replacing NAME with your `name` variable and food with each food in your `favorite_foods` list. 
# 
# Hint: You should print out the same number of lines as your answer for the previous question.

# In[ ]:





# ## Twitter Bot Practice

# ## Install and import the "tweepy" library of code that gives us twitter functions

# In[ ]:


get_ipython().system('pip install tweepy')
import tweepy


# ## Log in

# In[ ]:


# copy in the code from test_twitter_bot_keys.ipynb


# ## Tweepy Review (refer to lab 1.5, but do NOT use the same answers)

# 1) Search for a tweet that includes the phrase "happy wednesday"

# In[ ]:





# 2. Create a variable called `username` and assign it to a username of an account of your choice.

# In[ ]:





# 3. Get the user ID of the same account as above using the `username` variable. Store the user ID in the variable `user_id`. Show the output of the variable using the `display()` function.

# In[ ]:





# 4. Get the user mentions using the `user_id` variable.

# In[ ]:





# 5. Get who the user follow using the `user_id` variable.

# In[ ]:





# ## Tweeting

# ### Writing and posting a tweet

# In[ ]:


# before tweeting, we recommend you display the output first:

display("This tweet was posted by a computer program!")


# this is the basic structure to post a tweet. if you want, try running this code block and
# check your twitter account to see if it worked!

client.create_tweet(text="This tweet was posted by a computer program!")


# 6. Display something you learned in the class so far.

# In[ ]:





# 7. Now, tweet the sentence you displayed in question #6.

# In[ ]:





# 8. Display 5 tweets of your choice at least 20 seconds apart.

# In[ ]:





# 9. Now, post the tweets in question #8.

# In[ ]:





# 10. Look up tweets that include the phrase "hello world" and store it in a variable called `test_list`. 

# In[ ]:




