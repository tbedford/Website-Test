# The woeful web

Summary: In this article I look at what I think are some serious
issues with the web today.

The web is in a terrible state. I found this out the hard way
recently. I was tasked with scraping some data off various sites in
Thailand. It was not a pleasant experience. 

Exhibit A: the Grand Old Daddy of Bangkok malls inflicts [this
beauty](http://www.mbk-center.co.th) on customers. 

What's more, every time you load a page you'll see this character, for
probably a lot longer than you'd like:

![MBK rabbit](./images/mbk_rabbit.png "MBK rabbit")

Trust me, that rabbit gets real annoying after two or three page
loads.

It gets worse.

There's [this site](http://www.centralplaza.co.th/index.php). The
company that owns this one is a $2 billion a year company. So not
exactly a fly-by-night outfit. You would have thought they could put
together something better than this.

## Slow, slow, slow

First, these sites are SLOW. Check out this data for the Central Plaza
site tested via the excellent [pingdom](https://tools.pingdom.com):

![Central Plaza Pingdom](./images/central_plaza_pingdom.png "Central Plaza Pingdom")

Yep, you are looking down the barrel of 46 second page load
times. While testing the site I was, even with page caching, very
often looking at 29 second page load times. Most definitely a 'D' for
performance! Sure, your mileage may vary, depending where you are in
the world, but it's still slow in my book.

By contrast, this pathetic site you are reading loads in around a
second, and that is largely due to the fact I have not yet minimized
my CSS file. I will be making that part of my website building script
in due course. If I fixed that, page load would be milliseconds.

## Poor navigation

Setting aside the less than blistering performance issues, the sites
just aren't very good at doing what websites are supposed to do -
provide relevant information. 

Again with Central, event articles and promotions that are often out
of date as soon as they are uploaded is one issue I've noticed more
often that I'd like. There's also no RSS feed of events - more on this
topic later. It's almost like these things are an afterthought, rather
than part of an integrated approach to delivering a business platform.

Take another example - location information. First you've got to try
and find that Locations page - Central don't make that a top menu
item - it should be. What you really want is a web crawler friendly
page of mall names, nicely formatted address information, postcodes,
and consistently formatted phone numbers.

What you get (if you can find it) is a Google map. The trouble is that
the drop down list of locations on the Locations page means nothing
unless you already have some experience with Thailand, and you
basically know which area you are in (sometimes people don't). And you
might not have location-based services switched on (for legitimate
security reasons), so that's no help.

To test this out, try getting the address for Central Plaza Rama 3. Do
you know what "Rama 3" is? I know this mall quite well as it's one of
my favourites, but without that insider info I'd be struggling. It's
often quite nice to be able to print out the address to give to a taxi
driver. On this page you can't, at least without going through various
shenanigans.

You can probably scrape together some information from this, but it's
fiddly, regardless of whether you are a human or a machine.

I am not especially "picking" on these sites, they are sympomatic of
what's out there generally. I've also dealt with a lot worse, believe
me.

## It's not all bad

By contrast [here's a site](https://www.furama.com/silom/Contact-Us)
that gets the location-based information right. On the Contacts page
which is probably where you'll look first, they have good quality
information laid out in plain text. They even double up, taking a
belt-and-braces approach, and put the information on the bottom right
corner of the [Location
page](https://www.furama.com/silom/Location). And if you really want a
map that's there too on another page.

Generally, the site loads at a reasonable speed too, and has good
navigation, with a simply laid out top menu - nothing fancy - but
effective. Nice and web crawler friendly, so Google likes you (they
also have a sitemap) - and so do the poor unfortunates like me who
have to try and crawl these pages too, and make some kind of sense of
them.

Furama even include their various hotel codes such as their Amadeus
code. These are useful pieces of data for uniquely identifying
hotels. Well done Furama! Nice job. (As an aside I actually stayed in
that hotel in 2003 when it was Tower Inn. Furama have done a great job
of improving it.)

## Why are things so bad?

I think there are three main reasons why things are so bad:

1. HTML
2. Wordpress
3. Data hoarding

Let me explain.

## 1. HTML is presentational

Here's the thing everyone forgets about HTML - **it is a
presentational format, not a semantic format**. This problem is best
illustrated by a simple example. Imagine you are a web spidery thing
for a moment and you saw this:

``` html
<b>Brooklyn Beckham</b>
```

What would you make of that text? Is it a place? Is it a name? How the
hell would you know? The point here is you just know it's something
that's in bold. You don't know what the thing in the bold tags
actually **means**. If you are a human though, you can make an
educated guess, based on your knowledge, that this is David Beckham's
son, not a place, restaurant, hotel, or anything else. You would at
the very least guess that it is the name of a person.

Now consider this:

``` xml
<person>
  <firstname>Brooklyn</firstname>
  <lastname>Beckham</lastname>
</person>
```

You can clearly see that we are defining what the "thing" means, not
how it looks - we couldn't give a fig whether it's bold or not - let
CSS decide that. This markup is most definitely semantic. A machine
reading this, such as a semantic indexer, would know that this is a
person - it's explicitly marked up as such.

As the web mostly consists of HTML pages, the markup is mostly
presentational. This lack of semantic information is tragic. It means
that a lot of the information on the web today is lost - humans never
see a lot of it. Machines could, but they have a hard time making
sense of data in a soup of presentational markup, when what they need
is semantically keyed information.

There are some companies like [diffbot](https://www.diffbot.com) who
are using artificial intelligence and Natural Language Processing
(NLP) to try and figure out what this mess means - but they have their
work cut out for them.

### Microformats

There are microformats like hCard too that allow you to put semantic
markup into HTML. Again this is best explained by example. 

Rather than this:

``` html
<!-- Copied from Wikipedia -->
<ul>
    <li>Joe Doe</li>
    <li>Jo</li>
    <li>The Example Company</li>
    <li>604-555-1234</li>
    <li><a href="http://example.com/">http://example.com/</a></li>
</ul>
```

You would have this:

``` html
<!-- Copied from Wikipedia -->
<link rel="profile" href="http://microformats.org/profile/hcard">
...
</head>
...
<ul class="vcard">
    <li class="fn">Joe Doe</li>
    <li class="nickname">Jo</li>
    <li class="org">The Example Company</li>
    <li class="tel">604-555-1234</li>
    <li><a class="url" href="http://example.com/">http://example.com/</a></li>
</ul>
```

Without knowing much about vCard or its HTML equivalent hCard, you can
see that semantic markup has been used to give the content
**meaning**. 

Really, this is the difference between the "dumb" web that we have
now, and the "smart" web that we should have had. 

The sad fact of the matter is [Microformats](http://microformats.org)
(and there are numerous flavours) has had very little take up.

There are some good people, like [schema.org](http://schema.org) who
are trying to move things in the right direction with standards such as
RDFa, Microdata and JSON-LD. But many sites don't take advantage of
these standards.

This is a shame because Google and Microsoft (Bing), the big search
engine players today, will make use of this information if their web
crawlers see it. 

Some of the big sites do use some kind of semantic markup, but most
web sites out there don't. Trip Advisor for example uses JSON-LD, but
I'm guessing mostly so Google and Microsoft can do a better job of
indexing their site.

## 2. Wordpress

The second problem I want to talk about is Wordpress. 

Even back in 2015 Wordpress [powered 25% of the
web](https://venturebeat.com/2015/11/08/wordpress-now-powers-25-of-the-web/).

This fact is not a good thing. 

Wordpress is not only slow (unless you throw lots of metal and
replication database systems at it), but it is potentially insecure
too.

I remember a few years back testing Wordpress powered sites for fun
and lost count of how many sites never removed the `install.php` file
after installing - you could literally run that and reinstall their
website for them, wiping out all their data - I suspect there are more
than a few of those sites around still.

The bigger problem is that it allows people that have very little web
training create sites that are both slow and insecure, as well as just
poorly designed from an informational point of view. They often use a
"one click install" facility, and never get near a MySQL database,
unless things go horribly wrong (which they sometimes do).

Often the focus for desginers is on getting up some glossy pics (that
should have been compressed more or resized) and "creating a brand"
than actually providing useful information. 

When the "web masters" manually test the site, they often assume that
any perceived slowness (if they perceive it at all) is because "the
Internet is slow", or that's "just the way the Internet is". It may
well be, but their site isn't helping things.

Very often there is no *information flow* too, so content is manually
entered by someone into a WP site, but then updates are an after
thought - there is often no automatic process in place to update
data. This problem is exacerbated when a third-party developer is
responsible for the site - there is often a poor communication channel
between this agency and the parent company, if they talk to eachother
at all.

Now Wordpress is an awesome Content Management System for very large
artcile-based websites. Look at [QZ](https://qz.com) for a Wordpress
site done right. But you are looking at a site that cost over a
million dollars to develop and costs a shedload of money each month to
keep running. They are using Wordpress VIP and it depends on your
level of service but I believe that costs around $10k a month - not
exactly chump change.

My point is many sites built with Wordpress shouldn't have been. Sure
Wordpress makes it easy to make a site, it also makes it easy to make
a bad site.

In this respect I believe the resurgence of static sites and static
site generators (Hugo, Octopress, Jekyll) is actually A Good Thing
(TM), and not the step backwards many people seem to think it is.

## 3. Data hoarding

There's a problem at play here that you maybe only really notice when
you come to extract data from the web. The web is becoming stratified
into the data "haves" and "have nots".

There is a constant battle in play to control information on the
web. Many of the big outfits, are intent on hoarding as much data as
they can. You see this reflected in removal of RSS feeds of data, and
APIs, that would let external programs access this data.

Now, while I fully support an organization's right to protect its hard
won data, right now we don't have a level playing field. The big
players like Google and TripAdvisor, Booking.com and hotels.com have
the potential to monopolize data.

Some of the big data players built their databases by (at least
partially) scraping the web, and then deny the same right to others as
they hoard their scraped data.

The general problem is that "data hoarding" in the wider web is not a
good thing.

### Hello APIs

But there is a possible plus side here. APIs. 

For example, Trip Advisor do at least [offer an
API](https://developer-tripadvisor.com/content-api/) (currently). You
can get the following data from their site:

* Location ID, name, address, latitude & longitude
* Read reviews link, write-a-review link
* Overall rating, ranking, subratings, awards, the number of reviews the rating is based on, rating bubbles image
* Price level symbol, accommodation category/subcategory, attraction type, restaurant cuisine(s)

This is a very useful subset of data. But...

### Goodbye APIs

The above APIs are all well and good as long as they are
maintained. And there's the rub.

Google long since abandoned its own Search API, and many of Google's
search-related APIs have been [closed
down](https://developers.googleblog.com/2016/01/retirement-of-certain-google-search-apis.html)
over the years. Google Custom Search only searches *your* site.

Google are also [closing
down](https://techcrunch.com/2017/11/01/google-will-pull-its-qpx-express-api-in-april-2018-cutting-off-its-flight-data-feed/amp/)
their flight search API too. 

Yahoo too has become notorious for [closing down APIs](https://searchengineland.com/confirmed-yahoo-to-close-buzz-traffic-apis-maybe-delicious-59012).

This loss of API coverage exacerbates the issue of data hoarding. Data
silos are order of the day.

In this respect Microsoft are increasingly becoming the "good guys"
these days. Bing has a [very nice
API](https://docs.microsoft.com/en-gb/rest/api/cognitiveservices/bing-web-api-v7-reference)
you can use to access Bing's search results.

### The case of the disappearing RSS feeds

As people move away from blogs and websites and into the smothering
embrace of "social media" their data disappears into a walled garden -
accessible no more, unless you are into advertising and fake
news. This is a shame. RSS feeds were one of the best inventions of
the web - they allowed you to suck in data from a variety of sources,
process it to your own ends, and store it for posterity. These days a
lot of sites don't bother with RSS feeds, which I think it a real
shame. Back to Trip Advisor again and this thread about how they
[closed down their RSS
feeds](https://www.tripadvisor.co.uk/ShowTopic-g1-i12104-k7514343-Reinstate_RSS_feeds-Help_us_make_TripAdvisor_better.html). Data
disappearing into the walled garden again?

I think all websites should have RSS feeds to provide a data feed
where it makes sense to do so. 

And before you say it - yes it is on my TODO list for this site. Give
us a chance precious, give us a chance...

## Why does any of this matter?

This stuff is important, not only for the customer's sense of
satisfaction, but for much bigger reasons. Websites should be fast and
responsive and have the information we need. Semantic markup should be
widespread and sites should be designed with web spiders and indexing
at least partly in mind.

All these problems - slowness, poor design, poor training, lack of
semantic markup, removal of RSS feeds and lack of APIs, data hoarding,
it all leads to one thing - the woeful state of the web. 

Things could be so much better.

**Updates:**

1. In a future article I'll take a look at what can be done to improve
things.

2. [James](https://www.instagram.com/countryside.coder/) pointed me at
   [Webflow](https://webflow.com), which I'd not seen before. It looks
   awesome. I also notice one of the first words they use on their
   website is "semantic". Nice.

---
* Published: 2017-11-07 09:00:00 UTC
* Updated: 2017-11-15 12:56:00 UTC
* UUID: 86EF52C7-CF29-47BA-B804-FCB6F5770F39


