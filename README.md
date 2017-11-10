# Website-Test

My website. 

The website is also hosted at [Neocities](https://coffeeandcode.neocities.org).

## About

The website is a few notes mostly on technical topics. It is not meant
to be taken too seriously - I do enough "serious writing" in my day
job thank you very much. This is some light relief.

## TODO

- [x] Add dates to articles and use CSS to highlight them (ISO-8601) YYYY-MM-DD
- [x] Change scripts so it's easier to build one page at a time
- [ ] Code to convert general date format to ISO-8601 full date format
- [x] Code to extract metadata from article
- [ ] Add summary to each article (required for Atom feed)
- [ ] Add metadata to each article (required for Atom feed)
- [ ] Differentiate between date and iso-date for styling (needs regex and CSS)
- [ ] Add published date/time and last updated date/time
- [ ] Simple Atom feed generator
- [ ] Makefile for site build
- [ ] h1 should always have horizontal rule beneath it (regex) 

Experimental:

- [ ] Page from CSV
- [ ] Page from database (MySQL)
- [ ] Page from text
- [ ] Page from XML
- [ ] Page from API
- [ ] Page from web calendar

## Tools

So, I could have set up Wordpress and a MySQL database and all that
jazz but the DIY approach seemed fine for what I needed.

A few notes on how this website is put together:

1. Source is written in GitHub flavoured markdown (GFM). This has the
   advantage of being quite readable in GitHub itself.
2. I use [this markdown tool](https://github.com/cwjohan/markdown-to-html) to convert to GFM to HTML.
3. I then post process the HTML to add syntax colouring and a full HTML page structure using `clean.py`.
4. The website building script, which is very simple, also cleans HTML Tidy to tidy up the HTML.
5. I upload a copy of the generated HTML to Neocities.


I use Emacs to edit pretty much everything. Here's a screen shot of me
editing the website - I was actually fixing my TODO list.

![Emacs screenshot](./images/emacs_screenshot.png "Emacs screenshot")

OK so my website is very simple, but it does have fast page load
times, and it would be a *lot* faster if I had no CSS and no syntax
colouring.



