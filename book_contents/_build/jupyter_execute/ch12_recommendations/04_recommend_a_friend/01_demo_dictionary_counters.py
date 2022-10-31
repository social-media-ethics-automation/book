#!/usr/bin/env python
# coding: utf-8

# # Demo: Dictionary Counters
# We've already seen in Chapter 8 how to make loop variables in order to keep track of something we are looping over. We are now going to learn a way of using dictionaries to do that which will help us solve more problems.
# 
# But first, let's remember how we did loop variables
# 
# ## Loop Variables (review)
# 
# To use loop variables, we create a variable before our loop, and give it an initial value (often 0). Then within the loop over each item in our list, we can optionally add something to our loop variable. After the loop, our variable will have our final result.
# 
# For example, here is code to count the number of "i"s in "Mississippi":

# In[1]:


# create a loop variable to track the total number of i's
# start it with 0, since we've seen 0 i's so far
num_i = 0

# go through each letter in the word
for letter in "Mississippi":
    # if the letter was an i, then add one to our loop variable
    if letter == "i":
        num_i += 1

# we now have the total number of i's
display("total number of i's was: " + str(num_i))


# In the code above we made a variable to count the number of "i"s. But what if we wanted to count the other letters? Then we'd need one variable for each letter. For the code above we could do this:

# In[2]:


# create a loop variable to track the total number of each possible letter
# start it with 0, since we've seen 0 letters so far
num_M = 0
num_i = 0
num_s = 0
num_p = 0

# go through each letter in the word
for letter in "Mississippi":
    # check each letter, then add one to the correct loop variable
    if letter == "M":
        num_M += 1
    elif letter == "i":
        num_i += 1
    elif letter == "s":
        num_s += 1
    elif letter == "p":
        num_p += 1

# we now have the total number of i's
display("total number of M's was: " + str(num_M))
display("total number of i's was: " + str(num_i))
display("total number of s's was: " + str(num_s))
display("total number of p's was: " + str(num_p))


# Now what if we didn't know what letters were possibly in the word we wanted to check? We'd need to make 26 variables, or if we had capital and lowercase letters separate, then we'd need 52 variables. But what about numbers? Punctuation? Other symbols?
# 
# Making separate loop variables is going to become a real pain. But there is another strategy we can use:

# ## Dictionary Counters
# We can make use of dictionaries, which are good for looking up values, to store information about each letter we come across.
# 
# So instead of having the variables: `num_M`, `num_i`, `num_s`, and `num_p`, we could have a dictionary called `letter_counts` that we want in the end to look like this:
# ```
# {
#     "M": 1,
#     "i": 4,
#     "s": 4,
#     "p": 2
# }
# ```
# 
# The way we can build up this dictionary in code is that we can create our `letter_counts` dictionary before the loop, and initialize it empty (`{}`), with no letters or count values.
# 
# Then, in our loop, when we see a letter, we can look it up in our dictionary. If we don't find it in our dictionary, we add that letter and set it's count to 1 (since we just saw one). If we did find a count already in our dictionary, then we add one to the count.
# 
# At the end, we will have entries in our dictionary for all the letters we found, showing their count. All the letters that don't have entries in are dictionary are ones we didn't find (implying their count is 0).
# 
# Here is the code re-written with a dictionary counter:

# In[3]:


# create a dictionary counter before the loop
# it has no entries, since we have seen no letters yet
letter_counts = {}

# go through each letter in the word
for letter in "Mississippi":
    if letter not in letter_counts: # If there is no entry for this letter yet 
        letter_counts[letter] = 1   # then make an entry set to 1
    else: # otherwise, there was an entry
        letter_counts[letter] += 1  # so add one to that entry

# we now have the total number of letters
display("total letter counts are: ")
display(letter_counts)


# Now we don't have to figure out what letters we are expecting, and we will just add as many entries to our dictionary as letters we come accross. We we can change our string we are looking through and our code still works:

# In[4]:


# create a dictionary counter before the loop
# it has no entries, since we have seen no letters yet
letter_counts = {}

# go through each letter in the string
for letter in "unexpected letters: &$$*&":
    if letter not in letter_counts: # If there is no entry for this letter yet 
        letter_counts[letter] = 1   # then make an entry set to 1
    else: # otherwise, there was an entry
        letter_counts[letter] += 1  # so add one to that entry

# we now have the total number of letters
display("total letter counts are:")
display(letter_counts)


# One final trick we'll do with our count dictionary, is order it by the most common letters (with the most common ones first).
# 
# This code has a few different Python features, so don't worry about it too much, but we'll explain it a little below

# In[5]:


# Sort the letter counts (and save in a new variable: sorted_letter_counts)
sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: -x[1])

display("total letter counts (sorted) are:")
display(sorted_letter_counts)


# The code above had a few new features. Again don't worry about understanding it too much, but the pieces of this code are:
# - `sorted()` - a function that takes a list, and a function that gets the value to use for sorting
# - `letter_counts.items()` - this takes a dictionary and gets all the key-value pairs (together in a list-like datatype called a "tuple"). So it has, for example ('e', 5) to mean the dictionary said the count for e was 5.
# - `key=lambda x: -x[1]` - this part is for getting the key (that is, the thing to be sorted)
#   - it takes a function (in this case a function that we don't give a name, which we call a `lambda` function)
#   - the function for each of the key-value pairs (saved into a variable called `x`), gets the value out (the second thing in the key-value pair, so `x[1]`) and makes it negative (`-x[1]`) so it puts the highest count first
