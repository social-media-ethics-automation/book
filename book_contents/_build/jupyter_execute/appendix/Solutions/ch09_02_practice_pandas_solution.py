#!/usr/bin/env python
# coding: utf-8

# # Pandas Intro

# ## User-Defined Functions VS Built-In Functions
# 
# In all programming and scripting language, a function is a block of code which can be used repetitively in a program.
# 
# #### Built-In Functions:
# 
# ```
# len()
# append()
# range()
# print()
# ```
# 
# 
# 
# 
# #### User-Defined Functions (UDFs):
# 
# A user-defined function is a function you create that can be used repetitively. In Python a function is defined using the 'def' keyword.
# 
# Creating a User-Defined Function:
# 
# ```
# def function_name(argument1, argument2):
#     STATEMENT
#     STATEMENT
#     STATEMENT
# ```
# 
# Using a Used-Defined Function that you previously made:
# 
# ```
# function_name(argument1, argument2)
# ```

# In[1]:


# Try out the following example:

import time

def counter():
    for i in range(10):
        print(i)
        time.sleep(1)


# In[2]:


# Using the previously made UDF. Try out the following example:

counter()


# ## Parameters

# #### A parameter is the variable listed inside the parentheses of the function definition.

# In[3]:


# You can also include parameters. Try out the following example:

def counter_advanced(x):            # includes parameter 'x'
    for i in range(x):
        print(i)
        time.sleep(1)


# In[4]:


# Calling the function & specifying a value in place of the paramter.
# Try out the following example:

counter_advanced(5)


# In[5]:


# Try out the following example:

def addition_machine(x, y):
    print(x + y)


# In[6]:


# Try calling the function:

addition_machine(52846, 300)


# #### 1. Create a function that does NOT include a parameter (the function name should be followed by an exmpty parenthesis).

# In[7]:


def example_function():
    x = 254
    y = 123
    print(254 % 123)


# #### 2. Call that funtion.

# In[8]:


example_function()


# #### 3. Create a function called `multiplier` that takes in two parameters and prints out the product of the two.

# In[9]:


def multiplier(x, y):
    print(x * y)


# #### 4. Call the `multiplier` function.

# In[10]:


multiplier(15,20)


# ## Pandas

# Pandas is an extremely useful library used for large data anlysis. Pandas makes it very easy to perform certain tasks quickly and easily.

# #### "pandas" is the name of the library. When we include "as pd", we're nicknaming the library in order to shorten the name when we reference it. This is standard practice in data science. 
# 
# #### Run the following code block to load in the pandas library: 

# In[11]:


import pandas as pd


# #### Load in data using function `read_csv`

# In[12]:


df = pd.read_csv('../INFO-198-content/faculty.csv')
df


# What is df? It's a pandas object called a DataFrame which stores a table of values, similar to aan Excel table.
# 
# Notice on the top row, it shows the name of the columns (Name and Salary) and on the left-most side, it shows an index for each row (0, 1, and 2).
# 
# DataFrames are powerful because they provide lots of ways to access and perform computations on your data without you having to write much code!

# ## Accessing a Column

# In[13]:


# Try running the following example:

df['name']


# #### 5. TRY IT YOURSELF: Access the 'salary' column.

# In[14]:


df['salary']


# ### Series
# A series is essentially one column of a DataFrame.The previous two code blocks are examples of Series.

# #### pandas isn't useful just because it not only lets you access this data conveniently, but also perform computations on them.
# 
# A Series object has many methods you can call on them to perform computation. Here is a list of some of the most useful ones:
# 
# ```
# mean: Calculates the average value of the Series
# min: Calculates the minimum value of the Series
# max: Calculates the maximum value of the Series
# count: Calculates the number values in the Series
# unique: Returns a new Series with all the unique values from the Series.
# And many more!
# ```

# In[15]:


# Try running the following example to compute the average Salary of the names:

average_salary = df['salary'].mean()
average_salary


# In[16]:


df2 = pd.read_csv('../INFO-198-content/emissions.csv')
df2


# #### One useful feature of pandas is it lets you combine values from different Series. For example, if we wanted to, we could add the values of the salary column and the bonus column.

# In[17]:


# Try out the following example:

df2['Emissions'] + df2['Population']


# This returns a new Series that represents the sum of those two columns. The first value in the Series is the sum of the first values in the two that were added, the second is the sum of the second two, etc. 
# 
# *Note: this does NOT change the dataframe.

# #### 6. TRY IT YOURSELF: In the cell below, find the maximum "emissions per capita" (emissions divided by population). Start by computing this value for each city and then find the maximum value of that Series (using one of the Series methods shown above). 
# 
# #### Save the result in a variable called `max_emissions`.
# 
# #### Hint: You can save a Series in a variable! It's just like any other Python value!

