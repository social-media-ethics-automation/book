# Combination Data Types
We can represent much more information with lists, and dictionaries, and lists of dictionaries and dictionaries of lists, etc.

## Strings (Text)
Text is generally stored as a list of characters (like the example before of e, t, h, i, c, s). These lists of characters are called "strings" (that is a bunch of characters strung together).

[![A photo of a string banner with shiny individual letters hanging on it spelling "HAPPY BIRTHDAY"](happy_birthday_banner.jpg)](https://www.pexels.com/photo/a-rocking-horse-and-birthday-decorations-7600328/)

A list of characters then can represent words, sentences, books, etc.

Additionally, text can be stored with extra formatting information (like fonts, colors, in a [Document File Format](https://en.wikipedia.org/wiki/Document_file_format) like with Word Documents, PDF files, [html website files](https://www.w3schools.com/html/html_intro.asp), etc.).

Note: We'll demonstrate strings later in this chapter, and in more detail in Chapter 7: Trolling

## Images / Sounds / Videos

TODO: Images: grid (list of lists) of pixels, each with a color

Sound: sound wave represented by position (number) of sound wave over time (list)

Videos: sequence of images along with sound

Note: compression algorithm

Note: We won't cover these data types in detail in this book.

## Dates and Times
There are several options for how to save dates and times. Some options include a series of numbers (year, month, day, hour, minute, and second), or a string that includes all of those. You can also include time zone as well.

Dates end up being one of the trickier data types to work with in practice. One of the main reasons for this is that dates and times are different in different time zones, TODO: Finish

Note: We'll show these a little bit in chapter 18: Public Shaming

## Custom combined data types
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
