# Website-Test

My website. 

The website is also hosted at [Neocities](https://coffeeandcode.neocities.org).

## About

The website is a few notes mostly on technical topics. It is not meant
to be taken too seriously - I do enough "serious writing" in my day
job thank you very much. This is some light relief.

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

OK so my website is very simple, but it does have fast page load
times, and it would be a *lot* fast if I had no CSS and no syntax
colouring.


