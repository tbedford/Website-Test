# Don't forget the Unix tools

So many times we get lost in complexity. But the core ideas of Unix
helps me stay sane in an insane world. The idea of small, single
purpose tools, that you can chain together through pipes to create
custom processing, is just so powerful. Keeping things in plain,
simply delimited text files, and being cogniscent of standard input
and output in your tool design helps massively too.

Of course with a generation of computer users brought up on Windows
and "ICT" at school it's easy to dismiss a concept with origins in the
1970s. All those funny beards and flared trousers -
so...yesterday. Until you are bogged down in endless Java minutiae and
can't see the forest for the trees and you are wondering why you
didn't become an actuary like your mum told you. It's all too easy to
forget the lessons of Unix, and the great value of its approach.

I was reminded of that value just the other day. A company I do some
occasional odds-and-sods for has a giant multi-purpose Excel
spreadsheet with lots of data (yes, one of those, horrible things that
they are). They needed some data generated from the master spreadsheet
based on a simple filter. Now I guess you _could_ do that in Excel
VBScript or something...but I don't have Word installed and really
don't want Word installed to be honest.

Then I remembered this little Unix tool called `cut`. And Google
Sheets (where they store the master) lets you export as TSV. Very
sensible that. Oh the joy of simple tools and plain text file
processing.

It took about a minute to write and test the following, and I probably
could have made the syntax a little more succint too:

``` shell
$ cut -f2,4,7,9 master.tsv | grep NDT | cut -f1-3 > ndt.tsv
```

Imagine doing the same thing in Java. Sweet Christmas.

Within a couple of minutes I had the required email list imported into
MailChimp and had a coffee and blueberry muffin lined up as a
reward. Happy customer. Happy me.

Reference:

[Unix Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy).
