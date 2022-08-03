#!/usr/bin/env python
# coding: utf-8

# ## Scheduling Tasks Demo

# This lab focuses on scheduling tasks. We're giving you some examples of python library features you could use for your project if you choose to.

# #### Run this code block to install the 'schedule' package

# In[1]:


get_ipython().system(' pip install schedule')


# #### Run this code block to import schedule and time libraries.

# In[2]:


import schedule
import time


# #### Run this code block to define a function called `job`.

# In[3]:


def job():
    print("I'm working...")


# ### You can schedule a task to run periodically using `schedule.every()`

# schedule is a simple library used to schedule the of running functions. You can create bots for automated processes that enable programs to run without human interaction. We'll be going through some examples of how you could do this.

# ### Before we go over some examples, let talk about how to Interrupt the Kernel & why this matters.

# ##### The task of scheduling, especially in this lab, usually creates an infinite loop. An infinite loop is a sequence of instructions that will continue endlessly, unless an external intervention occurs.
# 
# ##### To stop a code block from continuing to run, you can use the stop kernel button at the top of your JupyterHub Notebook:
# 
# &nbsp; &nbsp; &nbsp; <img src="stop_kernel.png" alt="a screenshot of the top bar of JupyterHub wiith an arrow pointing ar the 'stop kernel'" width="500" />

# ### Try out the following example:

# In[4]:


# This line of code runs the "job" function every 10 seconds.
# Note: If you want to run the next code block, press the stop kernel button

schedule.every(10).seconds.do(job)

# Loop so that the scheduling task keeps on running forever.
while True:
    schedule.run_pending()
    time.sleep(1)


# ### Try out the following example with minutes:

# In[ ]:


# This line of code runs the "job" function every 2 minutes.
# Note: If you want to run the next code block, press the stop kernel button

schedule.every(2).minutes.do(job)

# Loop so that the scheduling task keeps on running forever.
while True:
    schedule.run_pending()
    time.sleep(1)


# ### These are a few more examples you could use in your projects (you probably don't want to run this code block right now): 

# In[ ]:


# runs a task every 10 minutes
schedule.every(10).minutes.do(job)

# runs a task every x hours
schedule.every().hour.do(job)

# runs a task at a specific time of day
schedule.every().day.at("10:30").do(job)

# runs a task every 5 to 10 minutes
schedule.every(5).to(10).minutes.do(job)

# runs a rask every monday
schedule.every().monday.do(job)

# runs a task every wednesday at 1:15pm
schedule.every().wednesday.at("13:15").do(job)

# runs a task every 
schedule.every().minute.at(":17").do(job)

# Loop so that the scheduling task keeps on running forever.
while True:
    schedule.run_pending()
    time.sleep(1)


# #### 1. YOU TRY: Create a function of your choice.

# In[ ]:





# #### 2. Implement a scheduling task to run your function every 3 seconds. 

# In[ ]:





# #### CHALLENGE: Check out the documentation and implement a scheduling task not shown in any of the previous examples: 
# 
# https://schedule.readthedocs.io/en/stable/
# 
# https://schedule.readthedocs.io/en/stable/examples.html

# In[ ]:




