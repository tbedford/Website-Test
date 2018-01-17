# Real-time systems - networks and protocols

Summary: this will be the summary

- Network limitations 
  - limits of unreliable network, latency, response
- Protocol limitations
  - connection oriented
  - connectionless
  - HTTP
  - request/response (half-duplex)
  - web sockets (full-duplex over TCP connection) browser/server


In a real-time communications system, such as in VoIP, we might have a
response time of between 500ms and say 2 seconds for a packet. If for
example a packet then took 10 seconds it may as well not have arrived
and will most likely affect speech quality. We would like to have
predictability within our chosen time constraints. Depending on the
network that may not be possible. The Internet for example is
notoriously unpredictable, with nodes going down, multiple potential
routing paths, unpredictable network traffic, and variable
bandwidth. Still, as long as the network is deterministic enough, we
could still implement a real-time system.


## Real-time systems and the web



## Real-time systems and the Internet of Things (IoT)

edge of netwrok
asymmetrical
real-time control

---

* Published: 2017-11-07 09:00:00 UTC
* Updated: 2017-11-15 12:56:00 UTC
* UUID: 5424F74B-749B-42AA-A726-40EE59463EE3


