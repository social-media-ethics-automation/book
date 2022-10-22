#!/usr/bin/env python
# coding: utf-8

# # Demo: Writing Functions
# 
# Before we can do our demo of tracking tweepy use, we need to learn how to create functions in Python.
# 
# Functions allow us to run another computer program. In our recipe analogy earlier, we said it was like:
# 
# `- Make the dumpling dough (see recipe on page 42).`
# 
# Or
# 
# `- to make dumplings vegan, make the dumpling dough (see recipe on page 42), but instead of using the egg, subsititute 2 teaspoons olive oil and 2 tablespoons hot water.`
# 
# ## Benefits of Functions
# There are several advantages to creating and using functions in computer programs, such as:
# 
# __Reusing code instead of repeating code__: When we find ourselves repeating a set of actions in our program, we end up writing (or copying) the same code multiple times. If we put that repeated code in a function, then we only have to write it once and then use that function in all the places we were repeating the code. 
# 
# __Single, standardized definitions__: Let's say we made code that takes a name and tries to split it into a first name and last name, and we have that code copied in several places in our program. Then we realize that our code isn't handling some last names correctly, like "O'Reilly" and "Del Toro." If we fix this bug in one of the places the code is copied in our program it still will be broken elsewhere, so we have to find all the places and fix it there. If, on the other hand we had the code to split names in a function, and used that function everywhere else, then we only have to fix the bug inside that one function and our code everywhere is fixed.
# 
# __Code organization__: Making functions also can help us organize our code. It lets us give a name to a block of code, and when we use it, those function names can help make the code more understandable. Making code as functions also helps in letting us put those pieces of code in other files or in code libraries, so the file we are working on is smaller and easier to manage.
# 
# 
# ## Using Functions
# 
# We have been using many functions so far in this book, such as:
# - `display(2 + 2)`
# - `sleep(3)`
# - `client.create_tweet(text="This is a tweet")`
# - `sentence.upper()`
# 
# Now we will be defining our own functions, which we can then use later in our code.

# ## Defining Functions 
# 
# In Python a function is defined using the 'def' keyword.
# 
# Creating a Function:
# 
# ```
# def function_name(argument1, argument2):
#     STATEMENT
#     STATEMENT
#     STATEMENT
# ```
# 
# Using a Function that you previously made:
# 
# ```
# function_name(argument1, argument2)
# ```
# 
# 
# Let's start with an example function that doesn't use any arguments:

# In[1]:


def say_hi():
    print("Hi!")


# In the code above, `def` tells Python we want to define a funciton, `say_hi` is the name we chose for our function, and the empty parentheses `()` mean that it doesn't take any parameters. There is then a colon (`:`) to say what follows is a code block that will be what happens when the function is called.
# 
# When we run the code above that defines our function, we don't see any output, but now the function `say_hi` exists and is ready for us to try using it:

# In[2]:


say_hi()


# We can now call this function many times, for example in a `for` loop

# In[3]:


for i in range(5):
    say_hi()


# We can also re-define our functions by doing a new `def` statement. It will just replace the old functions definition with the new one:

# In[4]:


def say_hi():
    print("Hi there!")


# In[5]:


for i in range(5):
    say_hi()


# ## Parameters
# Parameters (also called "arguments") are like variables for a function.
# 
# In the definition of the function, you can list inside the parentheses the parameters you want to be given for you to use in your function code.
# 
# Let's redefine our `say_hi` function so it takes a paratemeter for the name of a person to say hi to:

# In[6]:


def say_hi(name):
    print("Hi " + name + "!")


# Now when we call the function `say_hi` we need to give it a value in the parentheses (or it gives us an error: `missing required positional argument`)

# In[7]:


say_hi("Kyle")


# We can again use a loop to call our function multiple times, but this time we will loop over a list of names and send a different name each time the function runs:

# In[8]:


names = ["Kyle", "Susan", "Another Person"]
for name in names:
    say_hi(name)


# We can make a function that takes multiple parameters. Let's redefined our function again to take first and last names:

# In[9]:


def say_hi(first_name, last_name):
    print("Hi " + first_name + " " + last_name + "!")


