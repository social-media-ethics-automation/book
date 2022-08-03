#!/usr/bin/env python
# coding: utf-8

# # A3: Political Bias
# In this assignment, you will be trying to calcualate the political bias and reliability of tweets in tweet searches. 
# 
# To do this, you will use some website bias and reliability ratings based on the Media Bias Chart (https://adfontesmedia.com/static-mbc). When you find tweets that link to a website, if you have a rating for it you will find the bias and reliability ratings, and at the end you will report the average bias and average reliability of the tweets in your search.
# 
# There are, of course, many problems with trying to calculate political bias and reliability in this way, which you will answer questions about after the programming section of the assignment.
# 
# In the programming portion, there are many pieces already created for you, but there are labeled sections where you will have to write the code yourself.

# ### Our usual twitter set-up code:

# In[1]:


# make sure tweepy library is installed
get_ipython().system('pip install tweepy')
import tweepy


# In[2]:


# load my twitter keys
import my_bot_keys


# In[3]:


# log into tweepy
client = tweepy.Client(
    bearer_token=my_bot_keys.bearer_token,
    consumer_key=my_bot_keys.consumer_key, consumer_secret=my_bot_keys.consumer_secret,                   
    access_token=my_bot_keys.access_token, access_token_secret=my_bot_keys.access_token_secret
)


# ### Install libraries for handling website urls and for loading csvs
# You will need `URLExtract` and `urllib3` to find website urls in tweet text, and turn shortened urls (like https://bit.ly/3gE1Nsl) into the full urls where you can tell what news organization (if any) it points to.
# 
# You will also need `pandas` to load the csv data file of media website bias and reliability

# In[4]:


get_ipython().system('pip install URLExtract')
get_ipython().system('pip install urllib3')
from urlextract import URLExtract
import urllib.request as urlreq
extractor = URLExtract()
import pandas as pd


# ### Load the media site info
# Our measure of media website bias and reliability is based on the Media Bias Chart 9.0 (https://adfontesmedia.com/static-mbc)
# 
# I have made a csv (comma separated varaible) file with some of the sites shown on that chart. I made my own simplification based on the grid in the graphic with bias ranging from -4 to +4, and reliability from -4 to +2 as follows:
# ![Media bias chart with grid, showing the range labels](./bias_chart_divisions.jpg)
# 
# These are saved in the file `media_info.csv`, where each row of text is the info for one media site. For example:
# `wsws.org,-3,-1`
# Means that the site wsws.org has a bias of -3 (Hyper-Partisan Left) and a reliability of -1 (Opinion OR High Variation in Reliability). 
# 
# If you want to modify the `media_info.csv` file, you can open it by right-clicking and selecting Open With -> Editor. You can then modify entries, or add new ones for more sites (like from the interactive media bias chart here: https://adfontesmedia.com/interactive-media-bias-chart/). Then save it and rerun this code and the code below.
# 
# ![Show context menues for right clicking the csv file, then choosing Open With, then choosing Editor](./open_csv_editor.jpg)
# 
# 

# In[ ]:


media_info_df = pd.read_csv('media_info.csv')


# ### Now reorganize the information for easier use
# Get a list of just the media websites in the variable `media_sites`
# 
# Make a dictionary where you can look up the bias for a site in the variable `media_bias_lookup`
# 
# Make a dictionary where you can look up the reliability for a site in the variable `media_reliability_lookup`

# In[ ]:


media_sites = media_info_df['site']

media_bias_lookup = {m_info['site']: m_info['bias'] for i, m_info in media_info_df.iterrows()}
media_reliability_lookup = {m_info['site']: m_info['reliability'] for i, m_info in media_info_df.iterrows()}


# ### Demo of looking up media site info
# This is a demo of how to get information from the variables from the code above. You will need to access this info yourself below

# In[ ]:


# media_sites has a list of sites to look for in the tweets
# you can loop through them like this
for site in media_sites:
    print(site, end=', ')

print()

# media_bias_lookup lets you look up the bias for a site from the media_sites list
print(media_bias_lookup["pbs.org"])

# media_reliability_lookup lets you look up the reliability for a site from the media_sites list
print(media_reliability_lookup["pbs.org"])


# ### Utility functions: find all the urls in the text, and turn shortened urls into full urls
# 
# The function `follow_url_redirects` takes a potentially shortened url (like https://bit.ly/3gE1Nsl), and turns it into the full url with the news site. Note: You do not need to use this function directly.
# 
# The function `find_expanded_urls` takes a piece of text that has urls in it, and returns a list of the expanded version of all those urls. Note: You **will** have to use this function.

# In[ ]:


import requests
def follow_url_redirects(url):
    still_redirecting = True
    new_url = url
    status_code = 301
    num_tries = 0
    while still_redirecting and num_tries < 4:
        try:
            r = requests.get(new_url, allow_redirects=False, timeout=1)
            status_code = r.status_code
            if 'Location' in r.headers: 
                new_url = r.headers['Location']
            if status_code == 301 and 'Location' in r.headers:
                still_redirecting = True
            else:
                still_redirecting = False
        except BaseException as err:
            print("-- Warning: could not load url: " + url + ", err: " + str(err))
            still_redirecting = False
        
    return new_url

def find_expanded_urls(piece_of_text):
    urls = extractor.find_urls(piece_of_text)
    fullURLs = []
    for url in urls:
        fullURL = follow_url_redirects(url)
        fullURLs.append(fullURL)
    return fullURLs


# ### Demo of how to use the function `find_expanded_urls`

# In[ ]:


urls = find_expanded_urls("An article on misuse of facial recognition https://bit.ly/3gE1Nsl. a documentary on bias and algorithms: https://bit.ly/3Lr0Xx7")

for url in urls:
    print(url)


# # Your Code!
# ### Create functions to look up bias an reliability for a website
# You need to create two functions: `find_bias` and `find_reliability`
# 
# Note: These two functions should look very similar. 
# 
# * They should each take as an argument a url. 
# * They should then do a for loop over all the sites in the `media_sites` list. 
#     * If that site string (e.g., "reuters.com") appears in the given url string (e.g, "https://www.reuters.com/lifestyle/sports/..."), then the function should return the bias or reliability for that site in the `media_bias_lookup`/`media_reliability_lookup` dictionary. 
# * If none of the media_sites sites is found in the url, then no need to do anything as the function will by default return "None".
# 
# Suggestion: write the code first not in a function, and then turn it into a function at the end

# In[ ]:


#TODO: Your code here!


# ### Test your code for find_bias and find_reliability

# In[ ]:


# youtube isn't in the list, so should return None for bias
print(find_bias("https://www.youtube.com/watch?v=JTfhYyTuT44"))

# reuters should return -1 for bias
print(find_bias("https://www.reuters.com/lifestyle/sports/alpine-skiing-womens-downhill-pushed-back-by-least-30-mins-due-wind-2022-02-15/"))

# reuters should return 2 for reliability
print(find_reliability("https://www.reuters.com/lifestyle/sports/alpine-skiing-womens-downhill-pushed-back-by-least-30-mins-due-wind-2022-02-15/"))


