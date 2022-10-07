#!/usr/bin/env python
# coding: utf-8

# # Demo: Lists and Loops
# 
# ## Lists
# 
# Many types of data on social media platforms are organized as lists, such as
# - lists of friends or followers
# - lists of posts
# - lists of photos in a post
# - lists of people who liked a post
# - etc.
# 
# The way to create a list in Python is to make a list of values, separated by commas, inside of square brackets, like this:

# In[1]:


book_authors = ["Kyle Thayer", "Susan Notess"]

display(book_authors)


# If we are making a list and it gets too long, Python will let us use several lines to do this:

# In[2]:


some_book_chapters = ["Intro",
                     "Definitions",
                     "Bots",
                     "Data",
                     "History of Social Media",
                     "Authenticity"]

display(some_book_chapters)


# Lists are in order, so Python let's us use the "index" to ask for a specific entry, like the 1st, 2nd, 3rd, etc. 
# 
# As we stated in the Data chapter, many programming languages, for historical reasons, make a list's first entry have index 0, it's 2nd entry have index 1, it's 3rd entry have index 2, etc.
# 
# So if we want to see the first chapter in my `some_book_chapters` list, I select it by putting the index number inside square brackets (`[`, `]`) after the variable name:

# In[3]:


first_chapter = some_book_chapters[0]
display(first_chapter)


# And if I want the 4th chapter, I'd select it like this

# In[4]:


fourth_chapter = some_book_chapters[3]
display(fourth_chapter)


# Now, let's say we have a list of Twitter users who liked our latest tweet:

# In[5]:


users_who_liked_our_tweet = ["@pretend_user_1", "@pretend_user_2", "@pretend_user_3"]


# What if we wanted to follow all of them?
# 
# If our list was long, it would take a lot of code to pull out each one and try to follow them. But Python gives us an easy way to perform actions on all the items in a list, by using `for` loops.

# ## `for` Loops
# 
# 
# `for` loops let us perform an action or a set of actions for all of the items in a list.
# 
# So, if we wanted to go through all the the users that liked our tweet and display a message for each one, we could do this:

# In[6]:


for user in users_who_liked_our_tweet:
    display("Yay! " + user + " liked our tweet!")


# Now, there are several things that went into making that for loop code above:
# - Start the line with a `for`
# - Make up a new variable name that will be a temporary variable to hold whichever item from the list we are doing our actions on. In this case each item in the list will be a user, so we call our variable `user`
# - Then we write the word `in` 
# - Then we put the list that we want to go through, in this case `users_who_liked_our_tweet'
# - Then put a colon (`:`). In Python, a colon like this means that what comes next is a block of statements that goes together. This block of statements is indented over to indicate that it is part of the block.
# - Then, on the next line and indented over, we have our display function that uses the `user` variable. This is the line of code that is repeated for each item in the list.
# 
# If we want to do several actions in our loop, all we need to do is add more lines of code spaced over the same amount, like this (note: We'll use `print` instead of `display`, which mostly work the same, but we think `print` happens to look a little better in this situation):

# In[7]:


for user in users_who_liked_our_tweet:
    print("Yay! " + user + " liked our tweet!")
    print("Perhaps we should follow " + user)
    print("We could put tweepy code here to do that!")
    print()


# In the above code our for loop runs a block of code that has four statements, each doing a `print`. You'll notice we added an extra blank `print` which makes a blank line and helps us see in the output what each loop did.

# ### Loop a set number of times
# In order to loop a set number of times, we can use the `range` function to effectively make a list of numbers to go over, so we can loop that many times. 
# 
# For example, if we wanted to ask "Are we there yet?" repeatedly, 10 times, we can do this:

# In[8]:


for i in range(10):
    print("Are we there yet?")


# Now, if we look at what the numbers were in `range(10)`, we can output the `i` we saved the numbers in.

# In[9]:


for i in range(10):
    print("This is loop number " + str(i))


# You'll notice that, while there are 10 numbers, it starts with 0, just like how list indices start with 0.
# 
# If we want to do a list from 1 to 10 instead, we can do that by either making a new variable and saving i + 1 to it, like this:

# In[10]:


for i in range(10):
    new_i = i + 1
    print("This is loop number " + str(new_i))


# Or, the `range` function let's you set a start and stop, with the first number being the number it starts with, and the last number being the one it stops before:

# In[11]:


for i in range(1, 11):
    print("This is loop number " + str(i))

