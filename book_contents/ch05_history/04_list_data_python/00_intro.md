# Lists in Python


```{tableofcontents}
```


TODO: Add these to the demos:
## for loops
For loops allow you to repeat an action multiple times.

```
for loop_value in thing_to_loop_over:
    # Put actions to repeat here
```

For loops have to have something to loop over, which goes after "in".
* You can use it with the function range to repeat an action a given number of times.
* You can use it on a list, though we'll cover that more later.

As the loop goes, it saves the current thing it is looking at in the temporary variable you list before the in.

The commands you want to repeat need to be tabbed in one more level than the for statement to indicate they go inside the for loop.


# TODO: Demo some for loops, including the one below

for x in range(10):
    print("<<<<< " + str(x*4 + 1) + "/40")
    print("^^^^^ " + str(x*4 + 2) + "/40")
    print(">>>>> " + str(x*4 + 3) + "/40")
    print("vvvvv " + str(x*4 + 4) + "/40")

for loop: are we there yet


Indexing
When we think of strings, we commonly think of them as a sequence of characters, where each character has an index in the string. Each character has its own spot in the sequence, and the spots are ordered starting at index 0 going up to the end of the string.
​
Python lets you access a character at a specific index using the [] notation
​
Note: You can use either "double quotes" or 'single quotes' to indicate a string

# try running the following examples:

wa = 'Washington'
wa[0]
wa[1]
wa[5:]
wa[:5]
wa[2:4]

Return the first letter of your name

Return all the letters of your name EXCEPT for the first.


Loops
For loops let you iterate over a sequence of values.
# try out this example:

for num in range(10):
    print(num)

Create a loop of range 5, mutiplying each number by 2

Create a loop of range 5, squaring each number


Lists
Variables can also store different data structures such as lists. Create a list of at least 3 food items and assign it to a variable called favorite_foods.

Remember, lists have this structure:

[item1, item2, item3]

Lists
Variables can also store different data structures such as lists. Create a list of at least 3 food items and assign it to a variable called favorite_foods.

Remember, lists have this structure:

[item1, item2, item3]

# try out this example:

states = ['California', 'Washington', 'New York']
states[0]

Return the second index in your list.

Use the len() function to return the length of your list

Loop through the list. For each iteration, print out the sentence: "NAME's favorite food is FOOD", replacing NAME with your name variable and food with each food in your favorite_foods list.

Hint: You should print out the same number of lines as your answer for the previous question.


Tweepy Review (refer to lab 1.5, but do NOT use the same answers)

Search for a tweet that includes the phrase "happy wednesday"

Create a variable called username and assign it to a username of an account of your choice.

Get the user ID of the same account as above using the username variable. Store the user ID in the variable user_id. Show the output of the variable using the display() function.

Get the user mentions using the user_id variable.

Get who the user follow using the user_id variable.
