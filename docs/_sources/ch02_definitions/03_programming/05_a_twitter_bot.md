# A program that posts one tweet
Below is a computer program written in the Python programming language. The program will post a single tweet that says: "This is tweet was posted by a computer program!".

Don't worry if you don't understand any of this Python code yet; we will build an understanding of code like this throughout the book.

```
import tweepy

consumer_key = "sa@#4%fdfdsa_fake_consumer_key_$%DSG#%DG"
consumer_secret = "45adf$T$A_fake_consumer_secret_JESdsg"
access_token = "56sd5Ss4tsea_fake_access_token_%YE%hDsdr"
access_token_secret = "j^$dr_fake_consumer_key_^A5s#DR5s"

client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,
                       access_token=access_token, access_token_secret=access_token_secret)

client.create_tweet(text="This is tweet was posted by a computer program!")
```

Though you may not understand anything in the above code yet, I want to point out a couple things:
- The code above is full of English words like "import", "key", "secret", which may help you guess the meaning of the code.
- There are also other symbols as well, though being used in a different way than in normal English, symbols like ``=``, `_`, `.`, `(`, and `)`
- One particular piece of code gives a good hint as to what it is doing: `create_tweet`. That indeed is the part of the program where the tweet is posted.
- There are four pieces of text with random numbers and letters that include things like "fake_consumer_key" inside. These pieces of text are meant to be replaced with a set of special passwords to your actual twitter account. You can get these special passwords if you get developer access to twitter (TODO: link to appropriate page). Once you put your special passwords in those locations then this code will post a tweet on your account.

We will go through that example code in more detail next.
