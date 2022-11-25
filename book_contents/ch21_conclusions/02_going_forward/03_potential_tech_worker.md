# As a Potential Tech Worker

 - as tech worker [if you end up as one]: consider ethics of what you are making. You might not have power, but you also might sometimes

As a potential tech workers that might work for a social media site, we hope you learn how to analyze the ethical tradeoffs made in designing automated systems. We hope you could then bring those concerns into how you design and implement automated systems for social media sites.


## An Example of Action

https://twitter.com/stevekrenzel/status/1589700721121058817

Steve Krenzel
@stevekrenzel

With Twitter's change in ownership last week, I'm probably in the clear to talk about the most unethical thing I was asked to build while working at Twitter.

🧵
11:26 AM · Nov 7, 2022
·Twitter for iPhone

To set the stage, this was the 2015-2016 era.
@dickc
 was just ousted, though he was wonderful and made us feel like family.
@jack
 came in as part-time CEO. Twitter had been near death for a while and was desperately trying to find a buyer. Facebook and Google both refused.

 Most people don't really appreciate how close Twitter was to shutting down. The 2016 election was the only thing that saved them and made them relevant again (to the detriment of us all). But I digress...

 I worked as a software engineer on a team with a charter to make Twitter work better for people in emerging markets (Brazil, India, Nigeria, etc...). This meant a lot of mobile work. And was mostly non-visual stuff - reducing bandwidth, memory usage, battery consumption.

 Oh and app size... we fought tooth and nail to keep the app under 10MB. FB had the money to zero-rate for people in India to d/l a 100MB app, but we did not. We finally lost the 10MB battle when Twitter Video launched (iirc). After that, all discipline around app size was lost.

 One of the first areas I worked on was improving the way our mobile apps uploaded logs. Twitter, like most mobile apps, logs *everything* users do – every swipe, tap, edit, delay, etc… – for debugging, metrics, and experiments.

The size of logs adds up quickly.

In the app, HTTP responses were compressed, but requests weren't. Logs are highly compressible, so I wired up support to gzip HTTP requests, and tweaked our log ingestion server to handle these.

(That reduced mobile bandwidth consumption by ~40% iirc. It was absurd.)

So I became known as the mobile logs guy. And that sets the stage for why I was pulled into a Sales conversation. Twitter was on its death bed and was desperate for money. A large telco wanted to pay us to log signal strength data in N. America and send it to them.

My plan was to aggregate signal strength by carrier / by location. I worked with Data Science to find a granularity – minimum area size and minimum distinct users per area – that would preserve anonymity even when combined with other sources of data (differential privacy).

When we sent this data to the telco they said the data was useless. They switched their request and said they want to be able to tell how many of our users are entering their competitors’ stores.

A bit sketchier, but maybe workable in a privacy respecting way?

We ran an alternative by the telco. They didn’t like it and were frustrated. So was Sales. I was asked to go to telco’s HQ and figure out exactly what they want.

The subsequent request was absurd.

I wound up meeting with a Director who came in huffing and puffing.

The Director said “We should know when users leave their house, their commute to work, and everywhere they go throughout the day. Anything less is useless. We get a lot more than that from other tech companies.”

I responded with some variant of “No fucking way”.

There was no universe where I was going to help sell granular identifiable user location data.

This led to more internal meetings. Legal said the request was fine – none of it violated the user ToS.

Normally they might find another engineer to do this work, but my whole team was aligned with the privacy concerns. Twitter had also just done layoffs (aside: time is a flat circle), so there were no spare engineers around.

My team wasn’t touched by layoffs, but half of them had quit anyway. Twitter was having a mass exodus.

I had done what I could, but Twitter was no longer a place to do good work. I decided to join the exodus and would pull any levers to kill this on my way out.

One random anecdote:

In the middle of this, I had gotten a new manager who, in a retention attempt I’ll never forget, said “If we filled a dump truck with money and dumped it on you, would you stay and build this?”

I wasn’t really sure how to respond to that… but no dice.

My last email written at Twitter was to Jack. To his credit, he responded quickly with something to the effect of “Let me look into that and make sure there isn’t a misunderstanding. It doesn’t  seem right. We wouldn’t want to do that.”

It was in his hands now.

As far as I know, the project actually got canned. Jack genuinely didn’t like it.

I don’t know if this mindset will hold true with the new owner of Twitter though. I would assume Elon will do far worse things with the data.

And, for the any employees still at Twitter, don’t underestimate the power of a pocket veto.

Sometimes it doesn’t work out, or you have to escalate and risk it back firing, but a good pocket veto is a tool to learn to wield well.