# # Your Code!
# ### Create a function that, for a given query, displays the average bias and reliability for sites linked to from the found tweets
# 
# Create a function `find_twitter_bias_and_reliability` that takes a query and optionally max_results (by default 10). You can also make an optional `show_progress` argument as well if you want (see lecture 12 demo).
# 
# What your function should do: 
# 
# Do a twitter search (you can do our normal `search_recent_tweets`, or if you want, you can experiment with `search_all_tweets`).
# 
# Create some variables to track the total number of links you were able to evaluate for bias/reliabilty, and the total sum of the bias and the total sum of the reliability you encounter with those links.
# 
# Next loop through all the tweets in your search.
# 
# For each tweet, use the `find_expanded_urls` function to get all the expanded urls in the tweet. Also, print the tweet text/link.
# 
# For each url in those urls:
# * try to find the bias and the reliability of the url (using your `find_bias` and `find_reliability`)
# * If you were able to find the bias and reliability
#   * add to the count of urls you were able to evaluate
#   * add the bias to the total bias you found from links
#   * add the reliability to the total reliability found from your links
#   * Also, print the url and the bias/responsibility info
# * If you were not able to find the bias and reliability
#   * Print the url and say you weren't able to evaluate it.
#   
# After all of that, print out the total number of urls you were able to evaluate.
# 
# If you were able to evaluate at least 1 url, then print out the average bias and average reliability for all the urls in your search.

# In[ ]:


#TODO: Your code here!


# ### Test of your code 
# This should test your code with a search for "senate," making sure it has a link to some website, that it doesn't link to twitter (many tweets refer to other tweets), and that it isn't a retweet. Also, have it request 100 tweets.

# In[ ]:


query = 'senate has:links -is:retweet -url:twitter.com'
find_twitter_bias_and_reliability(query, max_results=100)


# # Your Code!
# Do three more searches of your own choosing which give at least some urls that your code can evaluate. 
# 
# You can search for different news topics, political figures, or other interests. You can also search for tweets from a particular user (though if you are using search_recent_tweets, it only gets their tweets from the last 7 days)
# 
# You can also try searching for phrases used specifically by different groups. For example, if you want searches that are more likely to turn up unreliable or conspiracy theory sites, you can try searches like: 
# * Soros 
# * "covid cult" 
# * #Censorship 
# * shitlibs
# 
# You can do other modifications to your search as well (like restricting more websites in the search than just twitter.com).
# 
# After each search there are some questions to answer. And some final reflection questions at the end as well.

# In[ ]:


# TODO: Search 1 code here


# ### Search 1 follow-up questions

# Write at least 2 sentences in response to each of these questions (you can edit this text):
# 
# * Looking at your calculated average bias and reliability, and skimming through the tweets, how well do you think those averages represent the tweets in the search?
# 
# * Are there particular sites that showed up a lot that your program wasn't able to find bias/reliability websites for? How hard do you think it would be to evaluate those sites too?

# In[ ]:


# TODO: Search 2 code here


# ### Search 2 follow-up questions

# Write at least 2 sentences in response to each of these questions (you can edit this text):
# 
# * Looking at your calculated average bias and reliability, and skimming through the tweets, how well do you think those averages represent the tweets in the search?
# 
# * Are there particular sites that showed up a lot that your program wasn't able to find bias/reliability websites for? How hard do you think it would be to evaluate those sites too?

# In[ ]:


# TODO: Search 3 code here


# ### Search 3 follow-up questions

# Write at least 2 sentences in response to each of these questions (you can edit this text):
# 
# * Looking at your calculated average bias and reliability, and skimming through the tweets, how well do you think those averages represent the tweets in the search?
# 
# * Are there particular sites that showed up a lot that your program wasn't able to find bias/reliability websites for? How hard do you think it would be to evaluate those sites too?

# ### Final Reflection questions

# Write at least 2 sentences in response to each of these questions (you can edit this text):
# 
# * In what ways do you feel like the info from the Media Bias Chart works well?
# 
# * In what ways do you feel like the info from the Media Bias Chart works poorly?
# 
# * If you could redesign the Media Bias Chart, what would you want to do (e.g., add some other dimension besides just bias/responsibility, change how it is evaluated, add more news sources, consider different countries)?
# 
# * If you were able to run your `find_twitter_bias_and_reliability` function on the whole history of a twitter user (e.g, thousands of tweets), how accurately do you think you'd be able to judge that users' political views and susceptibility to consipracy theories?
# 
# * What might a social media company or an advertizer (including political campaigns) want to do with information on a users' political views and susceptibility to consipracy theories?
