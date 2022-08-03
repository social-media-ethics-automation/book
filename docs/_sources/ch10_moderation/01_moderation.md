# Content Moderation

## Readings due
- [Against “Don’t read the comments”](https://medium.com/humane-tech/against-don-t-read-the-comments-aee43ce515b9)
- [Facebook’s race-blind practices around hate speech came at the expense of Black users, new documents show](https://www.washingtonpost.com/technology/2021/11/21/facebook-algorithm-biased-race/)

## Moderation tools - User controls
- Block
- Mute
- Delete
- Report

![](comment_review.png)

## Moderation tools - platform controls
- Delete
- Suspend
- Ban
- Auto-detect
- Flag for evaluation

## Free Speech?
- [1st Amendment](https://constitution.congress.gov/constitution/amendment-1/):
  - Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances
- What is the value of free speech?
- What are the limits on free speech?
- Who has freedom of speech and when?
  - Individuals
  - Corporations (including social media companies)

[![](free_speech_2x.png)](https://xkcd.com/1357/)

## What content might a person or platform moderate for?

- Quality control
  - Spam
  - Ads
  - Disinformation
  - Off topic
- Safety
  - Trolling
  - Harassment
- Potentially offensive content
  - Violence
  - Sex
  - Nudity
  - Language
- Copyright infringement

## Different Platform approaches
- 4chan/8chan - minimal moderation
- Reddit - different moderators in each subreddit, some very toxic, others not
  - [Study finds Reddit’s controversial ban of its most toxic subreddits actually worked](https://techcrunch.com/2017/09/11/study-finds-reddits-controversial-ban-of-its-most-toxic-subreddits-actually-worked/)
    - “Reddit finally banned a handful of its most hateful and deplorable subreddits, including r/coontown and r/fatpeoplehate.”
    - “Post-ban, hate speech by the same users was reduced by as much as 80-90 percent.”
    - “Members of banned communities left Reddit at significantly higher rates than control groups.”
    - “Migration was common, both to similar subreddits (i.e. overtly racist ones) and tangentially related ones (r/The_Donald).”
    - “However, within those communities, hate speech did not reliably increase, although there were slight bumps as the invaders encountered and tested new rules and moderators.”
- [News sites got rid of having comment sections at the end of articles in 2013](https://www.wired.com/2015/10/brief-history-of-the-demise-of-the-comments-timeline/)
- Public Figure Exception?
- Facebook
  - https://www.technologyreview.com/2021/03/11/1020600/facebook-responsible-ai-misinformation/
    - “The more likely a post is to violate Facebook’s community standards, the more user engagement it receives, because the algorithms that maximize engagement reward inflammatory content.”
- Political Leaders Exception
  - Twitter/Facebook/etc. Had an [exception to their normal moderation policies for political leaders](https://help.twitter.com/en/rules-and-policies/public-interest), where they wouldn’t ban them even if they violated site policies (most notably applied to Donald Trump)
  - These policies changed some when Donald Trump was banned from Twitter and then Facebook after the January 6th Insurrection
    - [Facebook to end special treatment for politicians after Trump ban](https://www.theverge.com/2021/6/3/22474738/facebook-ending-political-figure-exemption-moderation-policy)

## Discussion

- Have you ever reported a post/comment for violating social media platform rules?
- Have you ever faced consequences for breaking social media rules (or for being accused of it)?
- In unmoderated online spaces who has the most power and ability to speak and be heard? Who has the least power and ability to speak and be heard?

## Programming
Functions with named params and default values

https://www.w3schools.com/python/python_functions.asp
```
def function_name(arg_1 = "default"):
  # do various actions, like this:
  print("arg 1 will be default if not sent:" + arg_1)

# call function
    function_name()
    function_name(arg_1 = "a different value")
```


Function returns

- Functions can “return” a value, that is, a value comes back when the function is done, that can be used (e.g., stored in a variable). E.g.

```
message = "this is a test message"

how_long_message =      len(message)
```   
             <- Output (return)    <- Inputs (arguments, parameters)


- When writing a function, to return a value, use the word “return” followed by a value

```
def mult(num1, num2):
  return num1 * num2

# call function
    number_var = mult(3, 4)
```
