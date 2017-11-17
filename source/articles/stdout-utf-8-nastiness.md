# Stdout was a bad, bad boy

Summary: Sometimes an application may open `stdout` with ASCII
encoding, rather than UTF-8.

There's two statements you hear bandied about with Python 3:

1. Python uses Unicode for all strings!
2. Python uses UTF-8 for the default character encoding!

The first is true enough, at least internally. Python uses Unicode
strings, coded in UCS-2 or UCS-4 (probably UCS-4 for you).

I discovered there's a gotcha with the second statement. 

So here's what happened. I was working on a database app for a
friend. He has a database with thousands of companies in there, and
the companies are based in Thailand mostly and some are
international. The database entries were compiled in Thailand, and
guess what? Some of the entries used Thai script! Oh weird, funny
squiggly characters everywhere! But nothing Unicode doesn't have a
codepoint for, and nothing UTF-8 can't encode.

So after some epic coding, the database app is all working nicely and
displaying records on the console. And then in a moment of madness
(well actually because he wanted to access the database over the web)
I got the thing working as a CGI web app, and the whole thing choked. And
after a closer look it seemed to be choking on the Thai characters. Oh
dear. I knew those squiggly characters were going to be trouble.

So, a quick check of my content header:

``` python
header = '''
Content-type: text/html; charset=utf-8


<html>
<head><title>Query Results</title></head>
<body>
<table border='1'>
<thead>
<tr><th>ID</th><th>Company Name</th><th>Location</th><th>Categories</th><th>Services</th></tr>
</thead>
<tbody>
'''
```

Well, I definitely have a UTF-8 in there.

After an overdose of caffeine I realized that while Python was happily
emitting a byte stream encoded in UTF-8, `stdout` itself was being
opened in `ascii` mode by Apache.

There was only one thing for it. I was going to have to grab `stdout`
by the scruff of the neck and tell it in no uncertain terms it **was**
going to have UTF-8 rammed up its bum and it had better like it!

I worked up a little output function to help out:

``` python
# Support Unicode characters in web stream
# Odd one - utf-8 does not appear to be selected for non-tty type output
# in some cases !!!
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
    
def write_out (s):
    print (s, end='\r\n', file=utf8stdout)
```

So, now `stdout` gets opened as UTF-8 whether it likes it or not! Now,
UCS-4 integers would already get encoded to UTF-8 on their way out
from Python land to the big wide world (by default), but now `stdout`
was configured explicitly to be compatible with them.

It all started working, `stdout` stopped choking. I breathed a sigh of
relief. Those squiggly characters became cute and cuddly rather than
the mark of the Devil.

All was good in the world, until I ran into _another_ problem with
`stdout`, but that's another story for another time.

## Things to remember

1. Python uses Unicode for strings (internally) in UCS-4.
2. Unicode strings needed to be encoded and decoded as they exit and enter Python.
3. `stdout` might not be opened with UTF-8 encoding (you might need to
   do it explicitly). For example, it is when working in a correctly
   configured terminal on Mac OS X, but may not be when opened by
   Apache.
4. You can explicitly specify the encoding when you open a file (file
   can be stdin, stdout, stderr)

## Useful Notes

`sys.getdefaultencoding()`
Return the name of the current default string encoding used by the
Unicode implementation.

There's a difference between Python running as an interpreter, as a
standalone application, as a CGI application on a web server.

`sys.maxunicode`
An integer giving the value of the largest Unicode code point,
i.e. 1114111 (0x10FFFF in hexadecimal).

Changed in version 3.3: Before PEP 393, `sys.maxunicode` used to be
either 0xFFFF or 0x10FFFF, depending on the configuration option that
specified whether Unicode characters were stored as UCS-2 or UCS-4.


`stdin`, `stdout`, `stderr`:

These streams are regular text files like those returned by the
`open()` function. Their parameters are chosen as follows:

The character encoding is platform-dependent. Under Windows, if the
stream is interactive (that is, if its **isatty()** method returns
True), the console codepage is used, otherwise the ANSI code
page. Under other platforms, the locale encoding is used (see
`locale.getpreferredencoding()`).

Under all platforms though, you can override this value by setting the
PYTHONIOENCODING environment variable before starting Python.

``` python
>>> locale.getpreferredencoding()
'UTF-8'
>>> 

>>> import os
>>> os.isatty(1)
True
>>> 

>>> sys.stdout.isatty()
True
>>>
```

Here's a little bit of debugging code I put at the start of my app to
figure out what was going on:

``` python
DEBUG_MODE = True

if DEBUG_MODE:
    cgitb.enable()

if DEBUG_MODE:
    if sys.stdout.encoding != 'UTF-8':
        error_str = '''
        <html>
        <body><h1>ERROR</h1></body>
        <h2>Encoding of stdout was not UTF-8 it was {}</h2>
        </html>
        '''.format(sys.stdout.encoding)
        print (error_str)
        exit()
```

---

* Published: 2017-10-19 07:17:12 UTC
* Updated: 2017-10-19 07:17:12 UTC
* UUID: 2DE35009-4AA6-48CB-B99D-0FFB8B722748


