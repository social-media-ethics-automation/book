#!/usr/bin/env python
# coding: utf-8

# # Demo: Statements, Variables, and Sleep

# ## Statements
# As we said before, a computer program in a programming language like Python is often composed of a list of statements, that is steps to be run in order (like a recipe):
# ```text
# - statement 1
# - statement 2
# - statement 3
# ```
# 
# In Python, generally each new line of code is a new statement, to be run after the previous statement.
# 
# We will start writing statements using a line of code that looks like this which runs a function called `display`:
# 
# ```display("Ethics might be relevant!")```
# 
# Below you will see this line of code (one statement), and right below it will be displayed the text in the quotes ("Ethics might be relevant!").

# In[1]:


display("Ethics might be relevant!")


# Now let's try several statements in a row, with mulitple lines of code that display text:

# In[2]:


display("This book is about:")
display("  - Social Media")
display("  - Ethics")
display("  - Automation")


# Now that we've made multple statements in a row, let's do something a little more complicated than just displaying text by using variables.

# ## Variables and assignment (single "=")
# 
# As we said in the previous section, Variables are a way of saving information on the computer, so we can use it later in the computer program, similar to how we might put mix ingredients in different bowls, using the mix from each bowl at the relevant time.
# 
# In a computer program, these variables are given names so we can more easily get the information back out again.
# 
# ### Saving a text value
# To store something in a variable (called "assigning" it a value), write the variable name, followed by an "=" symbol, followed by whatever we want to save in the variable. For example:

# In[3]:


greetings_message = "Hello and welcome to programming with variables!"


# The line of code above saved the text "Hello and welcome to programming with variables!" into a variable called "`greetings_message`"
# 
# Since this was just saving something into the computer, there is nothing displayed after we run that line of code.
# 
# Note: The `=` symbol in Python does not mean the same thing it does in a math formula. In a math formula, "=" means that both sides of the equation are the same (like "1 + 1 = 2"). In Python, `=` means that the value on the right gets stored into the variable on the left (this is called "assignment", that is, assigning a value into a variable).
# 
# ### Displaying a value
# If we want to see what we saved in the variable we can display it using the display function.

# In[4]:


display(greetings_message)


# ### Storing numbers
# We can also store numbers in variables. For example, we can save 
# - the number of likes a tweet has in a variable called "`number_likes`"
# - the number of replies a tweet has in a variable called "`number_replies`"
# - the number of quote tweets a tweet has in a variable called "`number_quote_tweets`"
# 
# (We're just invent numbers for these for now)

# In[5]:


number_likes = 30
number_replies = 12
number_quote_tweets = 8


# Again, the computer shows no output after running these lines of code, but the computer now has numbers saved for "`number_likes`", "`number_replies`", and "`number_quote_tweets`"
# 
# ### Displaying multiple variables
# We can see what is saved in those variables by calling the `display` function again:

# In[6]:


display(number_likes)
display(number_replies)
display(number_quote_tweets)


# ### Taking from variables and storing in new variable
# In python we can look up variables and do something with them and save them into new variables. For example, if we consider "total engagement" of a tweet to be the sum of all the number of likes, replies, and quote tweets, we can calculate that and store it into a new variable:

# In[7]:


total_engagement = number_likes + number_replies + number_quote_tweets


# And then we can see what was saved in that new variable:

# In[8]:


display(total_engagement)


# ### Updating a variable value
# One particular trick we can do with variables is look up what is currently stored in the variable, update the value, and resave it into the same variable. 
# 
# For example if I have a variable called `current_likes` that has the the number 5 stored in it:

# In[9]:


current_likes = 5


# Now, if someone pressed the like button, we'd want to make that number one higher (6). 
# 
# To do this, we can look up the value in current likes and add 1 to it by writing `current_likes + 1`, and then we can store this updated value into current_likes but putting `current_likes =` in front, like this:

# In[10]:


current_likes = current_likes + 1


# Remember: the `=` sign in programming isn't saying both sides are equal like in math, it is saying, take the value on the right of the `=`, and store it into the variable on the left of the `=`.
# 
# We can display the current_likes and see it is now 6

# In[11]:


display(current_likes)


# We can run the same line of code again and see the number get higher each time

# In[12]:


current_likes = current_likes + 1
display(current_likes)


# In[13]:


current_likes = current_likes + 1
display(current_likes)


# ### Other options for displaying
# Before we move on we wanted to show you two more ways of viewing a variable:
# 
# There is a function called `print` that does almost the exact same thing as `display`, it "prints" the output to the screen (not to paper). Note: `print` is a commonly used function in Python, so you may see `print` if you look at other Python code.
# 
# 
# 
# - just write variable name (if it is the last thing in the code block
# - print()

# In[14]:


print(current_likes)


# The other way of displaying a variable value is to just write the name of the variable. 

# In[15]:


current_likes


# But this way of displaying a variable will only work if it is the last line of code in the code block. So if I write a bunch of variables on their own lines, only the last one will be displayed:

# In[16]:


number_likes
number_replies
number_quote_tweets
current_likes


# ## Sleep (pausing)
# 
# One thing we can make our code do is pause before continuing. To do this we will use a function called `sleep` that comes from a code library called `time`. 
# 
# So we will start by importing that `sleep` function from `time`:
# 

# In[17]:


from time import sleep


# Now that we have sleep imported, we can use it to pause between code actions. This will be most noticeable when we are displaying something, like this:

# In[18]:


display("I am displaying a message before pausing for two seconds")

sleep(2)

display("I have finished my two second pause. Now I will pause for 3 more seconds")

sleep(3)

display("I have finished the three second pause, and now I am done")


# If you run the code above you will see that the program pauses as it displays the output above.
# 
# These pauses may come in handy when posting tweets, to make it look like your bot is taking time to type in the text. You will get a chance to try that in the next practice section.
