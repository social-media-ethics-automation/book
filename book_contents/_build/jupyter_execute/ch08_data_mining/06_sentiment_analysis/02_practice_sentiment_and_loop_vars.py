#!/usr/bin/env python
# coding: utf-8

# # Practice: Sentiment Analysis and Loop Variables

# Now it's your turn to practice sentiment analysis and loop variables
# 
# ## Sentiment Analyasis
# First run the code to load up the Sentiment Intensity Analyzer

# In[1]:


import nltk
nltk.download(["vader_lexicon"])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# Also, look at this example from the demo of running sentiment analysis:

# In[2]:


sentence = "I love love love pizza!!!!!!!!"
sia.polarity_scores(sentence)["compound"]


# Now, copy that two lines of code above, and try out your own sentences, and run the sentiment analysis on them

# In[3]:


# TODO: enter your code here


# Try several sentences and see how the Sentiment Intensity Analyzer handles them

# In[4]:


# TODO: enter your code here


# ## Loop variables
# 
# Now let's practice with loop variables.
# 
# Below is a for loop which goes through each letter in the word "Mississipi".

# In[5]:


for letter in "Mississipi":
    print(letter)


# Make another copy of that loop, but add a variable before the loop called `num_letters` and use it count how many letters were in the word "Mississipi". At the end display the number of letters.

# In[6]:


# TODO: enter your code here


# Make another copy of what you just did, but this time also count the number of "i"s. Make a variable called `num_i` to count how many "i"s. 
# 
# _Hint: To see if a letter is an "i", check if `letter == "i"`_
# 
# At the end print out how many of the letters were "i"s and what percentage of the word was "i"s.

# In[7]:


# TODO: enter your code here

