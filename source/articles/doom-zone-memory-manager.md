# Doom Zone Memory Manager

Summary: On the mysteries of the Doom Zone Memory Manager.

So Fabien Sanglard's Game Engine Black Book - Doom dropped through the
letter box yesterday, just about 25 years after the original Doom was
uploaded. On first inspection the quality of the book blew me
away. Syntax coloured code snippets, colour diagrams, photos, trivia,
detailed tech explanations - wonderful stuff and I'm sure this book
will keep me engrossed over the xmas period. One section I already
read though was the brief section on Doom's Zone Memory Manager.

One question that I'd always wondered about - what were these
mysterious zones? Looking at the code there is only ever one zone -
main zone. So, why zone memeory allocator?

Fabien says in the book that the intention originally was to support
multiple zones, but with the introduction of DOS 4GW, the Watcom DOS
extender, the 32-bit flat model became availble.

This suggests perhaps that originally Doom was targeting machines that
had a segregated memory map - with DOS, upper memory, extended memory,
exapnded memory and all that nonsense that made the original Wolf 3D
such a nightmare to work with. Personally I think this is unlikely. I
think the more likely explanation is to do with memory fragmentation.

One of the problems in games is that memory allocations come in all
shapes, sizes and durations. Some are small allocations in the range
less than 1k, other allocations may be tens or hundreds of K in
size. Some allocations are brief and quickly freed, some are static
for the diuration of the game. So frequency and lifetime of
allocations can be quite varied.

All this leads to fragmentation of the memory map, where your map ends
up looking like swiss cheese. One solution is to use something like
the original Wolfenstein's compacting allocator, where memory is moved
around to create a big contiguous free memory space. Another solution
is to use [buffer
pools](https://coffeeandcode.neocities.org/diving-into-the-buffer-pool.html)
where allocations of fixed size can be made, thus reducing the chance
of a failed allocation due to fragmentation. 

The idea behind a Zone memory allocator is that you have Zones where
memory allocations of a particular size are made. For example, you
could have a Zone where allocations less than 1K are made. You could
have another zone for allocations from 8K to 32K. You could have
another Zone where allocations greater than 100k are made and so
on. The actual zones would depend on the nature of the app, in this
case the game.

The idea behind this is by keeping allocations of approxinately the
same size in the same zone you reduice fragmentation, compared to the
case where you have a single zone where you have lots of tiny
allocations (for say a texture) and big allocations for level data,
sound effects and music etc. When the small allocations are freed up
you end up with lots of little gaps in your map, meaning the chances
of finding a contiguous free space of a sufficient size for a larger
allocation reduces. 

In the end Doom did not use this approach, but I think that may have
been the original intention. Probably what was found was that on
profiling the game the single zone was sufficient, or they simply ran
out of time to add in the support for multiple zones. 

One strong piece of evidence in favour of this idea was from Carmack
himself, who [stated](https://doom.fandom.com/wiki/Zone_memory) in a
code comment "the only stuff that might have been useful for
Quake". If you look at the memory manager in Quake 1 you can see that
the memory was split into "zones" for different purposes. You can see
that Doom's Zone Memory Manager code was reused in Quake, but it
serves only to provide allocations for small dynamic allocations
e.g. temporary strings. In effect the Zone memory manager ended up
being used to manage the "zone" for small allocations, which is
somewhat ironic.

## Doom's skies and backdrops

As minor digression at this point. Those backdrops in Doom such as the
mountain views and skies and city skylines had always fascinated
me. Fabien reveals in his book where those images actually came from -
I was really surprised! The book is full of gems like this and I have
only scanned through it. I'm sure many more Doom secrets will be
revealed when I read things in more detail.

## Summary

In summary Doom's Zone Memory Manager has always fascinated me, and it
was interesting to read Fabien's description of it. The Game Engine
Black Book - Doom is an absolutely fantastic resource, if you have any
interest in game technology, or the history of Doom it is a Must Buy.


## Resources

* [Wolfenstein's compacting memory allocator](https://coffeeandcode.neocities.org/wolf-memory-manager.html)
* [My experimental memory allocator - first version](https://github.com/tbedford/Ant-Allocator/tree/master/attempt1)
* [Quake Zone Memory Manager](https://github.com/id-Software/Quake/blob/master/WinQuake/zone.h)

---

* Published: 2018-12-13 08:14:22 UTC
* Updated: 2018-12-13 12:13:00 UTC
* UUID: C9945431-87D7-45BC-B83B-442BBA0D2FE2



