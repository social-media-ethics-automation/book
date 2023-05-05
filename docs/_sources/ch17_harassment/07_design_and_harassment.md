# Design Example: Quoting

% TODO: change file name


## Quote Tweets

The way social media sites are designed can encourage and discourage different forms of harassment.

For example, people have made complaints about how [Quote Tweets Have Turned Us All Into Jerks](https://onezero.medium.com/quote-tweets-have-turned-us-all-into-jerks-d5776c807942). And the way that even trying to defend people can increase the harassment they face. One of the arguments is that by allowing quote Tweets, users will find a Tweet they disagree with, and quote the Tweet with a joke, insult, or comment to show how bad the original Tweet was ("dunking"). Then the original Tweet will spread through communities who disagree with it, all trying to do their own version of their best dunk or insult. As it spreads, some users may turn to other means of harassment, like direct messaging threats, or doxing the original Tweeter. Katherine Cross argues in [It's Not Your Fault You're a Jerk on Twitter: The design of the internet lets you harass and harm people without ever once interacting with them directly. Even if you're trying to defend them.](https://www.wired.com/story/social-media-harassment-platforms/) that even people jumping in to defend the original Tweet may only cause it to go more viral and get even more negative attention. 


% Story: Neighbor Chili
% original Tweet: https://twitter.com/Chinchillazllla/status/1591921147611856901
% Author info: https://twitter.com/Chinchillazllla, https://twitter.com/KuneKuneRufus, https://www.patreon.com/RufusTheKunekune?fan_landing=true
% Might not want to be part of another story... "you all discoursed me into the fucking Washington Post against my will."
% chili_ images
% The people who complained then got dogpiled themselves. People involved deleted or temporarily deactivated their accounts. Yay! Healthy discourse!
% sources https://cheezburger.com/18473221/woman-cooks-for-neighbors-insults-weirdos-on-the-internet
% https://www.washingtonpost.com/food/2022/11/18/chili-neighbors-twitter-etiquette/
%   archive copy: https://web.archive.org/web/20221121094327/https://www.washingtonpost.com/food/2022/11/18/chili-neighbors-twitter-etiquette/

In 2019 [Twitter began considering how to measure "health" of interactions](https://www.vox.com/2019/3/8/18245536/exclusive-twitter-healthy-conversations-dunking-research-product-incentives) on the platform and figure out how to optimize their platform for healthier interactions. In 2020 [Twitter began giving users a warning before posting something that it's algorithm guessed could be offensive](https://www.theverge.com/2020/5/5/21248201/twitter-reply-warning-harmful-language-revise-tweet-moderation), and [made further updates in 2021](https://www.theverge.com/2021/5/5/22420586/twitter-offensive-tweet-warning-prompt-updated-success-rate).


## Mastodon
When creating the Twitter-like social media protocol Mastodon, its creator, Eugen Rochko, decided not to allow quote-tweet like posts:

> I've made a deliberate choice against a quoting feature because it inevitably adds toxicity to people's behaviours. You are tempted to quote when you should be replying, and so you speak at your audience instead of with the person you are talking to. It becomes performative. Even when doing it for "good" like ridiculing awful comments, you are giving awful comments more eyeballs that way. No quote toots. Thank's
>
> [Eugen](https://mastodon.social/@Gargron/99662106175542726) in 2018

But others have argued that design decisions and community decisions made on Mastodon, such as no quotes (as well as their content-warning system) have made it more outwardly polite. But they also complain that this has made the platform very white, hostile to people of color talking about experiences of racism, and difficult to make a social movement. When masses of Twitter users migrated to Mastodon following Elon Musk's purchase of Twitter in the fall of 2022, there was renewed discussion:

[@mekkaokereke@mastodon.cloud questions](https://mastodon.cloud/@mekkaokereke/109334079258663352):
> Is it possible to drive social change through Mastodon? Could "Black Lives Matter" have happened on Mastodon? Or do the "intentionally slow, pleasant conversation" features eliminate the possibility of this? Do the "interest silo" tendencies discourage cross pollination?
>
> [...]
>
> I know that we can have more pleasant interactions on Mastodon than on Twitter. I already feel it.
>
> What I'm unsure of, is if that means giving up on the capacity for social change. Are we Lotus eating?


And [Dr. Jonathan Flowers argues](https://zirk.us/@shengokai/109347027270208314):
> The quote tweet function in conjunction with the hashtag are what allow users to align with communities, and communities with conversations through how they enable cultural practices by means of a digital environment.
>
> On Black Twitter, the quote tweet and hashtag enable what Black cultural scholars call "call and response," something crucial to Black community practices. The hashtags curate the conversation and allow for its visibility.

(See also an interview with Dr. Jonathan Flowers on [The Whiteness of Mastodon](https://techpolicy.press/the-whiteness-of-mastodon/))


Writer [Leslie Ye argued](https://twitter.com/lesliezye/status/1593631667037638660) about some of the advantages of what Twitter:
> many of us have spent our lives observing institutional power from the outside, how power behaves, how power acts, when confronted when communities like ours who are actually able to HOLD power to account, connect the dots across expertises and specialties
>
> [...]
>
> [Twitter] is a place where we have direct access to the most powerful and can hold them to account


Professor John R. Marks, IV argued that the [spread of negative content was actually a good thing on Twitter](https://mastodon.social/@jrm4/109702486481162255 ).
> Here's the thing:
>
> Twitter's ability to rapidly spread objectionable and distressing content is (was?) the *best* thing about it, not the worst, see e.g. police brutality.
>
> It's not pleasant, but long run it's more valuable than "nuanced / moderated conversation," which you can get elsewhere.
>
> This is more-or-less what is wrong with how many -- if not *most* -- picture #mastodon. and the #fediverse 
>
> #blackmastodon #blackfedi

<br>

```{figure} this_you_fbi.png
---
name: this_you_fbi_fig
width: 300px
alt: "Tweet from Marc Lamont Hill (@marclamonthill) quote Tweeting the FBI. The FBI tweet says \"On this 40th anniversary of #MLKDay as a federal holiday, the #FBI honors one of the most prominent leaders of the Civil Rights movement and reaffirms its commitment to Dr. King’s legacy of fairness and equal justice for all.\" Marc Lamont Hill quotes with the words \"This you?\" and a photo of a letter send to King to encourage him to commit suicide,"
---
When the FBI account made a [Tweet in honor of Martin Luther King Jr. on the MLK holiday](https://twitter.com/FBI/status/1614986534318493696), author Marc Lamont Hill [used a quote tweet to dunk on the FBI Tweet by posting a copy of the letter the FBI sent Martin Luther King Jr. encouraging him to kill himself](https://twitter.com/marclamonthill/status/1615156250735435782). This is a different style of making the same point as the Tweet we showed in the Trolling chapter where Jaboukie Young-White impersonated the FBI account.
```

<br>

On January 2nd, 2023, Mastodon creator [Eugen Rochko said](https://mastodon.social/@Gargron/109623891328707089):
> I don't feel as strongly about quote posts as I did in 2018. Personally, I am not a fan, but there is clearly a lot of demand for it. We're considering it.

% masto_quote_announce.png
% https://mastodon.social/@Mastodon/110294411952997299
% You asked for it, and it’s coming. Quote posts, search, and groups are on their way. In the meantime, check out the new onboarding experience launching today. https://blog.joinmastodon.org/2023/05/

% https://ubiqueros.com/notes/9e8u8l4ui2
% Are0h@ubiqueros.com
% Ro @Are0h@ubiqueros.com
%I'll say one thing about Bluesky. It's making Mastodon's leadership nervous.

% And white guys don't pay attention to anyone like other white guys.

% Because we've been talking about Masto's failing for a loooooooooooooooong time, but here we are.

% May 01, 2023

## Reflection Questions
- How does social media design enable or reduce harassment?
- What good things are lost in trying to reduce harassment?
- How do you balance these different concerns?

## Further Reading
- [Quote Tweeting: Over 30 Studies Dispel Some Myths](https://absolutelymaybe.plos.org/2023/01/12/quote-tweeting-over-30-studies-dispel-some-myths/)
- [Black Twitter, quoting, and white views of toxicity on Mastodon](https://privacy.thenexus.today/black-twitter-quoting-and-white-toxicity-on-mastodon/)