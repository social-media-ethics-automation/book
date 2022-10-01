#!/usr/bin/env python
# coding: utf-8

# # Demo: Looping through posts and freinds
# ## Try looping through friend relationships?
# TODO: build to looping through lists of dictionaries (posts with user info, friend/follow relationships, etc.)

# ## Install helpful library
# Before we begin, run the code below to install a helpful library, then refresh your browser tab.
# 
# Once you've done that, when you right click here, one of the bottom options should be "Variable Inspector." Open that and then drag it to the side to make two divided tabs (as I'll demonstrate). 
# 

# In[1]:


get_ipython().system('pip install lckr-jupyterlab-variableinspector')


# ## for loops with lists
# For loops allow you to repeat an action multiple times.
# 
# ```
# for loop_value in things_to_loop_over:
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

# In[10]:


for num in range(10):
    print(num)


# In[11]:


for text in ["Kyle", "Emily", "Another Person"]:
    print(text)


# In[13]:


for text in ["Kyle", "Emily", "Another Person"]:
    print(text + " is awesome!")


# In[14]:


for text in ["Kyle", "Emily", "Another Person"]:
    sentence = text + " is awesome!"
    upper_sentence = sentence.upper()
    print(upper_sentence)


# In[15]:


#Error if inside is not spaced over
# for loops need sonmething inside, which is signaled
# by the spaced over line after it
# if there is no spaced over line, it thinks you forgot
for text in ["Kyle", "Emily", "Another Person"]:
print(text + " is awesome!")


# In[16]:


for x in range(10):
    print("<<<<< " + str(x*4 + 1) + "/40")
    print("^^^^^ " + str(x*4 + 2) + "/40")
    print(">>>>> " + str(x*4 + 3) + "/40")
    print("vvvvv " + str(x*4 + 4) + "/40")

