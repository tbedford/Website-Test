# Links

## Funny

* [A hilarious video on developers](https://www.youtube.com/watch?v=ocwnns57cYQ)

## General

* [FaceBook's tech research website](https://research.fb.com)
* [FaceBook code](https://code.fb.com)
* [FaceBook Open Source](https://opensource.fb.com)
* [Superscale Networks use Rust and Linux-based routers](https://www.superscale.io)
* [Great website by Paul Hsieh](http://www.azillionmonkeys.com/qed/index.html)
* [Hashing functions](http://burtleburtle.net/bob/c/lookup3.c)
* [Try out old DiskMags - very cool!](https://archive.org/details/diskmags?and[]=subject%3A%22MS-DOS+diskmags%22)
* [Handmade Hero Episode Guide](https://hero.handmade.network/episodes)


## Documentation systems

* [Docusaurus](https://docusaurus.io/blog/2017/12/14/introducing-docusaurus)

## Character sets and encoding

* [Strange details of strings at FaceBook](https://www.youtube.com/watch?v=kPR8h4-qZdk)
* [Unicode strings](https://www.youtube.com/watch?v=ysh2B6ZgNXk)

Interesting presentation. Interesting that U+21B4 requires three bytes
if encoded in UTF-8 and only two bytes with UTF-16 - which explains
why UTF-16 is commonly used for non-latin (e.g. Japanese) character
encoding - it's a lot more efficient at encoding those non-latin
characters. I think what they are doing with
[CopperSpice](http://www.copperspice.com/index.html) is also
interesting. It's amazing the state (i.e. mess) of many legacy
libraries when it comes to encodings. Also have a [YouTube
channel](https://www.youtube.com/copperspice). Documentation on
[string
terminology](http://www.copperspice.com/docs/cs_string/overview_terminology.html).


## Databases/distributed data

* [RethinkDB and real-time web apps](https://www.rethinkdb.com/blog/realtime-web/)
* [Berkeley DB architecture](http://www.aosabook.org/en/bdb.html)
* [RocksDB blog](http://rocksdb.blogspot.co.uk)
* [RocksDB research topics](http://rocksdb.blogspot.co.uk/2017/04/research-topics-in-rocksdb.html)
* [History of RocksDB](http://rocksdb.blogspot.co.uk/2013/11/the-history-of-rocksdb.html)
* [Riak's Bitcask overview](http://highscalability.com/blog/2011/1/10/riaks-bitcask-a-log-structured-hash-table-for-fast-keyvalue.html/)
* [Bitcask intro paper](http://basho.com/wp-content/uploads/2015/05/bitcask-intro.pdf)
* [Excellent talk on CoackroachDB by Alex Robinson](https://www.youtube.com/watch?v=6OFeuNy39Qg)
* [Redis LRU algorithms](http://antirez.com/news/109)
* [Spencer Kimball on history of database](https://www.youtube.com/watch?v=TA-Jw78Ms_4)
* [Crate Scalable SQL](https://crate.io)
* [Riak revisited podcast](https://changelog.com/podcast/40)
* [Wallaroo Labs - users of Pony](https://www.wallaroolabs.com/technology)
* [Google Megastore](https://research.google.com/pubs/pub36971.html)
* [Google Bigtable](https://research.google.com/archive/bigtable.html)
* [Google Spanner](https://research.google.com/archive/spanner.html)
* [Lucene segment merges](http://blog.mikemccandless.com/2011/02/visualizing-lucenes-segment-merges.html)
* [Programming SSDs by Emmanuel Goossaert](http://codecapsule.com/2014/02/12/coding-for-ssds-part-1-introduction-and-table-of-contents/)
* [Distributed systems by Emmanuel Goossaert](http://codecapsule.com/2016/01/03/how-to-get-started-with-infrastructure-and-distributed-systems/)
* [LSM advantages over B-tree](http://smalldatum.blogspot.co.uk/2016/01/summary-of-advantages-of-lsm-vs-b-tree.html)
* [Amazing amount of info on databases](https://db-engines.com/en/)


## Games tech

* [Memory by Handmade Hero - Casey
Muratori](https://www.youtube.com/watch?v=MvDUe2evkHg&list=PLEMXAbCVnmY6Azbmzj3BiC3QRYHE9QoG7)

## Information Retrieval / Search

* [Free IR book online](https://nlp.stanford.edu/IR-book/html/htmledition/irbook.html)
* [Interview with Matt Wells of Gigablast (PDF)](http://www.gigablast.com/acmqueue.pdf)
* [Gigablast costs](http://www.gigablast.com/searchfeed.html) - Bing also offers a paid search API (free on small scale)

## Operating systems tech

* [Deconstructing the OS](https://www.youtube.com/watch?v=h7D88U-5pKc)

* [Rust and Concurrency by David
  Sullins](https://www.youtube.com/watch?v=oIikwmeGVYY)
  
As a programmer it's really important to understand concepts of
Resources, Ownership, Lifetime, Scope - and this is critical in a
concurrent context. One minor point, scope is not necessarily the same
thing as lifetime, at least in C (you can have a static variable in a
function with global lifetime but local scope).

* [Kavya Joshi on Keeping Time in Real
  Systems](https://youtu.be/BRvj8PykSc4) 
  
Great talk on clocks and clock synchronization in distributed systems.
  
* [You can be a kernel hacker by Julia
  Evans](https://www.youtube.com/watch?v=0IQlpFWTFbM) 
  
Wonderful talk by Julia Evans. She is a "high energy" presenter - you
won't be bored. I really like it when Julia uses /proc to recover a
deleted file. Cool. She is also very, very funny - the piece on how to
submit a kernel patch around 18 minutes in is hilarious. I _loved_
this talk! One of the best presenters I've seen in a while.



## Syndication / publishing protocols

* [Dive into Python 3 - Atom notes](http://www.diveintopython3.net/xml.html)
* [Python Universal Feed Parser](https://pypi.python.org/pypi/feedparser)
* [Atom publishing protocol](https://www.ibm.com/developerworks/library/x-atompp1/index.html)

## Python

* [Python, Fabric, Ansible by Tim
  Henderson](https://www.youtube.com/watch?v=4qav2EuXsGU) 
  
Not many presentations start with a poem, but this one does and it's
great. Very good presenter who speaks clearly and at the right
pace. Very useful presentation on managing systems.

* [LXML Python XML library](http://lxml.de)

## Memory

* [Making Allocators Work Part 1 by Alisdair Meredith](https://www.youtube.com/watch?v=YkiYOP3d64E)
* [Anatomy of a memory allocation by Jorge Rodriguez](https://www.youtube.com/watch?v=c0g3S_2QxWM)
* [Memory and C++ debugging at EA by Scott Wardle](https://www.youtube.com/watch?v=8KIvWJUYbDA)
* [Julia Evans on memory profiling](https://jvns.ca/blog/2018/02/06/profiler-week-5/)
* [Scudo hardened memory allocator](https://llvm.org/docs/ScudoHardenedAllocator.html)
* [General article on memory allocators - good background reading before implementation](http://www.flounder.com/memory_allocation.htm)
* [Are we out of memory?](http://www.swedishcoding.com/2008/08/31/are-we-out-of-memory/)
* [Inside a storage allocator](http://www.flounder.com/inside_storage_allocation.htm)

## Data compression

* [Snappy compression](http://google.github.io/snappy/)
* [History of data compression in Japan](http://oku.edu.mie-u.ac.jp/~okumura/compression/history.html)
* [Data compression course](http://www.fadden.com/apple2/hdc/index.html)
* [FaceBook's Zstandard](https://facebook.github.io/zstd/)

## Pony

* [An early history of Pony](https://www.ponylang.org/blog/2017/05/an-early-history-of-pony/)
* [Blog post on using Pony](https://blog.wallaroolabs.com/2017/10/why-we-used-pony-to-write-wallaroo/)

## Erlang

* [Learn you some Erlang - free book](http://learnyousomeerlang.com/content)

## C/CPP

* [Strange details of strings!](https://www.youtube.com/watch?v=kPR8h4-qZdk)
* [C file I/O](https://www.cs.bu.edu/teaching/c/file-io/intro/)
* [Unicode and wchar_t](http://icu-project.org/docs/papers/unicode_wchar_t.html)
* [Hashtables in C](https://stackoverflow.com/questions/6118539/why-are-there-no-hashtables-in-the-c-standard-library)

## Go

* [Go strings](https://blog.golang.org/strings)

## Emacs

* [Emacs article](https://blog.fugue.co/2015-11-11-guide-to-emacs.html)
* [Emacs keybindings](http://www.cs.colostate.edu/helpdocs/emacs-bindings)
* [Extensive info on Emacs key bindings including hard to find syntax](http://www.nongnu.org/emacs-tiny-tools/keybindings/)
* [Great Emacs related info and blog by Sacha Chua](http://sachachua.com/blog/category/emacs/) 

## Travel

* [Trip Advisor API](https://developer-tripadvisor.com/content-api/description/)
* [Hotel global ID](https://www.tnooz.com/article/can-the-latest-dip-into-the-global-hotel-id-swamp-work/)
* [Open travel specs](http://www.opentraveldevelopersnetwork.com/implementation-guide)
* [Travel companies defeating web scrapers](https://www.tnooz.com/article/how-icruise-com-defeated-web-scrapers-with-distil-networks/)

