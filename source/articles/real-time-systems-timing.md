# Real-time systems - timing

Summary: This article is the first in a series that attempts to
explore what is meant by a real-time system, specifically in the
context of communications, the web, and the Internet of Things (IoT).

The term "real-time" is bandied about a great deal these days. You
will hear about the "real-time web" and "real-time systems". But what
exactly does "real-time system" mean though?

Let's start with a simple definition and work from there...

> A real-time system is one in which time is a **key** consideration.

This serves us well as a definition, but as nearly all systems care
about time to a lesser or greater extent, we can refine our definition
somewhat depending on the context. For example, a chat program has a
different set of timing characteristics compared to an Anti-lock
Braking System (ABS), and the ABS has different timing constraints
compared to a video streaming application.

The actual scale of time of interest depends on the application. In
some systems you might be interested in milli- or micro-second
timescales, as for example in a missile guidance system or car ABS,
and in other systems we may only be interested in a timescale measured
in seconds.

With time as a key aspect of a real-time system, there are at least
three parameters of timing to consider:

1. Response time
2. Determinism
3. Deadlines (hard, firm, soft)

## Response time

This is the time it takes for the system to process an _event_ to
_completion_.

So, what is an event? An event is just something happening. It could
be an event in the real world, such as a user hitting an emergency
stop button, pressing a brake, or perhaps a child running into the
road. It could be the arrival of a network packet. Usually that event
will need to be processed in some way, at the very least we need to
record that the event happened.

What do we mean by completion? This depends on the event and how it is
best processed, but it is possible to illustrate by example.

Let's take the case of a hardware interrupt, such as a keyboard
keypress. This would generate a hardware interrupt which would cause
an interrupt service routine (ISR) to handle the interrupt. The ISR
may read a hardware register to obtain the keyboard scan code and
place the code in a buffer. In this example we could consider the
event to be processed on completion of the ISR. If the keyboard ISR
was itself interrupted by another ISR, and possibly other nested ISRs,
we could not consider the event to have completed until the keyboard
ISR itself returns. 

In the case of a web browser, clicking a link to retrieve some result
may initiate an HTTP request which arrives at the server at some time
later after taking into account the latency of the network. The server
may perform some calculation or a database lookup and then send an
HTTP response, which will again be subject to delays in the
network. Finally, the response arrives back in the client, where the
web browser displays the result. We can now consider this event to
have completed.

Let's consider one more example. Let's say our application performs an
asynchronous (AIO) filesystem read. A callback handler is written in
our application. We then perform the asynchronous read, registering
the appropriate callback handler and perhaps specifying a buffer into
which data can be placed. The read will not block the app so the read
method returns immediately and the app then most likely sleeps. The
operating system code runs, disks spin, read/write heads move
ponderously about, and the requested bytes are read from the disk at
some point. The OS signals completion by invoking the registered
callback handler and the data is safely stored. The operation has
completed when the callback handler returns. 

There are no hard and fast rules here, but to be able to measure
response time we need to be clear about what we are measuring. To have
meaningful timing data we need to be clear about what the event is and
at what point do we consider it to have completed.

Now consider again a subsequent filesystem read where the bytes
requested are already cached. The response time will be a lot less
because the mechanical gubbins does not need to be spun. However, we
will still know when completion is - it will be when the callback
handler returns. This illustrates the variable nature of response
times for the same type of event.

Actual values of response times may be quite different, but may be
perfectly viable depending on the use case. As long as the response
time is within the parameters that suit the system design then things
look good.

However, what if the response time of the ABS event was 10 ms and then
the next time that event occurred the response time was 500ms, we
could have a problem on our hands. That brings us to the question of
consistency or predictability in the timing constraints of the
system. This predictabiity is referred to as the determinism of the
system.

## Determinism

Let start with an example.

Let's say we have determined that a reponse time of between 5 and 15
milliseconds is acceptable for our ABS. We start testing our
system. On testing we find that we get response times of 5ms, 5ms,
5ms, 5ms, ..., 5ms. The response time is within our desired range and
is very predictable.

