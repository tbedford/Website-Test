# Real-time systems - Internet of Things

Summary: My series on real-time systems concludes with some brief
thoughts on the Internet of Things.

Internet of Things (IoT) is a big subject and I can't hope to cover
all aspects of it in this article. I shall mostly cover some thoughts
on the "edge of network" as it's known - the area of the IoT that
connects directly into the real world.

## TCP/IP requirement

Many of the solutions to IoT I've seen proposed recommend a full
TCP/IP stack enabled device at the edge-of-network. This is not
without its issues - the most significant being cost. With regards a
TCP/IP-enabled device you are thinking of a device such as the
Raspberry Pi, which while relatively cheap (compared to a laptop) is
expensive when you consider a large number of end points. While a
Rasberry Pi is a cost effective solution for, say, a one off water
level monitoring solution, it would not be suitable if you have a
system monitoring 1000 points along a canal or river - at least not
without driving up cost considerably. 

## OS requirement

A TCP/IP stack also implies a supporting operating system. This need
not be a full-blown OS such as Linux, but could be a smaller OS such
as FreeRTOS or uCOS. Still, these systems also have more than minimal
requirements in terms of memory and CPU. For the edge-of-network then
a simple polling or interrupt-driven solution is fine in many cases,
without the need for a full-blown RTOS executive.

## Small data packets

Many IoT monitoring applications require infrequent and small amounts of
data at the edge-of-network. 

In the case of one thousand monitoring points along a river, measuring
water levels, the change in river level is not likely to be fast or
significant, so we can further reduce data requirements by encoding
only the difference between readings. The real-time requirements in
many IoT monitoring applications are not stringent. Readings every
five minutes would be fine in this application.

The data from a level sensor or temperature sensor is a few bytes. If
you receive, say, 4 bytes of data every five minutes throughout a
24-hour period you are looking at (without compression) 1152 bytes of
data or just over 1K. This amount of data lends itself nicely to
transmission over radio telemetry, phone line, packet radio, or mobile
phone network. Further, the data packets are often not critical, so
simple parity-based error checking is sufficient - packets where the
parity check fails can simply be discarded - no retransmission is
required.

## Edge-of-network devices

Edge-of-network devices would typically be something similar to an
Arduino device. It would have a data acquisition program written in C
and use simple polling techniques. Battery life could almost certainly
be improved by using a interrupt-driven rather than polling
solution. In both cases (polling/interrupts) you lose some determinism
that might be granted by an RTOS executive, but this is not critical
in many applications.

## Intermediate nodes

The edge-of-network devices would periodically send data to
intermediate nodes, which would be more spohisticated devices
containing a full TCP/IP stack. This would typically be an industrial
computer or perhaps a device of a similar capacity to a Raspberry
Pi. Their job is to concentrate time-stamped data from a multitude of
edge-of-network devices. Data could then be transferred to a web
server via some of the techniques already looked at (web sockets for
example).

## Back end

Eventually all data ends up on what I am losely referring to as a "web
server". At this point the data involved could be large. Imagine for
example a system that monitors the levels of all rivers in the
country, or concentrates data from 1000 weather stations scattered
across the country. Real-time data collected from custom telemetry
boxes, and perhaps other data feeds to provide context -
flightradar24.com is an excellent example of this. This quantity of
data requires number-crunching to interpret it. These "back ends" fall
outside the scope of this article though.

## Real-time control

In some applications real-time control is required at
edge-of-network. For example, a milling machine, robot arm or
temperature controller may have relatively tight real-time
requirements. The only solution in these cases is to have local
intelligence to perfom the control - network lag is not something you
can tolerate when you are trying to control a robot arm!


## Tiered approach

The IoT is a large area of application. There is a full-spectrum of
real-time requirements from minimal (simple monitoring) to hard
(robot control). In many cases though, the requirements for
edge-of-network devices is much less than is usually
considered. Rather than reaching for Raspberry Pi and a TCP/IP stack,
it may be much more cost effective to consider a tiered system with
very low cost edge-of-network devices such as Arduino or MicroBit type
devices that forward data to much more capable nodes for data
concentration and transmission over TCP/IP networks. This tiered
approach has the affect of reducing cost and hardware/software
requirements and expertise considerably.

## Conclusion

The secret to reducing cost in IoT solutions is to use a tiered
approach. Rather than using TCP/IP-enabled devices throughout the
solution, much more minimal devices are used at edge-of-network, but
these devices forward data to much more capable, and fully
TCP/IP-enabled computers. These in turn forward data to larger servers
for number crunching and interpretation.


---

* Published: 2018-02-28 07:30:00 UTC 
* Updated: 2018-02-28 07:30:00 UTC 
* UUID: CE155B0C-857D-41B8-A2AF-6E3D5B571FF7



