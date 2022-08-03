# Data Mining

## Homework Due
- Look up what a social media site thinks about you and your interests
- [Your Friends’ Online Connections Can Reveal Your Sexual Orientation](https://www.vice.com/en/article/gvydky/your-friends-online-connections-can-reveal-your-sexual-orientation)
- [Housing companies used Facebook’s ad system to discriminate against older people, according to new human rights complaints](https://www.washingtonpost.com/technology/2019/09/18/housing-companies-used-facebooks-ad-system-discriminate-against-older-people-according-new-human-rights-charges/)

## What all data is available to social media platforms?
- Data user directly provides
  - E.g., filling out your profile info
- Other data platform collects
  - What you click on, what you pause on, when you log in, etc.

## Data mining (what we can infer from the existing data)
- Info about individuals
  - E.g., Sexual orientation, race, political leanings, interests, etc.
- Other information
  - Trends about users or topics
     - E.g., tracking disinformation
     - E.g., Covid trends based on Candle reviews
       - [![](covid_candles.png)](https://twitter.com/zornsllama/status/1473575508784955394) NOTE: This might be correlational due to other factors, like seasonal trends

## How is this data used
- What content is shown to users
  - Try to keep users engaged by showing them things that will keep them there and make them come back
- Targeted advertising
  - Can give people ads for things they are interested in
  - If we can infer who would be likely to be addicted to gambling, we can target gambling ads to them
  - [Trump 2016 campaign 'targeted 3.5m black Americans to deter them from voting'](https://www.theguardian.com/us-news/2020/sep/28/trump-2016-campaign-targeted-35m-black-americans-to-deter-them-from-voting)




## Programming
- Sentiment analysis
- Look at full structure of twitter data (including dictionaries)
- How to read / navigate tweepy docs:
Official docs: https://docs.tweepy.org/en/stable/client.html

### Dictionaries
- A data structure with a set of “keys” that refer to a set of “values.” Sort of like saving a bunch of variables in another variable.
- Create an empty dictionary:
```
example_dictionary = {}
Create a dictionary with some keys and values:
example_dictionary = {
  "first_name": "Kyle",
  "last_name": "Thayer"
}
```
- Get a value from a dictionary:
```    
person = example_dictionary["first_name"]
```
- Set a value from a dictionary:
```
    Example_dictionary["age"] = 38
```
- Read more: https://www.w3schools.com/python/python_dictionaries.asp
