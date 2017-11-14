# How Python saved my sanity!

They were dark days.

I had to build 12 million lines of J2EE code before breakfast and
Maven wasn't having any of it. The work day was spent in a
caffeine-fuelled daze. Nothing seemed to work. You've heard of the
Midas Touch? I had the opposite - everything I touched turned to
shit. Everything was drenched in complexity and the software fragile
at the best of times. DevOps would spend a week raving about some new
Chef or Puppet script and then the deployed system would just fart and
crap its pants. Databases imploded left, right and centre. It wasn't
supposed to be this way.

I was getting stressed and burnt out. Small companies would come to me
with real-world business problems and I would look at Java and
"enterprise tools" and want to poke my own eyes out..

By 2014 I was on the road to quitting the IT business after over 30
years in it. I'd worked as a coder, a trainer, a tech writer, a
manager. I felt like I'd done it all and had the freebie conference
T-shirts to prove it.

I wanted out. I was becoming jaded and cynical about the business and
software in particular. Web apps made me laugh like a rabid
hyena. Someone wrote a web app to tell you when to go to pee-pee and
the irony of it was lost on many. I realized we'd jumped the shark. I
was becoming majorly depressed.

And then one day I got an itch that needed scratching - and I'm not
talking about fleas. It was the run up to Christmas 2015. I had a
couple of days free. I was catching up on some reading on a website
I've been visiting since 2002. It's a great site. Mostly
travel-related writing, but delves into relationships and various
other things.

It was one of those sites that was very old school. It was all static
HTML files created in FrontPage. Anyone remember FrontPage? It was The
Dog's Balls back in the late 1990s, early 00s, when the site was
started. While the content was great the site design sucked. It used
really bright white and lurid coloured text on a black
background. Reading for any more than 10 minutes and you felt like you
were going blind. There was no CMS involved so you couldn't do dynamic
queries, say for all articles by a certain contributer. Finally I'd
had enough.

I figured I could write a little app to download the web pages, and
perhaps tidy them up, save them out as text files, and then maybe
whack them in a database so I could do proper queries to find articles
based on submission date or author. I could even add a little CGI web
app on the front end to pull the articles from the database.

I reached for Eclipse and experienced something resembling a small
cranial haemorrhage. I just couldn't. Writing the Java to do it would
be painful, and I just didn't have the time or energy, or the desire
to be even more insane than I already was.

PHP was the next option. I'd done a project previously in PHP,
a command line set of tools for turning DITA XML into HTML 5. It had
worked out quite well although I ran out of time on the project. PHP
could certainly do it. But I remembered I'd had a hard time when I
came back to the PHP codebase 6 months later, trying to figure out
what the heck I'd done. There was too much line noise, too many $s and
too many things that seemed like a good idea at the time but turned
out to be very horrible (and mostly my fault).

Could Python help?

A few characters typed at the terminal confirmed I had Python already
installed on my MacBook Pro. I figured it couldn't be worse than PHP.

I wrote a little spider program. It worked. Soon I had about 8000
articles downloaded and Python was flinging text files around and
whacking things into MySQL and I was running queries and getting back
useful results. 

``` python
# Inject all records into MySQL database

import pymysql

# Open input file

f = open ('sub_lists/article_data.dat', 'r')

# Open connection to database
conn = pymysql.connect(host='localhost', user='xxxxxx', passwd='xxxxxx', db='articledb', charset='utf8mb4')
cur = conn.cursor()

# Select database to use
cur.execute("USE articledb")

for line in f:

    line_array = line.split('|')
    url = line_array[0].rstrip('\n')
    title = line_array[1].rstrip('\n')
    sub_date = line_array[2].rstrip('\n')
    author = line_array[3].rstrip('\n')

    print("Injecting record: ", title, sub_date)
    sql = "INSERT INTO `Articles` (`url`, `title`, `sub_date`, `author`) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (url, title, sub_date, author))

    # Must do this!
    conn.commit()

# Clean up!
cur.close()
conn.close()
f.close()
```

I then wrote a little author stats program in about five minutes that
worked first time:

``` python
# author_stats.py

filename = "sub_lists/article_data.dat"
authors = []

f = open(filename, 'r')

for line in f:
    record = line.split('|')
    authors.append(record[3].rstrip('\n'))

f.close()

stats = {}

for author in authors:
    if author in stats:
        stats[author] = stats[author] + 1
    else:
        stats[author] = 1

i = 0
for author in sorted(stats, key=stats.get, reverse=True):
    print (i, ": ", author, stats[author], " : %.2f" % (stats[author]*100/8782))
    i = i + 1
```

I was getting real insight into the authors and how frequently they
submitted, how many pieces they'd written and how long they'd been
writing for the site. This was real data mining (albeit on a small
scale). And what's more I was having a blast! Suddenly programming was
not only productive - it was fun again.

My two day coding adventure with Python came to a close, all too soon,
but it was a revelation. Programming could be productive and fun! Who
knew? Python programmers I guess.

I'd like to say I saw the light at that point and became a raving
Python fanatic. I was sold, but didn't get much chance to do Python
coding again for a while. Until a friend who owned a small company
came to me with some business problems that needed solving and Python
was a good match. But that's another story...

Python has been a Godsend. It's a very readible and clean
language. It's very capable. It can crunch text, HTML, XML and pretty
much any type of file you can throw at it. It can read and write
databases, you can build simple but effective web apps in it.

Python restored my faith in programming, and it restored any semblence
of sanity I may have had left.

Thanks Python. I owe you. Big time.


