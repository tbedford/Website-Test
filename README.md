# Website-Test

My website. This was designed to test out various ideas around using
Markdown as a source format.

The website is also hosted at
[Neocities](https://coffeeandcode.neocities.org) for viewing in a
browser.

You can view the site here, but images will not display correctly as I
use a slightly different images layout on the actual site.

## TODO

- [x] Add dates to articles and use CSS to highlight them (ISO-8601) YYYY-MM-DD
- [x] Change scripts so it's easier to build one page at a time
- [x] Code to convert general date format to ISO-8601 full date format
- [x] Code to extract metadata from article
- [x] Add summary to each article (required for Atom feed)
- [x] Add metadata to each article (required for Atom feed)
- [x] Add published date/time and last updated date/time
- [x] Simple Atom feed generator

## Tools

A few notes on how this website is put together:

1. Source is written in GitHub flavoured markdown (GFM). This has the
   advantage of being quite readable in GitHub itself.
2. I use [this markdown tool](https://github.com/cwjohan/markdown-to-html) to convert to GFM to HTML.
3. I then post process the HTML to add syntax colouring and a full HTML page structure using `clean.py`.
4. The website building script, which is very simple, also cleans HTML Tidy to tidy up the HTML.
5. I upload a copy of the generated HTML to Neocities.

---
