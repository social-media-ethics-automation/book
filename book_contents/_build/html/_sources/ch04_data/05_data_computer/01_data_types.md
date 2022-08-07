# Data Types

We previously covered in chapter 2 how [computers speak binary](../../ch02_definitions/03_automation/03_binary.html), and all data and instructions are turned into binary, and gave examples of how images or text can be represented with binary. There are many ways of representing data on a computer, so we'll look at a few types of them here:

## Some Simple Data Types

First we'll look at a few simple data storage types, called [primitive data types](https://en.wikipedia.org/wiki/Primitive_data_type).

### Booleans (True / False)
Binary consisting of 0s and 1s make it easy to represent true and false values, where 1 often represents true and 0 represents false. Most programming languages have built in ways of representing True and False values.

### Numbers
Numbers are normally stored in two different ways:
- Integer: whole numbers like 5, 37, -10, and 0
- Floating point numbers: these can represent decimals like: 0.75, -1.333, and 3 x 10 ^ 8

In both of those storage methods, there are inevitably how much space is used to save them, limiting how big (or small) the numbers can be, and floating point numbers are rounded when doing math and saving.

Additionally programming languages might include ways of representing fractions, or [complex numbers](https://en.wikipedia.org/wiki/Complex_number).

### Characters (Letters and other symbols)
Computers can store "characters" can be letters, numerals, or other symbols (like math symbols, spaces, and "[newlines](https://en.wikipedia.org/wiki/Newline)" which go to the next line when you press "Enter"). Some ways of storing characters, like [unicode](https://en.wikipedia.org/wiki/Unicode), support storing symbols and letters from many languages, and also [emojis](https://unicode.org/emoji/charts/full-emoji-list.html).


## Grouping data

Once we have some types of data representation on a computer, we can create different groupings of data to represent more types of data. We'll look at two types of groupings here, then look at what we can do with groupings next.

### Lists
The first way of combining data is by making a list with data.

So we can make a list of the numbers from 1 to 10:
 - 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Or we can make a list of letters [which happen to form a word] like this:
 - e, t, h, i, c, s

 The items in these lists are normally numbered with an "index", so you can ask for the 1st item, or 2nd item, or any other.

Note: Largely due to [historical peculiarities in the development of programming languages](https://en.wikipedia.org/wiki/Zero-based_numbering#Origin), most programming languages (including Python) number the 1st item in a list as item `0`. So:
- 1st item has index 0
- 2nd item has index 1
- 3rd item has index 2
- etc.

### Dictionaries
The other method of grouping data that we will discuss here is called a "dictionary" (sometimes also called a "maps").

Dictionaries allow programmers to combine several pieces of data, naming each piece. So for example, if you want to combine some pieces of information

[TODO: Example of dictionary that I can make with just numbers, booleans and characters?]


## Combination Data Types
We can represent much more information with lists, and dictionaries, and lists of dictionaries and dictionaries of lists, etc.

### Strings (Text)
Text is generally stored as a list of characters (like the example before of e, t, h, i, c, s), which is called a "string" (that is a bunch of characters strung together).

[![A photo of a string banner with shiny letters hanging on it spelling "HAPPY BIRTHDAY"](happy_birthday_banner.jpg)](https://www.pexels.com/photo/a-rocking-horse-and-birthday-decorations-7600328/)

A list of characters then can represent words, sentences, books, etc.

Additionally, text can be stored with extra formatting information (like fonts, colors, in a [Document File Format](https://en.wikipedia.org/wiki/Document_file_format) like with Word Documents, PDF files, etc.

### Images


### Images, Sound, Video

## Other Data Concerns

### Categorical Data


### Extra limitations
 - Text


- Different types of storage
  - Integer (whole number)
  - Float (number with decimal points)
  - Boolean (true/false) and binary (0/1)
  - String (text)
    - Pre-set options
    - Open ended
  - List of something
  - Etc.

## Reflection Questions
- What storage types make sense for different types of data?
  - Age
  - Gender
  - Name
  - Address
  - Relationship status
