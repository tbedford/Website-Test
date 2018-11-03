# Understanding Unix time

Summary: This article takes a look at the idea behind Unix time. It
also shows you how to get the current Unix time from the shell and
from Python. The concept of the Unix timestamp will be used again in
subsequent articles.

## What is Unix time?

Unix time is the number of seconds that have elapsed since midnight
(00:00:00), Thursday, 1 January 1970, UTC, not including leap
seconds. 

If you read my piece on [dealing with
dates](./dealing-with-dates.html) you'll know this particular date can
be represented in ISO-8601 format as 1970-01-01T00:00:00Z. This
reference point in time is known as the Unix Epoch.

As with many timing schemes based on computers or atomic timing
devices, there is a difference between these absolute times and
astronomical times. This is because astronomical times are based on
the Earth's rotation and this is not exactly consistent. Discrepencies
therefore creep in over time. Leap seconds are therefore required to
adjust UTC to resynchronize it with astronomical time.

Since 1970 only positive leap seconds (insertions) have been added to
a day, and no negative leap seconds have been required (yet). 

Unix time treats _each and every day_ as exactly `24 * 60 * 60`
seconds, which is 86400 seconds, and so does not take into account
leap seconds. Unix time is therefore equivalent to the value of UTC
seconds since midnight 1st January 1970 minus one second for each leap
second since the Epoch. Since UTC was introduced in 1972 there have
been 27 leap seconds inserted into it, so, as I write this, it is:

``` shell
Unix time seconds = UTC seconds (since midnight 1st January 1970) - 27
```

There's a slightly strange area between 1st January 1970 and 1st
January 1972 because UTC wasn't introduced until the latter of those
dates.

There's quite a bit of controversy around leap seconds, and how to
implement them in Unix libraries, and even a move to just get rid of
them completely. As far as Unix time is concerned though, to all
intents you can ignore them unless you are trying to convert between
Unix timestamps and UTC and vice versa. I have provided some links
below though in case you are a masochist - it's gnarly stuff...

So moving swiftly on to more practical matters...

## Working with dates

If you run `date` on the command line:

``` shell
date
```

You would get a datetime in a human readable format:

``` shell
Tue 30 Oct 2018 14:35:59 GMT
```

To obtain UTC time you can do:

``` shell
date -u
```

This would return a date in the format:

``` shell
Tue 30 Oct 2018 14:47:27 UTC
```

> NOTE: In UK we just came off BST this weekend, so GMT and UTC are essentially the same thing. 

You can also obtain an ISO-8601 format UTC date using:

``` shell
date -u +"%Y-%m-%dT%H:%M:%SZ"
```

## Working with Unix time

On the command line you can easily find Unix time with:

``` shell
date +%s
```

This would result in a number such as:

``` shell
1540910388
```

Which is the number of **seconds** since Unix Epoch (ignoring leap seconds).

There's also a quick bit of Python code you can run in the shell to
obtain Unix time rounded to whole seconds:

``` shell
python -c 'import time; print int(time.time())'
```

Which you can easily convert to years:

``` shell
python -c 'import time; print int(time.time()) / (365 * 24 * 60 * 60)'
```

## What's Unix time good for?

Mostly Unix time is used for timestamps on files, events, and other
data (such as in databases) and is not really used for "calendar time"
directly. However, there are various utilities that will convert
correctly between a Unix timestamp and a UTC datetime (the web appears
to be awash with them for some reason).

Because a Unix timestamp is simply a number with respect to Unix
Epoch, it is easier to compare two Unix timestamps (you just find the
difference in seconds) than it is to compare two ISO-8601 format
dates.

Unix time also has the advantage that it is completely indifferent to
timezones and daylight savings adjustments. It is simply the number of
seconds since the Epoch. This is especially useful as a means of
specifying time in a web app where users may be geographically
distributed.

Unix time is used in timestamps in other applications too. One that we
will be looking at in a forthcoming article is in timestamps for JSON
Web Tokens (JWTs).

## The Y2038 Problem

There's a problem with some systems where Unix time is stored in a
32-bit integer. This is due to overflow on January 19th 2038. Modern
systems circumvent this issue by using a 64-bit integer for Unix time,
which will probably be enough to last until all known civilizations
(and a few unknown ones) fall into the final black hole.

In Y2038 I will be 76 (if still alive and kicking) and no doubt
sporting a long white Unix hacker beard and grumpily shooing a
multitude of grandchildren away from my carefully preserved Apple
MacBook Pro (hahaha), which uses a silicon-based processor (hahahaha),
with a clock speed of 2.5 GHz (hahahaha) and 16GB RAM
(hahahahahahaha). They will flaunt and frolic with their neural net
bio-processors, running Neural OS 12.1, while I remember when a Unix
timestamp was considered a pretty neat and useful thing.

## Summary

Unix time, in the form of simple timestamps, is used anywhere that an
absolute measure of time since the Unix Epoch is required. Unix
timestamps are independent of timezones, daylight savings adjustments,
leap second adjustments, and various UTC and ISO style formatting
concerns. They are easy to generate on the command line, or in
code. All major programming languages have support for Unix time built
in. In a forthcoming article we will look at how Unix timestamps are
used in generating JWTs.

## Resources

* [It's all a big mess!](http://www.madore.org/~david/computers/unix-leap-seconds.html)
* [Why 1st January 1970?](https://www.wired.com/2001/09/unix-tick-tocks-to-a-billion/)
* [Unix Time on Wikipedia](https://en.wikipedia.org/wiki/Unix_time)
* [More on leap seconds from the inventor of NTP](https://www.eecis.udel.edu/~mills/leap.html)

---

* Published: 2018-10-30 17:03:12 UTC
* Updated: 2018-10-30 17:03:12 UTC
* UUID: F4020C79-4516-4BB0-933A-6B5019260AA0

