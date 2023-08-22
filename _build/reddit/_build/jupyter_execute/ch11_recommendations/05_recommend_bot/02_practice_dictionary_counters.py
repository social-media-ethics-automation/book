#!/usr/bin/env python
# coding: utf-8

# # Practice: Dictionary Counters
# 
# Now it's your turn to practice dictionary counters
# 
# 1. Copy the code from the demo that counts letters in a string. Modify the string to be something else and find the letter_counts (no need to sort)

# In[1]:


# TODO: enter your code here


# Now let's try this with words.
# 
# The code below makes a string, and then splits it into words by dividing it apart at each space.

# In[2]:


# Save a poem into a string (we can use """ to make a multiline string)
# Fire and Ice BY ROBERT FROST (now public domain)
poem = """Some say the world will end in fire,
Some say in ice.
From what I’ve tasted of desire
I hold with those who favor fire.
But if it had to perish twice,
I think I know enough of hate
To say that for destruction ice
Is also great
And would suffice."""

# split the string (all lowercase) into words
import re # import the Regular Expressions library, to help us split words

#make the poem all lowercase
lower_case_poem = poem.lower()

# split the poem into pieces at all spaces and newlines (\s), and ,'s and .'s
poem_split_by_spaces_and_punctuation = re.split(("[\s,.]"), lower_case_poem)

# get rid of some empty strings "" that ended up in our list
split_poem = list(filter(None, poem_split_by_spaces_and_punctuation))

print(split_poem)


# 2. Make code that counts how often each word appears in the poem (it should be very similar to the code from problem 1 above

# In[3]:


# TODO: enter your code here

