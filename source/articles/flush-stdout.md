# Don't forget to flush!

Summary: On solving a mysterious problem in a CGI web app.

So, here's a weird one. 

I had my little app working fine in a console. I could do a database
query and get back 800+ records no problem. So, I tried it deployed as
a web app and only about 400 records would get displayed. Weird.

A quick Stack Overflow search returned one guy who seemed to have a
similar problem - results were truncated in the web app deployment
mode. But no solution. 

I first thought the problem was the ouput code was choking on Unicode
characters - a problem that had occurred earlier in testing due to a
problem I [solved here](./stdout-utf-8-nastiness.html). But carefully
limiting the number of results returned showed that once the result
set got up to exactly 391 records, that was it - no more records would
come.

Then I had some flash of insight - no idea where that came from, but
it just happens now and then. Call it experience. It smelled like a
buffer wasn't getting flushed. How about stdout?

I whacked in a flush method call:

``` python
sys.stdout.flush()
```

Lo and behold - all 800+ records coming back - no problem.

It just goes to show, `stdout` in Python 3, may behave differently
depending on exactly what you are connected to - a tty? A socket? A
pipe?

And, one piece of advice, don't forget to flush!

---

* Published: 2017-10-07 09:11:12 UTC
* Updated: 2017-11-17 12:13:00 UTC
* UUID: B840D3C7-8B56-4F21-92EE-23381F9127EA


