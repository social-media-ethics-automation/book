#!/usr/bin/env python
# coding: utf-8

# # Practice: Python Data Types

# In[ ]:





# ### String Manipulation

# *Some notes: A string is a list of characters in order. An empty string is a string that has 0 characters. Python recognize as strings everything inside quotation marks
# (” ” or ‘ ‘).

# ### String Review!

# 12. Create a variable that stores the string "Hello World". Return only the second word using indexing.

# In[ ]:





# 13. Using the variable you made in question #12, store the first letters of both words in a new variable called `first_characters`.

# In[ ]:





# 14. Return the length of the variable you made in question #12.

# In[ ]:





# ### count()

# The `count()` function returns the number of times a specified character is in a string.

# In[1]:


# try out the following example:

weather = "Seattle has a slight drizzle"
weather.count('t')


# 15. Return the number of times the character 'l' is in "Hello World" using `count()`

# In[ ]:





# ### index()

# The `index()` function finds the first occurrence of the specified value. It raises an exception if the value is not found.

# In[2]:


# try out the following example:

weather.index('t')


# In[3]:


# try out the following example:

weather.index('drizzle')


# In[4]:


# try out the following example:

weather.index('p')      # it should return an error!


# 16. Return the index of the word, "World" in "Hello World".

# In[ ]:





# ### upper() & lower()

# These functions change upper and lower case strings

# In[ ]:


# Try out the following example:

weather = weather.upper()
weather


# In[ ]:


# Try out the following example:

weather = weather.lower()
weather


# 17. Change your "Hello World" string to all upper case letters.

# In[ ]:





# ### quotes

# What if you want to include the quote character " inside of a string? You can put a backslash character followed by a quote (\" or \'). This is called an escape sequence. Python will remove the backslash, and put just the quote in the string.
# 
# It looks like this:
# 
# ```
# print('Bob\'s favorite language is Python')
# ```

# In[ ]:


# try it out:

print('Bob\'s favorite language is Python')


# In[ ]:


# again with double quotes:

print("Bob once said, \"Coding is so fun!\"")


# 18. Print your own sentence with quotes!

# In[ ]:





# ### the 'in' operator

# The 'in' operator is the best way to check if a python string contains a substring.
# 
# Here's what it looks like:
# 
# ```
# 
# if "Seattle" in "Seattle has a slight drizzle":
#     print("Exists")
# ```

# In[ ]:


# try it out:

if "Seattle" in "Seattle has a slight drizzle":
    print("Exists")


# In[ ]:


# similar example:

if "Seattle" in "San Francisco has a slight drizzle":
    print("Exists")
else:
    print("Does not exist")


# In[ ]:


# you can also use variables:

if "seattle" in weather:
    print("Exists")


# 19. Find out if "hey" is in "Hello World" using the 'in' operator.

# In[ ]:





# ### split() function

# The `split()` function splits a string into a list.

# In[ ]:


# try out the following example:

hello_example = "Hello world! Who's ready to code?"

hello_example = hello_example.split()

print(hello_example)


# In[ ]:


# try out this example:

weather_example = "it was a gloomy, rainy, brisk Wednesday morning."

weather_example = weather_example.split(", ")

print(weather_example)


# 20. Split a sentence of your choice based on spaces:

# In[ ]:





# 21. Split your UW email based on the "@" symbol:

# In[ ]:




