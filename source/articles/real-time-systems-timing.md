# Real-time systems - timing

Summary: This article is the first in a series that attempts to
explore what is meant by a real-time system, specifically in the
context of communications, the web, and the Internet of Things (IoT).

The term "real-time" is bandied about a great deal these days. You
will hear about the "real-time web" and "real-time systems". But what
exactly does "real-time system" mean though?

A simple definition serves as a starting point:

**A real-time system is one in which _time_ is a _key_
consideration.**

This serves us well as a simple definition, but as nearly all systems
care about time to a lesser or greater extent, the definition can be
refined depending on the context. For example, a chat program has a
different set of timing characteristics compared to a car Anti-lock
Braking System (ABS), and the ABS has different timing requirements
compared to a video streaming application.

The actual scale of time of interest depends on the application. In
some systems it may be in the milli- or micro-second timescale, as for
example in a missile guidance system or car ABS.  In other systems
timescales may be measured in seconds, hours, or even days.

With time as a key aspect of a real-time system, there are at least
three parameters of timing to consider:

1. Response time (time to process an event)
2. Determinism (predictability)
3. Deadlines (hard, firm, soft)

Each of these will be explored in the following sections.

## Response time

Response time can be defined differently depending on the context. In
this series of articles it is taken to have the following definition
unless otherwise stated:

**Response time is the time it takes for the system to process an
_event_ to _completion_.**

So, what is an **event**? An event is just something happening. It could
be an event in the real world, such as a user hitting an emergency
stop button, pressing a brake, or perhaps a child running into the
road. It could be the arrival of a network packet. Usually that event
will need to be processed in some way, at the very least it is
necessary to record that the event happened.

What is **completion**? This depends on the event and how it is best
processed, but it is possible to illustrate by example.

Consider the case of a hardware interrupt, such as a keyboard
keypress. This generates a hardware interrupt which causes an
interrupt service routine (ISR) to handle the interrupt. The ISR may
read a hardware register to obtain the keyboard scan code and place
the code in a buffer. In this example the event is considered complete
to on the return of the ISR. At this point it is confirmed that the
key event has been recorded at least at the lower level of the
system - critically the key event has not been lost. If the keyboard
ISR was itself interrupted by another ISR, and possibly other nested
ISRs, the event could not be considered to have been recorded until
the keyboard ISR itself returns. At this point the event processing
has completed.

In the case of a web browser, clicking a link to retrieve some result
may initiate an HTTP request which arrives at the server at some time
later after taking into account the latency of the network. The server
may perform some calculation or a database lookup and then send an
HTTP response, which will again be subject to delays in the
network. Finally, the response arrives back in the client, where the
web browser displays the result. The event is now considered to have
completed.

Consider one more example. An application performs an asynchronous
(AIO) filesystem read. A callback handler is written in our
application. The asynchronous read is called, registering the
appropriate callback handler and perhaps specifying a buffer into
which data can be placed. The read will not block the app (it's a
non-blocking asynchronous call), so the read method returns
immediately and the app then most likely sleeps. The operating system
code runs, disks spin, read/write heads move ponderously about, and
the requested bytes are read from the disk at some point. The OS
signals completion by invoking the registered callback handler and the
data is safely stored in the buffer. The operation has completed when
the callback handler returns.

There are no hard and fast rules here, but to be able to measure
response time it is necessary to be clear about what is being
measured.

Now consider again a subsequent filesystem read where the bytes
requested are already cached. The response time will be a lot less
because the mechanical "gubbins" does not need to be spun. However,
completion is still when the callback handler returns. 

This last example also illustrates the variable nature of response
times for the same type of event. It is not known in advance, at the
application level, whether the data is cached or not.

Consider the response time of the ABS event. If in one test it was 10
ms and then the next time that event occurred the response time was
500ms, this may indicate a problem - even a potentially dangerous
situation.

That brings us to the question of consistency or predictability in the
timing constraints of the system. 

In this series of articles the level of predictabiity is referred to
as the determinism of the system.

## Determinism

Consider an ABS event where a response time of between 5 and 15
milliseconds is acceptable. On testing the response times obtained are
5ms, 5ms, 5ms, 5ms, ..., 5ms. The response time is within the desired
range and is very predictable (deterministic).

With a different ABS design the following results set might be
obtained: 5ms, 10ms, 15ms, 6ms, 14ms. These results are still within
acceptable limits, but are much less predictable.

Now consider the following results (in ms): 16, 17, 16, 16, 17,
16, 16. These results are fairly predictable, but outside the desired
range (the deadline of 15ms has been exceeded).

Now consider the following results (in ms): 5, 500, 4, 2, 700, 300,
250, 15, 177. These results not only fall outside the required range
on occasion, but also appear quite unpredictable. 

**The degree of predictability is called the determinism of a
system.**

Determinism in a system is really a measure of how accurately response
times can be predicted. Deterministic system are quite stable in their
response times. Non-deterministic systems tend to have unpredictable
response times. It is important to understand the levels of
determinism in a system when designing applications with real-time
constraints.

Looking at the ABS again, why might things be unpredictable? Well, it
may have been something like a flurry of hardware events interrupts
occurred at approximately the same time, delaying processing.

In the real world it is often not possible to predict if and when
certain events will happen. Perhaps the engine management circuitry is
already busy processing another interrupt such as a timer interrupt
and cannot be interrupted, this represents an unpredictable delay even
before the incoming interrupt is processed.

This problem of unpredictable real-time events might be accute in a
system such as a self-driving car. Here you may have many real-world
events happening all at once due to what is happening on the road. A
car strays from its lane, a child steps into the road, the GPS
updates, the LIDAR generates new data that needs processing, and so
on.

The ABS ISR may itself be interrupted by another interrupt causing
another Interrupt Service Routine (ISR) to run, which itself was
interrupted causing another ISR to run and so on in a nested
fashion. This results in unpredictability or lack of determinism. 

The solution to the lack of determinism in the case of the ABS ISR may
be to make it the highest priority interrupt, and so it cannot by
interrupted until its code has _completed_. Note that if another ISR
was running when the ABS interrupt occurred, the other ISR would be
interrupted by the higher priority ABS ISR. This might bring the
predictability back to within our timing constraints, as exceeding the
15ms deadline may be unacceptable.

This is now getting to the heart of designing effective real-time
systems - the system designer cannot predict if and when real-world
events will occur, but she can design the system in such a way that it
processes these events, whenever they happen, with predictable
response times and within appropriate time constraints.

## Deadlines

A deadline is a timing constraint that must not be exceeded.

Real-time systems can be broadly categorized depending on the gravity
of outcomes should the system fail to meet timing deadlines:

1. Hard
2. Firm
3. Soft

In **hard real-time systems** this could lead to a hazardous situation
and potentially a loss of life. Examples of hard real-time systems
include nuclear reactors, missile guidance systems, robots, ABS,
self-driving cars, and aircraft flight control systems.

**Firm real-time systems** have less disastrous outcomes if deadlines
are exceeded. An example might be a trade is not carried out in an
algorithmic trading system, resulting in a loss of income.

In **soft real-time systems** a deadline exceeded might be reflected
as a mild annoyance, such as a voice packet being missed, a game
dropping a frame, or a annoyingly long database response time for a
specific query.

Note that in some systems a response time might be micro or
millseconds but these are soft deadlines. On the other hand a system
such as a nuclear reactor might have response times of five seconds
for some processes but these are deemed quite acceptable. On the other
hand the same system might have a deadline of ten seconds that is a
hard limit. It is the outcome of failing to meet a deadline that is
the defining characteristic.

## Summing up

A real-time system is any system where timing is a key consideration.

Specifically three timing-related characteristics (at least) should be
considered when designing a real-time system:

1. Response time (the time to process an event to completion)
2. Determinism (predictibility of response times)
3. Deadline (timing constraints that must not be exceeded)

More broadly a real-time system can be considered to be a system in
which real world events occur with a degree of unpredictability on the
time axis, and where predictabililty of response times is desirable.

In the next article in this series I will take a quick look at
networks and protocols in the context of real-time systems.

---

* Published: 2018-01-16 19:39:00 UTC
* Updated: 2018-01-17 10:51:00 UTC
* UUID: 2462CBC1-93A1-4AE4-A246-17B947066619


