#!/usr/bin/env python
# coding: utf-8

# # Ch 5 Practice: Looping through lists and dictionaries
# Try out these coding problems to practice looping, lists, and dictionaries

# Make a loop that displays "Are you awake yet?" 5 times

# In[1]:


for i in range(5):
    display("Are you awake yet?")


# Make a list of names (at least three), and save it in a variable called `names`

# In[2]:


names = ["Kyle", "Susan", "Another person"]


# Now loop over each of those names, and for each name display "[name] is awesome!"

# In[3]:


for name in names:
    display(name + " is awesome!")


# Now, do the same thing as before, but for each name, first make a string that has "[name] is awesome!" and save it in a variable, then use the `.upper()` function on the string to make it all uppercase and save it into a variable, then display the final string.

# In[4]:


for text in names:
    sentence = text + " is awesome!"
    upper_sentence = sentence.upper()
    display(upper_sentence)


# Now, we are going to make a dictionary with information on a photo

# In[5]:


photo_1_info = {
    "width": 800,
    "height": 600,
    "location": "that one mountain",
    "device": "iPhone 6"
}


# Select and display the width of the photo

# In[6]:


photo_1_info["width"]


# Select and display the location of the photo

# In[7]:


photo_1_info["location"]


# Now we are going to make a list of photo info for you to go through

# In[8]:


photo_info_list = [
    {
        "width": 800,
        "height": 600,
        "location": "that one mountain",
        "device": "iPhone 6"
    },
    {
        "width": 800,
        "height": 600,
        "location": "on the lake",
        "device": "iPhone 5"
    },
    {
        "width": 1600,
        "height": 800,
        "location": "The underground mines",
        "device": "Nokia 3310"
    }
]


# Now, make a for loop to go through each set of phone info in `photo_info_list`, and for each one, use `print` commands to display the width, height, location, and device

# In[9]:


for photo_info in photo_info_list:
    print(photo_info["width"])
    print(photo_info["height"])
    print(photo_info["location"])
    print(photo_info["device"])
    print()