However, let's say we had the following results set: 5ms, 10ms, 15ms,
6ms, 14ms. These results are still within our range, but less
predictable. 

Now consider the following results (in ms): 16, 17, 16, 16, 17,
16, 16. These results are fairly predictable, but outside our desired
range (our hard deadline of 15ms has been exceeded).

Now consider the following results (in ms): 5, 500, 4, 2, 700, 300,
250, 15, 177. These results not only fall outside our required range
on occasion, but also appear quite unpredictable. The degree of
predictability is called the determinism of a system.

Determinism in a system is really a measure of how accurately we can
predict response times. Deterministic system are quite stable in their
response times. Non-deterministic system tend to have highly
unpredictable response times.

Looking at our ABS again, why might things be unpredictable? Well, it
may have been something like a flurry of hardware events interrupts
occurred at approximately the same time, delaying processing.

In the real world we often can't predict if and when certain events
will happen. Perhaps the engine management circuitry is already busy
processing another interrupt such as a timer interrupt and cannot be
interrupted, we now have an unpredictable delay even before we get to
start processing the incoming interrupt.

This problem of unpredictable real-time events might be accute in a
system such as a self-driving car. Here you may have many real world
events happening all at once due to what is happening on the road. A
car cuts you up, a child steps into the road, the GPS updates, the
LIDAR generates new data that needs processing, and so on.

The ABS ISR may itself be interrupted by another interrupt causing
another Interrupt Service Routine (ISR) to run, which itself was
interrupted causing another ISR to run and so on in a nested
fashion. This results in unpredictability or lack of determinism. 

You'll notice that with real-world events we often cannot predict if
and when they will happen. You could get lots of events all happening
at the same time which puts a load on the system.

The solution to the lack of determinism in the case of the ABS ISR may
be to make it the highest priority interrupt, and so it cannot by
interrupted until its code has _completed_. Note that if another ISR
was running when the ABS interrupt occurred, the other ISR would be
interrupted by the higher priority ABS ISR. This might bring the
predictability back to within our timing constraints - we do not wish
to exceed to 15ms deadline as this could have safety implications.

This is getting to the heart of designing effective real-time
systems - we cannot predict if and when real-world events will occur,
but we can design the system so that it processes these events
whenever they happen with predictable response times and within
appropriate time constraints.

## Deadlines

We have already touched on the idea of deadlines. This is a timing
limit that we do not wish to exceed in the ideal situation.

Real-time systems can be broadly categorized depending on the gravity
of outcomes should the timing deadline be exceeded:

1. Hard
2. Firm
3. Soft

In hard real-time systems this could lead to a hazardous situation and
potentially loss of life. Examples include alarms in a nuclear
reactor, missile guidance systems, robots, ABS, self-driving cars, and
aircraft control systems.

Firm real-time system have less disastrous outcomes if deadlines are
exceeded. An example might be a trade is not carried out in an
algorithmic trading system, resulting in a loss of income.

In soft real-time systems a deadline exceeded might be reflected as a
mild annoyance, such as a voice packet being missed or a annoyingly
long database response time for a specific query.

Note that in some systems a response time might be micro or
millseconds but these are soft deadlines. On the other hand you might
have a system such as a nuclear reactor where response times of five
seconds are quite acceptable but a deadline of ten seconds is a hard
limit. Again it is the outcome of failing to meet a deadline that is
the important thing.

## Summing up

So, in summary, how do we define a real-time system? A real-time
system is any system where timing is a key consideration. 

Specifically we are interested in three timing-related
characteristics:

1. Response time
2. Determinism (predictibility of timing of events and response times)
3. Deadline

More broadly we can consider a real-time system to be a system in
which real world events occur with a degree of unpredictability, and
where predictabililty of response times is desirable.

In the next article I will take a quick look at networks and protocols
in the context of real-time systems.

---

* Published: 2018-01-16 19:39:00 UTC
* Updated: 2018-01-16 19:39:00 UTC
* UUID: 2462CBC1-93A1-4AE4-A246-17B947066619


