#!/usr/bin/env python
# coding: utf-8

# # Practice: Looping through lists and dictionaries
# ### Looping through lists

# 11. Create a loop. Loop through the list `test_list`. Display the first 5 tweets in the list.

# In[1]:


for text in ["Kyle", "Emily", "Another Person"]:
    sentence = text + " is awesome!"
    upper_sentence = sentence.upper()
    print(upper_sentence)

