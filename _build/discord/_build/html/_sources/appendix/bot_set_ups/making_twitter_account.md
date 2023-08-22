# Making a Twitter Bot Account

In using this textbook, you will have opportunities to create and run twitter bots on your own twitter account.

While we have made a fake version of Twitter for you to test all the code in this book, we highly encourage you to make a twitter bot account and try it out for real!

## Sign up for Twitter
[https://twitter.com/signup](https://twitter.com/signup)

You might want to make a new twitter account, just for making twitter bots, since you don't want to accidentally get your main twitter account banned or labeled as a bot.

Note: If you want to make a new account and you already have one, you may need to sign out from your current account, or use a different web browser (e.g., Mozilla, Google Chrome, Microsoft Edge, Safari).

## Sign up for "developer access" (bot permisson)
Now that you have a twitter account, you need to get permission to use it as a bot. This is called "developer access." The fastest way of doing this is to sign up for
"Essential access," so go here to sign up for essential accesss:
[https://developer.twitter.com/en/portal/petition/essential/basic-info](https://developer.twitter.com/en/portal/petition/essential/basic-info)

```{figure} twitter_developer_signup.png
---
name: twitter_developer_signup_fig
width: 400px
alt: "A screenshot of the essential access form, with country set as United States, Use Case set as Student, and will twitter content be made available to a government set to No."
---
```

Note when filling this out, that the information button on the question about sharing data with a government says that a government funded university doesn't count.

## Get special "bot" passwords
Once you have developer access, you'll need a set of 5 special passwords to be able to make a fully functional Twitter bot:
- Bearer Token
- Consumer Key (aka "API Key")
- Consumer Secret (aka "API Key Secret")
- Access Token
- Access Token Secret

You'll want to get all of these and then save them somewhere so that you can find them again (e.g., send yourself an email).

In order to get these 5 special passwords, do the following:

Go to the twitter developer portal (https://developer.twitter.com/en/portal)

In Projects & Apps, press “Add App” (note in my screenshot I already have an app added).

```{figure} twitter_add_app.png
---
name: twitter_add_app_fig
alt: A screenshot of the projects and apps view, with the "Add App" button circled
---
```


For the App Environment, select production

```{figure} twitter_production_environment.png
---
name: twitter_production_environment_fig
width: 300px
alt: A screenshot of the "Choose an App Environment" view, with production circled
---
```

Then choose whatever name you want for this “project,” for example “testbotkylethayer”


Now save these keys somewhere on your computer. Later, when you write Twitter bots:
- “API Key” will be called “consumer_key”
- “API Key Secret” will be called “consumer_secret”
- “Bearer Token” will be called “bearer_token”

```{figure} twitter_API_keys.png
---
name: twitter_API_keys_fig
width: 500px
alt: A screenshot of the "Keys and Tokens" view, showing the API Key labeled "consumer_key", the API Key Secret labled "consumer_secret", and the Bearer Token labled "bearer_token"
---
```

Then go to the app settings for your project:
```{figure} twitter_app_settings.png
---
name: twitter_app_settings_fig
width: 300px
alt: A screenshot of the "Keys and Tokens" view, but with the "App Settings" button circled
---
```




Under User Authentication Settings, click “Set-Up”
```{figure} twitter_set_up_auth.png
---
name: twitter_set_up_auth_fig
width: 500px
alt: A screenshot of the overview page for the prod project, with the "Set-Up" button circled
---
```


Enable both OAuth 2.0 and OAuth 1.0a and set your app type to “automated App or bot”:
Note: (I am guessing you don’t need OAuth 2, but we’ll turn it on just in case)
```{figure} twitter_oath_setup.png
---
name: twitter_oath_setup_fig
width: 400px
alt: A screenshot of the User authentication settings view, with OAuth 2.0 and OAth 1.0a enabled. For OAuth 2.0 Settings, the Type of App is selected to be "Automated App or bot"
---
```


Then Set OAuth 1 settings to allow read and write and direct message, and if it requires “Callback URI / Redirect URL” and “Website URL”, those can be anything, and just put “http://uw.edu”
```{figure} twitter_oath_1_settings.png
---
name: twitter_oath_1_settings_fig
width: 400px
alt: A screenshot of the OAuth 1.0A Settings view, With App permissions set to "Read and write and Direct message", the Callback URI to "http://uw.edu" and the Website URL to "http://uw.edu"
---
```


Save your settings. You will be given a Oath2.0 Client ID and Client Secret. I don’t think you need these, but save them somewhere on your computer just in case


Now, in your app settings, press “Keys and tokens”
```{figure} twitter_keys_and_tokens.png
---
name: twitter_keys_and_tokens_fig
width: 600px
alt: A screenshot of the overview page for the prod project, with the "Keys and tokens" tab cicled
---
```

And press “Generate” for “Access Token and Secret”
```{figure} twitter_generate_access_tokens.png
---
name: twitter_generate_access_tokens_fig
width: 500px
alt: A screenshot of the keys and tokens tab for the prod project. There are generate (or regenerate) buttons for API Key and Secret, Bearer Token, and Access Token and Secret. The last one of these (Access Token and Secret) has the generate button circled.
---
```



Now save these keys, both somewhere on your computer. Later, when you write Twitter bots:
- “Access Token” will be called “access_token”
- “Access Token Secret” will be called “access_token_secret”

```{figure} twitter_access_tokens.png
---
name: twitter_access_tokens_fig
width: 500px
alt: A screenshot of the "Sva your new Access Token and Access Token Secret" popup, showing the "Access Token" labeled "access_token", and the "Access Token Secret" labeled "access_token_secret"
---
```

Note: If you ever lose these special passwords, or accidentally share them, you can regenerate them.

##  Test your keys
When you get to chapter 2.3.8 ([](../ch02_definitions/03_automation/08_demo.ipynb)), you can try running the code and replacing the fake special passwords with the ones from your account, and see if you can use the code to post an actual tweet to your account.

## Understand Twitters Rules for Bots
Before you try doing anything too creative with twitter bots, make sure you look over [Twitters Policy on what you are allowed to do](https://help.twitter.com/en/rules-and-policies/twitter-automation), that way you don't get yourself banned.