# In[18]:


max_emissions = df2['Emissions'] / df2['Population']
max_emissions = max_emissions.max()
max_emissions


# #### These computations also work if one of the values is a single value rather than a Series. For example, the following cell adds 10 to each of the populations.

# In[19]:


# Try out this example:

df2['Population'] + 10


# #### 7. TRY IT YOURSELF: Divide each emission by 3

# In[20]:


df2['Emissions'] / 3


# #### Another useful case for something like this is to compare the values of a column to a value. For example, the following cell computes which cities have an emissions value of 200 or more. Notice that the datatype of the output is boolean since the condition is checking whether or not each row in the column meets the condition or not.

# In[21]:


df2['Emissions'] >= 200


# #### 8. TRY IT YOURSELF: Check whether each population is less than or equal to 50000.

# In[22]:


df2['Population'] <= 50000


# ## Filtering Data

# #### You might have wondered why would it be useful to compare a Series to some random value? The power comes from using this bool Series to <b>filter</b> the DataFrame to the rows you want.
# 
# #### For example, what if I wanted to print the names of the cities that have an emissions of 200 or more? I can use this bool Series to filter which rows I want!

# In[23]:


# Here's what the syntax looks like to filter rows with 'Emissions' of 200 or greater.:

df3 = df2[df2['Emissions'] >= 200]
df3


# In[24]:


# Now let's return only the city names:

df3['City']


# #### We recommend splitting up the code into many variables. This makes the code more readable and often easieir to work with:

# In[25]:


# Here's the previous code blocks rewritten (the output should be the same):

emissions = df2['Emissions'] >= 200
df3 = df2[emissions]
cities = df3['City']
cities


# Notice how we can get this result without having to write any loops!

# #### 9. TRY IT YOURSELF: Return the Countries that have populations of less than or equal to 50000.

# In[26]:


populations = df2['Population'] <= 50000
df3 = df2[populations]
country = df3['Country']
country


# ## Filtering on Multiple Conditions

# #### Last week we went over 'or' and 'and' opperators. padas has a different syntax for these operators:
# 
# ```
# | = or
# & = and
# ```

# #### If you want to find all cities that have high emissions OR are in the US, you would write this:

# In[27]:


# Try out the following example:
df2[(df2['Emissions'] >= 200) | (df2['Country'] == 'U.S.A.')]


# ### What about cities that have high emissions AND are in the US?

# In[28]:


# Try out the following example:
df2[(df2['Emissions'] >= 200) & (df2['Country'] == 'U.S.A.')]


# In[29]:


# A much more readable version of the previous code:
emissions = df2['Emissions'] >= 200
country = df2['Country'] == 'U.S.A.'
high_usa = df2[emissions & country]
high_usa


# #### 10. TRY IT YOURSELF: write code to select all rows from the dataset that are in France OR have a population greater than 50000. 
# 
# #### Save the result in a variable called `pop_or_france`.

# In[30]:


populations = df2['Population'] <= 50000
country = df2['Country'] == 'France'
pop_or_france = df2[populations | country] 
pop_or_france


# #### 11. TRY IT YOURSELF: write code to select all rows from the dataset that are in France OR have a population greater than 50000. 
# 
# #### Save the result in a variable called `pop_and_france`.

# In[31]:


populations = df2['Population'] <= 50000
country = df2['Country'] == 'France'
pop_or_france = df2[populations & country] 
pop_or_france


# #### 12. Create a function called `max_machine` that takes in one parameter, the name of a column `col_name`, and prints the `max()` value from the column

# In[32]:


def max_machine(col_name):
    print(df2[col_name].max())


# #### 13. Call the `max_machine` function you just made with the parameter 'Population'

# In[33]:


max_machine('Population')


# #### 14. Create a function called `average_machine` that takes in two parameters: a dataframe, `df`, and a column, `col`. The function should print the average of the specified column of the specified dataframe.

# In[34]:


def average_machine(df, col):
    print(df[col].mean())


# #### 15. Call the `average_machine` function you just made with parameters, "df" and "'salary'".

# In[35]:


average_machine(df, 'salary')


# #### 16. Call the `average_machine` function you just made with parameters, "df2" and "'Emissions'".

# In[36]:


average_machine(df2, 'Emissions')


# #### CHALLENGE: Create a function called `emissions_per_capita` that PRINTS out the sentence "CITY has NUM emissions per capita." for each city in the dataframe.

# In[37]:


def emissions_per_capita():
    names = df2['City']
    epc = df2['Emissions'] / df2['Population']
    for i in range(len(names)):
        print(str(names[i]) + " has " + str(epc[i]) + " emissions per capita.")
        
emissions_per_capita()


# In[ ]:




