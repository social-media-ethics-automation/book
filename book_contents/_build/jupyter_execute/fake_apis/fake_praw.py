#!/usr/bin/env python
# coding: utf-8

# # Fake Praw Library
# This library is intended to mimic praw so that the book demoes can be run without actually needing reddit credentials, and not actually posting to reddit

# In[1]:


from types import SimpleNamespace

class SimplishNamespace(SimpleNamespace):
    pass

setattr(SimplishNamespace, "__getitem__", lambda self, key: self.__dict__[key])

from IPython.display import HTML, Image, display
import html

import datetime



# In[2]:


def print_info(text):
    display(
        HTML(
            "<strong style='color:darkred'>" + 
            html.escape(text) + 
            "</strong>"
        )
    )


# In[3]:


print_info("Fake praw is replacing the praw library. Fake praw doesn't need real passwords, and prevents you from accessing real reddit")


# In[4]:


def print_tweet(text="", in_reply_to_tweet_id=0):
    print_info("Fake Tweepy is pretending to post this tweet (note: real tweepy shows no output here when a tweet is posted): ")
    print(text)
    if(in_reply_to_tweet_id > 0):
        print("Tweet in reply to: " + str(in_reply_to_tweet_id))


# In[5]:


def search_recent_tweets(query="", tweet_fields=[], expansions=[], media_fields=[], user_fields=[], next_token=None, max_results=10):
    print_info("Fake Tweepy is pretending to search for '"+query+"' and is returning some fake tweets.")
    if(query == '"cute cat"'):
        return SimpleNamespace(
          data = [
              SimpleNamespace(
                  text = "While trying to tweet right now, I am being attacked by my cute cat! It's so hard to tpye wihsaoae as fesadf asd fssasaf sa",
                  id = 129308937494,
                  author_id = 239048094385,
                  created_at = datetime.datetime(2022, 2, 22, 22, 22, 22, 0, datetime.timezone.utc),
                  lang = 'en',
                  source = 'Twitter for Android',
                  public_metrics = {
                      'retweet_count': 7,
                      'reply_count': 3,
                      'like_count': 6,
                      'quote_count': 2                  
                  }
              ),
              SimpleNamespace(
                  text = "I wish I could be sleeping now like my cute cat is!",
                  id = 93298432,
                  author_id = 23409023,
                  created_at = datetime.datetime(2022, 2, 22, 2, 2, 2, 0, datetime.timezone.utc),
                  lang = 'en',
                  source = 'Twitter for iPhone',
                  public_metrics = {
                      'retweet_count': 2,
                      'reply_count': 1,
                      'like_count': 5,
                      'quote_count': 3                  
                  }
              ),
              SimpleNamespace(
                  text = "Why won't my cute cat stop scratching my face in the morning!",
                  id = 321923,
                  author_id = 32892394,
                  created_at = datetime.datetime(2022, 2, 22, 3, 3, 3, 0, datetime.timezone.utc),
                  lang = 'en',
                  source = 'Twitter for iPhone',
                  public_metrics = {
                      'retweet_count': 3,
                      'reply_count': 4,
                      'like_count': 2,
                      'quote_count': 3                  
                  }
              )
          ]
        )
    if(query == "from:fake_celebrity"):
        return SimpleNamespace(
          data = [
              SimpleNamespace(
                  text = "Why is the line at the grocery store taking so long???",
                  id = 129308937494,
                  source = 'Twitter for iPhone'
              ),
              SimpleNamespace(
                  text = "Remember, my show tonight starts at 7:00pm!",
                  id = 93298432,
                  source = 'Fake Social Media Manager',
              ),
              SimpleNamespace(
                  text = "Hope all my followers are having a lovely day!",
                  id = 321923,
                  source = 'Fake Social Media Manager',
              )
          ]
        )
    if(query == "dog -is:retweet has:images"):
        return SimpleNamespace(
          includes = {
              "media": [
                   SimpleNamespace(
                      media_key = "7_4353463",
                      type = "photo",
                      height = 600,
                      width = 800,
                      alt_text = "Photo of a small dog lying flat on floor, looking exhausted",
                      url = "fake_website_photo1.jpg"
                  ),
                  SimpleNamespace(
                      media_key = "4_354354",
                      type = "photo",
                      height = 300,
                      width = 400,
                      alt_text = None,
                      url = "fake_website_photo2.jpg"
                  ),
                  SimpleNamespace(
                      media_key = "4_324654",
                      type = "photo",
                      height = 300,
                      width = 400,
                      alt_text = None,
                      url = "fake_website_photo3.jpg"
                  ),
                  SimpleNamespace(
                      media_key = "5_45353",
                      type = "photo",
                      height = 1200,
                      width = 1024,
                      alt_text = "photo taken by fake user 2",
                      url = "fake_website_photo4.jpg"
                  )
              ],
              "users": [
                  SimpleNamespace(
                      id = 213412413,
                      name = "Fake User 1",
                      username = "fakeuser1",
                      profile_image_url = "fake_profile_image1.jpg"
                  ),
                  SimpleNamespace(
                      id = 309453565,
                      name = "Fake User 2",
                      username = "fakeuser2",
                      profile_image_url = "fake_profile_image2.jpg"
                  )
              ]
          },
          data = [
              SimpleNamespace(
                  text = "Look at my cute dog!",
                  id = 2342352355,
                  author_id = 213412413,
                  data = { "attachments": {
                      "media_keys": ["7_4353463"]
                  } }
              ),
              SimpleNamespace(
                  text = "check out these dog photos",
                  id = 93298432,
                  author_id = 309453565,
                  data = { "attachments": {
                      "media_keys": ["4_354354", "4_324654"]
                  } }
              ),
              SimpleNamespace(
                  text = "lol silly dog!",
                  id = 43954354,
                  author_id = 309453565,
                  data = { "attachments": {
                      "media_keys": ["5_45353"]
                  } }
              )
          ]
        )
    if(query == "from:fake_news_site"):
        return SimpleNamespace(
          data = [
              SimpleNamespace(
                  text = "Breaking news: A lovely cat took a nice long nap today!",
                  id = 129308937494
              ),
              SimpleNamespace(
                  text = "Breaking news: Someone said a really mean thing on the internet today!",
                  id = 93298432
              ),
            SimpleNamespace(
                  text = "Breaking news: Some grandparents made some yummy cookies for all the kids to share!",
                  id = 93298432
              ),
              SimpleNamespace(
                  text = "Breaking news: All the horrors of the universe revealed at last!",
                  id = 321923
              )
          ]
        )
    if(query == "conversation_id:1234567" and next_token is None):
        return SimpleNamespace(
          data = [
              SimpleNamespace(
                  id = 24345,
                  data = {
                      "id": 24345,
                      "text": "It sure was hard, what score did you get?",
                      "author_id": 1093458,
                      "public_metrics": {'retweet_count': 4, 'reply_count': 2, 'like_count': 3, 'quote_count': 2}
                  },
                  referenced_tweets = [SimpleNamespace(
                      type = "replied_to",
                      id = 98778587
                  )]
              ),
              SimpleNamespace(
                  id = 434543,
                  data = {
                      "id": 434543,
                      "text": "I got a 67% :(",
                      "author_id": 123456789,
                      "public_metrics": {'retweet_count': 0, 'reply_count': 0, 'like_count': 2, 'quote_count': 0}
                  },
                  referenced_tweets = [SimpleNamespace(
                      type = "replied_to",
                      id = 24345
                  )]
              ),
              SimpleNamespace(
                  id = 3496834,
                  data = {
                      "id": 3496834,
                      "text": "I got a 73%",
                      "author_id": 943534,
                      "public_metrics": {'retweet_count': 0, 'reply_count': 0, 'like_count': 3, 'quote_count': 0}
                  },
                  referenced_tweets = [SimpleNamespace(
                      type = "replied_to",
                      id = 24345
                  )]
              ),
              SimpleNamespace(
                  id = 267445,
                  data = {
                      "id": 267445,
                      "text": "I didn't think it was that bad",
                      "author_id": 745769364,
                      "public_metrics": {'retweet_count': 1, 'reply_count': 2, 'like_count': 1, 'quote_count': 6}
                  },
                  referenced_tweets = [SimpleNamespace(
                      type = "replied_to",
                      id = 98778587
                  )]
              ),
              SimpleNamespace(
                  id = 32124,
                  data = {
                      "id": 32124,
                      "text": "how was that not a super hard exam?",
                      "author_id": 945356,
                      "public_metrics": {'retweet_count': 2, 'reply_count': 0, 'like_count': 8, 'quote_count': 2}
                  },
                  referenced_tweets = [SimpleNamespace(
                      type = "replied_to",
                      id = 267445
                  )]
              ),
              SimpleNamespace(
                  id = 34546,
                  data = {
                      "id": 34546,
                      "text": "of coure you didn't",
                      "author_id": 123456789,
                      "public_metrics": {'retweet_count': 1, 'reply_count': 1, 'like_count': 6, 'quote_count': 1}
                  },
                  referenced_tweets = [SimpleNamespace(
                      type = "replied_to",
                      id = 267445
                  )]
              ),
              SimpleNamespace(
                  id = 4354,
                  data = {
                      "id": 4354,
                      "text": "what's that supposed to mean?",
                      "author_id": 745769364,
                      "public_metrics": {'retweet_count': 0, 'reply_count': 1, 'like_count': 1, 'quote_count': 0}
                  },
                  referenced_tweets = [SimpleNamespace(
                      type = "replied_to",
                      id = 34546
                  )]
              ),
              SimpleNamespace(
                  id = 57533,
                  data = {
                      "id": 57533,
                      "text": "you're an overachiever",
                      "author_id": 123456789,
                      "public_metrics": {'retweet_count': 0, 'reply_count': 1, 'like_count': 3, 'quote_count': 0}
                  },
                  referenced_tweets = [SimpleNamespace(
                      type = "replied_to",
                      id = 4354
                  )]
              ),
              SimpleNamespace(
                  id = 67644,
                  data = {
                      "id": 67644,
                      "text": "and that's bad how?",
                      "author_id": 745769364,
                      "public_metrics": {'retweet_count': 0, 'reply_count': 0, 'like_count': 0, 'quote_count': 0}
                  },
                  referenced_tweets = [SimpleNamespace(
                      type = "replied_to",
                      id = 57533
                  )]
              )
          ],
          meta = {},
          includes = {
            "users": [SimplishNamespace(
                    id = 123456789,
                    data = {
                        "name": "Fake User",
                        "username": "fake_user" 
                    }
                ),SimplishNamespace(
                    id= 1093458, 
                    data= {
                        "name": "Unreal User",
                        "username": "unreal_user"
                    }
                ), SimplishNamespace(
                    id = 943534, 
                    data= {
                        "name": "Imaginary User",
                        "username": "imaginary_user"
                    }
                ), SimplishNamespace(
                    id = 945356,
                    data= {
                        "name": "False User",
                        "username": "false_user"
                    }
                ), SimplishNamespace(
                    id = 745769364,
                    data= {
                        "name": "Pretend User",
                        "username": "pretend_user"
                    }
                )
            ]
          }
        )
        


