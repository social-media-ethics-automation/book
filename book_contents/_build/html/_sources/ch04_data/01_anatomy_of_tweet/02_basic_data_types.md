# Basic Data Types

First we'll look at a few basic data storage types.

## Booleans (True / False)
Binary consisting of 0s and 1s make it easy to represent true and false values, where 1 often represents true and 0 represents false. Most programming languages have built in ways of representing True and False values.

```{figure} dog_tweet_binary.png
---
name: tweet_binary_fig
alt: Screenshot of the tweet from before, but with the blue checkmark highlighted
---
```


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


## Strings (Text)
Text is generally stored as a list of characters (like the example before of e, t, h, i, c, s). These lists of characters are called "strings" (that is a bunch of characters strung together).

Computers can store "characters" can be letters, numerals, or other symbols (like math symbols, spaces, and "[newlines](https://en.wikipedia.org/wiki/Newline)" which go to the next line when you press "Enter"). Some ways of storing characters, like [unicode](https://en.wikipedia.org/wiki/Unicode), support storing symbols and letters from many languages, and also [emojis](https://unicode.org/emoji/charts/full-emoji-list.html).

[![A photo of a string banner with shiny individual letters hanging on it spelling "HAPPY BIRTHDAY"](happy_birthday_banner.jpg)](https://www.pexels.com/photo/a-rocking-horse-and-birthday-decorations-7600328/)

A list of characters then can represent words, sentences, books, etc.

````{admonition} Click to see example Python code
:class: dropdown
```python
# Save a string with the word ethics in a variable called key_word
key_word = "ethics"

# Get the first letter ("e"), and save it in variable first_letter
first_letter = key_word[0]

Get the second letter ("t"), and save it in variable second_letter
second_letter = key_word[1]
```
````

Additionally, text can be stored with extra formatting information (like fonts, colors, in a [Document File Format](https://en.wikipedia.org/wiki/Document_file_format) like with Word Documents, PDF files, [html website files](https://www.w3schools.com/html/html_intro.asp), etc.).

````{admonition} Click to see example HTML code
:class: dropdown
```html
<article>
  <h1> This is the title of the article! </h1>
  <section>
    <p> This is the first paragraph in the first section of the article. </p>
    <p> This is the second paragraph in the first section of the article. </p>
  </section>
  <section>
    <p> This is the first paragraph in the second section of the article. </p>
    <p> This is the second paragraph in the second section of the article. </p>
  </section>
</article>
```
````

Note: We'll demonstrate strings later in this chapter, and in more detail in Chapter 7: Trolling
