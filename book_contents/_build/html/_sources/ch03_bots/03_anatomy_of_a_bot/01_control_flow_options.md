# Organizing a Computer Program

In order to understand how a bot is built and can work, we will now look at the different ways computer programs can be organized. We will cover a bunch of examples quickly here, to hopefully give you an idea of many options for how to write a program. Don't worry if you don't follow all of it, as we will go back over these one at a time in more detail throughout the book.

In this section we will not show actual Python computer programs (that will be in the next section). Instead here we will focus on what programmers call "[psuedocode](https://en.wikipedia.org/wiki/Pseudocode)," which is an human language outline of a program. Psuedocode is intended to be easier to read and write. Pseudocode is often used by programmers to plan how they want their programs to work, and once the programmer is somewhat confident in their pseudocode, they will then try to write it in actual programming language code.

```{note}
The programs outlined below in pseudocode are meant to demonstrate what could be done with a computer program, not what should be done or what would necessarily be a good idea.
```

## Statements: Steps that Run In Order
Python is in a group of programming languages called [imperative programming languages](https://en.wikipedia.org/wiki/Imperative_programming).[^language_types_footnote] At their core, programs written in imperative programming languages consist of a list of "statements" to be run in order.

[^language_types_footnote]: There are other types of programming organizations as well, such as [functional programming](https://en.wikipedia.org/wiki/Functional_programming) (like [Excel](https://www.microsoft.com/en-us/research/blog/lambda-the-ultimatae-excel-worksheet-function/) and [Google Sheets](https://www.google.com/sheets/about/)),  [visual programming](https://en.wikipedia.org/wiki/Visual_programming_language) (like the educational [Scratch](https://scratch.mit.edu/), or the 3D Graphics [Blender node editor](https://docs.blender.org/manual/en/2.79/editors/node_editor/introduction.html])), [declarative programming](https://en.wikipedia.org/wiki/Declarative_programming) (like HTML and CSS web content) [object oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming) (can be done in Python, JavaScript, and many others), and [many more](https://en.wikipedia.org/wiki/Programming_paradigm).

So a program in one of these languages would look like:
```text
- statement 1
- statement 2
- statement 3
```
And when the program is run, statement 1 runs first, then statement 2, then, finally, statement 3.

You might recognize this as the same style of instructions as a cooking recipe, like making a scrambled egg:
```text
- Put frying pan on stove and turn it on.
- Crack egg, and pour into the frying pan (throwing away the shell).
- Add salt and pepper.
- Stir egg while it cooks, until fully cooked.
```

In fact, the format of a cooking recipe is basically an imperative programming language where the cook acts as a "human computer" following the cooking instructions.

> ![Photo of a man in a kitchen, looking at a notebook while mixing something in a bowl. The bowl is surrounded by eggs, strawberries and other ingredients.](cooking.jpg)
> A human computer running a cooking program. In other words: "someone following a recipe" ([photo source](https://www.pexels.com/photo/a-man-cooking-at-the-kitchen-6944110/))

Twitter bots are generally organized in this same way, so one bot might be organized like this:
```text
- Log into Twitter
- Find any new tweets that mention me that also have curse words
- Look up the users who posted those tweets
- Block those users
```

We will show how to use statements in Python in the next section.

## Variables: Save information for later
Variables are a way of saving information on the computer, so we can use it later in the computer program.

In a cooking recipe, the equivalent would be spaces or containers to hold ingredients. So you might place the ingredients on the counter in preparation for cooking. Or you might combine some ingredients in a mixing bowl, so the mixing bowl holds the combined ingredients through each step, like:
```text
TODO: Pound cake directions, something like
- Put one pound of butter in a bowl
- Add one pound of sugar to the bowl and mix
```

Sometimes in cooking, you use multiple mixing bowls to mix different parts of the recipe separately:
```text
- while the dough is rising in the first bowl:
  - mix the powdered sugar, butter, and milk in another bowl to make the frosting
```

In a computer program, when you save information for later use, instead of putting it in a bowl, you give it a name. The computer then makes a place in its memory with that name, and saves the information you asked it to save. Then you can use that name later in the program to ask the computer what was saved in that spot.

For example I might save my first and last name separately in the computer, then combine them together to make my full name (which I save), and then use that full name to send a private message to introduce myself:
```text
- Save my first name in a variable called "first_name"
- Save my last name in a variable called "last_name"
- Create the text of my full name by combining what is in the variable "first_name",
  followed by a space, followed by what is in the variable "last_name", then save
  it in a new variable called "full_name"
- Send a private message saying "Hello my name is ___" but filling in the blank
  with what is in the variable "full_name"
```

Or, when I am looking something up, like my latest tweets, I can save that in a variable so I can look up replies to those tweets the next step:
```text
- Find my latest tweet, and save it as a variable named "my_latest_tweet"
- Search for all tweets that are a reply to the tweet saved in the variable "my_latest_tweet"
```

We will show how to use cariables in Python in the next section.


## Events: When you do something depends
Events let us perform a programming action in response to something happening. The computer may sit and do nothing while waiting for an event to happen.

Within cooking this might look like:
```text
- Put the tea kettle on a burner turned to high and leave it
- When kettle whistles, that means the water is boiling, and you can make tea
```

Within programming, it might look like:
```text
- Whenever someone tags me in a post
  - like their post which has me tagged
```

### Pausing/Scheduling
One of the most common events to program for is around time: We can also tell programs to wait for a period of time, or start at a given time.

In cooking this might look like:
```text
- Put the muffins in the oven, and let them bake for 10 minutes.
```

In programming, it might look like:
```text
- Post this set of tweets, pausing 30 seconds between each tweet
```

Or

```text
- every day at noon, post a report on the weather
```

We will show how to use pausing in the next section.

We will show how to use other Events and Scheduling in Python in Chapter 18: Public Shaming.


## Conditionals: What you do depends
Conditionals let us change what we do depending on the situation.

In cooking, we might use a toothpick to see if the muffins are done and change our course of action depending on that test:
```text
- After 10 minutes pull out the muffins and poke through with a toothpick.
  - If the toothpick comes out clean, the muffins are done
  - If the toothpick comes out with batter, put them in for another 2 minutes
```

In programming, we might do this:
```text
- look up the latest tweet mentioning me
  - if that tweet says "delete your account", then delete my account
  - otherwise, don't delete my account
```

We will show how to use conditionals in Chapter 7: Trolling.


## Loops: Repeating Actions
Loops are used to repeat actions, though there are several different types of repetitive actions.

In cooking you can repeat an action a set number of times:
```text
- Stir 10 times [Better example???]
```

Or you can repeat the same action, but to different items:
```text
- Put frosting on each of the cupcakes.
```

Or you can repeat the same action until you get a certain result:
```text
- Continue stirring until the batter is smooth
```

In computer programming you can repeat an action a set number of times

<pre>
- Tweet this 100 times: "Warner Brothers should <a href="https://www.rollingstone.com/tv-movies/tv-movie-features/justice-league-the-snyder-cut-bots-fans-1384231/">#ReleaseTheSnyderCut</a> of the Justice League movie."
</pre>

Or a computer program can repeat an action to a set of items

```text
- Like each of the tweets that were replies to my latest tweet
```

Or a computer program can repeat an action until a condition is met:
```text
- Keep sending private messages to this person until they block me
```

We will show how to use loops in Chapter 5: History of Social Media.

## Code Blocks: Grouping statements
Sometimes in programming, we want to group several steps (i.e., statements) together. When we group these steps together we call it a code "block." These blocks of code often used with conditionals (e.g., if this condition is true, do these five steps), and with loops (e.g., for each of these items, do these five steps).

In a recipe, you might create a block of instructions like this:
```text
- for each of the cupcakes:
  - put on a layer of white frosting
  - with pink frosting, make a flower on top
  - add sprinkles
```

In a computer program, you might make a code block of statements like this:

```text
- for each of the latest tweets that mention me:
  - look up the time of the tweet (in your time zone)
  - look up the location the tweet was posted in
  - calculate the local time of the person tweeting when they tweeted
  - reply to their tweet ("you posted that tweet at ___ in your time zone")
```

Using code blocks allows you to do things like put conditionals inside of loops
```text
- for each of the latest tweets that mention me:
  - look up if the tweet was posted from android or an iPhone
    - if it was from an android, like the tweet
    - if it was from an iPhone, block the user who made the tweet
```


We will show how to use code blocks in Chapter 5: History of Social Media.

## Functions/Libraries: Run another program
The final programming organization feature we will cover here is functions and libraries, which basically allow you to run another computer program. This could be a small program that you made that want to use, or it could be a program written by someone else that you are using.

In cooking this might look like a step of asking the cook to make something from another recipe.
```text
- make a base dough (see recipe on page 42).
```

The recipe also could ask you to make a different version of a recipe from another page:
```text
- make a base dough (see recipe on page 42), but mix in two tablespoons of cocoa powder.
```

In programming, a function is a small program that you can run from another place in the code (programmer call this "calling" a function). Functions also can accept data and options for how they run. Code libraries are a collection of functions and data that help with certain tasks.

In this book, we will be using the [tweepy](https://www.tweepy.org/) code library, which comes with many pre-written functions that help us do actions on twitter, functions like:
- create_tweet
- delete_tweet
- retweet
- search_recent_tweets
- follow_user
- etc.

You may be able to figure out what the purpose of each of those tweepy functions are based on the name, though we'll look at the specifics of how to use them throughout the book.

If you look back over the various psuedocode examples above, most of them would involve calling various functions, such as those tweepy functions.

We will show examples of calling functions starting in the next section.

We will show how to write functions in Chapter ?? [TODO: figure out].
