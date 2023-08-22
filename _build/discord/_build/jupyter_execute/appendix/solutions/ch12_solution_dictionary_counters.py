#!/usr/bin/env python
# coding: utf-8

# # Ch 12 Solution: Dictionary Counters
# 
# Now it's your turn to practice dictionary counters
# 
# 1. Copy the code from the demo that counts letters in a string. Modify the string to be something else and find the letter_counts (no need to sort)

# In[1]:


# create a dictionary counter before the loop
# it has no entries, since we have seen no letters yet
letter_counts = {}

# go through each letter in the string
for letter in "your text here":
    if letter not in letter_counts: # If there is no entry for this letter yet 
        letter_counts[letter] = 1   # then make an entry set to 1
    else: # otherwise, there was an entry
        letter_counts[letter] += 1  # so add one to that entry

# we now have the total number of letters
display("total letter counts are:")
display(letter_counts)


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


# 2. Make code that counts how often each word appears in `split_poem` (it should be very similar to the code from problem 1 above, but you should have `word_counts` instead of `letter_counts`, and you should loop over `word`s instead of `letter`s)

# In[3]:


# create a dictionary counter before the loop
# it has no entries, since we have seen no words yet
word_counts = {}

# go through each word in the list of words
for word in split_poem:
    if word not in word_counts: # If there is no entry for this word yet 
        word_counts[word] = 1   # then make an entry set to 1
    else: # otherwise, there was an entry
        word_counts[word] += 1  # so add one to that entry

# we now have the total number of words
display("total word counts are:")
display(word_counts)


# In[ ]:




