# Real-time systems - networks and protocols

Summary: This article continues the series on real-time systems by
looking at infrastructure (networks and protocols) underlying the web
and the Internet of Things (IoT).

The previous article described how a real-time system is one in which
timing is a key characteristic. The real-world consists of many events
that can occur randomly and inherent properties of the specific system can take
an unpredictable amount of time to process. Real-time system design
consists of ensuring that events are processed within a predictable
timeframe, so that any timing deadlines are met.

To explore real-time systems in the context of the web or the IoT, it
is necessary to look at the properties of the underlying system,
specifically the network infrastructure and the protocols used to
manage the transfer of data. This allows an assessment of the
real-time properties of these systems.

## Network infrastructure

The network infrastructure underlying the Internet is potentially
unreliable. Packets can be lost in transmission, traffic is variable,
protocols add varying degrees of overhead, servers can vary in
performance and response time, network nodes and routers can fail, and
bandwidth varies considerably from low-speed ADSL to high-speed fibre
links. This makes the Internet inherently unpredictable, and as has
been described, determinism (predictability) is a desirable property
of real-time systems - predictable timing is desirable so it is
possible to meet any timing constraints.

There's not much that can be done by the application developer to
chnage this inherently problematic state of affairs, it is the nature
of the beast. The good news however is that it was known that the
Internet would be unreliable since its conception, and so its design
has taken this into account. 

The "oil" that keeps the Internet running smoothly despite its
unreliable nature are protocols. These protocols keep packets moving
over this unreliable and unpredictable infrastructure.

## Protocols

The main protocol stack running on the Internet today is the TCP/IP
protocol stack. This is a layered stack that consists of the following
layers:

1. Application (Sockets, HTTP)
2. Transport (TCP/UDP)
3. Internet (IP)
4. Link / physical (Ethernet, PPP)

The application layer is the highest layer. 

These protocols attempt to deal with the problems of an unreliable
network by adding different levels of overhead. For example,
Transmission Control Protocol (TCP) offers a connection-oriented
protocol where an end-to-end connection is established. Any lost or
corrupted packets, or packets that arrive out of order, are dealt with
by the protocol, and may require a handshake that resends the required
packets. TCP therefore provides a reliable connection, where packet
delivery is guaranteed.

User Datagram Protocol (UDP) on the other hand does not guarantee
delivery of packets. Packets may arrive out of order and may also be
lost or corrupted. UDP is known as a connectionless protocol, it does
not establish a reliable end-to-end transmission stream. However,
compared to TCP, it is a relatively lightweight protocol. It is used
in applications where the occasional loss or corruption of packets can
be handled by the application or ignored on some cases. UDP is used
for example as a way a game server can update clients. Should network
conditions deteriorate, then packets will be lost and the client
application can use techniques such as client-side prediction to
compensate. If conditions deteriorate further it could mean the game
drops frame and becomes jerky. This may not be deemed to be a "show
stopper" and it may be that once the network conditions improve the
client simply resynchromizes with the server and reliable gameplay
continues. TCP is deemed to add unnecessary overhead to the network
connection here and so is not used in this scenario.

Protocols at the application level can be quite varied and examples
are FTP, Telnet, HTTP, web sockets, and the low-level sockets API.
Much of the web today is based on the HTTP protocol. This is
essentially a round-trip, stateless, request-response protocol. The
client, typically a web browser, will send an HTTP request packet to a
remote server. The remote server will process the request, which may
consist of loading a web page or performing a database query and
generating HTML to return to the client in a response. The web browser
will then display the response as a web page. 

This round-trip type protocol is relatively slow and unpredictable due
to network latencies and variable performance over the
connection. This is also a half-duplex mode of communication - in HTTP
you have to wait for a response - the client cannot transmit and
receive a stream of packets at the same time using HTTP. HTTP is
therefore not an ideal protocol where speedy full-duplex high speed
data streams are involved. To improve matters some techniques have
appeared over the years - AJAX being one. This allows the browser to
communicate with a server and obtain a response using JavaScript and
XML, without the roundtrip overhead usually associated with full HTTP.

To improve matters further, and allow high-volume data streams to be
exchanged between a server and a client in full-duplex communication,
new protocols such as web sockets have been established. Web sockets
sits on TCP, so is designed for connection-oriented, reliable, high
volume, full-duplex data transfers. This protocol will be described
further in upcoming articles in the series in the context of the
"real-time web".

---

* Published: 2018-01-17 09:51:00 UTC
* Updated: 2018-01-17 09:51:00 UTC
* UUID: D877DC5C-E6EB-4F17-A256-61B50F088E9A
