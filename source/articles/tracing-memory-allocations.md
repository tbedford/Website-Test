# Tracing memory allocations

Summary: On various attempts to try and trace memory allocations.

Having written the basis of a simple memory allocator, I was thinking
about debugging memory allocations. Of course there are various tools
out there such as `dmalloc`, Electric Fence, Valgrind and so on. I had
a quick look at `dmalloc` and realized I could spend a week figuring
it out. So I wondered what could be put together in a few
minutes. Basically I wanted to at least print out the line number and
file that a `malloc()` was called from.

The approach I took, which I think is quite common, is to interject a
fake malloc which does my tracing and possible other clever stuff,
before calling the real `malloc()`.

My first attempt used functions pointers and was an epic fail. I
created a `fake_malloc()` and the idea was to do this:

1. Set a function pointer `real_malloc` with `malloc`. `real_malloc`
   now points at `malloc` - if you call `real_malloc()`, `malloc()`
   actually gets called. This bit worked fine.
2. Create a new function `fake_malloc` which has my tracing in it.
3. Set `malloc = fake_malloc`, so that whereever I have `malloc` my
   `fake_malloc` would actually get called. I couldn't get this to
   work.  The compiler doesn't like you assigning something to
   `malloc` - even a function pointer.
   
I then tried another approach where I tried to #define malloc to
fake_malloc, but I couldn't quite get the syntax right to make this
work. Does anyone out there know?

So, after a bit of reading on Stack Overflow I discovered there are
another couple of cool ways you can do this. The first was using GCC's
`--wrap=malloc` option. This allows you to wrap any function with a
wrapper function of your own design. But, this only works for GCC. I'm
using `clang` on Mac and I couldn't find a similar option.

Anyway, I ended up modifiying something on Stack Overflow which seemed
to work fine on Mac.

Here's what I used:

``` C
#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>

void* malloc(size_t sz, char *file, int line)
{
    void *p;
    void *(*libc_malloc)(size_t) = dlsym(RTLD_NEXT, "malloc");
    p = libc_malloc(sz);
    printf("malloc: %s %d %zu %p\n", file, line, sz, p);
    return p;
}

void free(void *p)
{
    printf("free: %p\n", p);
    void (*libc_free)(void*) = dlsym(RTLD_NEXT, "free");
    libc_free(p);
}

int main()
{
    void *m = malloc(1024, __FILE__, __LINE__);

    // do interesting stuff

    free(m);
    return 0;
}
```

It works fine, but there's a couple of problems:

1. I have to modify my original malloc calls to accept the filename
   and line number as parameters. That's a bit of a no-no in a large
   codebase.
2. What other useful checks might I do in the fake malloc call?

You can build and run with:

``` shell
clang -ldl fake_malloc.c -o test
./test
```

You do get a warning though when you compile. The system knows enough
to know that changing `malloc(size_t)` to `malloc(size_t, ...)` is
probably a dodgy thing to do:

``` shell
fake_malloc.c:5:7: warning: incompatible redeclaration of library function
      'malloc' [-Wincompatible-library-redeclaration]
```

The code runs though.

It also worked without the `-ldl` option.

So, a work in progress. Maybe it's time to learn Valgrind?

---

* Published: 2017-10-05 04:37:12 UTC
* Updated: 2017-10-05 04:37:12 UTC
* UUID: 16FD03D5-C110-44FB-96D4-28B2EDD88683
