#!/usr/bin/env python
# coding: utf-8

# # Demo: Conditionals and String Manipulation
# 
# We are later going to build a bot that, if you tweet at it: 
# - "Hi @mybotname, please ___" (where the ___ is some action)
# - then the bot will reply, "I will now ____" (where the ___ is that same action).
# 
# But in order to build a bot that does this, we will first need to learn how to use conditionals (`if`) and some string manipulation techniques.

# ## Conditionals
# ### `if` statements
# 
# Conditionals let us change what we do depending on the situation. In a Python we do this using an `if` statement. 
# 
# Here is an example:

# In[1]:


if 1 < 2:
    display("We have determined that 1 is indeed less than 2")


# In the above code we can see the different pieces we need for an `if`:
# - We start by writing `if`
# - After the `if` we have a piece of code (an "expression") that will produce a booolean. In this case `1 < 2` checks if 1 is less than 2, and since it is, it `1 < 2` comes out as `True`
# - After expression that produced a boolean is a `:` which indicates that next will come a block of code indented over. That block of code will only run __if__ the expression came out as `True`
# - Inside the block of code we have a display statement, which runs because `1 < 2` came out as `True`
# 
# Let's do another example, but where the expression comes out as false

# In[2]:


if 1 > 2:
    display("We have determined that 1 is greater than 2")


# In this case we test if 1 is greater than two, but `1 > 2` comes out as `False`, so the code block in this if statement does not get run and we never display that "`We have determined that 1 is greater than 2`"

# ### `else` and `elif` statements

# What if we want to do something different if the expression turned out to be `False`? 
# 
# For that we can use `else` or `elif` statements.
# 
# Here's an example with `else`:

# In[3]:


if 1 > 2:
    display("We have determined that 1 is greater than 2")
else:
    display("We NOT have determined that 1 is greater than 2")


# In the above code, after the code block inside an `if`, we have an `else` (at the same indent as the `if`), with a `:` indicating that next will be a block of code to run in case the `if` expression came back as `False` (which it did, because 1 is not greater than 2).
# 
# Now, what if we have multiple courses of action we might want to take depending on several checks? For that we can use an `elif` (short for "else if") like this:

# In[4]:


if 1 > 1:
    display("1 is greater than 1")
elif 1 < 1:
    display("1 is less than 1")
else:
    display("1 is neither greater than 1, nor less than 1, so it must be equal to 1")


# The `elif` above works just like an `if` statement, but the check in the `elif` is only run if the `if` statement's check came back `False`.
# 
# _Note: in a sequence of an `if` statement, followed by `elif`s and ending with an `else`, only one of the code blocks will run._

# ### variables in `if` statements
# 
# In the above examples, all of our checks were based on specific numbers (like `1 > 2`), which will always come out to the same answer. But we can make our code more useful by using variables, like below:

# In[5]:


money_in_wallet = 7
cost_of_item = 5

if money_in_wallet > cost_of_item:
    change = money_in_wallet - cost_of_item
    display("You can purchase the item with $" + str(change) + " in change")
elif money_in_wallet == cost_of_item:
    display("You can purchase the item, but with no change")
else: # This else runs when money_in_wallet < cost_of_item
    display("You don't have enough money to purchase the item")


# In the above code we have variables that represent how much money we have in our wallet and the cost of the item. Note: You can change the values and run the code to get different results!
# 
# We then have a series of checks to see if we have more than enough money, or exactly the right amount of money. The final else will only run in the remaining situation where there wasn't enough money, so we added a comment to clarify this, even though the code will work fine without the comment.

# ## String Manipulation
# The next programming topics we need to cover have to do with string manipulation (which we will also use some with `if` statements)

# ### using strings like lists of characters
# Python lets us treat strings like a list of characters, so we can do things like:
# - loop through each character in a string
# - get the first character of the string
# 
# You can loop through each character of a string like this:

# In[6]:


important_word = "Ethics"

for character in important_word:
    print(character)


# The above code looped through the letters in "Ethics" and for each letter it printed the letter out on its own line (note: I use `print` instead of `display` because it happens to look better in the online textbook)
# 
# We can select letters as well by their index, like this:

