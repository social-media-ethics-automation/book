#!/usr/bin/env python
# coding: utf-8

# # Practice: Functions (WHERE DOES THIS GO?)

# ### PRINT vs RETURN

# #### `print` shows a string representing what is going on inside the computer. The computer cannot make use of that printing. `return` is how a function gives back a value. This value is often unseen by the human user, but it can be used by the computer in further functions.

# ### Let's first go over print

# In[1]:


# example of print:

# defining the function
def hello_world1():
    print('hello world')
    
# calling a function
hello_world1()


# In[2]:


# another example of print:

# defining the function
def function_example2(a,b):
    print(15 ** a)
    print()
    if b % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
        
# calling a function        
function_example2(4,15)


# In[3]:


# another example of print (using default arguments):

# defining the function
def function_example3(a=5,b=3):
    print(a * b)


# In[4]:


# calling the function, specifying the parameters

function_example3(15, 70)


# In[5]:


# calling the function, NOT specifying the parameters

function_example3()


# #### Printing can be super useful visually, but functions are most often used to get values and use them with other code which you can't do wth printing

# In[6]:


# try out the following example where we try adding 30 to the output of the function
# ... you should get an error!

#defining the function
def function_example4(a,b):
    print(a + b)
    
    
# calling the function & trying to add 30 to the output
function_example4(5,10) + 30   


# ##### ^Notice how the output still gets printed, but the error occurs when we try to add 30.

# ### Before we move on, let's do some function practice.

# #### 1. Create a function of your choice without a parameter.

# In[ ]:





# #### 2. Call that function.

# In[ ]:





# #### 3. Create a function of your choice WITH a parameter.

# In[ ]:





# #### 4. Call that function

# In[ ]:





# #### 5. Create a function with 3 parameters AND specifying default values for each one.

# In[ ]:





# #### 6. Call that function, specifying all 3 parameters.

# In[ ]:





# #### 7. Call that function again. This time, leave the parenthesis empty.

# In[ ]:





# ### Now let's go over Returns

# A return statement is used to end the execution of the function call and “returns” the result to the caller. The statements after the return are NOT executed.
# 
# Example:
# 
# ```
# def fun():
#     STATEMENT
#     STATEMENT
#     STATEMENT
#     return [expression]
# ```

# #### The following example is based on the previous hello_world example. Instead of printing hello world, we RETURN it.

# In[ ]:


# Try out this example:

def hello_world2():
    return 'Hello World'


# In[ ]:


# Try calling the function and see what happens.
hello_world2()


# In[ ]:


# Try running this code block and see what happens.
print(hello_world2())


# #### 8. Describe the difference between the previous two code blocks in the markdown block below.

# 

# #### We can store function calls in variables

# In[ ]:


# try out this example

# storing hello_world2() in a variable, and printing that variable
hello_variable = hello_world2()
print(hello_variable)

print()

# adding onto the "hello_variable" variable & printing it out
hello_variable = hello_variable + "! It's a beautiful day."
print(hello_variable)


# #### The following code block demonstrates the same example, except with the original print function

# In[ ]:


# try out this example using PRINT

def hello_world1():
    print('hello world')

# storing hello_world1() in a variable, and printing that variable
hello_variable = hello_world1()
print(hello_variable)


# ##### ^Note how the `hello_world1()` runs and prints "hello world", but it doesn't get saved into the `hello_variable`. Therefore, when we try to print out the variable, we get "None".

# In[ ]:


# try out this example:

def divide_func(a, b):
    return a / b

# ----------------------------------

var_a = 35
var_b = 7
divided = divide_func(var_a, var_b)
divided


# In[ ]:


# Try out this example:

def add_func(a, b):
    return a + b


def sub_func(a, b):
    return a - b

# ----------------------------------

var_a = 50
var_b = 20
output = add_func(var_a, var_b)
print(output)

var_c = 100
updated_output = sub_func(output, var_c)
print(updated_output)


# #### 9. Create a function that takes in a list of integers and returns the sum of all the numbers.
# 
# #### *Hints: use a variable to keep track of the "sum", loop through the list to access each number.

# In[ ]:





# #### 10. Call the function and assign it to the variable `summed`. Print out the variable.

# In[ ]:





# #### 11. Add 55 to the `summed` variable and reassign it back to the same variable. Print out the variable.

# In[ ]:





# ## Refactoring

# Refactoring is the technique of changing an application so that it behaves the same way on the outside (output), but INTERNALLY (code) has improved. We often do this by creating functions to avoid repetitive actions, improve efficiency in our code, and prevent human error.

# #### Check out the example below where the program prints out an image of a pattern

# In[ ]:


# run this code block


# stars
for i in range(0,5):
    for j in range(0, i+1):
        print("* ",end="")
    print("\r")

# squiggles
for i in range(0,10):
    for j in range(0, 5):
        print("|*~ ",end="")
    print("\r")

# diamonds
for i in range(0,8):
    for j in range(0, i+1):
        print("<> ",end="")
    print("\r")    

# stars
for i in range(0,5):
    for j in range(0, i+1):
        print("* ",end="")
    print("\r")
    
