# Presentations

Some recently watched presentations (with notes):

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

[Memory by Handmade
Hero](https://www.youtube.com/watch?v=MvDUe2evkHg&list=PLEMXAbCVnmY6Azbmzj3BiC3QRYHE9QoG7)

Note watch any videos by Handmade Hero yet, but they look very cool.


