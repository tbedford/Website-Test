# The woeful web

The web is in a terrible state. I found this out the hard way
recently. I was tasked with scraping some data off various sites in
Thailand. It was not a pleasant experience. 

Exhibit A: the Grand Old Daddy of Bangkok malls inflicts [this
beauty](http://www.mbk-center.co.th) on customers. 

What's more every time you load a page you'll see this character, for
probably a lot longer than you'd like:

![MBK rabbit](./images/mbk_rabbit.png "MBK rabbit")

Trust me, that rabbit gets real annoying after two or three page
loads.

It gets worse.

There's [this site](http://www.centralplaza.co.th/index.php). The
company that owns [this one](http://www.centralplaza.co.th/index.php)
is a $2 billion a year company. So not exactly a fly-by-night
outfit. You would have thought they could put together something
better than this.

First, these sites are SLOW. Check out this data for the Central Plaza
site tested via the excellent [pingdom](https://tools.pingdom.com):

![Central Plaza Pingdom](./images/central_plaza_pingdom.png "Central Plaza Pingdom")

Yep, you are looking down the barrel of 46 second page load
times. While testing the site I was, even with page caching, very
often looking at 29 second page load times. Sure, your mileage may
vary, depending where you are in the world, but it's still slow in my
book.

By contrast, this pathetic site loads in around a second, and that is
largely due to the fact I have not yet minimized my CSS file. I will
be making that part of my website building script in due course. If I
fixed that, page load would be milliseconds.

Setting aside the less than blistering performance issues, the sites
just aren't very good at doing what websites are supposed to do -
provide relevant information. Event articles and promotions that are
often out of date as soon as they are uploaded is one issue I've
noticed more often that I'd like. It's almost like these things are an
afterthought, rather than part of an integrated approach to delivering
a business platform.

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
you know what "Rama 3" is? I know this mall quite well, but without
that insider info I'd be struggling. It's often quite nice to be able
to print out the address to give to a taxi driver. On this page you
can't, at least without going through various shenanigans.

You can probably scrape together some information from this, but it's
fiddly, whether you are a human or a machine.

I am not especially "picking" on these sites, they are sympomatic of
what's out there generally. I've also dealt with a lot worse, believe
me.

By contrast [here's a site](https://www.furama.com/silom/Contact-Us)
that gets the location-based information right. On the Contacts page
which is probably where you'll look first, they have good quality
information laid out in plain text. They even double up, taking a
belt-and-braces approach, and put the information on the bottom right
corner of the [Location
page](https://www.furama.com/silom/Location). And if you really want a
map that's there too on another page.

Generally, the site loads at a reasonable speed too. Nice and web
crawler friendly, so Google likes you (they also have a sitemap) - and
so do the poor unfortunates like me who have to try and crawl these
pages too, and make some kind of sense of them. Furama even include
their various hotel codes such as their Amadeus code. These are useful
pieces of data for uniquely identifying hotels. Well done Furama! Nice
job. (As an aside I actually stayed in that hotel in 2003 when it was
Tower Inn. Furama have done a great job of improving it.)

## Why are things so bad?

I think there are two main reasons why things are so bad:

1) HTML
2) Wordpress

Let me explain.

Here's the thing everyone forgets about HTML - **it is a presentational
format, not a semantic format**. This is best illustrated by a simple
example. Imagine you are a web spidery thing for a moment and you saw
this:

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
CSS decide that. This markup is most definitely semantic.

As the web mostly consists of HTML pages, the markup is mostly
presentational. This lack of semantic information is tragic. It means
that a lot of the information on the web today is lost - humans never
see a lot of it. Machines could, but they have a hard time making
sense of data in a soup of presentational markup, when what they need
is semantically queued information.

There are some companies like [diffbot](https://www.diffbot.com) who
are using artificial intelligence and Natural Language Processing to
try and figure out what this mess means - but they have their work cut
out for them.

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
(and there are numerous flavours) has very little take up.

There are some good people, like [schema.org](http://schema.org) who
are trying to move people in the right direction with standards such as
RDFa, Microdata and JSON-LD. But many sites don't take advantage of
these standards.

This is a shame because Google and Microsoft (Bing), the big search
engine players today, will make use of this information if their web
crawlers see it. 

Some of the big sites do use some kind of semantic markup, but most
web sites out there don't. Trip Advisor for example uses JSON-LD, but
I'm guessing mostly so Google and Microsoft can do a better job of
indexing their site.

The second problem I want to talk about is Wordpress. 

Even back in 2015 Wordpress [powered 25% of the
web](https://venturebeat.com/2015/11/08/wordpress-now-powers-25-of-the-web/).

This fact is not a good thing. 

Wordpress is not only slow (unless you throw lots of metal and
replication database systems at it), but it is potentially insecure
too. I remember a few years back testing Wordpress powered sites for
fun and lost count of how many sites never removed the `install.php`
file after installing - you could literall run that and reinstall
their website for them, wiping out all their data - I suspect there
are more than a few of those sites around still.

The bigger problem is that it allows people that have very little web
training create sites that are both slow and insecure - and as well
have seen just poorly designed from an informational point of
view. Often the focus is on getting up some glossy pics (that should
have been compressed more or resized) than actually relaying useful
information. When they manually test the site, they often assume that
any perceived slowness (if they perceive it at all) is because "the
internet" is slow. It may well be, but their site isn't helping
things.

Now Wordpress is an awesome Content Management System for very large
websites, but my point is many sites built with it shouldn't have
been. In this respect I believe the resurgence of static sites is
actually A Good Thing (TM).

## Why does any of this matter?

This is stuff is important, not only for the customer (the end user's)
sense of satisfaction, but for much bigger reasons. The web is
becoming stratified into the "haves" and "have nots". There is a
constant battle in play to control information on the web. Many of the
big outfits, are intent on hoarding as much data as they can. You see
this reflected in removal of RSS feeds of data, and APIs, that would
let external programs access this data. Now, while I fully support an
organization's right to protect its hard won data, right now we don't
have a level playing field. The big players like Google and
TripAdvisor, Booking.com and hotels.com tend to monopolize data. They
built their databases by (at least partially) scraping the web, and
then deny the same right to others. 

For example, look at this Trip Advisor `robots.txt` file:

``` text
# Hi there,
#
# If you're sniffing around this file, and you're not a robot, we're looking to meet curious folks such as yourself.
#
# Think you have what it takes to join the best white-hat SEO growth hackers on the planet?
#
# Run - don't crawl - to apply to join TripAdvisor's elite SEO team
#
# Email seoRockstar@tripadvisor.com
#
# Or visit https://boards.greenhouse.io/tripadvisor/jobs/843249
#
#
Sitemap: https://www.tripadvisor.co.uk/sitemap/2/en_UK/sitemap_en_UK_index.xml
Sitemap: https://www.tripadvisor.co.uk/sitemap/vr/en_UK/sitemap_en_UK_rental_property_manager_index.xml
Sitemap: https://www.tripadvisor.co.uk/sitemap/vr/en_UK/sitemap_en_UK_rentals_index.xml
Sitemap: https://www.tripadvisor.co.uk/sitemap/vr/en_UK/sitemap_en_UK_vacation_rental_review_index.xml
Sitemap: https://www.tripadvisor.co.uk/sitemap/vr/en_UK/sitemap_en_UK_vacation_rentals_index.xml
Sitemap: https://www.tripadvisor.co.uk/sitemap/vr/en_UK/sitemap_en_UK_vacation_rentals_near_index.xml
Sitemap: https://www.tripadvisor.co.uk/sitemap/vr/en_UK/sitemap_en_UK_vr_show_user_reviews_index.xml
Sitemap: https://www.tripadvisor.co.uk/sitemap/att/en_UK/sitemap_en_UK_attractions_index.xml
Sitemap: https://www.tripadvisor.co.uk/sitemap/att/en_UK/sitemap_en_UK_attraction_review_index.xml
Sitemap: https://www.tripadvisor.co.uk/sitemap/att/en_UK/sitemap_en_UK_attractions_near_index.xml
User-Agent: *
Disallow: /5349
Disallow: /AboutRail
Disallow: /AbuDhabi
Disallow: /AccessTokenLogin
...
```

Well, I will pass on the job offer thanks.

Then take a look at their T&Cs. 

``` text
PROHIBITED ACTIVITIES

The content and information on this Website (including, but not limited to, messages, data, information, text, music, sound, photos, graphics, video, maps, icons, software, code or other material), as well as the infrastructure used to provide such content and information, is proprietary to us. You agree not to otherwise modify, copy, distribute, transmit, display, perform, reproduce, publish, license, create derivative works from, transfer, or sell or re-sell any information, software, products, or services obtained from or through this Website. Additionally, you agree not to:

(i) use this Website or its contents for any commercial purpose;
(ii) access, monitor or copy any content or information of this Website using any robot, spider, scraper or other automated means or any manual process for any purpose without our express written permission;
(iii) violate the restrictions in any robot exclusion headers on this Website or bypass or circumvent other measures employed to prevent or limit access to this Website;
(iv) take any action that imposes, or may impose, in our discretion, an unreasonable or disproportionately large load on our infrastructure;
(v) deep-link to any portion of this Website for any purpose without our express written permission;
(vi) "frame", "mirror" or otherwise incorporate any part of this Website into any other website without our prior written authorization; or
(vii) attempt to modify, translate, adapt, edit, decompile, disassemble, or reverse engineer any software programs used by TripAdvisor in connection with the Website or the services.
```

Note in particular: **"(ii) access, monitor or copy any content or
information of this Website using any robot, spider, scraper or other
automated means or any manual process for any purpose without our
express written permission;"**

Could it be any clearer? I suppose you could always try writing to
them. Good luck with that unless you are Microsoft or Google.

Now, I don't really want to pick on Trip Advisor particularly - it's a
great site that I have used myself in the past, and will continue to
do so. The problem is that this "data hoarding" is not a good thing
for the wider web.

You'll notice in my previous list of "data hoarders" I did not include
Microsoft. These days Microsoft are increasingly becoming the "good
guys". Bing has a [very nice
API](https://docs.microsoft.com/en-gb/rest/api/cognitiveservices/bing-web-api-v7-reference)
you can use to access Bing's search results. Google long since
abandoned its own Search API. Many of Google's search APIs have been
[closed
down](https://developers.googleblog.com/2016/01/retirement-of-certain-google-search-apis.html)
over the years. Google Custom Search only searches *your* site. 

Google are also [closing
down](https://techcrunch.com/2017/11/01/google-will-pull-its-qpx-express-api-in-april-2018-cutting-off-its-flight-data-feed/amp/)
their flight search API too. This exacerbates the issue of data
hoarding. Data silos are order of the day.

All these problems - slowness, poor design, poor training, lack of
semantic markup, removal of RSS feeds and APIs, data hoarding, it all
leads to one thing - the woeful current state of the web.

In a future piece I will be looking at things can be improved.
