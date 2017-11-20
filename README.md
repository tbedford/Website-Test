# Website-Test

My website. 

The website is also hosted at
[Neocities](https://coffeeandcode.neocities.org) for viewing in a
browser.

You can view the site here, but images will not display correctly as I
use a slightly different images layout on the actual site.

## About

The website is a few notes mostly on technical topics. It is not meant
to be taken too seriously - I do enough "serious writing" in my day
job thank you very much. This is some light relief.

My website is very simple, but it does have fast page load
times, and it would be a *lot* faster if I had no CSS and no syntax
colouring.

I do tend to like to work things out from scratch, which is sometimes
not the fastest way to achieve something, but you do learn a lot!

## TODO

- [x] Add dates to articles and use CSS to highlight them (ISO-8601) YYYY-MM-DD
- [x] Change scripts so it's easier to build one page at a time
- [x] Code to convert general date format to ISO-8601 full date format
- [x] Code to extract metadata from article
- [x] Add summary to each article (required for Atom feed)
- [x] Add metadata to each article (required for Atom feed)
- [x] Add published date/time and last updated date/time
- [x] Simple Atom feed generator
- [ ] Links page should be XML which gets converted to HTML
- [ ] Articles page should be automagically generated
- [ ] Makefile for site build
- [ ] h1 should always have horizontal rule beneath it (regex) 
- [ ] Script to build cat pics page (resize pics etc.) so I don't have to do it manually
- [ ] Add indexing system (and later add search facility)

Experimental:

- [ ] Page from CSV
- [ ] Page from database (MySQL)
- [ ] Page from text
- [ ] Page from XML
- [ ] Page from API
- [ ] Page from web calendar

## Tools

A few notes on how this website is put together:

1. Source is written in GitHub flavoured markdown (GFM). This has the
   advantage of being quite readable in GitHub itself.
2. I use [this markdown tool](https://github.com/cwjohan/markdown-to-html) to convert to GFM to HTML.
3. I then post process the HTML to add syntax colouring and a full HTML page structure using `clean.py`.
4. The website building script, which is very simple, also cleans HTML Tidy to tidy up the HTML.
5. I upload a copy of the generated HTML to Neocities.

## Emacs

I use Emacs to edit pretty much everything. Here's a screen shot of me
editing the website - I was actually fixing my TODO list.

![Emacs screenshot](./images/emacs_screenshot.png "Emacs screenshot")

## Dates

Dates are tricky little things in a way that isn't apparent when you
first look at them. As I burrowed into the requirements around
generating an Atom feed for this site I realized the best approach
would be to standardize on a date reference and two date formats.

First, the date reference point for all dates associated with this
site is UTC. It does not matter whether or not I am on summer time,
dates are UTC - period. I will say that again - dates on this site as
always UTC. To obtain a UTC referenced date on the command line (Mac
OS X) is:

``` shell
date -u +"%Y-%m-%dT%H:%M:%SZ"
```

This will give you an ISO-8601 format date corrected to UTC. Example
output is:

``` shell
2011-08-27T23:22:37Z
```

Generally when you are looking at ISO-8601 dates they always have the
format YYYY-MM-DD. This avoids the confusing situation where some
countries put the month before the day and so on.

I also use two date-time _formats_:

1. I have a human readable (at least more human readable) format which
I use in the article source. This is of the format `2017-10-01
12:21:36 UTC`. Note the UTC on the end which is my way of clarifying
this is a UTC date-time. It's quick and clean and because it's more or
less ISO-8601 (but not quite) it should be unambiguous.

2. The second format you have already seen - it is an ISO-8601 format
date corrected to UTC. This is only used within the generated Atom
feed for the site.

As an aisde, if you do `date` in the terminal normally you will get a
date-time in this format `Fri 10 Nov 2017 14:03:59 GMT`. In summer
this would probably show a BST on the end I would guess - that's why I
avoid this format.



