#!/usr/bin/env python
# coding: utf-8

# # Demo: Python Data Types

# ## Data types
# Python automatically handles many different types of data, including:
# 
# For text:
# * str - a String of characters
# 
# For numbers:
# * int - an integer (whole number)
# * float - a floating point number (one with decimals)
# 
# True/False:
# * bool - a true/false value
# 
# 
# See more here: https://www.w3schools.com/python/python_datatypes.asp

# In[1]:


# TODO: Demo data types
message = "Hello World!"
my_name = "Kyle"

pi = 3.141592653

is_kyle_at_home = True
is_kyle_at_uw_now = False


# ## Dictionary (mapping)
# Python also lets you have a variable that has multiple named pieces (it's like your variable has its own variables). The type of this is "dict"
# 
# We won't go into details here, but if you have a variable that is type "dict", you can access the different components by using a dot. 
# 
# For example, if I have a variable `book` which is a type "dict" and it has components `pages` and `author`, I can get the value of the pages and author like this:
# ```
# book.pages
# book.author
# ```

# ## Error demos

# In[2]:


# error when I put a number in a string
example_text = "how old are you? I am " + 3

