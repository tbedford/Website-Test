# Real-time systems

Summary: This article attempts to explore what is meant by a real-time
system, specifically in the context of communications and the Internet
of Things (IoT).

What is a real-time system? What is the Internet of Things? How are
these two ideas related if at all? 

There has certainly been a lot of hype around the idea of Internet of
Things (IoT) in recent years. I thought I would put my own thoughts
down on what is meant by a real-time system, and later I would like to
expand on this with further articles, exploring real-time systems in
the context of the Internet of Things (IoT).

But first, what is a real-time system? 

A real-time system is one in which, obviously, time is an important
consideration. The actual scale of time (from microseconds, to
seconds) depends on the application. In some systems we are interested
in milli or microsecond timescales, as for example in a missile
guidance system or car Anti-lock Braking System (ABS), and in other
systems we may only be interested in a timescale measured in seconds.

With time as a key aspect of a real-time system, there are three
parameters of the system of interest:

1. Response time
2. Determinism
3. Deadlines (hard, firm, soft)

Response time - this is the time it takes for the system to respond to
an input event. This input event could be a hardware interrupt, or
clicking on a link in a web browser. In the case of a hardware
interrupt we might expect the system to respond in milli-seconds. In
the case of a web browser, clicking a link may initiate an HTTP
request which arrives at the server at some time later after taking in
the latency of the network. The server may perform calculation or a
database lookup and then send a response, which will be subject to
delays in the network. Finally, the response arrives back in the
client. In these different situations the actual reponse time is quite
dfferent, but may be perfectly viable depending on the use case. As
long as the response time is within the parameters that suit the
system design then things look good. However, what if in one case the
response time was 100 ms and then the next time that event occurred
the response time was three seconds we could have a problem on our
hands. That brings us to the question of consistency or predictability
in the timing constraints of the system. This predictabiity is
referred to as the determinism of the system. 

Determinism - Let's say we have determined that a reponse time of
between 5 and 15 milliseconds is acceptable for our real-time
system. We start testing our system, let's say it's an ABS. On testing
we find that we get response times of 5ms, 5ms, 5ms, 500ms, 5ms. Is
this acceptable? We have exceeded our deadline of 10ms in one case
here. What happened?

Well, it may have been something like a flurry of interrupts occurred
in the car engine management system or guidance system, that caused an
interrupt storm. Perhaps the ABS interrupt what itself interrupt by
another interrupt causing another Interrupt Service Routine (ISR) to
run, which itself was interrupted causing another ISR to run and so
on. This resulted in unpredictability. This unpredictability or lack
of determinism, can be a problem in real-time systems. It might be
possible to fix this issue in the case of the ABS by making it the
highest priority interrupt, and so it cannot by interrupted until its
code has completed. This might bring the predictability back to within
our timing constraints - we do not wish to exceed to 10ms deadline as
this could have safety implications.

In a real-time communications system, such as in VoIP, we might have a
response time of between 500ms and say 2 seconds for a packet. If for
example a packet then took 10 seconds it may as well not have arrived
and will most likely affect speech quality. We would like to have
predictability within our chosen time constraints. Depending on the
network that may not be possible. The Internet for example is
notoriously unpredictable, with nodes going down, multiple potential
routing paths, unpredictable network traffic and variable
bandwidth. Still, as long as the network is determistic enough, we
could still implement a real-time system.

Deadlines. We have already touched on the idea of deadlines. This is a
timing limit that we do not wish to exceed in the ideal
situation. Real-time systems can be broadly categorized depends on the
gravity of outcomes should the deadline be exceeded. In hard real-time
systems this could lead to a hazardous situation and potentially loss
of life. Examples include alarms in a nuclear reactor, missile
guidance systems, ABS and aircraft control systems as well as robot
arms. 

Firm real-time system have less disastrous outcomes if deadlines are
exceeded. An example might be a trade is not carried out in a robot
trading system, resulting in a loss of income.

In soft real-time systems a deadline exceeded might be reflected as a
mild annoyance, such as a voice packet being missed or a annoyingly
long database response time for a specific query.

Note that in some systems a response time might be micro or
millseocnds but still a soft real-time system, whereas you might have
a system such as a nuclear reactor where response times of five
seconds are quite acceptable but a deadline of ten seconds is hard.

So, in summary, how do we define a real-time system? A real-time system is any system where timing is a consideration, and specifically three timing related aspects: 

1. Response times
2. Determinism (predictibility of timing)
3. Deadlines

In the next article I will take a quick look at real-time
communications on the web.


## Real-time communications and the web

- Network limitations 
  - limits of unreliable network, latency, response
- Protocol limitations
  - connection oriented
  - connectionless
  - HTTP
  - request/response (half-duplex)
  - web sockets (full-duplex over TCP connection) browser/server


## Real-time systems and the Internet of Things (IoT)

edge of netwrok
asymmetrical
real-time control

---

* Published: 2017-11-07 09:00:00 UTC
* Updated: 2017-11-15 12:56:00 UTC
* UUID: 

