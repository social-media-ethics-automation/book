# Who does data fit?
Because all data is a simplification of reality, those simplifications work well for some people and some situations, but can cause problems for other people and other situations.

Thus, when designers of social media systems make decisions about how data will be saved and what constraints will be put on the data, they are making decisions about who will get a better experience. Based on these decisions, some people will fit naturally into the data system, while others will have to put in extra work to make themselves fit, and others will have to modify themselves or misrepresent themselves to fit into the system.

So, for example, if we made a form that someone needed to enter their address, we could assume everyone is in the United States and not have any country selection.
- Address fields:
  - Street address
  - City
  - State
  - Zip Code

Someone in another country would have to try to find a way to indicate that they aren't in the United States even though there is no clear place to indicate that. If this is a form for shipping to people in the US only, then this limitation might make sense.

If we wanted people to be able to enter other countries we could make a country drop down tool to select a country, but then would we auto-fill it with a country? If there is a list of countries to scroll through, what order do we put them in? If it's alphbetical, that will make it easier for people in countries whose name starts with "A."


## Form fails
Let's look at some examples where forms show problems with data entry and representation:

### Name Length
Here are some screenshots from a [help forum discussion](https://ttlc.intuit.com/community/taxes/discussion/my-last-name-is-to-long-what-do-i-do/00/655670) on the United States tax software TurboTax:

![Screenshot from turbotax help forum. A user in 2019 has posted the question: "My last name is to long, what do I do?"](tax_name1.png)

![Screenshot from turbotax help forum. A user in 2019 has replied "You can fix that by removing the last letters that don't fit. The IRS matches the social security number with only the first few letters of the last name."](tax_name2.png)

![Screenshot from turbotax help forum. A user in 2020 has replied "Same thing for me. I end up filling by mail because it fails every time."](tax_name3.png)

As you can see, TurboTax has a limit on how long last names are allowed to be, and people with too long of names have different strategies with how to deal with not fitting in the system.

### Gender/Sexuality
% TODO: https://genders.wtf/
Data collection and storage can go wrong in other ways as well, with incorrect or erroneous options. Here are some screenshots from a thread of people collecting strange gender selection forms (the images link to the tweets I got them from if you want to see more in the twitter thread):

- [![Tweet from user "Coding Drag Queen Anna Lytical" with handle "@theannalytical". The tweet text is "send me the worst gender selection forms you've seen, I'll start" and the image is of a dropdown with the following options: Female, Male, N/A, Unknown, Tax Entity"](gender_select1.png)](https://twitter.com/theannalytical/status/1349392166716657664?s=20)

- [![image that says "ah yes, the three genders" and below it is a screenshot of a form that says "What is your gender? Please select one." and the options are: "Male", "Female", and "I have no plans to purchase a new vehicle"](gender_select2.png)](https://twitter.com/annabookwriter/status/1349410399574102016?s=20)

- [![A picture of a form (perhaps on paper?) that says "Sexual orientation: Please identify your sexual orientation:" and the options are: "Bisexual", "Gay man", "Gay woman/lesbian", "Chinese", "Heterosexual/straight", and "Other: Please describe:"](gender_select3.png)](https://twitter.com/324_B21/status/1349560223447408641?s=20)

- [![A gender dropdown selection box with the following options: "F", "M", "Male", "Female", "Famale", "Felmale", "High School visit on March 17", "Gender", "International High School Visit at Ho Chi Minh City at March 19"](gender_select4.png)](https://twitter.com/ValkyriePyra/status/1349477953978195970)
