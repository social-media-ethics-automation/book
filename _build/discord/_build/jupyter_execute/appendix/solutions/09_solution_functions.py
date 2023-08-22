#!/usr/bin/env python
# coding: utf-8

# # Ch 9 Practice: Functions

# Create a function called `say_goodbye` which displays the text "Goodbye!"

# In[1]:


def say_goodbye():
    print("Goodbye!")


# Write code that calls the function `say_goodbye`

# In[2]:


say_goodbye()


# Redefine the function `say_goodbye` to take a parameter called `name`, and have it display "Goodbye name!" where "name" is replaced by whatever was in the `name` variable 

# In[3]:


def say_goodbye(name):
    print("Goodbye "+name+"!")


# Write code that calls the function say_goodbye but with your name as a parameter

# In[4]:


say_goodbye("Kyle")


# Try out the code below which counts from 0 to 4 slowly:

# In[5]:


import time # We need the time library for the following examples


# In[6]:


for i in range(5):
    print(i)
    time.sleep(1)


# We can put that for loop in a function like this:

# In[7]:


def counter():
    for i in range(5):
        print(i)
        time.sleep(1)


# And then we can call it:

# In[8]:


counter()


# Now redifine `counter` by 
# 1. copying the code above which defines `counter` 
# 2. make the counter take a parameter called `max` 
# 3. Have the `range` call use the parameter `max` 

# In[9]:


def counter(max):
    for i in range(max):
        print(i)
        time.sleep(1)


# Now try calling the new version of `counter` but passing it the argument 7

# In[10]:


counter(7)


# Create a function called `multiply` which takes two arguments, multiplies them together (`*`), and then returns the multiplied value

# In[11]:


def multiply(num_1, num_2):
    return num_1 * num_2


# Call the `mutliply` function with two numbers and save the result in a variable. Then print out the variable to see that the multiplied number was saved.

# In[12]:


new_num = multiply(3, 5)
display(new_num)


# In[ ]:




