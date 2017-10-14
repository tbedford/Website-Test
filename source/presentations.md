# Presentations

Some recently watched presentations (with notes):


[Memory by Handmade Hero - Casey
Muratori](https://www.youtube.com/watch?v=MvDUe2evkHg&list=PLEMXAbCVnmY6Azbmzj3BiC3QRYHE9QoG7)

Wow! AMAZING VIDEO. If you have any interest at all in memory,
especially games - go watch this!

* Game allocation (asset management) is essentially a caching problem,
  not a GC problem.
* Fragmentation can be an issue because assets are of different sizes.
* Try to have fixed size allocators if possible.
* RAII - Resource Acquisition Is Initialization.
* Fascinating to see how other programmers work.

[Anatomy of a memory allocation by Jorge Rodriguez](https://www.youtube.com/watch?v=c0g3S_2QxWM)

Interesting video on memory allocation. The video looks at what
happens after you do a `new` in C++. I also learnt that the point at
the end of the heap, marking the void between the heap and the stack,
is called the 'break'. I hadn't heard that before but it explains why
the `sbrk` instruction has that name! 

The lack of speed in memory allocation comes from the usual culprits:
locking (to avoid context switching during memory allocation routines)
and context switching from user space to kernel mode (to extend the
heap if required) and then back again. There may be paging out to disk
(in the worst case scenario).

Interesting point is the constructor (in C++) is potentially unbounded
(in time). Not ideal for 'real-time' systems.

Things to read up on:

- Ring allocator
- Frame allocator
- Static allocator

[Deconstructing the OS](https://www.youtube.com/watch?v=h7D88U-5pKc)

Absolutely brilliant talk by Alfred Bratterud. Alfred is a great
presenter and this is a wonderful talk. Say what you like about the
old DOS days but you _were_ in control of your system. You could write
directly to the hardware (get a pointer to VGA memory, put a byte, and
yay a pixel in one of 256 colours). Of course with that power came a
certain danger. If a pointer went awry you could bring your system
down. With a single (protected) address space that is less likely. DOS
DPMI was the "protected mode" - you could have a crash control handler
that would get invoked if your code started to write to places it
shouldn't. Some of the "demoscene" demoes had built-in crash
protection handlers, which was pretty cool. On DOS you could access
hardware directly, and do things like intercept timer interrupts,
reprogram the CTC, read and write various ports and so on. I do like
the idea of Microkernels which this talk is about. Definitely one
worth watching.
  
[Unicode strings](https://www.youtube.com/watch?v=ysh2B6ZgNXk)

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

[Python, Fabric, Ansible by Tim
  Henderson](https://www.youtube.com/watch?v=4qav2EuXsGU) 
  
Not many presentations start with a poem, but this one does and it's
great. Very good presenter who speaks clearly and at the right
pace. Very useful presentation on managing systems.

[Rust and Concurrency by David
  Sullins](https://www.youtube.com/watch?v=oIikwmeGVYY)
  
As a programmer it's really important to understand concepts of
Resources, Ownership, Lifetime, Scope - and this is critical in a
concurrent context. One minor point, scope is not necessarily the same
thing as lifetime, at least in C (you can have a static variable in a
function with global lifetime but local scope).

[Kavya Joshi on Keeping Time in Real
  Systems](https://youtu.be/BRvj8PykSc4) 
  
Great talk on clocks and clock synchronization in distributed systems.
  
[You can be a kernel hacker by Julia
  Evans](https://www.youtube.com/watch?v=0IQlpFWTFbM) 
  
Wonderful talk by Julia Evans. She is a "high energy" presenter - you
won't be bored. I really like it when Julia uses /proc to recover a
deleted file. Cool. She is also very, very funny - the piece on how to
submit a kernel patch around 18 minutes in is hilarious. I _loved_
this talk! One of the best presenters I've seen in a while.

## Presentations yet to watch

[Making Allocators Work Part 1 by Alisdair Meredith](https://www.youtube.com/watch?v=YkiYOP3d64E)

Started.
