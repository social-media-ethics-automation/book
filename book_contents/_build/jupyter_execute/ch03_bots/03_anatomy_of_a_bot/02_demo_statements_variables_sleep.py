#!/usr/bin/env python
# coding: utf-8

# # Demo: Statements, Variables, and Sleep

# ## Statements
# As we said before, a computer program in a programming language like Python is often composed of a list of statements, that is steps to be run in order (like a recipe):
# ```text
# - statement 1
# - statement 2
# - statement 3
# ```
# 
# In Python, generally each new line of code is a new statement, to be run after the previous statement.
# 
# We will start writing statements using a line of code that looks like this which runs a function called `display`:
# 
# ```display("Ethics might be relevant!")```
# 
# This line of code will display the text in the quotes ("Ethics might be relevant!") below the code, as you can see below, in a program that has one statement:

# In[1]:


display("Ethics might be relevant!")


# Now let's try several statements in a row, with mulitple lines of code that display text:

# In[2]:


display("This book is about:")
display("  - Social Media")
display("  - Ethics")
display("  - Automation")


# Now that we've made multple statements in a row, let's do something a little more complicated than just displaying text by using variables.

# ## Variables and assignment (single "=")
# 
# As we said in the previous section, Variables are a way of saving information on the computer, so we can use it later in the computer program, similar to how we might put mix ingredients in different bowls, using the mix from each bowl at the relevant time.
# 
# In a computer program, these variables are given names so we can more easily get the information back out again.
# 
# To store something in a variable (called "assigning" it a value), write the variable name, followed by an "=" symbol, followed by whatever we want to save in the variable. For example:

# In[3]:


greetings_message = "Hello and welcome to programming with variables!"


# The line of code above saved the text "Hello and welcome to programming with variables!" into a variable called "greetings_message"
# 
# Since this was just saving something into

# In[4]:


```
num_days = 3
```

The code above saves the number 3 into the variable called "num_days"

Variables can then be referred to by just typing their name. You can even make a formula with their name

```
num_days * 3
```

The code above will give the number 9 (3 times the number of days, which was 3)

Note: Variable names can't have spaces in them, and can't start with a number


# In[ ]:


num_days = 3
num_days * 3


# In[ ]:


# TODO: More demos: (saving, seeing result, using to save new variable)
years = 3
days = years * 365
hours = days * 24
minutes = hours * 60


# In[ ]:


# try updating years
years = 4
# it doesn't update previous variables 
# that were made based on years


# In[ ]:


years = years + 1


# In[ ]:


minutes


# ## Sleep
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

# In[2]:


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





# In[ ]:




