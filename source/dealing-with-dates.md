# Dealing with dates

Summary: In this article I describe dates, how they are used on this
site, and how you can generate ISO-8601 format dates on the Mac OS X
command line.

Dates are tricky little things in ways that aren't apparent when you
first look at them. As I burrowed into the requirements around
generating an Atom feed for this site I wandered into the thorny
wastelands of ISO-8601 dates. For example, look at this simple Atom 
feed:

``` xml
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Coffee and Code  Feed</title>
  <link href="https://coffeeandcode.neocities.org/"/>
  <updated>2017-11-10T08:15:26+0000</updated>
  <author>
    <name>Tony Bedford</name>
  </author>
  <id>urn:uuid:B2F5F303-9B73-4D58-B4DF-32EC8F74136F</id>
  <!-- Entries go here -->
  <entry>
    <title>Creating an Atom feed</title>
    <link href="https://coffeeandcode.neocities.org/creating-atom-feed.html"/>
    <id>urn:uuid:2E4A626F-FF02-47F0-9538-254F76F5C7EF</id>
    <updated>2017-11-10T11:07:29+0000</updated>
    <summary>This is a summary of the article.</summary>
  </entry>
</feed>
```

You'll notice if you look at an Atom feed dates in a format similar
to `2017-11-10T11:07:29+0000`. This is an ISO-8601 format date. It has
various forms. This one is in a format where the time difference to 
UTC is shown, in this case the difference is zero. 

The other common ISO-8601 format you might come across is
`2011-08-27T23:22:37Z`. This format is converted to UTC, in other
words the local date-time has been modified to be a UTC date-time.

This can be clarified by example, while showing you how you can
generate ISO-8601 dates on the command line (in Mac OS X, Linux, or
Cygwin).

To obtain a UTC referenced date on the command line you can issue the
following command:

``` shell
date -u +"%Y-%m-%dT%H:%M:%SZ"
```

This will give you an ISO-8601 format date corrected to UTC - the `-u`
option tells `date` you want the date-time automagically converted
from your local time to UTC. Example output from the command would be:

``` shell
2011-08-27T23:22:37Z
```

If you've not come across UTC before you can think of it as
approximately GMT. GMT is based on astronomical time, but UTC is based
on fancy-pants atomic time as dictated by super accurate atomic
clocks. This atomic time is called International Atomic Time (TAI).

One of the problems with astronomical time is it's based on, well,
astronomical bodies, and their spinning and motion tends to speed up
and slow down depending on tides, the moon, the sun, and which way the
wind is blowing.

So astronomical time and TAI get out of synch, so there's this "fiddle
factor" called the leap second they have to apply now and then and
that's when [Linux crashes](https://access.redhat.com/articles/15145)
and [all hell breaks
loose](https://www.wired.com/2012/07/leap-second-glitch-explained/). This
TAI with the fiddle factor is called Universal Coordinated Time (UTC).

The reasons the acronyms don't quite match is the acronyms were based
on the original French names for these standards.

Anyway, I digress...

I realized the best approach with regards dates for my website would
be to standardize on a date reference and two date formats.

First, the date reference point for all dates associated with this
site is UTC. It does not matter whether or not I am on summer time,
dates are UTC - period. I will say that again - dates on this site are
always UTC.

Generally when you are looking at ISO-8601 dates they always have the
format YYYY-MM-DD. This avoids the confusing situation where some
countries put the month before the day and so on.

I also use two date-time _string formats_:

1. I have a human readable (at least more human readable) format which
I use in the article source at the bottom of each article. This is of
the format `2017-10-01 12:21:36 UTC`. Note the UTC on the end which is
my way of clarifying this is a UTC date-time. It's quick and clean and
because it's more or less ISO-8601 (but not quite) it should be
unambiguous. This is basically used for `published` and `updated`
date-times.

2. The second string format I use is one you have already seen - it is
an ISO-8601 format date corrected to UTC. This is only used within the
generated Atom feed for the site, so you generally won't see it. This
format is a little 'busy' to be used as a human readable format, but
feed readers love it!

As an aisde, if you do `date` in the terminal normally you will get a
date-time in this format `Fri 10 Nov 2017 14:03:59 GMT`. In summer
this would probably show a BST on the end I would guess - that's one
reason why I avoid this format, you'd have to start dealing with
setting clocks backwards and forwards and all that malarkey. By
sticking with UTC I never have to worry about that.

I hope you've found this article useful. Feel free to contact me or
borrow any of my code if you think it might be useful.

References:

* [Stack overflow article](https://stackoverflow.com/questions/7216358/date-command-on-os-x-doesnt-have-iso-8601-i-option#7216394)
* [Wikipedia ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)

---

Published: 2017-10-01 12:21:36 UTC
Updated: 2017-11-10 12:26:00 UTC 
UUID: 6768260E-5713-4899-BE43-130BF74DFED2