# In[6]:


def get_user(id="", username="", user_auth=False):
    if(id == "me" or username=="fake_user"):
        return SimpleNamespace(
            data = SimpleNamespace(
                id = 123456789,
                username = "fake_user"
            )
        )


# In[7]:


def get_tweet(tweetId, tweet_fields=[], expansions=[]):
    if(tweetId == 98778587):
        return SimpleNamespace(
            data = SimplishNamespace(
                id = 98778587,
                author_id = 123456789,
                text = "That last exam in sure was hard!",
                conversation_id = 1234567,
                username = "fake_user",
                public_metrics= {'retweet_count': 10, 'reply_count': 2, 'like_count': 8, 'quote_count': 4},
                referenced_tweets = [],
                __getitem__ = lambda self, key: 123456789 if key == "author_id" else None 
            ),
            includes = {
                "users": [SimplishNamespace(
                    id = 123456789,
                    data = {
                        "name": "Fake User",
                        "username": "fake_user" 
                    }
                )]
            }
        )


# In[8]:


mentions_counter = 0

def get_users_mentions(id=0):
    global mentions_counter
    if(id == 123456789):
        mentions_counter += 1
        if(mentions_counter == 1):
            return SimpleNamespace(
              data = [
                  SimpleNamespace(
                      text = "Hi @fake_user, please jump",
                      id = 232434,
                  )
              ]
            )
        elif(mentions_counter == 2):
            return SimpleNamespace(
              data = [
                  SimpleNamespace(
                      text = "Hi @fake_user, please do something horrible!",
                      id = 234356,
                  )
              ]
            )
        elif(mentions_counter == 3):
            return SimpleNamespace(
              data = [
                  SimpleNamespace(
                      text = "Hi @fake_user, please fly",
                      id = 245454,
                  )
              ]
            )
        elif(mentions_counter == 4):
            return SimpleNamespace(
              data = [
                  SimpleNamespace(
                      text = "Hi @fake_user, please do something horrible!",
                      id = 245454,
                  )
              ]
            )
        elif(mentions_counter == 5):
            return SimpleNamespace(
              data = [
                  SimpleNamespace(
                      text = "Hi @fake_user, please stop talking. But that doesn't mean I won't say horrible things like: I hate everybody!",
                      id = 245454,
                  )
              ]
            )


