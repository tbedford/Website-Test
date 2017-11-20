# Generating an Atom feed

Summary: This article explains how an Atom feed was added to this site
using Python code. The article also describes adding automatic feed
discovery to the site.

So, after ranting about how RSS and Atom feeds are disappearing from
the web in my article [The Woeful Web](./woeful-web.html), I decided I
ought to offer a feed for this humble site.

I settled on offering an Atom feed, as the situation around RSS feeds
is complicated. Atom was designed to deal with various issues that
were arising in RSS feeds. Most feed readers will support both RSS and
Atom, so generating both formats for my site would be overkill. I
decided on Atom which seemed clean and modern and did not suffer the
legacy issues that seem to trouble RSS.

The Atom feed format is more correctly known as Atom Syndication
Format. It is the Atom Syndication format I mean when I refer to an
Atom feed.

Having looked initially at the [Atom Syndication Format
RFC](https://tools.ietf.org/html/rfc4287), I was a bit worried about
what I was getting myself into - the RFC is fairly impenetrable. The
solution, for me, was to look at examples of Atom feeds and this
clarified things. Once you get your bearings by looking at generated
Atom feeds, the RFC makes a lot more sense.

One of the hardest aspects of this was retrofitting the correct
metadata to my existing content. I had to work out what data would be
required, and how this would be added to my content. In the end I
settled on Published date, Updated date, Summary, and Title. In
addition each article has a UUID. This is required by the Atom feed
spec. A UUID can be generated easily enough on the command line (in
Mac OS X), using the command `uuidgen`. This seemed to be sufficient
for my purposes. I decided not to add the full content of the article
to my feed, as the user can simply click on the article heading in a
feed reader to read the content on my site. This has the advantage
that it keeps the feed simpler and quicker to generate. The downside
is the user will need to be able to access the web in order to read
the content - if they were using a desktop feed reader the content
would be saved for offline reading if I provided a full feed. In this
case the advantages of speed of generation and simplicity outweighed
this convenience for the user. However, in the future I could offer a
full feed capability. This would be relatively simple to add to the
existing code based on my investigations so far.

The other aspect I needed to determine was dates and how to format
them.  The Atom feed uses ISO-8601 date times. I have already
described dates and the issues around them in my article [dealing with
dates](./dealing-with-dates.html), so I won't go into these again
here.

The data extracted from each article is used to populate an entry in
the Atom feed. The header and footer for the Atom feed are more or
less static pieces of text. The only requirement here is that the
header is patched with the date-time of the feed
generation. Essentially the entries are appended to the header in the
output file, and then the footer written before the feed file is
closed.

Metadata can be extracted from either the Markdown source for each
article, or the generated HTML, with simple regular expressions. I
originally planned to extract the data from the generated HTML, but
decided to use the Markdown source instead. No changes were required
to the regular expressions. However, a little additional code needed
to be added to deal with the fact that the links to the articles in
the Atom feed should reference HTML files. The reason for using the
Markdown article source was I only need to add articles, not pages, to
the Atom feed. The articles are, for convenience, stored separately
from the static pages in `source/articles`. I can find these easily
enough with some Bash shell scripting: `find ./source/articles -name
"*.md"`. These are then fed to the Python code that generates the Atom
feed. I find is extremely useful to use Python's fileinput facility. This is rather similar to Perl's diamond operator `<>`. This facility allows your
Python code to accept a list of files to operate on from `stdin`:

``` python
for filename in fileinput.input():

    # chomp
    filename = filename.rstrip()
    ...
```

This reads files in from `stdin` and you'll notice I do a Perl-style
`chomp` to remove any extraneous new lines on the end of the file
name.

Typically you will use some Bash shell script to find the required
files and then pipe these into your Python code:

``` shell
find ./source/articles -name "*.md" | ./generate_atom_feed.py
```

This may not be the prettiest approach to solving the problem as you
could write all code in Python and have no Shell script at all. This
is something I will consider for the future, but for now this is an
effective way of directing the Python code.

I will not go into the Python source code to generate the feed as it
is available in my GitHub - the file to look at is
`generate_atom_feed.py`. The code is called from the
`build_website.sh` shell script. It takes milliseconds to build the
feed right now. I expect that even if the site expanded to thousands
of articles (which won't happen any time soon), the feed would take a
few seconds to build.

I tested the feed with Inoreader, the web-based feed
reader. Everything seems to work fine. One thing I did need to do was
add automatic feed discovery to each page. This was a matter of simply
adding a little bit of code to the header that is automatically used
in the building of each web page. To allow auto-discovery of the feed
you simply need to indicate to the web browser / feed reader that a
feed is available by adding a link in the `<head> ... </head>`
element. This addition to `clean.py` is shown here:

``` html
<link rel="alternate" type="application/atom+xml" title="Coffee and Code Atom Feed" href= "https://coffeeandcode.neocities.org/atom.xml">
```

Once the metadata was added to each article it was not too bad to
generate the feed. It was mostly an exercise in regexes. I could
perhaps have used an XML parser, but I think that would have been
overkill in this case. If I was writing a general purpose generator,
or perhaps a feed reader, I would almost certainly have needed to use
an XML parser, and perhaps one of the feed parser/generator libraries
out there. It was however quite fun to generate my Atom feed without
any external libraries.

I hope you find the Atom feed useful. If you experience any issues
please let me know via my [contact page](./contact.html).

---

* Published: 2017-11-20 16:16:09 UTC
* Updated: 2017-11-20 16:16:09 UTC
* UUID: ED0C22B5-50F3-4C74-A3C9-C7F31EEDBD26