# diamonds
for i in range(0,8):
    for j in range(0, i+1):
        print("<> ",end="")
    print("\r")

# line division
for i in range(2):
    for j in range(25):
        print("-",end="")
    print("\r")
    for k in range(12):
        print("|X",end="")
    print("|")
    for l in range(25):
        print("-",end="")
    print("\r")
    
# stars    
for i in range(0,5):
    for j in range(0, i+1):
        print("* ",end="")
    print("\r")
    
# diamonds
for i in range(0,8):
    for j in range(0, i+1):
        print("<> ",end="")
    print("\r")

# squiggles
for i in range(0,10):
    for j in range(0, 5):
        print("|*~ ",end="")
    print("\r")
    
# stars    
for i in range(0,5):
    for j in range(0, i+1):
        print("* ",end="")
    print("\r")


# #### 12. Look over the code and the output. Explain some repetitive patterns you notice.

# In[ ]:





# #### Check out the code block below, where we refactor the previous code.

# In[ ]:


# refactored version:

# run this code block

def squiggles():
    for i in range(0,10):
        for j in range(0, 5):
            print("|*~ ",end="")
        print("\r")

def stars():
    for i in range(0,5):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")

def line_division():
    for i in range(2):
        for j in range(25):
            print("-",end="")
        print("\r")
        for k in range(12):
            print("|X",end="")
        print("|")
        for l in range(25):
            print("-",end="")
        print("\r")
    
def diamonds():
    for i in range(0,8):
        for j in range(0, i+1):
            print("<> ",end="")
        print("\r")
        
def pattern():
    stars()
    squiggles()
    diamonds()
    stars()
    diamonds()
    line_division()
    stars()
    diamonds()
    squiggles()
    
    
pattern()    # the output should look exactle the same


# ##### ^ Notice how the output is exactly the same as above. 
# 
# ##### We simplified the code: Instead of writing out the same code and printing out repetitive patterns, we put the code that repeats in <b>functions</b> and just called those functions whenever we wanted to print the same pattern.

# ### 13. YOU TRY: Create your own image using various keyboard symbols. Make sure to include at least three functions for the different parts of your image and include one main function, putting everything together (4 functions in total).

# In[ ]:





# ## Refactoring & Returns

# Sometimes there is a line of code or a set of lines of code whose purpose is to produce a specific result. You can take those lines of code and make them a new function that returns that specific result. For example, look at the function below:

# In[ ]:


# try running this code:

def create_welcome_message(first_name, last_name, class_name):
    # combine first and last names into the full name
    full_name = first_name + " " + last_name
    
    # make a welcom message with the full name and class name
    message = "Hi " + full_name + ", welcome to " + class_name + "!"
    return message
    
print(create_welcome_message("Kyle", "Thayer", "Info 198"))


# ##### In that function, the line `full_name = first_name + " " + last_name` is a line that produces a specific result, which makes it a candidate to refactor into its own function (placed earlier in the code block, so it is defined when the create_welcome_message function tries to use it).

# In[ ]:


# try running this code:

def get_full_name(first_name, last_name):
    # combine first and last names into the full name
    full_name = first_name + " " + last_name
    return full_name

def create_welcome_message(first_name, last_name, class_name):
    full_name = get_full_name(first_name, last_name)
    
    # make a welcom message with the full name and class name
    message = "Hi " + full_name + ", welcome to " + class_name + "!"
    return message
    
print(create_welcome_message("Kyle", "Thayer", "Info 198"))


# ##### ^The code does the same thing, but we now have a reusable function called `get_full_name()`

# #### Another example of a function that could be refactored using returns:

# In[ ]:


# try running this code:

def make_first_letters_uppercase(text):
    # use spaces to separate text into a list of words
    words = text.split(" ")
    
    #start a new list of what will be the capitalized words
    capitalized_words = [] 
    
    for word in words:
        # Separate the first letter and rest of word
        # then recombine them with the first letter capitalized
        first_letter = word[0]
        rest_of_word = word[1:]
        capitalized_word = first_letter.upper() + rest_of_word
        
        # take our newly capitalized word, and add it to the list of all the capitalized words
        capitalized_words.append(capitalized_word)
    
    # now that all words are capitalized, recombine the list 
    # of words with a space between each one
    new_sentence = " ".join(capitalized_words)
    
    #return our newly capitalized word
    return new_sentence
    
make_first_letters_uppercase("Let's see what happens to this example sentence.")


# #### 14. YOU TRY: Take the first set of lines of code in the for loop and make a new function at the top of the code block called `capitalize_word()` which takes in a word as an argument, and returns a capitalized version of that word. 
# 
# #### THEN have the `make_first_letters_uppercase()` function call your new capitalize_word function, passing it the argument word and saving the result in the `capitalized_word()` variable.

# In[ ]:





# #### 15. Finally, think back to your previous ps2 homework assignment. How might refactoring have saved you time and space in your JupyterNotebook for the code section? 
# 
# #### Please answer your question in the markdown block below.

# In[ ]:




