# Wolfenstein's memory manager

I just bought [Fabien Sanglard's](http://fabiensanglard.net) Game
Engine Black Book which is now available on Kindle. It looks like a
great book and I will do a full review once I've read all of
it. However, I dived straight to the section on Id's memory manager
for the game. I've put together some notes based on Fabien's work and
looking at the Wolf 3D source code (the original version - there are
various codebases out there.)

The first question of course is why have a custom memory allocator at
all? The problem is using `malloc()` leads to memory fragmentation as
I have talked about on this site and in my extensive notes on
allocators in my GitHub. 

The problem with memory fragmentation is that when your memory map
looks like Swiss cheese (that is, it's full of holes) it can be that
an individual hole is not big enough to satisfy a memory request. The
game then fails as it cannot load the required texture, level or sound
effect.

What you really want to do is take all those lovely holes (free space)
and squash them all together so that they make up a much more usable
free space lump. This is memory defragmentation or compaction.

Unfortunately `malloc()` does not compact memory (or at least it did
not back in the days of Turbo C - around 1992). Hence the need for the
custom allocator.

You have to remember that back in 1992 when Wolf 3D was released the
systems of the time could be considered "memory constrained". The
[Intel 80286](https://en.wikipedia.org/wiki/Intel_80286), which was
the target of Wolf, had a 24-bit address bus. In theory that meant it
could address a 16MB address space. However, most 286-based PCs at
that time had 1MB. The reason for this was due to the fact that RAM
upgrades were hideously expensive (expect to pay something like $1,500
for a 4MB expansion card - yes that is MegaBytes - not GigaBytes).

Also, DOS, which was the prevalent operating system at the time, was
essentially designed for the 8086 chip which had a 20-bit address
bus. The memory setup on DOS machines was complicated, but basically
you had a 640K "conventional memory" area where the program code and
most data was stored. Then, depending on your setup, you might have
access to the memory between 640K and the 1MB point, and some data
could be stored there.

So with all this and complications such as XMS, EMS and upper memory
areas, and the need for compaction, the memory manager had to be a
custom job.

The Wolf memory manager uses an interesting design. Rather than
keeping a list of free blocks it actually keeps a list of allocated
blocks. As memory is allocated and freed the memory map becomes
fragmented, and you have "holes" (free memory) between the allocated
blocks. The Wolf memory manager scans the memory map for these holes
and uses them.

It's a bit more complicated than that though because Wolf also has the
idea of purgeable blocks. When memory is allocated you can specify a
block as purgeable. When the manager scans for a free block it can
discard purgeable blocks and reuse their space. This purging idea is
neat because it provides a way to make room for new assets to be
loaded. 

A problem can arise though if you are low on memory and you have a lot
of objects in a scene and what happens is the memory manager purges
blocks to try and create free space and then reloads those same assets
as they are required for the scene. You end up with thrashing going
on. 

You would expect the frame rate to drop off a cliff at this point
because the manager will scan the block list, purge it to try and make
space, and then reload assets - all this takes time.

Thrashing might happen on a PC with only conventional memory as the
user has not set up the system to use the area above 640K - or has
that area clogged up with so-called Terminate and Stay Resident
programs (TSRs). TSRs were "a thing" back in the DOS days.

Of course even with purging, you can still end up with fragmentation,
and a subsequent "out of memory" error.  So the Id memory manager has
another trick up its sleeve - compaction.

Compaction in this implementation involves copying allocated blocks so
they are contiguous. This eliminates the holes between allocated
blocks, in effect collecting the holes together at the upper end of
the memory map in a contiguous free space. In other words you gather
all the little holes into one big hole!

This is somewhat complicated in the implementation as some blocks are
deemed locked and so cannot be moved. I've not investigated this in
detail but at a guess I would say that some data in memory is
transferred by the DMA controller, say from RAM to the Sound Blaster
card, and if you moved the source memory, the DMA controller would
quite happily copy over incorrect data, the original source data
having moved!

The list of allocated blocks is structured as a singly linked-list,
which is set up with a head pointer and a "rover", which points to the
last block in the list before the wilderness. 

There's an interesting point here which is when you keep a list of
free blocks you can embed the list node data structure in the free
block itself, as it's not being used for anything - it's free
memory. However, if you keep a list of allocated blocks like the Wolf
memory manager, where do you store the list node data structures?

Looking at the source code, what Wolf seems to do is allocate memory
for the list node data structures on the stack by simply allocating an
array. It looks like the array is hardcoded to have enough space for
700 list nodes. I'm guessing this number was based on John Carmack's
familiarity with the requirements of the game, some basic
instrumenting, and a bit of trial and error. You have to remember this
is a game-specific allocator, not a general purpose allocator. You
could not really get away with hard-coded limits like this in a
general purpose allocator.

There's also another interesting little aspect. When you do a
compaction and move blocks of data, it means that the pointer to the
original allocation is no longer valid. How is this dealt with? 

Well there are a couple of possible approaches. One is to use memory
handles which are a lookup into a table of pointers. If a pointer is
moved then the pointer entry in the table is updated, but the handle
is unchanged and still valid.

What the Wolf memory manager does is store a pointer to the original
returned pointer in its allocated memory block data structure. This
pointer to a pointer is called the `Usepointer` (U). This points to
the memory pointer (M) which is the thing that actually points to the
allocated memory area that the application will use.

In other words the application uses the pointer M, but the memory
manager uses U. If a block of allocated memory is moved during
compaction, U is dereferenced in order to update the value of M. 

I'm not quite sure what would happen if the game logic made a copy of
the M pointer and then manipulated itself to process a block of
memory. You would then have a potentially rogue pointer on your
hands. However, it's possible I didn't fully understand how the
usepointer is used. I will need to spend some more time on that to be
absolutely sure.

John Carmack himself has said that custom memory managers are a source
of many bugs. Any code that has a lot of pointer manipulation (think
lists, queues, circular buffers, trees etc.) are a rich source of
bugs.

Overall the Wolf memory manager is a clever piece of software that
John Carmack wrote when he was just 21 years old. When you consider it
was just one of many ground-breaking pieces of technology he had to
create in order to get a fast First Person Shooter up and running fast
on the limited hardware of the time, it really puts into perspective
what an amazing achievement it was.


