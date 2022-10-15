#!/usr/bin/env python
# coding: utf-8

# # Practice: Conditionals and String Manipulation

# ## While Loops

# Just like the For loop, the while loop performs repetitions, each iteration executes the body only if the condition is True, otherwise the loop ends.
# 
# The structure of the loop looks like this:
# 
# ```
# while CONDITION:
#     STATEMENT
#     STATEMENT
#     STATEMENT
# ```

# In[1]:


# Try out this example:

x = 5
while x > 0:
    print(x)
    x = x - 1


# 1. Create a 30 second coutdown using a while loop, the ``sleep()`` function, and the ``print()`` function.

# In[ ]:





# ## IF ELSE Statements

# Conditional statements let you execute code based on some condition.
# 
# A conditional block is an `if` block, optionally followed by any number of `elif` blocks ("elif" is short for "else if", optionally followed by at most one `else` block. The conditional block will only ever let one condition run.

# In[2]:


# try out the following example:

if 5 < 7:
    print('Yes!')
else:
    print('No!')


# In[3]:


# try out the following example:

x = 15
if x < 11:
    print('A')
elif x >= 13:
    print('B')
elif x >= 25:
    print('Never')
else:
    print('C')


# 2. Refer to the example. Let's say x was changed to 30. What would the output be?
# 
# *Do Not Code. Please answer this question as a markdown block. Modify the code above to check your answer afterwords.

# 

# 3. What value would the `x` variable have to be in order to get the output 'C'?
# 
# *Again, Do Not Code. Please answer this question as a markdown block Modify the code above to check your answer afterwords.

# 

# ## Expressions

# You guys already have a lot of experience working with expressions. Let's review.
# 
# 
# Here are the operations defined for `int` types and `float` types:
# 
# *  <b>Addition: </b> `a + b`
# *  <b>Subtraction: </b> `a - b`
# *  <b>Multiplication: </b> `a * b`
# *  <b>Division: </b> `a / b` (e.g., 7 / 3 == 2.333333333)
# *  <b>Integer division: </b> `a // b` (e.g., 7 // 3 == 2)
# *  <b>Mod: </b> `a % b` (i.e., remainder from integer division as in 7 % 3 == 1)
# *  <b>Exponentiation: </b> `a ** b`  (i.e., raise to a power a^b)
# 
# 

# In[4]:


# you can also nest expressions, try out the following example:
a = 3
print(a - (2 * a) + (a ** (1 + 2)))


# 4. What would be the output? (Try to figure it out by hand, then check it with code)
# 
# ```
# x = 7
# y = 2
# print(x / y)
# ```

# In[ ]:





# 5. What would be the output? (Try to figure it out by hand, then check it with code)
# 
# ```
# x = 7
# y = 2
# print(x // y)
# ```

# In[ ]:





# 6. What would be the ouput? (Try to figure it out by hand, then check it with code)
# 
# ```
# x = 10
# y = 50
# if x ** 2 > 100 and y < 100:
#     print(x, y)
#     
# ```

# In[ ]:





# 7. Create a list called `random_numbers`. Choose five random numbers at random in your head to put in the list.

# In[ ]:





# 8. Create a loop that goes through the `random_numbers` list. Within the loop, include an if else statement checking:
# 
#     * If the number is even, print "A" (hint: even numbers have a remainder of 0)
#     * Else if the number is divisible by 3, print "B"
#     * Else print "C"

# In[ ]:





# ## Variables + Loops

# We often use variables to keep track of information within loops. A common combination of utilizing variables within loops is for counting purposes. 

# In[5]:


# check out the following example:

x = 5

# before the loop
print(x)

for i in range(5):
    x += 1               # same as x = x + 1

# after the loop    
print(x)


# In[6]:


# check out the following example:

# initializing counter variable
s_count = 0

state = 'Mississippi'

# loop
for i in range(len(state)):
    if state[i] == 's':
        s_count += 1

        
print(s_count)


# In[7]:


# check out the following example:

week_temp = ['45 °F', '43 °F', '45 °F', '45 °F', '49 °F', '45 °F', '46 °F']

temp45_count = 0

for temp in week_temp:
    if temp == '45 °F':
        temp45_count += 1

print(temp45_count)


# 9. Using your previously made `random_numbers` variable, loop through the the list and check how many numbers are greater than ten. At the end, print that count.

# In[ ]:





# ## Nested Loops

# Lets say we have a list of sentences and we are searching for a specific word. We must use nested loops. Check out the example bellow:

# In[8]:


lyrics = ['You used to call me on my cell phone',
         'Late night when you need my love',
         'Call me on my cell phone',
         'Late night when you need my love',
         'And I know when that hotline bling',
         'That can only mean one thing',
         'I know when that hotline bling',
         'That can only mean one thing']

phone_count = 0

for line in lyrics:
    split_line = line.split() # splitting up sentence into list of words
    for word in split_line:
        if word == 'phone':
            phone_count += 1
            print(line)
            print(phone_count)
            


# 10. Recreate the previous example with your favorite song.

# In[ ]:





# ## Twitter Practice

# ### Install and import the "tweepy" library of code that gives us twitter functions

# In[9]:


import tweepy


# ### Login

# In[10]:


# copy in the code from test_twitter_bot_keys.ipynb


# 11. Search for recent tweets that include the word 'Weather'. Assign this list to a variable called `weather`.

# In[ ]:





# 12. Loop through the `weather` list and count how many times you come across the words "cold", "freezing", or "chilly"

# In[ ]:





# 13. Create a variable called `long_words` and assign an emepty list to it --> []. 
# 

# In[ ]:





# 14. Loop through the `weather` list. If a word has a length of 5 OR GREATER, add it to the `long_words` list. Make sure to return the `long_words` list at the end of your code block.
# 
# *Hint: you can add to a list using the `append()` function
# 
# ```
# append() example:
# 
# list = [1, 2, 3]
# list.append(4)
# 
# list  -->  [1, 2, 3, 4]
# ```

# In[ ]:





# 15. Get the length of your `long_words` list and store it in a variable called `long_words_length`.

# In[ ]:





# 16. Create a while loop, printing out the sentence: <b>"The word, WORD, is extremely long."</b> for each word in the `long_words` list.
# 
# *Hint: use the `long_words_length` variable to check if you've gone through the entire list. With each iteration, subtract 1 from the variable.

# In[ ]:





# CHALLENGE: Copy and paste the code from the previous question. Alter the code to create the sentence: 
# 
# <b>"The word, WORD, is LENGTH letters long."</b>

# In[ ]:




