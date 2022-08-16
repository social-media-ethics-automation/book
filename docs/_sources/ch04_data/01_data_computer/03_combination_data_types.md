# Combination Data Types
We can represent much more information with lists, and dictionaries, and lists of dictionaries and dictionaries of lists, etc.

## Strings (Text)
Text is generally stored as a list of characters (like the example before of e, t, h, i, c, s). These lists of characters are called "strings" (that is a bunch of characters strung together).

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

## Images / Sounds / Videos

While we wont interact very much with how images, sound, and video are stored, we wanted to at least briefly discuss it here.

__Images__ are created by defining a grid of dots, called pixels. Each pixel has three numbers that define the color (red, green, and blue), and the grid is created as a list of lists.

[TODO: pixilated image]

__Sounds__ are represented as the position of the speaker diaphragm over time (a sound wave). The position is saved as a number, and there positions saved at each time point, so the sound wave is saved as a list of numbers.

[TODO: sound wave image]

__Videos__ are represented as a squence of images (a list of images), along with a sound wave to be played at the same time.

[TODO: gif]

In most cases, after the initial data representation is created, the computer runs a compression algorithm, which takes the image, sound, or video, and finds a way of storing it in much less computer memory, often losing some of the quality when doing so.

[TODO: show compression fragments]

### Metadata
In addition to the main components of the images, sound, and video data, this information is often stored with __metadata__, which is extra data that tells you more about the data. This metadata might include:
- The time the image/sound/video was created
- The location wher the image/sound/video was taken
- The type of camera or recording device used to create the image/sound/video
- etc.

## Dates and Times
There are several options for how to save dates and times. Some options include a series of numbers (year, month, day, hour, minute, and second), or a string that includes all of those. You can also include time zone as well.

Dates end up being one of the trickier data types to work with in practice. One of the main reasons for this is that dates and times are different in different time zones, TODO: Finish

Note: We'll show these a little bit in chapter 18: Public Shaming

## Custom combined data types
TODO: Example of user info for a social media site


List of users:

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


````{admonition} Click to see example Python code
:class: dropdown
```python
users = [
  {
    username: "@kylemthayer",
    first_name: "Kyle",
    last_name: "Thayer",
    profile_picture: "kylethayer.jpg",
    friends: ["@SusanNotess", "@UW", "@UW_iSchool"]
  },
  {
    username: "@SusanNotess",
    first_name: "Susan",
    last_name: "Notess",
    profile_picture: "susannotess.jpg",
    friends: ["@kylemthayer"]
  },
]
```
````
