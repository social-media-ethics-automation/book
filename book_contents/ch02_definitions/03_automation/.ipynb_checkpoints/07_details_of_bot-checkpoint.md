# Understanding the Twitter Bot Code

Let's look more at that program that posts one tweet.

There are a number of ways of looking at the code, but first, let's look at it as a template with a couple pieces we can change.

## The program as a template

Below I've highlighted the text of the sections of the program that you might want to modify.

<pre style="color:gray">
import tweepy

bearer_token = "<strong style="color:black;background-color:lightgreen">n4tossfgsafs_fake_bearer_token_isa53#$%$</strong>"
consumer_key = "<strong style="color:black;background-color:lightgreen">sa@#4%fdfdsa_fake_consumer_key_$%DSG#%DG</strong>"
consumer_secret = "<strong style="color:black;background-color:lightgreen">45adf$T$A_fake_consumer_secret_JESdsg</strong>"
access_token = "<strong style="color:black;background-color:lightgreen">56sd5Ss4tsea_fake_access_token_%YE%hDsdr</strong>"
access_token_secret = "<strong style="color:black;background-color:lightgreen">j^$dr_fake_consumer_key_^A5s#DR5s</strong>"

client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)
client.create_tweet(text="<strong style="color:black;background-color:lightgreen">This tweet was posted by a computer program!</strong>")
</pre>

The first five highlighted pieces of code are for the special passwords you can get when you get approved for developer access to twitter [TODO: link] (I've put fake values in them for now):
- bearer token
- consumer key
- consumer secret
- access token
- access token secret

These special passwords are needed for different actions on twitter. Rathan than worry about which of these passwords are needed for which action, I'll just always including all of them.

The final highlighted piece of code (in the parentheses after `create_tweet`) is the text of what will be tweeted when this bot runs. You can change the text there to change what gets tweeted.

So, by changing those sections of code, you run this program to post whatever tweet you want to your twitter account. It is, of course, much easier to just open twitter and tweet, but as we get to more complicated programs, we'll start to see more of the power and dangers of automation on social media.

_Note: all the highlighted sections of code are surrounded by double quotes. In the Python programming language, putting something in quotes indicates that you want the computer to think of the things inside the quotes as pieces of text, in this case passwords and tweet contents._

## Adding code comments

The goal of programming language code is to be readable by both humans and computers, but sometimes the meaning of code isn't always clear to humans trying to read it. In order to aid humans reading the code, most programming languages allow "comments," which are pieces of code that the computer will ignore. These comments allow the person writing the code can leave a note to future people reading the code, without the computer reading it (like an [aside](https://en.wikipedia.org/wiki/Aside) in play).

In Python, you can add a comment by use the `#` symbol. Python will ignore everything on a line that comes after the `#`. But humans programmers will often look for the meaning of the program in these comments.

So, in order to make the program above easier for future humans to understand, let's add two comments telling these future humans where to add their special passwords and where they can change the text of the tweet:

```python
import tweepy

# TODO: Put your twitter account's special developer access passwords below:
bearer_token = "n4tossfgsafs_fake_bearer_token_isa53#$%$"
consumer_key = "sa@#4@fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"

client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)

# TODO: modify the text in the quotes below to change what this bot tweets:
client.create_tweet(text="This tweet was posted by a computer program!")
```

With those, hopefully a future human reader will have a better chance of understanding how to modify the program to do what they want.

_Note: I started each comment with "TODO" to tell the future human that there is a task they have **to do** to get the program to work for them. Since this is only intended for human readers, I could have written it in any way I want, but all capital letter TODOs are commonly used like this by programmers._


## Purpose of each section of code

Now that we've looked at the code as a modifiable template, let's break the code into sections and look at what the purpose of each part is.

_Note: It's normal if you don't understand everything here. Over the course of this book you will learn to understand more of how programs work, but also, even professional programmers often don't understand parts of the programs they are working on, they just understand enough to modify the parts they need to._

The first line of code is:
```python
import tweepy
```

The purpose of this line of code that loads another set of code. The code it loads is called [tweepy](https://www.tweepy.org/), which is code specially written to help make programs that work with twitter.


The next section of code is five lines long:
```python
bearer_token = "n4tossfgsafs_fake_bearer_token_isa53#$%$"
consumer_key = "sa@#4@fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"
```

This is code to store all of our twitter developer access passwords into Python so we can use them later. Again, you'll have to get your actual developer access passwords and replace the fake ones currently in the code.

The next section of code is five lines long:

```python
client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)
```

The purpose of this code is to take all the developer access passwords you entered above, and give them to the tweepy code so that the tweepy code can log into your twitter account and provide the needed passwords for whatever twitter action you want to do.

The final line of code is:
```python
client.create_tweet(text="This tweet was posted by a computer program!")
```

This is the line of code where a tweet is actually posted. The action is called "create_tweet" since the code is creating a tweet. Inside the double quotes is the text that is going to be tweeted.

## Adding more code comments
Now that we've looked at the purpose of each section of code, we can add additional comments explaining what each section does, so that future humans reading the code are more likely to understand it.

Following the common practice of programmers, we will put the comment before the section of code that the comment is explaining. We can also make multiple comment lines as needed if our comments are too long.

```python
# Load some code called "tweepy" that will help us work with twitter
import tweepy

# Load all your developer access passwords into Python
# TODO: Put your twitter account's special developer access passwords below:
bearer_token = "n4tossfgsafs_fake_bearer_token_isa53#$%$"
consumer_key = "sa@#4@fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"

# Give the tweepy code your developer access passwords so
# it can perform twitter actions
client = tweepy.Client(
   bearer_token=bearer_token,
   consumer_key=consumer_key, consumer_secret=consumer_secret,
   access_token=access_token, access_token_secret=access_token_secret
)

# Post a tweet
# TODO: modify the text in the quotes below to change what this bot tweets:
client.create_tweet(text="This tweet was posted by a computer program!")
```

Now that we've looked over the code and commented it, let's go to the next page, where you can try running it!