# In[9]:


def get_users_following(id="", max_results=5):
    if(id==123456789): # fake user
        return SimpleNamespace(
            data = [SimpleNamespace(id = 1093458, username = "unreal_user"),
                    SimpleNamespace(id = 943534, username = "imaginary_user"),
                    SimpleNamespace(id = 945356, username = "false_user")
                   ]
        )
    if(id==1093458): # unreal_user
        return SimpleNamespace(
            data = [SimpleNamespace(id = 435364, username = "great_user"),
                    SimpleNamespace(id = 785645, username = "awesome_user"),
                   ]
        )
    if(id==943534): # imaginary_user
        return SimpleNamespace(
            data = [SimpleNamespace(id = 563463, username = "ok_user"),
                    SimpleNamespace(id = 943534, username = "awesome_user"),
                   ]
        )
    if(id==945356): # false_user
        return SimpleNamespace(
            data = [SimpleNamespace(id = 435364, username = "great_user"),
                    SimpleNamespace(id = 943534, username = "awesome_user"),
                    SimpleNamespace(id = 435345, username = "mediocre_user"),
                    SimpleNamespace(id = 436775, username = "another_user"),
                   ]
        )


# In[10]:


class MessageSimpleNamespace(SimpleNamespace):
    def reply(self, text):
        print_info("Fake praw is pretending to reply to a message with: "+ text)
    pass


