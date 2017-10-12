# Python env issue on Ubuntu 16.04

I ran into an odd issue a few months back. I thought I should ut this
up here in case anyone else runs into it. I was setting up an Ubuntu
VPS on Digital Ocean (love it by the way). I had both Python 2.7 and
Python 3.5 installed. However, when I wrote a test script it wasn't
working. Here's what I had in my `testme.py` file:

``` python
#!/usr/bin/env python 

# Python goodness
...
```

Only, when I ran the script `./testme.py` I got the following error:

``` shell
/usr/bin/env: no 'python'
```

Basically, `env` couldn't find Python. Hadn't I just installed both
versions of Python?!

Now this wasn't one of those `chmod` issues. I had done a `chmod +x
testme.py` already.

After some head scratching, checking the installed binaries
highlighted the issue. The `locate` command is a blessing here by the
way. Python 2.7 and 3.5 **were** installed. `/usr/bin/python2.7` and
`/usr/bin/python3`. But no soft link to `/usr/bin/python`!

I can see why they did that. It's up to you to decide whether you want
`python` (`/usr/bin/python`) to run 2.7 or 3.x.

Fair enough!

The fix was easy enough. I wanted to use Python 2.7 in this case so I
created a softlink:

``` shell
sudo ln -s /usr/bin/python2.7 /usr/bin/python
```

Job done. Sort of thing that can catch newbies like me out!
