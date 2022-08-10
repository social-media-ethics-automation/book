# Representing Data in a Computer

[TODO: What is data?]


We previously covered in chapter 2 how [computers speak binary](../../ch02_definitions/03_automation/03_binary.html), and all data and instructions are turned into binary, and gave examples of how images or text can be represented with binary. There are many ways of representing data on a computer (called "data types"), so we'll look at a few types of them here.

As we've said previously, don't worry if you don't understand all of these data types yet. We'll be covering various ones in more detail throughout the book.

## Some Simple Data Types

First we'll look at a few simple data storage types, called [primitive data types](https://en.wikipedia.org/wiki/Primitive_data_type).

Note: We'll demonstrate these later in this chapter.

### Booleans (True / False)
Binary consisting of 0s and 1s make it easy to represent true and false values, where 1 often represents true and 0 represents false. Most programming languages have built in ways of representing True and False values.

### Numbers
Numbers are normally stored in two different ways:
- Integer: whole numbers like 5, 37, -10, and 0
- Floating point numbers: these can represent decimals like: 0.75, -1.333, and 3 x 10 ^ 8

In both of those storage methods, there are limits to how much space is used to save each number, limiting how big (or small) the numbers can be, and causing rounding with floating point numbers.

Additionally programming languages might include ways of representing fractions, or [complex numbers](https://en.wikipedia.org/wiki/Complex_number).

### Characters (Letters and other symbols)
Computers can store "characters" can be letters, numerals, or other symbols (like math symbols, spaces, and "[newlines](https://en.wikipedia.org/wiki/Newline)" which go to the next line when you press "Enter"). Some ways of storing characters, like [unicode](https://en.wikipedia.org/wiki/Unicode), support storing symbols and letters from many languages, and also [emojis](https://unicode.org/emoji/charts/full-emoji-list.html).


## Grouping data

Once we have some types of data representation on a computer, we can create different groupings of data to represent more types of data. We'll look at two types of groupings here, then look at what we can do with those groupings.

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

Note: We'll demonstrate lists later in Chapter 5: History of Social Media.

### Dictionaries
The other method of grouping data that we will discuss here is called a "dictionary" (sometimes also called a "maps").

Dictionaries allow programmers to combine several pieces of data, naming each piece. When we do this, the dictionary will have a number of names, and for each of those names a piece of information (called a "value" in this context). You can think of this as like a language dictionary where there is a word and a definition for each word. Then you can look up any name or word and find the value or definition.

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

We can also use any piece of information we want for the "name" in a dictionary. So if we wanted, we could make a color the "name" in a dictionary. For example, in this one, names are colors (in terms of red, green, and blue), and the values are the [most common names of that color in different languages]{https://uwdata.github.io/color-naming-in-different-languages/vis/full_color_maps.html}:

Most common name for a given color in English:
- <span style="background-color:rgb(231,37,37)"> &nbsp; </span>{Red: 231, Green, 37, Blue: 37}: Red
- <span style="background-color:rgb(167,37,128)"> &nbsp; </span>{Red: 168, Green, 37, Blue: 128}: Magenta

Most common name for a given color in Korean:
- <span style="background-color:rgb(231,37,37)"> &nbsp; </span>{Red: 231, Green, 37, Blue: 37}: 빨강
- <span style="background-color:rgb(167,37,128)"> &nbsp; </span>{Red: 168, Green, 37, Blue: 128}: 자주

Note: We'll demonstrate dictionaries later in Chapter 5: History of Social Media, and Chapter 8: Data Mining.

## Combination Data Types
We can represent much more information with lists, and dictionaries, and lists of dictionaries and dictionaries of lists, etc.

### Strings (Text)
Text is generally stored as a list of characters (like the example before of e, t, h, i, c, s). These lists of characters are called "strings" (that is a bunch of characters strung together).

[![A photo of a string banner with shiny individual letters hanging on it spelling "HAPPY BIRTHDAY"](happy_birthday_banner.jpg)](https://www.pexels.com/photo/a-rocking-horse-and-birthday-decorations-7600328/)

A list of characters then can represent words, sentences, books, etc.

Additionally, text can be stored with extra formatting information (like fonts, colors, in a [Document File Format](https://en.wikipedia.org/wiki/Document_file_format) like with Word Documents, PDF files, [html website files](https://www.w3schools.com/html/html_intro.asp), etc.).

Note: We'll demonstrate strings later in this chapter, and in more detail in Chapter 7: Trolling

### Images / Sounds / Videos

TODO: Images: grid (list of lists) of pixels, each with a color

Sound: sound wave represented by position (number) of sound wave over time (list)

Videos: sequence of images along with sound

Note: compression algorithm

Note: We won't cover these data types in detail in this book.

### Dates and Times
There are several options for how to save dates and times. Some options include a series of numbers (year, month, day, hour, minute, and second), or a string that includes all of those. You can also include time zone as well.

Dates end up being one of the trickier data types to work with in practice. One of the main reasons for this is that dates and times are different in different time zones, TODO: Finish

Note: We'll show these a little bit in chapter 18: Public Shaming

### Custom combined data types
TODO: Example of user info for a social media site

User 1:
- Username: @kylemthayer (a String)
- First name: Kyle (a String)
- Last Name: Thayer (a String)
- Profile Picture: [TODO picture here] (an image)
- Friends: @SusanNotess, @UW, @UW_iSchool, ... (a list of Strings)

User 2:
- Username: @SusanNotess (a String)
- First name: Susan (a String)
- Last Name: Notess (a String)
- Profile Picture: [TODO picture here] (an image)
- Friends: @kylemthayer, ??? (a list of Strings)

## Other Data Limitations
Additional limitations on data can be added:

- Strings (text) limits like
  - limiting what kind of characters appear in a name (e.g., disallowing emojis)
  - name length (e.g., minimum length, maximum length)
  - Could be restricted to a small set of options (e.g., which country do you live in?)
- Numbers
  - Disallow things like ages over 150, or a year in the future


## Reflection Questions
- What storage types make sense for different types of data?
  - Age
  - Gender
  - Name
  - Address
  - Relationship status