mentions_counter = 0

def inbox_messages(limit=1):
    global mentions_counter
    mentions_counter += 1
    if(mentions_counter == 1):
        message = (MessageSimpleNamespace(
          subject = "Wanting bot response",
          body = "I want you to jump"
        ),)
        return iter(message)
    elif(mentions_counter == 2):
        message = (MessageSimpleNamespace(
          subject = "Wanting bot response",
          body = "I want you to do something horrible!"
        ),)
        return iter(message)
    elif(mentions_counter == 3):
        message = (MessageSimpleNamespace(
          subject = "Wanting bot response",
          body = "I want you to fly"
        ),)
        return iter(message)
    elif(mentions_counter == 4):
        message = (MessageSimpleNamespace(
          subject = "Wanting bot response",
          body = "I want you to do something horrible!"
        ),)
        return iter(message)
    elif(mentions_counter == 5):
        message = (MessageSimpleNamespace(
          subject = "Wanting bot response",
          body = "I want you to stop talking. But that doesn't mean I won't say horrible things like: I hate everybody!"
        ),)
        return iter(message)


# In[11]:


class AuthorSimplishNamespace(SimplishNamespace):
    def __str__(self):
        return self.name
    pass

def hot(limit=10):
    submission_list = [
        SimpleNamespace(
            id = "904tjwdf093j",
            title = "Look at my cute dog!", 
            author = AuthorSimplishNamespace(
                name="fake_user",
                link_karma= 10,
                comment_karma= 50,
                has_verified_email = True,
                is_mod = False,
                is_gold = False                
            ),
            edited = False,
            created_utc = 1673327625,
            score = 23,
            upvote_ratio = .93,
            num_comments = 7,
            selftext = "",
            url = "example.com/fake_image.jpg"
        ),
        SimpleNamespace(
            id = "lk457j2l63",
            title = "A baby lizard!", 
            author = AuthorSimplishNamespace(
                name="pretend_user",
                link_karma= 25,
                comment_karma= 15,
                has_verified_email = True,
                is_mod = True,
                is_gold = False    
            ),
            edited = True,
            created_utc = 1673317625,
            score = 10,
            upvote_ratio = .5,
            num_comments = 1,
            selftext = "",
            url = "example.com/pretend_image.jpg"
        ),
        SimpleNamespace(
            id = "oiu45kje",
            title = "The cutest bird ever!", 
            author = AuthorSimplishNamespace(
                name="imaginary_user",
                link_karma= 3,
                comment_karma= 7,
                has_verified_email = True,
                is_mod = True,
                is_gold = True    
            ),
            edited = False,
            created_utc = 1673307625,
            score = 30,
            upvote_ratio = .9,
            num_comments = 10,
            selftext = "",
            url = "example.com/imaginary_image.jpg"
        ),
    ]
    return iter(submission_list)


# In[12]:


def submit(title, selftext=""):
    print_info("Fake praw is pretending to submit a post with the title: \""+title+"\" and the content: "+ selftext)


# In[13]:


def subreddit(subreddit_name):
    print_info("Fake praw is pretending to select the subreddit: " + str(subreddit_name))
    return SimpleNamespace(
      submit = submit,
      hot = hot
    )


# 

# In[14]:


def client_creator(username="", password="", client_id="", client_secret="", user_agent="" ):
    print_info("Fake praw is pretending to collect account info to use on reddit")
    return SimpleNamespace(
      subreddit = subreddit,
      inbox = SimpleNamespace(
          messages = inbox_messages
      )
    )


# In[15]:


praw = SimpleNamespace(
    Reddit = client_creator
)

