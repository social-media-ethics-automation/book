# Grouping data

Once we have some types of data representation on a computer, we can create different groupings of data to represent more types of data. We'll look at two types of groupings here, then look at what we can do with those groupings.

## Lists (Arrays)
The first way of combining data is by making a list with data.

So we can make a list of the numbers from 1 to 10:
 - 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

 ````{admonition} Click to see example Python code
 :class: dropdown
 ```python
 # Save a list of the numbers from 1 to 10 in a variable called one_to_ten
 one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 ```
 ````

Or we can make a list of letters [which happen to form a word] like this:
 - e, t, h, i, c, s

 ````{admonition} Click to see example Python code
 :class: dropdown
 ```python
 # Save a list of letters in a variable called key_word
key_word = ["e", "t", "h", "i", "c", "s"]
 ```
 ````

 The items in these lists are normally numbered with an "index", so you can ask for the 1st item, or 2nd item, or any other.

Note: Largely due to [historical peculiarities in the development of programming languages](https://en.wikipedia.org/wiki/Zero-based_numbering#Origin), most programming languages (including Python) number the 1st item in a list as item `0`. So:
- 1st item has index 0
- 2nd item has index 1
- 3rd item has index 2
- etc.

````{admonition} Click to see example Python code
:class: dropdown
```python
# Save a list of letters in a variable called key_word
key_word = ["e", "t", "h", "i", "c", "s"]

# Get the first letter ("e"), and save it in variable first_letter
first_letter = key_word[0]

Get the second letter ("t"), and save it in variable second_letter
second_letter = key_word[1]
```
````



Note: We'll demonstrate lists later in Chapter 5: History of Social Media.

## Dictionaries
The other method of grouping data that we will discuss here is called a "dictionary" (sometimes also called a "maps").

You can think of this as like a language dictionary where there is a word and a definition for each word. Then you can look up any name or word and find the value or definition.

Example: English Language Dictionary:
- Social Media: [TODO: define]
- Ethics: Thinking systematically about what makes something morally right or wrong, or using ethical systems to analyze moral concerns in different situations: [example definition]
- Automation: [TODO: define]

Dictionaries allow programmers to combine several pieces of data, naming each piece. When we do this, the dictionary will have a number of names, and for each of those names a piece of information (called a "value" in this context).

Dictionary:
- Name 1: Value 1
- Name 2: Value 2
- Name 3: Value 3

So as an example of using a dictionary, if you want to combine some pieces of information, like defining a color by [specifying the amount of red, green, and blue](https://www.w3schools.com/cssref/css_colors.asp), it might look like these:

[Purple](https://www.w3schools.com/colors/color_tryit.asp?color=Purple) <span style="background-color:rgb(128,0,128)"> &nbsp; </span>:
- Red: 128
- Green: 0
- Blue: 128

[Medium Aqua Marine](https://www.w3schools.com/colors/color_tryit.asp?color=MediumAquaMarine) <span style="background-color:rgb(102,205,170)"> &nbsp; </span>:
- Red: 102
- Green: 205
- Blue: 170

````{admonition} Click to see example Python code
:class: dropdown
```python
# Save dictionaries for RGB values for two colors in separate variables

purple = {
  "Red": 128,
  "Green": 0,
  "Blue": 128
}

medium_aqua_marine = {
  "Red": 102,
  "Green": 205,
  "Blue": 170
}
```
````

We can also use any piece of information we want for the "name" in a dictionary. So if we wanted, we could make a color the "name" in a dictionary. For example, in this one, names are colors (in terms of red, green, and blue), and the values are the [most common names of that color in different languages]{https://uwdata.github.io/color-naming-in-different-languages/vis/full_color_maps.html}:

Most common name for a given color in English:
- <span style="background-color:rgb(231,37,37)"> &nbsp; </span>{Red: 231, Green, 37, Blue: 37}: Red
- <span style="background-color:rgb(167,37,128)"> &nbsp; </span>{Red: 168, Green, 37, Blue: 128}: Magenta

Most common name for a given color in Korean:
- <span style="background-color:rgb(231,37,37)"> &nbsp; </span>{Red: 231, Green, 37, Blue: 37}: 빨강
- <span style="background-color:rgb(167,37,128)"> &nbsp; </span>{Red: 168, Green, 37, Blue: 128}: 자주

````{admonition} Click to see example Python code
:class: dropdown
```python

# Save dictionaries for RGB values for two colors in separate variables

color_1 = {
  "Red": 231,
  "Green": 37,
  "Blue": 37
}

color_2 = {
  "Red": 168,
  "Green": 37,
  "Blue": 128
}


# Save dictionaries that given a color will give you the most
# common name for that color (one dictionary for English, one for Korean)
most_common_english_name{
  color_1: "Red",
  color_2: "Magenta"
}

most_common_korean_name{
  color_1: "빨강",
  color_2: "자주"
}
```
````


Note: We'll demonstrate dictionaries later in Chapter 5: History of Social Media, and Chapter 8: Data Mining.
