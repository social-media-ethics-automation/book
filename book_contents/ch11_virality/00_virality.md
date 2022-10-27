# (Incomplete) Virality

Our next topic is virality, that is how content goes viral the consequences of virality. To understand virality, we need to start with understanding evolution.

```{tableofcontents}
```
TODO: Include in Programming

Nested Loops
Lets say we have a list of sentences and we are searching for a specific word. We must use nested loops. Check out the example bellow:

lyrics = ['You used to call me on my cell phone',
         'Late night when you need my love',
         'Call me on my cell phone',
         'Late night when you need my love',
         'And I know when that hotline bling',
         'That can only mean one thing',
         'I know when that hotline bling',
         'That can only mean one thing']

phone_count = 0

for line in lyrics:
    split_line = line.split() # splitting up sentence into list of words
    for word in split_line:
        if word == 'phone':
            phone_count += 1
            print(line)
            print(phone_count)

You used to call me on my cell phone
1
Call me on my cell phone
2
Recreate the previous example with your favorite song.

Twitter Practice
Install and import the “tweepy” library of code that gives us twitter functions
import tweepy
Login
_ copy in the code from test_twitter_bot_keys.ipynb
Search for recent tweets that include the word ‘Weather’. Assign this list to a variable called weather.

Loop through the weather list and count how many times you come across the words “cold”, “freezing”, or “chilly”

Create a variable called long_words and assign an emepty list to it –> [].

Loop through the weather list. If a word has a length of 5 OR GREATER, add it to the long_words list. Make sure to return the long_words list at the end of your code block.

*Hint: you can add to a list using the append() function

append() example:

list = [1, 2, 3]
list.append(4)

list  -->  [1, 2, 3, 4]
Get the length of your long_words list and store it in a variable called long_words_length.

Create a while loop, printing out the sentence: ”The word, WORD, is extremely long.” for each word in the long_words list.

*Hint: use the long_words_length variable to check if you’ve gone through the entire list. With each iteration, subtract 1 from the variable.

CHALLENGE: Copy and paste the code from the previous question. Alter the code to create the sentence:

”The word, WORD, is LENGTH letters long.”
