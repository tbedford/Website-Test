# Tracing version of malloc

Summary: I managed to create some useful macros for debugging C
programs.

It was a small victory, but after quite a bit of fiddling I managed to
get `#define` to do my bidding! This seemed to be much more fiddly
than I had expected. Still, it's working as the following example
shows:

``` C
#include <stdio.h>
#include <stdlib.h>

void * test3 (size_t size, char *file, int line)
{
    void *p;

    p = malloc (size);
    printf("test3: %zu %s %d %p\n", size, file, line, p);

    return p;
}

#define test1(s)                              \
    test3((s), __FILE__, __LINE__)

int main (int argc, char **argv)
{
    void *p;
    
    p = test1(1024); 

    printf("%p\n", p);

    free (p);
    return 0;
}
```

The great thing about this is that you can now hash define `malloc()`
to include tracing information, so you can trace out memory
allocations and of course `free()`. This can be useful for debugging
purposes.

So, to be specific:

``` C
#include <stdio.h>
#include <stdlib.h>

void * malloc2 (size_t size, char *file, int line)
{
    void *p;

    p = malloc (size);
    printf("test3: %zu %s %d %p\n", size, file, line, p);

    return p;
}

#define malloc(s)                              \
    malloc2((s), __FILE__, __LINE__)

int main (int argc, char **argv)
{
    void *p;
    
    p = malloc(1024); 

    printf("%p\n", p);

    free (p);
    return 0;
}
```

Of course you can do the same thing for `free()`.

---
* Published: 2017-10-25 06:00:00 UTC 
* Updated: 2017-11-15 17:45:00 UTC
* UUID: 43D0FFD9-5E04-493D-AF34-E1F144437695



