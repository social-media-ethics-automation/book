#!/usr/bin/env python
# coding: utf-8

# # Demo: Python Basic Data Types
# Let's now look specifically at how Python stores and lets you work with basic data types:
# * Booleans (True / False)
# * Numbers
# * Strings (Text)
# 
# But first we need to look a little more about how to use functions, since we'll be using them with the data types.

# ## Calling Functions
# A function is a named section of pre-written code, which we can "call," making that section of code run.
# 
# We have already been calling two different functions in particular: `display` and `create_tweet`:
# - `display("Ethics might be relevant!")`
# - `client.create_tweet(text="This is the tweet text")`
# 
# The structure of a standard function call has the following pieces:
# `function_name(input_parameters)`
# 
# So we first write the name of the function (e.g., `display` or `client.create_tweet`), then we put matching parentheses after that, and inside the parentheses we put the input arguments, which are data or options for how the function should run.
# 
# ### input arguments
# - These inputs are called "parameters" or "arguments"
# - Inputs go in parentheses after the function name
# - If there are multiple inputs, they are separated by commas
# - You can also specify which input you are giving within the parenthesis by putting parameter_name=value
# 
# 
# Additionally, some functions produce a result, which can be saved in a variable, or used in a calculation or some other fashion. When we save the result of running a function into a variable, it looks like this:
# 
# `save_result_var = function_name(input_parameters)`
# 
# ### function results
# * Functions can have outputs that are called "returns" or "results"
# * When the code intepreter sees the function call, it runs the code in the function with the inputs, and then puts the output in the place where that function call was
# * The results of the function can be stored in a variable, used in a formula, or used as an argument for another function
# 
# That was all a bit theoretical, so set's look at some data types now, and some specific functions that we can use with them.

# ## Boolean (True / False)
# 
# In Python there are two options for boolean: `True` and `False`
# 
# Note that the first letter is capitalized and the rest is lower case. Python only lets you write these True and False values in that way.
# 
# Let's save a boolean value in a variable, and then display it:

# In[1]:


does_user_have_blue_checkmark = True

display(does_user_have_blue_checkmark)


# Display lets us see what was in the variable, but we can also use a new function `type` to see what type of value is in the variable (it should be 'bool' which is short for boolean):

# In[2]:


type(does_user_have_blue_checkmark)


# ## Numbers

# ### integers and floats
# Python allows you to use two main types of numbers:
# - Integers (whole numbers), called "int"
# - A "floating point" number with a decimal point, called a "float"

# In[3]:


type(5)


# In[4]:


type(5.5)


# We can now do normal math operations on the numbers, like addition `+`, subtraction `-`, multiplication `*`, and division `/`.
# 
# 
# Even though there are two types of numbers, most of the time they work together pretty seemlessly, switching to whichever type makes the most sense. For example, let's look at what happens when we add and int and a float:

# In[5]:


example_num = 5 + 5.5


# In[6]:


display(example_num)


# In[7]:


type(example_num)


# ### functions for numbers
# Python provides functions that we can use with numbers, like:
# - find the maximum number in a set of numbers with `max()`
# - find the minimum number in a set of numbers with `min()`
# - round a floating point number into an integer with `round()`
#     
# Each of these functions produces a result at the end, which we can save into a variable

# In[8]:


# Demo of using the max() function
my_score = 74
your_score = 92
someone_elses_score = 83

highest_score = max(my_score, your_score, someone_elses_score)

display(highest_score)


# In[9]:


# Demo of using the min() function
bread_1_price = 2.30
bread_2_price = 2.15
bread_3_price = 1.79

cheapest_bread_price = min(bread_1_price, bread_2_price, bread_3_price)

display(cheapest_bread_price)


# In[10]:


# Demo using the round function
float_number = 14.6224

rounded_number = round(float_number)

display(rounded_number)


# ### number comparisons
# Python also lets us [compare numbers in various ways](https://www.w3schools.com/python/gloss_python_comparison_operators.asp), producing a boolean True or False value depending on if the comparison was true or false.
# 
# For example, we can see if one number is bigger than another by using the greater than comparison: `>`

