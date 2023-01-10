#!/usr/bin/env python
# coding: utf-8

# # Ch 8 Practice: Sentiment Analysis and Loop Variables

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


sentence = "This is an ok example"
sia.polarity_scores(sentence)["compound"]


# Try several sentences and see how the Sentiment Intensity Analyzer handles them

# In[4]:


sentence = "This is a horrible example"
sia.polarity_scores(sentence)["compound"]


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


num_letters = 0

for letter in "Mississipi":
    print(letter)
    num_letters += 1
    
print("There were " + str(num_letters) + " letters")


# Make another copy of what you just did, but this time also count the number of "i"s. Make a variable called `num_i` to count how many "i"s. 
# 
# _Hint: To see if a letter is an "i", check if `letter == "i"`_
# 
# At the end print out how many of the letters were "i"s and what percentage of the word was "i"s.

# In[7]:


num_letters = 0
num_i = 0

for letter in "Mississipi":
    print(letter)
    num_letters += 1
    
    if(letter == "i"):
        num_i += 1
    
print("There were " + str(num_letters) + " letters")

percent_i = num_i / num_letters * 100

print("i's made up " + str(percent_i) + " percent of the word")


# In[ ]:




