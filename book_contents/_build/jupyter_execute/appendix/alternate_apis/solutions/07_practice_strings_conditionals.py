#!/usr/bin/env python
# coding: utf-8

# # Ch 7 Practice: Conditionals and String Manipulation

# ## IF ELSE Statements
# Look at the following code example and try running it

# In[1]:


x = 5

if x < 11:
    print('A')
elif x >= 13:
    print('B')
else:
    print('C')


# Now what would happen if x was changed to 30? What would the output be?
# 
# _Do Not Code. Please answer this question as a markdown block. Modify the code above to check your answer afterwords._

# It would print 'B'

# What value would the `x` variable have to be in order to get the output 'C'?
# 
# _Again, Do Not Code. Please answer this question as a markdown block Modify the code above to check your answer afterwords_

# If x were 12, it would print C

# ## String Manipulation
# 
# Now, make a variable with your name in it, called `my_name`

# In[2]:


my_name = "Kyle"


# Write code to display the first letter of your name

# In[3]:


display(my_name[0])


# Write code to display the last letter of your name

# In[4]:


display(my_name[-1 : ])


# ## Ifs with Strings
# Save a string in a variable called `message` and have it end with either a question mark `?`, an exclamation mark `!`, or a period `.`

# In[5]:


message = "This is an example message!"


# Now, make a set of if/elif/else statements which will display either:
# - `The message was a question`
# - `The message was an exclamation`
# - `The message was a statement`
# - `The message ended unexpectedly`
# 
# depending on what character the message ended in a `?`, `!`, `.`, or something else. Hint: use the `endswith` function.

# In[6]:


if message.endswith("?"):
    display("The message was a question")
elif message.endswith("!"):
    display("The message was an exclamation")
elif message.endswith("."):
    display("The message was a statement")
else:
    display("The message ended unexpectedly")


# Now, go back and modify the message string to see if the different if/elif/else options all work
