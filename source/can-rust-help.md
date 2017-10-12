# Can Rust help?

I've heard a little bit about Rust and was thinking about its use in
developing low-level code. I'm not totally sure what it's capable of
though as I've not had time to go into it - yet. I think it may be a
better choice than C though for some low-level projects I'm working
on.

First here's some C code:

``` C
#include<stdlib.h>

void my_func (int *ptr)
{
    free (ptr);
}

int main (int argc, char **argv)
{

    int *p = malloc (1024);

    my_func(p);

    *p = 1234;
        
    return 0;
}
```

Can you see the problem? 

With clang this compiles and actually runs without error. The most
likely reason it doesn't crash is because we only just freed up that
memory so nothing else is using it. If that memory was in use we have
potential data corruption or a crash. Of course you could argue if you
do stupid things like the above what do you expect? This is true. It
would be nice if the compiler caught such problems. Could Rust do it
better?

And now another potential problem. 

Imagine a custom allocator that returns a memory object:

``` C
typedef struct memobj_s {
    void *ptr;
    size_t size;
} memobj_t;
...
memobj_t mo;

mo = c_alloc (1024); // mo contains pointer and size
...
```

Now, let's say our app does this:

``` C
mo.size = junk; // Should never be changed
```

We now later in the app pass the memory object back to free:

``` C
c_free (&mo); // pointer maybe correct, size wrong.
```

Oops. Bang! So, after we create the memory object, we do not want the
application to be able to change it (immutable after initialization). 

So, is there a C way to stop this happening?

Also, can the Rust compiler detect such a problem? Does it allow us to
define an object as immutable after initialization?

These are a couple of examples of things where I think Rust *might* be
able to help. If it could I could perhaps justify the time to learn
it.

If there are Rust programmers out there who know please contact
me via email (email address is on the Contact page of my website).