# In[10]:


say_hi("Kyle", "Thayer")


# ## Returns
# 
# In the above examples, our `say_hi` performs an action of displaying text (we used the `print` function).
# 
# But if we try to save what comes back from running the function:

# In[11]:


say_hi_result = say_hi("Kyle", "Thayer")


# In[12]:


display(say_hi_result)


# It says that nothing (`None`) came back out of the function.
# 
# There are other functions that we've run that have had things come back that we can save in a variable, like counting the number of characters in a string with `len`.

# In[13]:


num_letters = len("Ethics")


# In[14]:


display(num_letters)


# In Python, when we want to send something back that can be saved in a variable, we use a `return` in our function definition, like this function which creates the hi message and doesn't display it:

# In[15]:


def create_hi_message(first_name, last_name):
    hi_message = "Hi " + first_name + " " + last_name + "!"
    return hi_message


# The return says what value to send back to wherever the function was called. In this case we are sending back what got saved in the `hi_message` variable. 
# 
# When we use this function, we can save the result in a variable:

# In[16]:


tweet_to_make = create_hi_message("Kyle", "Thayer")


# This time the variable had the message saved, but nothing was displayed. We can now display the variable to see what was saved:

# In[17]:


display(tweet_to_make)


# If we want, we can simplify the code by telling return to just send back whatever `"Hi " + first_name + " " + last_name + "!"` is instead of saving it in an `hi_message` variable first.

# In[18]:


def create_hi_message(first_name, last_name):
    return "Hi " + first_name + " " + last_name + "!"


# In[19]:


tweet_to_make = create_hi_message("Susan", "Notess")


# In[20]:


display(tweet_to_make)


# ## Wrapping Functions
# One final trick we can do is wrap a function in another function. 
# 
# This is a bit of an unusual trick, so you generally don't have to worry 5oo much about it, but we are going to use it in the "Track Tweepy Use" demo shortly, so we want to explain it.
# 
# Let's start with a function that adds two numbers together (and yes, this is an unneccesarily complicated replacement for just using `+`)

# In[21]:


def add_numbers(num_1, num_2):
    return num_1 + num_2


# We can use this function to calculate the current state of our money:

# In[22]:


my_money = 4
money_you_gave_me = 3

my_current_money = add_numbers(my_money, money_you_gave_me)


# In[23]:


display(my_current_money)


# Now, we can take this function that already exists `add_numbers` and make a `new_add_numbers` function that works the same (it takes the same parameters and then calls the old `add_numbers` function with them), but it also displays what numbers it was called with.

# In[24]:


def new_add_numbers(num_1, num_2):
    display("--add_numbers was called with " + str(num_1) + " and " + str(num_2))
    return add_numbers(num_1, num_2)


# We've now "wrapped" a new function (`new_add_numbers`) around the old `add_numbers` function. 
# 
# When we use this new_add_numbers function, we see the output display when the function is called, but we still get the same result back.

# In[25]:


my_money = 4
money_you_gave_me = 3

my_current_money = new_add_numbers(my_money, money_you_gave_me)


# In[26]:


display(my_current_money)


# Now, we can take this one step further and _replace_ the original add_numbers function with the wrapped version. To do this, we need to save the old `add_number`s function in a variable which we will call `old_add_numbers` (and yes, we can save functions themselves into variables just like they were any other value)

# In[27]:


# save the original add_numbers function
old_add_numbers = add_numbers

# wrap a new add numbers function around the original one
# and have it display the arguments it was called with
def new_add_numbers(num_1, num_2):
    display("--add_numbers was called with " + str(num_1) + " and " + str(num_2))
    return old_add_numbers(num_1, num_2)

# replace the original add_numbers function with the new wrapped one
add_numbers = new_add_numbers


# Now, we can go back to our code that used the original `add_numbers` function, but now it will get the wrapped version.

# In[28]:


my_money = 4
money_you_gave_me = 3

my_current_money = add_numbers(my_money, money_you_gave_me)


# In[29]:


display(my_current_money)


# If wrapping functions was a confusing process, don't worry. We are only using it in the "Track Tweepy Use" demo in this chapter, and won't be using it again.
