# An example twitter bot

```
!pip install tweepy
import tweepy
import bot_keys

client = tweepy.Client(consumer_key=bot_keys.consumer_key, consumer_secret=bot_keys.consumer_secret,
                       access_token=bot_keys.access_token, access_token_secret=bot_keys.access_token_secret)

client.create_tweet(text="This tweet was posted by a computer program!")
```

## Reflection Questions
- When I ran the program, who made those tweets (me? the bot?)? How do you think about identity in this context?
- In what ways is a bot similar / different from a “normal” user? (what can a bot do that a “normal” user can’t)?
