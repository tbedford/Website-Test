# The woeful web

The web is in a terrible state. I found this out the hard way
recently. I was tasked with scraping some data off various sites in
Thailand. It was not a pleasant experience. 

Exhibit A: the Grand Old Daddy of Bangkok malls inflicts [this
beauty](http://www.mbk-center.co.th) on customers. Trust me, that
rabbit gets annoying after two or three page loads. It gets worse.

Then there's [this site](http://www.centralplaza.co.th/index.php). The
company that owns [this one](http://www.centralplaza.co.th/index.php)
is a $2 billion a year company. So not exactly a fly-by-night outfit.

First, these sites are SLOW. Check out this data for that last site
tested via the excellent [pingdom](https://tools.pingdom.com):

![Central Plaza Pingdom](./images/central_pingdom.png "Central Plaza
Pingdom")

Yep, you are looking down the barrel of 46 second page load
times. While testing the site I was, even with page caching, very
often looking at 29 second page load times.

Setting aside the less than blistering performance issues, the sites
just arent very good at doing what websites are supposed to do -
provide information. Event articles are often out of date as soon as
they are uploaded. 

Take another example - location information. First you've got to try
and find that Locations page - Central don't make that a top menu
item - it should be. What you really want is a web crawler friendly
page of mall names, nicely formatted address information, postcodes,
consistently formatted phone numbers.  What you get is a Google
map. The trouble is that drop down list of locations on the Locations
page means nothing unless you already have some experience with
Thailand, and you basically know which area you are in (sometimes
people don't). To test this out, try getting the address for the mall
on Rama 3. Do you know where Rama 3 is? I know this mall quite well,
but without that insider info I'd be struggling. It's often quite nice to be able to print out the address to give to a taxi driver. On this page you can't, at least without going through various shenanigans.

By contrast [here's a site](https://www.furama.com/silom/Contact-Us)
that gets the location information right - on the Contacts page which
is probably where you'll look first. They even double up, taking a
belt-and-braces approach, and put the information on the bottom right
corner of the [Location
page](https://www.furama.com/silom/Location). Well done Furama. Nice
and web crawler friendly, so Google likes you - and so do the poor
unfortunates like me who have to try and crawl these pages too.

## Why are things so bad?

I think there are two main reasons why things are so bad:

1) HTML
2) Wordpress

Let me explain.

Here's the thing everyone forgets about HTML - it is a presentational
format, not a semantic format. This is best illustrated by a simple
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
least guess, as a humn, that it is the name of a person.

Now consider this:

``` xml
<person>
  <firstname>Brooklyn</firstname>
  <lastname>Beckham</lastname>
</person>
```

You can clearly see that we are defining what the "thing" means, not
how it looks - we couldn't give a fig whether it's bold or not - let
CSS decide that.

This lack of semantic information is tragic. It means that a lot of
the information on the web today is lost - humans never see a lot of
it. Machines could, but they have a hard time making sense of
presentational information, when what they need is semantic
information. 

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
**meaning**. Really, this is the difference between the "dumb" web
that we have, and the "smart" web. The sad thing is
[Microformats](http://microformats.org) (and there are numerous
flavours) has virtually no take up. This is a shame because Google and
Microsoft will make use of this information if their web crawlers see
it. Some of the big players do use some kind of semantic markup, but
most web sites out there don't.

The second problem I want to talk about it Wordpress. 

Even back in 2015 Wordpress [powered 25% of the
web](https://venturebeat.com/2015/11/08/wordpress-now-powers-25-of-the-web/).

That fact is not a good thing. Wordpress is not only slow (unless you
throw lots of metal and replication database systems at it), but it is
potentially insecure too. I remember a few years back testing
Wordpress powered sites for fun and lost count of how many sites never
removed the install.php file after installing - you could literall run
that and reinstall their website for them, wiping out all their data -
I suspect there are more than a few of those sites around still.

The bigger problem is that it allows people that have very little web
training create sites that are both slow and insecure - and as well
have seen just poorly designed from an informational point of
view. Often the focus is on getting up some glossy pics (that should
have been compressed more or resized) than actually relaying useful
information.

In this respect I believe the resurgence of static sites is actually A
Good Thing (TM).

## Why does any of this matter?

This is stuff is important, not only for the customer (the end user's)
sense of satisfaction, but for much bigger reasons. The web is
becoming stratified into the "haves" and "have nots". There is a
constant battle in play to control information. Many of the big
outfits, like Trip Advisor, are intent on hoarding as much data as
they can. You see this reflected in removal of RSS feeds of data, and
the removal of APIs, that would let external programs access this
data. Now, while I fully support an organization's to protect its hard
won data, right now we don't have a level playing field. The big
players like Google and TripAdvisor, Booking.com and hotels.com tend
to monopolize data. They built ehir databases by scraping the web, and
then deny the same right to others. For example look at this Trip
Advisor `robots.txt` file:

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

Well, I pass on the job offer thanks.

Then take a look at their T&Cs. 

``` text
Terms of Use

Welcome to the TripAdvisor website or mobile properties, including related applications (collectively, this "Website"). This Website is provided solely to assist customers in gathering travel information, posting opinions of travel related issues, engaging in interactive travel forums, and searching for and booking travel reservations, and for no other purposes. The terms "we", "us", "our" and "TripAdvisor" refer to TripAdvisor LLC, and our corporate affiliates and websites (collectively, "TripAdvisor"). The term "you" refers to the customer visiting the Website and/or contributing content on this Website.

This Website is offered to you conditioned upon your acceptance without modification of any/all the terms, conditions, and notices set forth below (collectively, the "Agreement"). By accessing or using this Website in any manner, you agree to be bound by the Agreement and represent that you have read and understood its terms. Please read the Agreement carefully, as it contains information concerning your legal rights and limitations on these rights, as well as a section regarding applicable law and jurisdiction of disputes. If you do not accept all of these terms and conditions you are not authorized to use this Website.

We may change or otherwise modify the Agreement in the future in accordance with the Terms and Conditions herein, and you understand and agree that your continued access or use of this Website after such change signifies your acceptance of the updated or modified Agreement. We will note the date that revisions were last made to the Agreement at the bottom of this page, and any revisions will take effect upon posting. We will notify our members of material changes to these terms and conditions by either sending a notice to the email address provided to us at registration or by placing a notice on our Website. Be sure to return to this page periodically to review the most current version of the Agreement.

USE OF THE WEBSITE

As a condition of your use of this Website, you warrant that (i) all information supplied by you on this Website is true, accurate, current and complete, (ii) if you have a TripAdvisor account, you will safeguard your account information and will supervise and be completely responsible for any use of your account by anyone other than you, (iii) you are 13 years of age or older in order to register for an account and contribute to our Website and (iv) you possess the legal authority to enter into this Agreement and to use this Website in accordance with all terms and conditions herein.

TripAdvisor does not knowingly collect the information of anyone under the age of 13. We retain the right at our sole discretion to deny access to anyone to this Website and the services we offer, at any time and for any reason, including, but not limited to, for violation of this Agreement.

Copying, transmission, reproduction, replication, posting or redistribution of the Website Content or any portion thereof is strictly prohibited without the prior written permission of TripAdvisor. To request permission, you may contact TripAdvisor as follows:

Director, Partnerships and Business Development
TripAdvisor LLC
400 1st Avenue
Needham, MA 02494, USA

Users of the Website will not incur any charges for using the Website in accordance with these Terms and Conditions. However, the Website contains links to third-party websites which are operated and owned by independent service providers or retailers. Such third-parties may charge a fee for use of certain content or services provided on the website. Therefore, you should make whatever investigation you feel is necessary or appropriate before proceeding with any transaction with any third party to determine whether a charge will be incurred. Where TripAdvisor provides details of charges on the Website, such information is provided for convenience and information purposes only. TripAdvisor in no way guarantees that this information is correct nor is it in anyway responsible for content or services provided on such third party websites.

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
them. Good luck with that.

Now, I don't really want to pick on Trip Advisor particulalry - it's a
great site that I have used myself in the past, and will continue to
do so. The problem is that this "data hoarding" is not a good thing
for the wider web.

All these problems combined, slowness, poor design, lack of sematic
markup, removal of RSS feeds and APIs, data hoarding, it all leads to
one thing - the woeful state of the web.

