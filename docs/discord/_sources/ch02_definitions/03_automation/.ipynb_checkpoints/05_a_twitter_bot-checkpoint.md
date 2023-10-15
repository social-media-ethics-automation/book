# A program that posts one tweet
Below is a computer program written in the Python programming language. The program will post a single tweet that says: "This tweet was posted by a computer program!".

Don't worry if you don't understand any of this Python code yet; we will build an understanding of code like this throughout the book.

```
import tweepy
import bot_keys

client = tweepy.Client(consumer_key=bot_keys.consumer_key, consumer_secret=bot_keys.consumer_secret,
                       access_token=bot_keys.access_token, access_token_secret=bot_keys.access_token_secret)

client.create_tweet(text="This tweet was posted by a computer program!")
```

Though you may not understand anything in the above code yet, I want to point out a couple things:
- The code above is full of English words like "import", "keys", "secret", which may help you guess the meaning of the code.
- There are also other symbols being used as well, though in a different way than in normal English, symbols like ``=``, `_`, `.`, `(`, and `)`
- One particular piece of code gives a good hint as to what it is doing: `create_tweet`. That indeed is the part of the program where the tweet is posted.

We will go through that example code in more detail next.
