#!/usr/bin/env python
# coding: utf-8

# # Demo: Sentiment Analysis and Loop Variables
# 
# ## Sentiment Analysis
# In order to test out data mining on Twitter, we are going to use a Natural Language Processing library, which gives us functions to work with langauge data such as sentences, words, etc.
# 
# You don't need to know the details of how these work internally, but we will be using the "[Natural Language Toolkit](https://www.nltk.org/)" along with the "Valence Aware Dictionary and sEntiment Reasoner" (or VADER) lexicon.
# 
# So let's get the library and lexicon now.

# In[1]:


import nltk
nltk.download(["vader_lexicon"])


# We will now have the libary make a "Sentiment Intensity Analyzer" for us, which we save in a variable called `sia`

# In[2]:


from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# Now that we have the "Sentiment Intensity Analyzer" we can try it out on different sentences to have the computer guess how positive or negative they are. Let's start with a really positive sentance:

# In[3]:


sentence = "I love love love pizza!!!!!!!!"
sia.polarity_scores(sentence)["compound"]


# In the above code, we ran a `polarity_scores` function on the sentence and pulled out the `compound` result. In this case it came back as `0.941`, which is close to 1 and indicates a positive statement.
# 
# Now let's try a really  negative one:

# In[4]:


sentence = "I hate hate hate pizza!!!!!!!!"
sia.polarity_scores(sentence)["compound"]


# You can see that this sentence came out as `-0.9227`, which is close to -1 and indiates a negative statement.
# 
# Let's try once more with a more neutral sentence

# In[5]:


sentence = "I guess I'll eat pizza if you really want me to."
sia.polarity_scores(sentence)["compound"]


# The sentiment analyzer showed this sentence as `0.1513`, which is positve but close to 0, so indicates a slightly positive statement.
# 
# The Sentiment Intensity Analyzer is far from perfect, but we can use it some to try and find trends in social media posts.

# ### looping with sentiments
# If we want to look at trends over a series of sentences (or social media posts), we can use for loops.
# 
# So let's make an array of sentences and then do a loop to look at the sentiment of each sentence.

# In[6]:


# Make an array of movie reviews (each one a string)
movie_reviews = [
    "That movie was pretty good.",
    "I like the movie a lot!",
    "I thought the movie was boring",
    "I'd watch the movie again",
    "That sure was an exciting movie!"
]


# In[7]:


# loop through each review
for review in movie_reviews:
    # find the sentiment (compound polarity score) of the review
    review_sentiment = sia.polarity_scores(review)["compound"]
    
    # print out the sentiment and the original review
    print("Sentiment: " + str(review_sentiment))
    print("   Review: " + review)
    print() # print a blank line to space out each review sentiment printout


# We can now see at a glance the sentiments for each of our movie review sentences (and we can consider how accurate we think the sentiment scores are).
# 
# But what might be even more useful would be to do something like the average sentiment of all reviews, or what percentage were positive. 
# 
# In order to figure this out, we are going to make use of variables to track information while we are looping.
# 
# ## Loop Variables
# 
# First let's consider how to count the number of movie reviews in our list.
# 
# Python provides us an easy way of counting the how many movie reviews there were, by using the `len` function like this:

# In[8]:


len(movie_reviews)


# But we can also use a variable to keep track of how many reviews we've seen so far as we go through our loop. 
# 
# _Note: while this strategy requires more code than just doing `len(movie_reviews)`, it will build us to doing more complicate tracking as we loop_
# 
# ### loop count
# 
# We start by making a variable, which we will call `num_reviews` to track the number of reviews we've seen so far, and we'll set it to 0 since we haven't gone through any reviews yet.
# 
# Then as part of our loop, each time we go through a review we will add 1 to our `num_reviews` variable

# In[9]:


num_reviews = 0 # we haven't seen any reviews yet

for review in movie_reviews:
    # we're looking at a review, so add one to num_reviews
    num_reviews = num_reviews + 1
    print("we've now looked at " + str(num_reviews) + " reviews")
          
print("After the for, we see there were " + str(num_reviews) + " total reviews")


# We can rewrite the above code using a Python shorthand of `+=`, which means:
# - `num_reviews = num_reviews + 1`
# 
# can be rewritten as
# - `num_reviews += 1`

# In[10]:


num_reviews = 0 # we haven't seen any reviews yet

for review in movie_reviews:
    # we're looking at a review, so add one to num_reviews
    num_reviews += 1
    print("we've now looked at " + str(num_reviews) + " reviews")
          
print("After the for, we see there were " + str(num_reviews) + " total reviews")


# ### loop average
# Now let's loop through the list of reviews again, but this time try to find the average sentiment of all reviews.
# 
# To find the average of all the sentiments, we need to add all the sentiments together and then divide by the number of reviews. 
# 
# So what we will do is make another variable at the start of our loop called `total_sentiment` and each time we loop through a new review, we will add that review's sentiment to the `total_sentiment`. Then at the end, the average will be the `total_sentiment` divided by the `num_reviews`.

# In[11]:


num_reviews = 0 # we haven't seen any reviews yet
total_sentiment = 0 # we haven't seen any review sentiment yet

for review in movie_reviews:
    # we're looking at a review, so add one to num_reviews
    num_reviews += 1
    
    # find the sentiment (compound polarity score) of the review
    review_sentiment = sia.polarity_scores(review)["compound"]
    
    #add the current review sentiment to the total sentiment
    total_sentiment += review_sentiment

# now that the loop is done, the average_sentiment is 
#     the total_sentiment divided by the num_reviews
average_sentiment = total_sentiment / num_reviews

print("The average sentiment of the reviews was: " + str(average_sentiment))


# So that let us find the average sentiment of our reviews, which were generally positive.
# 
# We could also find out what percentage of reviews were positive by finding the number of reviews that had a sentiment bigger than 0, and then dividing by the total number of reviews and multiplying the answer by 100.
# 
# In this case we make a variable before the loop called `num_positive_reviews`, and add 1 to it whenever we find a review that is positive (using an `if` statement), like this:

# In[12]:


num_reviews = 0 # we haven't seen any reviews yet
num_positive_reviews = 0 # we haven't seen any positive reviews yet

for review in movie_reviews:
    # we're looking at a review, so add one to num_reviews
    num_reviews += 1
    
    # find the sentiment (compound polarity score) of the review
    review_sentiment = sia.polarity_scores(review)["compound"]
    
    # if the sentiment was positive (bigger than 0), add one to the num_positive_reviews
    if review_sentiment > 0:
        num_positive_reviews += 1

# now that the loop is done, the percentage of positive reviews is 
#     the num_positive_reviews divided by the num_reviews, and then multiplied by 100
precent_positive = num_positive_reviews / num_reviews * 100

print("The percentage of positive reviews was: " + str(precent_positive))

