# Really simple encryption

Summary: In this article I take a look at a really simple encryption
system. Applications could include sending ever-so-slightly more
secure text messages via APIs such as Nexmo or Clockwork.

So I had to delve into SMS character sets and encoding a little bit
for [work](https://developer.nexmo.com) and stumbled on [this
article](https://www.clockworksms.com/blog/the-gsm-character-set/). This
got me thinking a little about reduced character sets. What if you had
restrictions around which characters could be sent over a network
channel? This got me remembering the days when "non-printable
characters" were a pain (actually, they still are). You'd think you
were printing a sane message only to receive a series of beeps and
strange characters. That's what happens when you try to print
non-printable characters. It would be simple enough to simply reject
characters outside of a range. What if you did not want to do that?
What of you also wanted to carry out a primitive encryption algorithm
on your string too?

A few lines of Python code later...

Yes, it's all very possible. So what I came up with is a simple
algorithm to encrypt characters in a certain range to a certain
range. That range was chosen arbitrarily to be 32 to 126. Well it's
not quite arbitrary. 32 is the ASCII character code for SPACE. The
first character we're interested in and it conveniently skips over
those nasty non-printables. 126 is the last but one character in the
ASCII table, which is a 7-bit character set. 127 is the last character
but that is assigned to the special character DEL. We can do without
that one.

So, here is the encryption algorithm with some Python code by way of
example. 

NOTE: It's important to point out that this is in no way meant to be
any kind of secure encrytion algorithm - it's just a curious little
bit of code really.

## The strings

There are three components here:

1. The plain text message to be encrypted.
2. The key used in the encryption algorithm.
3. The encrypted text message.

In each of the above cases the only acceptable characters are ASCII 32
through to and including ASCII 126.

## The algorithm

The encryption algorithm works in the following way:

1. Take the first character from the plain text message.
2. Take the first character of the key.
3. Add these character values. 
4. If the result is greater than 126 then subtract 95. If the result
   is still greater than 126 then keep subtracting 95 until the result
   is less than or equal to 126.
5. The result is the first character in the encrypted message.
6. Proceed to the next character in the message and the next character in the key.
7. If the key has no more characters but input message remains then
   return to the first character in the key.
8. Repeat until all characters in the plain text input message have been encrytped.

The decryption algorithm is the reverse of this process. It only works
if you are completely symmetrical in how you deal with the characters.

## Example code

``` python
# Python 3
# *****  NOTE: works with BYTE strings ONLY ***** 
import sys

DEBUG = False

k = b"PythonRocks"
m = b"This message is a little bit more secure than usual."

def reduce (c):

    while c > 126:
        c = c - 95
    return c

def expand (c):

    while c < 32:
        c = c + 95
    return c

def encrypt (k, m):

    es = b"" # es = encrypted byte string 
    kl = len(k) # Length of key byte string
    i = 0 # index into key byte string
    for c in m:
        # Encrypt char
        e = c + k[i]
        e = reduce (e)
        if DEBUG == True:
            print ("k is `%c` e is `%c` %d" % (k[i], e, e))
        es = es + e.to_bytes(1, byteorder='little')
        # Reset key index if required
        i = i + 1
        if i > (kl - 1):
            i = 0
        
    return es

def decrypt (k, m):

    ds = b"" # ds = decrypted string
    kl = len(k) # Length of key string
    i = 0 # index into key string
    for c in m:
        # decrypt char
        e = c - k[i] # subtract for decrypt 
        e = expand(e)
        ds = ds + e.to_bytes(1, byteorder='little')
        # Reset key index if required
        i = i + 1
        if i > (kl - 1):
            i = 0
            
    return ds

if (sys.version_info < (3, 0)):
    print ("Python version 3 and above only - join the future!!")
    exit(-1)

em = encrypt(k, m)
print (em)

dm = decrypt (k, em)
print (dm)
```

## Notes on the code

You'll notice the code above is for Python 3. I did also write a
Python 2 version and you use things like `ord()` and `chr()` to deal
with turning ASCII characters into their corresponding numbers and
vice versa. The main difference between Python 2 and Python 3 in this
respect is, as you may know, Python 3 stores strings internally as
UCS-4 Unicode codepoints. When you are reading and writing data from
files and communications channels, which might be UTF-8 multi-byte
encoded or similar, you need to make sure you encode and decode
appropriately. For example if the content of a file is UTF-8 you need
to decode that with a UTF-8 decoder when reading into Python. If you
are writing data in Python out to a UTF-8 encoded file you must use
the UTF-8 encoder.

So, in short, Python 3 stores strings internally as Unicode
codepoints, Python 2 does not. The above code has to take this into
account.

## Next steps

I've not quite finished with this. I will be revisiting this in a
future blog post. First, I want to put input messages and keys in
files, so they can be bulk encrypted. That should be an interesting
challenge as out in the real world things are often UTF-8 encoded in
files. How will we deal with that? I'm also pretty sure I did not
address the whole question of character sets and encodings very well
in this article, and am assuming a certain level of familiarity on
your part, but I think I will write something hopefully a bit clearer
on this subject in the future. I also got interested in Base64
encoding while doing some research for this article, so expect
something on that soon too.

## Resources

- https://developer.nexmo.com
- https://www.clockworksms.com


---

* Published: 2018-11-07 08:01:13 UTC
* Updated: 2018-11-15 08:01:13 UTC
* UUID: B0B83A78-451E-4C0D-88E9-4A78020946A5
