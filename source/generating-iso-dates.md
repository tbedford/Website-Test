# Generating ISO-8601 dates on Mac OS X

Summary: In this article I talk about how you can generate ISO-8601
format dates on the Mac OS X command line, and also how you can do it
in Python too.

Dates are tricky little things in a way that isn't apparent when you
first look at them. As I burrowed into the requirements around
generating an Atom feed for this site I realized the best approach
would be to standardize on a date reference and two date formats.

First, the date reference point for all dates associated with this
site is UTC. It does not matter whether or not I am on summer time,
dates are UTC - period. I will say that again - dates on this site as
always UTC. 

To obtain a UTC referenced date on the command line (Mac OS X) is:

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




References:

* [Stack overflow article](https://stackoverflow.com/questions/7216358/date-command-on-os-x-doesnt-have-iso-8601-i-option#7216394)
* [Wikipedia ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)

---

Published: 2017-10-01 12:21:36 UTC
Updated: 2017-11-10 12:26:00 UTC 
UUID: 6768260E-5713-4899-BE43-130BF74DFED2