# In[11]:


money_in_wallet = 10
cost_of_item = 7

has_enough_money = money_in_wallet > cost_of_item

display(has_enough_money)


# We can check if two numbers are equal by using two equals signs: `==`
# 
# Note: this is an unfortunately confusing system that [most programming languages are now stuck with](https://www.quora.com/Why-do-most-programming-languages-have-the-equal-sign-as-an-assignment-operator-This-option-seems-to-be-nonintuitive-Isn%E2%80%99t-it-better-to-use-the-equal-sign-in-conditional-statements) since it became the standard: 
# - One equals sign (`=`) means save the value into a variable
# - Two equals signs (`==`) mean check if two numbers are the same

# In[12]:


my_follower_count = 23
your_follower_count = 23

same_number_of_followers = my_follower_count == your_follower_count

display(same_number_of_followers)


# ## Strings (text)
# In order to make a string (piece of text) in Python, you can write your text with either double quotes `"` or single quotes `'` at the beggining and end.

# In[13]:


tweet_text_1 = "what nice weather today"
display(tweet_text_1)


# In[14]:


tweet_text_2 = 'what horrible weather today'
display(tweet_text_2)


# Note: If you are copying from a word processor like word, you might get angled quotes like `’` or `”`, which Python doesn't like. So, if you try to run code like this:
# - `tweet_text_3 = “What normal weather today”`
# 
# you will get an error message like this:
# - ![Red error message box. The top says: "Input in [14] tweet_text_3 = “What normal weather today”". The bottom says: "SyntaxError: invalid character '“' (U+201C)](bad_quote_error.png)

# ### adding strings together
# If we want to add strings together to make a larger string, we can do that with the `+` operation.

# In[15]:


first_name = "Kyle"
last_name = "Thayer"

full_name = first_name + " " + last_name 
# Note: I had to add a space between the first and last name, or it would come out as KyleThayer

display(full_name)


# If we want to add something like a number, like my age, into the string though, it won't let us do it directly.
# 
# If we try running:
# - `example_text = "how old are you? I am " + 3`
# 
# Then we will get an error that 3 was an int and not a string, so it can't be added:
# - ![Error message: Says it is a type error and points to the line: 'example_text = "how old are you? I am " + 3'. At the bottom it says: "TypeError: can only concatenate str (not "int") to str"](add_int_to_str_error.png)
# 
# To fix this, we have to turn the number into a string before we add it. We do this by using the `str()` function:

# In[16]:


example_text = "how old are you? I am " + str(3)
display(example_text)


# Adding strings and numbers together is particularly useful for displaying information in a more readable fashion:

# In[17]:


num_likes = 78
num_retweets = 32
num_quote_tweets = 17

display("The number of likes was: " + str(num_likes))
display("The number of retweets was: " + str(num_retweets))
display("The number of quote tweets was: " + str(num_quote_tweets))


# ### actions with strings
# There are various actions Python let's us do with strings. For example, let's look for a smaller string ("cat") and see if it is in the bigger one (producing a True or False boolean value) using `in`

# In[18]:


animal_tweet_1 = "I like cats!"

tweet_1_has_cat = "cat" in animal_tweet_1

display(tweet_1_has_cat)


# In[19]:


animal_tweet_2 = "I like dogs!"

tweet_2_has_cat = "cat" in animal_tweet_2

display(tweet_2_has_cat)


# In[20]:


animal_tweet_3 = "I like caterpillars!"

tweet_3_has_cat = "cat" in animal_tweet_3

display(tweet_3_has_cat)


# We can also do actions like make a string all uppercase or all lowercase using the `upper()` and `lower()` functions.
# 
# Unlike previous uses of functions, for these we write the name of the variable we are using, then a `.` and then name of the function.

# In[21]:


normal_message = "I hope you are doing OK"


# In[22]:


loud_message = normal_message.upper()
display(loud_message)


# In[23]:


quiet_message = normal_message.lower()
display(quiet_message)


# _You can read more about Python data types at [w3schools explanation of Python data types](https://www.w3schools.com/python/python_datatypes.asp)_
