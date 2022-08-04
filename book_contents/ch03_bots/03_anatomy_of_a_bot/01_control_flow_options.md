# Different Ways a Program Can Be Organized

In order to understand how a bot is built and can work, we will now look at the different ways computer programs can be organized. We will not be looking at actual computer programming code in this section, but instead looking at how the code might be organized. We will look at real code examples of these in the next section.

TODO: Define psuedo code.

## Statements: Steps that Run In Order
Python is in a group of programming languages called [imperative programming languages](https://en.wikipedia.org/wiki/Imperative_programming). At their core, programs written in imperative programming languages consist of a list of "statements" to be run in order.

So a program in one of these languages would look like:
```text
statement 1
statement 2
statement 3
```
And when the program is run, statement 1 runs first, then statement 2, then, finally, statement 3.

You might recognize this as the same style of instructions as a cooking recipe, like making a scrambled egg:
```text
1. Put frying pan on stove and turn it on.
2. Crack egg, and pour into the frying pan (throwing away the shell).
3. Add salt and pepper.
3. Stir egg while it cooks, until fully cooked.
```

In fact, the format of a cooking recipe is basically an imperative programming language where the cook acts as a "human computer" following the cooking instructions.

> ![Photo of a man in a kitchen, looking at a notebook while mixing something in a bowl. The bowl is surrounded by eggs, strawberries and other ingredients.](cooking.jpg)
> A human computer running a cooking program. In other words: "someone following a recipe" ([photo source](https://www.pexels.com/photo/a-man-cooking-at-the-kitchen-6944110/))

Twitter bots are generally organized in this same way, so one bot might be organized like this:
```text
1. Log into Twitter
2. Post offense tweet 1
3. Private message user 2
4. Block user 3
```

## Variables: Save information for later
The next organizing feature of programming languages like Python are "variables." Variables are a way of saving information for later use.

In a cooking recipe, an equivalent would be something like putting ingredients in a bowl to use later, like:
```text
TODO: Pound cake directions, something like
1. Put one pound of butter in a bowl
2. Add one pound of sugar to the bowl and mix
...
```

Sometimes in cooking, you use multiple bowls to mix different parts of the recipe separately:
```text
...
while the dough is rising:
- mix the powdered sugar, butter, and milk in another bowl to make the frosting
```

In a computer program, when you save information for later use, instead of putting it in a bowl, give it a name, which you can use to get the information later.

```text
1. Save my first name in a variable called "first_name"
2. Save my last name in a variable called "last_name"
3. Display my full name as what is stored in the variable "first_name" followed
   by a space, followed by what is stored in the variable "last_name"
```

```text
1. Find my latest tweet, and save it as a variable named "my_latest_tweet"
2. Search for all tweets that are a reply to the tweet saved in the variable "my_latest_tweet"
```

## Loops: Repeating Actions
Next up is loops, which are used to repeat actions.

In cooking you can repeat an action a set number of times:
```text
...
5. Stir 10 times [Better example???]
...
```

Or you can repeat the same action, but to different items:
```text
...
7. Put frosting on each of the cupcakes.
...
```

Or you can repeat the same action until you get a certain result:
```text
5. Continue stirring until the batter is smooth
```

In computer programming you can repeat an action a set number of times

```text
1. Tweet "Warner Brothers should #ReleaseTheSnyderCut" 100 times
```
 (footnote: https://www.rollingstone.com/tv-movies/tv-movie-features/justice-league-the-snyder-cut-bots-fans-1384231/)

Or a computer program can repeat an action to a set of items

```text
...
3. Like each of the tweets that were replies to my_latest_tweet
...
```

Or a computer program can repeat an action until a condition is met:
```text
...
- Keep sending private messages to this person until they block me
...
```


## Code Blocks: Grouping statements
```text
TODO: recipe with a set of steps to repeat, like a complicated set of toppings for each cupcake
```

### Pausing/Scheduling
```text
TODO: recipe: pull the muffins out of the oven after 10 minutes.
```

## Conditionals: What you do depends
```text
TODO: recipe where at 10 minutes you pull out the muffins and put in a toothpick. **If** the toothpick is clean, they are done, otherwise, put them in for another 2 minutes and check again.
```


## Events: When you do something depends
```text
TODO: Kettle: put on heat and leave until the kettle whistles, then make tea
```

## Functions/Libraries: Run another program
```text
TODO: recipe: step 1: make a base dough (see recipe on page 42).
```
