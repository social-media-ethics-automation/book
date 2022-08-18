# Basic Data Types

First we'll look at a few basic data storage types.

TODO: Make this centered around tweet example

Note: We'll demonstrate these later in this chapter.

## Booleans (True / False)
Binary consisting of 0s and 1s make it easy to represent true and false values, where 1 often represents true and 0 represents false. Most programming languages have built in ways of representing True and False values.

Booleans are often created when doing sort of comparison or test, like:
- Is this piece of text less than or equal to 280 characters long?
- Does this piece of text end in a question mark?

````{admonition} Click to see example Python code
:class: dropdown
```python
# Save a boolean value in a variable called is_tweet_long
is_tweet_long = True

# Save a boolean value in a variable based on a comparison.
# The code checks if a wallet has more in it than the cost of the item
#   which will be True or False, and be saved in has_enough_money
has_enough_money = money_in_wallet > cost_of_item

# Save a boolean value in a variable based on a function call.
# The code checks if the text of a tweet (stored in tweet_text) starts
#   with "Hello", which will be True or False, and be saved in is_greeting
is_greeting = tweet_text.starts_with("Hello")
```
````

## Numbers
Numbers are normally stored in two different ways:
- Integer: whole numbers like 5, 37, -10, and 0
- Floating point numbers: these can represent decimals like: 0.75, -1.333, and 3 x 10 ^ 8

In both of those storage methods, there are limits to how much space is used to save each number, limiting how big (or small) the numbers can be, and causing rounding with floating point numbers.

Additionally programming languages might include ways of representing fractions, or [complex numbers](https://en.wikipedia.org/wiki/Complex_number).

````{admonition} Click to see example Python code
:class: dropdown
```python
# Save an integer value in a variable called max_tweet_length
max_tweet_length = 280

# Save a floating point number in a variable called average_tweet_length
average_tweet_length = 133.5
```
````

## Characters (Letters and other symbols)
Computers can store "characters" can be letters, numerals, or other symbols (like math symbols, spaces, and "[newlines](https://en.wikipedia.org/wiki/Newline)" which go to the next line when you press "Enter"). Some ways of storing characters, like [unicode](https://en.wikipedia.org/wiki/Unicode), support storing symbols and letters from many languages, and also [emojis](https://unicode.org/emoji/charts/full-emoji-list.html).

````{admonition} Click to see note about Python
:class: dropdown
Python does not directly let you save characters. Instead characters are always stored in "strings,"" which we will cover shortly.
````
