# Generating ISO-8601 dates on Mac OS X

Published: 2017-10-01 12:21:36 UTC
Updated: 2017-11-10 12:26:00 UTC 

Summary: In this article I talk about how you can generate ISO-8601
format dates on the Mac OS X command line, and also how you can do it
in Python too.

As I go through the process of figuring out how to generate an Atom
feed for my site, I've stumbled on a couple of interesting issues. 

Getting an ISO-8601 date/time referenced to UTC:

``` shell
date -u +"%Y-%m-%dT%H:%M:%SZ"
```

Output:

``` shell
2011-08-27T23:22:37Z
```

Or this format give you the time difference with UTC:

``` shell
date +%Y-%m-%dT%H:%M:%S%z
```
Output:

``` shell
2011-08-27T15:22:37-0800
```

References:

* [Stack overflow article](https://stackoverflow.com/questions/7216358/date-command-on-os-x-doesnt-have-iso-8601-i-option#7216394)
* [Wikipedia ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)