# In[7]:


important_word = "Ethics"

display("The first letter is: " + important_word[0])


# In[8]:


display("The sixth letter is: " + important_word[5])


# Python also lets us do more complicated selections (called a "slice") by index using the format:
# - `[start_index : stop_index]`
# 
# So, for example, to select the first 3 letters of our string, we can do this:

# In[9]:


important_word[0 : 3]


# Note: The start index is the first index selected, and the stop index is the one it stops __before__. So our code `important_word[0 : 3]` selected the letters at indexes: 0, 1, and 2.
# 
# If we want to select the characters at index 2 and 3 (that is the 3rd and 4th letters), we would write:

# In[10]:


important_word[2 : 4]


# If we leave have the `:` in our square bracket selector but leave one side blank, that side will go to the beginning or end.
# 
# So if we want to select the first three characters we can write:

# In[11]:


important_word[ : 3]


# And if we want to select everything after the first 3 letters we can write:

# In[12]:


important_word[3 : ]


# Python also lets us index backwards from the end of the string using negative numbers. So if we wanted to select the last two letters, we can do that like this:

# In[13]:


important_word[-2 : ]


# You can read more about Python string slicing on [GeeksforGeeks](https://www.geeksforgeeks.org/string-slicing-in-python/)

# ### `if` statements and strings
# Now let's see how we can use if statements together with strings.
# 
# First we will use `in` to see if a string appears as part of another string

# In[14]:


weather_report = "The weather will be cold and rainy today"

if "cold" in weather_report:
    display("bring a jacket")
else:
    display("probably don't need a jacket")
    
if "rainy" in weather_report:
    display("bring an umbrella")
else:
    display("no need for an umbrella")


# In the above code we are looking to see if the weather_report includes the text "cold" and "rainy" to decide whether we need a jacket or umbrella. 
# 
# Note: you can see how this code could give bad advice if the weather report used unexpected words like: "The weather will be freezing and there will be a downpour." Getting computers to correctly interpret human language can be very hard!
# 
# Now let's look at an example of using string slices.

# In[15]:


user_preference = "My favorite vegitable is broccoli"


# check if the user is telling us their favorite vegitable
if user_preference[ : 25] == "My favorite vegitable is ":
    display("The user was telling us their favorite vegitable")


# Now, in the above code I had to count the length of the text "`My favorite vegitable is `" (25 characters long) so I could cut out the same length start of user_preference and see if it matched.
# 
# I can improve this code by using variables and having Python count that length for me like using the `len` function:

# In[16]:


user_preference = "My favorite vegitable is broccoli"


vegitable_start = "My favorite vegitable is "
vegitable_start_len = len(vegitable_start)

# check if the user is telling us their favorite vegitable
if user_preference[ : vegitable_start_len] == vegitable_start:
    display("The user was telling us their favorite vegitable")


# The above code is longer, but now I have python doing the counting for me, which makes it (hopefully) easier to modify and understand.
# 
# Python offers us one more way of improving this code, which is with a function called `startswith` which does what we are trying to do (and if we looked at the source code for `startswith`, it is probably similar to what we were doing)

# In[17]:


user_preference = "My favorite vegitable is broccoli"


vegitable_start = "My favorite vegitable is "

# check if the user is telling us their favorite vegitable
if user_preference.startswith(vegitable_start):
    display("The user was telling us their favorite vegitable")


# We can also use the length of the `vegitable_start` string to take the `user_preference` string to select the thing the user said was their favorite:

# In[18]:


user_preference = "My favorite vegitable is broccoli"


vegitable_start = "My favorite vegitable is "
vegitable_start_len = len(vegitable_start)

# check if the user is telling us their favorite vegitable
if user_preference.startswith(vegitable_start):
    favorite_vegitable = user_preference[vegitable_start_len: ]
    display("The user's favorite vegitable: " + favorite_vegitable)


# This gives us some of the pieces we need to  build a bot that, if you tweet at it: 
# - "Hi @mybotname, please ___" (where the ___ is some action)
# - will reply, "I will now ____" (where the ___ is that same action).
# 
# Though before we do that, we'll give you some additional practice with conditionals and strings.
