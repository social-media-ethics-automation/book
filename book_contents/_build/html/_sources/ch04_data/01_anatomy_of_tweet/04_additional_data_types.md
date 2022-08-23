# Additional Data Types
You might have noticed that there are still a couple pieces of data on the example tweet that we haven't discussed yet. Let's look at those now.


## Images / Sounds / Videos

Our example tweet has several images in it:
```{figure} dog_tweet_with_images.png
---
name: tweet_images_fig
alt: "Screenshot of the tweet from before, but with the images highlighted: The user profile picture and the three puppy photos in the tweet contents"
---
The profile picture and the puppy photos in the tweet are images.
```

While you won't need to know the details of how images, sound, and video are stored for this class, we wanted to at least briefly discuss it here just to give you a rough idea of how computers store these kinds of data.

__Images__ are created by defining a grid of dots, called pixels. Each pixel has three numbers that define the color (red, green, and blue), and the grid is created as a list (rows) of lists (columns).

![A very close up photo of a small section of a screen with a white heart icon. You can make out that the screen is a grid and the grid squares where the heart is have red, green, and blue bands, which look white when seen from a distance](pixel_heart.jpg)

__Sounds__ are represented as the position of the speaker diaphragm over time (a sound wave). The position is saved as a number, and there positions saved at each time point, so the sound wave is saved as a list of numbers.


% image based on: https://pixabay.com/vectors/speaker-volume-medium-loud-sound-98509/
```{image} speaker.png
:alt: A diagram of a speaker, where the big middle round part (diapgragm) is indicated to move in and out, producing sound waves.
:width: 150px
:align: center
```

```{image} sound_wave_this.png
:alt: An image of a sound wave for the word "this". There is a horizontal line in the middle, and a bunch of vertical bars that are approxomitely centered. The vertical bars are different lengths makking a pattern of ups and downs that represent the sound wave.
:align: center
```


__Videos__ are represented as a squence of images (a list of images) called frames, often with a sound wave to be played at the same time.

![the "mind blown" gif: animated gif of a man making hand explosion out of his forhead while stars and explosions are overlayed on top](mind_blown.gif)

In most cases, after the initial data representation is created, the computer runs a compression algorithm, which takes the image, sound, or video, and finds a way of storing it in much less computer memory, often losing some of the quality when doing so.

![The author of Kyle Thayer, but highly compressed, making it look somewhat blocky and colors are a little off, and it is noisy.](kylethayer_compressed.jpg)

### Metadata
In addition to the main components of the images, sound, and video data, this information is often stored with metadata, such as:
- The time the image/sound/video was created
- The location wher the image/sound/video was taken
- The type of camera or recording device used to create the image/sound/video
- etc.

For our purposes in this class, most of the the time we run into images, we will find a string that tells us where the image, video, or sound is saved (e.g., we'll get something like "kylethayer.jpg"), and we might additionally get some metadata.

## Dates and Times
The final piece of data from the tweet we will cover is the date when the tweet was posted:

```{figure} dog_tweet_with_date.png
---
name: tweet_date_fig
alt: "Screenshot of the tweet from before, but with the date highlighted: Feb 10, 2020"
---
The tweet includes the date when it was posted.
```
There are several options for how to save dates and times. Some options include a series of numbers (year, month, day, hour, minute, and second), or a string that with all of those pieces of information written out. Sometimes only the date is saved, with no time information, and sometimes the time information will include the timezone.

Dates turn out to be one of the trickier data types to work with in practice. One of the main reasons for this is that what time or day it is depends on what time zone you are in.

So, for example, when twitter tells me that the tweet was posted on Feb 10, 2020, does it mean Feb 10 for me? Or for the person who posted it? Those might not be the same. Or if I want to see for a given account, how much they tweeted "yesteday," what do I mean by "yesterday?" We might be in different time zones and have different start and end times for what we each call "yesterday."

Note: We'll work with dates and times a little bit in chapter 18: Public Shaming
