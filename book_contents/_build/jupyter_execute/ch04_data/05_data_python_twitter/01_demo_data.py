#!/usr/bin/env python
# coding: utf-8

# # Demo: Python Basic Data Types
# Let's now look specifically at how Python stores and lets you work with basic data types:
# * Booleans (True / False)
# * Numbers
# * Strings (Text)
# 
# But first we need to look a little more about how to use functions, since we'll be using them with the data types.

# ## Calling Functions
# A function is a named section of pre-written code, which we can "call," making that section of code run.
# 
# We have already been calling two different functions in particular: `display` and `create_tweet`:
# - `display("Ethics might be relevant!")`
# - `client.create_tweet(text="This is the tweet text")`
# 
# The structure of a standard function call has the following pieces:
# `function_name(input_parameters)`
# 
# So we first write the name of the function (e.g., `display` or `client.create_tweet`), then we put matching parentheses after that, and inside the parentheses we put the input arguments, which are data or options for how the function should run.
# 
# ### Input Arguments
# - These inputs are called "parameters" or "arguments"
# - Inputs go in parentheses after the function name
# - If there are multiple inputs, they are separated by commas
# - You can also specify which input you are giving within the parenthesis by putting parameter_name=value
# 
# 
# Additionally, some functions produce a result, which can be saved in a variable, or used in a calculation or some other fashion. When we save the result of running a function into a variable, it looks like this:
# 
# `save_result_var = function_name(input_parameters)`
# 
# ### Function results
# * Functions can have outputs that are called "returns" or "results"
# * When the code intepreter sees the function call, it runs the code in the function with the inputs, and then puts the output in the place where that function call was
# * The results of the function can be stored in a variable, used in a formula, or used as an argument for another function
# 
# That was all a bit theoretical, so set's look at some data types now, and some specific functions that we can use with them.

# ## Boolean (True / False)
# 
# In Python there are two options for boolean: `True` and `False`
# 
# Note that the first letter is capitalized and the rest is lower case. Python only lets you write these True and False values in that way.
# 
# Let's save a boolean value in a variable, and then display it:

# In[1]:


does_user_have_blue_checkmark = True

display(does_user_have_blue_checkmark)


# Display lets us see what was in the variable, but we can also use a new function `type` to see what type of value is in the variable (it should be 'bool' which is short for boolean):

# In[2]:


type(does_user_have_blue_checkmark)


# ## Numbers

# Python allows you to use two main types of numbers:
# - Integers (whole numbers), called "int"
# - A "floating point" number with a decimal point, called a "float"

# In[3]:


type(5)


# In[4]:


type(5.5)


# Even though there are two types of numbers, most of the time they work together pretty seemlessly, switching to whichever type makes the most sense. For example, let's look at what happens when we add and int and a float:

# In[5]:


example_num = 5 + 5.5


# In[6]:


display(example_num)


# In[7]:


type(example_num)


# ???? Other functions for numbers (min max
# 

# In[8]:


import math
sqrt_years = math.sqrt(10)


# Python also lets us create boolean values by doing comparisons of numbers. Let's save in some variables how much money I have and how much an item costs, and then do a comparison to see if I have enough money (saving the result as a boolean in a variable)

# In[9]:


money_in_wallet = 10
cost_of_item = 7

has_enough_money = money_in_wallet > cost_of_item

display(has_enough_money)


# ## Data types
# Python automatically handles many different types of data, including:
# 
# For text:
# * str - a String of characters
# 
# For numbers:import math
# 
# * int - an integer (whole number)
# * float - a floating point number (one with decimals)
# 
# True/False:
# * bool - a true/false value
# 
# 
# See more here: https://www.w3schools.com/python/python_datatypes.asp

# In[ ]:





# In[10]:


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

# In[11]:


# error when I put a number in a string
example_text = "how old are you? I am " + 3

