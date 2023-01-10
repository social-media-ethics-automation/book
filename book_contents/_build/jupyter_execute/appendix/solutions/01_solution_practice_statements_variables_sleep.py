#!/usr/bin/env python
# coding: utf-8

# # Ch 3 Practice: Statements and Variables

# This Python Notebook is a chance for you to try out the programming concepts we have covered thus far.
# 
# As we mentioned previously in the first bot demo (2.3.8), in order to run the code, you can look for the rocket button at the top which will give you an option to "launch binder"
# 
# ![screenshot of this page in the online textbook, with the launch binder link highlighted under the rocket button at the top.](binder_link.png)
# 
# If you launch binder, it will take a while to load, but eventually show you a version of this page Jupyter Notebook in a code editor called Jupyter Lab
# 
# ![a screenshot of this page viewed in jupyter_lab, with menus and options above the editable page](jupyter_lab.png)
# 
# In Jupyter Lab you can double click any section to edit it, and you can press the triangle "run" button to run the code (or display the text).
# 
# ![a screenshot of this page viewed in jupyter_lab,with the triangle "run" button circled. Next to it are a square "interrupt the kernal" button and other options](jupyter_run_code.png)
# 
# When the code runs, the little number to the left of the code block should change. There might also be some output from your action displyed below the code block.
# 
# So now you can go through the rest of this page and try out the practice exercises for yourself!
# 

# ## Variables
# You will first practice saving values into variables. Remember, the way we save a value into a variable is like this:
# ```
# variable_name = value
# ```
# 
# First, save the piece of text "I am writing a computer program!" into a variable called `my_progress`

# In[1]:


my_progress = "I am writing a computer program!"


# ### Viewing variables in the debugger
# Before we continue, we are going to show you how to open the debugger so you can see what is being saved in your variables.
# 
# On the tp right of this tab, press the small bug icon to "enable debugging":
# 
# ![screenshot of this tab in jupyterhub, with the "enable debugging" icon circled at the top right (after the "git" option and before the "Python 3 (ipykernel)" option)](debugging_icon.png)
# 
# Then, if you did the step above correctly, you should see the variable `my_progress` with the value "I am writing a computer program!" next to it:
# 
# ![screenshot of this tab in jupyterhub, with the debugger tab opened on the right. The top section of that tab is variables, which has "special variables" then "function variables" then "my_progress:I am writing a computer program"](debugger_vars.png)

# ### Practice number variables
# First, write and run a line of code to save the value 5 into a variable named `number_of_pies`

# In[2]:


number_of_pies = 5


# Now, save the value 12.5 into a variable named `cost_per_pie`

# In[3]:


cost_per_pie = 12.5


# Now make a new variable called `total_pie_cost` and save into the value of the number_of_pies multiplied by the cost_per_pie.
# 
# Note: In python (and many programming languages), the symbol for multiply is `*`

# In[4]:


total_pie_cost = number_of_pies * cost_per_pie


# Now use the `display` function to display what is saved in total_pie_cost

# In[5]:


display(total_pie_cost)


# ### More variable practice
# 
# Now, make a new variable called `first_name` and assign your first name to it

# In[6]:


first_name = "Kyle"


# Now, make a variable calles `last_name` and save your last name to it

# In[7]:


last_name = "Thayer"


# Create a variable called `age` and assign your age to it.

# In[8]:


age = 38


# ~ A year goes by ~
# 
# Increase the `age` variable by 1. 

# In[9]:


age = age + 1


# Now write three lines of code, with each line using `display` to show what is saved in `first_name`, `last_name`, and `age 

# In[10]:


display(first_name)
display(last_name)
display(age)


# ## Sleep
# In order to use sleep, we must first import it from the time library

# In[11]:


from time import sleep


# Now try displaying 5 messages of your choosing, with some pauses between each one:

# In[12]:


display("message 1")
sleep(.01) #I am making these pauses small to make the book build faster
display("message 2")
sleep(.02)
display("message 3")
sleep(.01)
display("message 4")
sleep(0.05)
display("message 5")


# ## Reddit Bot Practice
# Now lets try a Reddit bot with variables and sleep!
# 
# ### Load Praw Library
# First, we need to load the praw library

# In[13]:


# Load some code called "praw" that will help us work with reddit
import praw


# ### (Optional) Step 1b: Make a fake praw connection with the fake_praw library
# For testing purposes, we've added this line of code, which loads a fake version of praw, so it wont actually connect to reddit. __If you want to try to actually connect to reddit, don't run this line of code.__

# In[14]:


get_ipython().run_line_magic('run', '../../fake_apis/fake_praw.ipynb')


# ### Step 2: Load your developer access passwords
# To use this on your real Reddit account, copy your [developer access passwords](../../appendix/bot_set_ups/making_reddit_account.md) into the code below, replacing our fake passwords.

# In[15]:


# Load all your developer access passwords into Python
# TODO: Put your reddit username, password, and special developer access passwords below:
username="fake_reddit_username"
password="sa@#4*fdf_fake_password_$%DSG#%DG"
client_id="45adf$TW_fake_client_id_JESdsg1O"
client_secret="56sd_fake_client_secret_%Yh%"


# ### Step 4: Give praw (or fake_praw) your developer access passwords

# In[16]:


# Give the praw code your reddit account info so
# it can perform reddit actions
reddit = praw.Reddit(
    username=username, password=password,
    client_id=client_id, client_secret=client_secret,
    user_agent="a custom python script"
)


# ### Step 5: Submit a post to Reddit
# Post something you learned in the class so far:
# 
# Remember, the code to post a tweet looks like this: 
# ```
# reddit.subreddit(
#    "soc_media_ethics_auto"
# ).submit(
#    "This is the title of the post", 
#    selftext = "This is the content of the post"
# )
# ```

# In[17]:


reddit.subreddit(
   "soc_media_ethics_auto"
).submit(
   "I found a way to solve the practice problem", 
   selftext = "I learned to look at the answer key!"
)


# ### Post from a variable
# Now try saving a piece of text in a variable for the title, and another for the content of a post, and then submitting a post of whatever you saved in the variables. 
# 
# To do this, where the code has `submit( ... )`, you'll replace the quoted text with the variable name, so it will look like:
# ```
# reddit.subreddit(
#    "soc_media_ethics_auto"
# ).submit(
#    title_variable, 
#    selftext = content_variable
# )
# ``` 
# (with whatever your variable name was instead of "title_variable" and "content_variable")

# In[18]:


title_to_post = "I can use more complicated code"
message_to_post = "by storing something in a variable"

reddit.subreddit(
   "soc_media_ethics_auto"
).submit(
   title_to_post, 
   selftext = message_to_post
)


# ### Submit multiple posts
# Next try submitting 3 posts, but use `sleep` to add pauses between each one (note that reddit might not want you to make more than 1 post every 15 minutes, so you can sleep for 15*60 seconds or more before posting again).
# 
# 

# In[19]:


reddit.subreddit(
   "soc_media_ethics_auto"
).submit(
   "Message 1", 
   selftext = "This is the first message"
)

sleep(.01) #note: I am using short times since these pauses slow down compiling the book

reddit.subreddit(
   "soc_media_ethics_auto"
).submit(
   "Message 2", 
   selftext = "This is the second message"
)

sleep(.02)

reddit.subreddit(
   "soc_media_ethics_auto"
).submit(
   "Message 3", 
   selftext = "This is the third message"
)

