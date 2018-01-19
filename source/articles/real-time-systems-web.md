# Real-time systems and the web

Summary: Previous articles in this series described the nature of
real-time systems and then the infrastructure (networks and protocols)
underlying the web and the Internet of Things (IoT). This article
provides a brief introduction to the real-time web, without delving
into language-specific details. A future article will look at
real-time aspects of the IoT.

As described in the previous article the web was built over the
Internet infrastructure and protocols by adding new technologies: in
particular the web browser on the client, the HTTP protocol and web
server (HTTP Server) technology. HTTP is a stateless request/reponse
protocol which was designed around the idea of requesting and serving
web pages. The client browser requests a resource identified by a URL
and the web server processes the request and responds with an HTTP
response. While this works for simple web pages, it is not a good
basis for large, real-time data transfers, or even the paradigm where
the server pushes real-time data to the browser. Some technologies
were created that addressed this need for updated data in primitive
ways - for example the Atom protocol allows a client to periodically
check for updated data to update the content of a news feed. This
works for relatively infrequently updated information such as blog
posts, but it not designed for continual real-time data streams.

## Before the real-time web

Going back to 2003 there were real-time applications to be found on
the web. Excite Chat was a very popular chat program. There were also
messenger applications such as Yahoo Messenger, MSN Messenger, ICQ,
and others. Skype was an exciting voice and textual communications
program - and the new kid on the block. There were also social media
sites such as Friendster, Multiply, and ICQ Lovematch.

These applications were typically implemented using traditional
Internet technologies. They were often native client programs
implemented in C, with C-based server code. The chat protocols were
often proprietary, while using traditional Internet protocols on the
lower layers of the stack. Excite Chat used TCP for a persistent
connection between the chat client, which could be a stand alone
desktop app or a Java applet running within the web browser. To scale
the chat servers, multiplexers whose sole task was to manage the
socket connections between the client and server were used. The
multiplexers would concentrate the chat messages from multiple clients
into a large packet which would then be passed on to the master chat
server via a single TCP socket connection. Login and authentication
was managed by additional servers connected to SQL databases. This
architecture enabled the Exite Chat master servers to scale to 100,000
client connections. While amazing at the time it falls short of the
scale of chat today, where Viber has 400 million users and Line has
over 200 million active users.

Smart phones at this time were not widely available and iOS and
Android did not yet exist.

So, while real-time applications were common, the technologies used
for implementation tended to based around traditional programming
technologies such as TCP/IP sockets.


## Introducing the real-time web

The introduction of web chat applications (which evolved into web apps
such as Slack), and social media sites such as FaceBook and Twitter
heralded the beginning of the real-time web. In early implementations
it was necessary to reload a web page in the browser to see your
updates. The user would therefore have to periodically poll the web
server to check for status updates. This is not user friendly - it is
far more efficient for the user's activity feed to update in real-time
(as and when events occur) without the user having to reload a page.

Users quickly became used to doing everything in the web browser, and
became reluctant to install additional clients for certain
applications. Also for web application developers, it was far better
to create applications that could present information using the
browser, but also now incorporate real-time updates.

For example, you might have a web application where the user checked
the value of an investment portfolio and received real-time updates of
key prices while viewing the value of the assets. Another application
might be where you create a document on a server and are able to
collaborate with several other team members, all editing the document
in real-time. The status/activity feeds of social media sites also
represents another key use-case of the real-time web. A Twitter feed
will automatically update showing the user that there are new tweets
available to read without the user having to reload the page. Rather
than a request-reponse paradigm, the server would now push out data in
real-time to a multitude of client browsers and in recent years native
apps running on smartphones.

## Real-time web technologies

There are many real-time web technologies out there today. One key
part of the technology is the use of a protocol between client and
server that moves away from the HTTP protocol and its inherent
problems for real-time applications. The solution is to use a protocol
such as web sockets. With web sockets HTTP is used to open a
full-duplex TCP stream between the client and the server. There are
then many tools and libraries for accessing this stream from the web
app and these can leverage several communication models such as
publish-subscribe (pubsub).

This article will not go into the details of using these technologies
as they are often language dependent. An example is the use of
socket.io in the node.js world. It is typical to find the use of an
event driven model in building real-time web applications.

In addition to language libraries and communication models there are
also database systems targeting real-time web applications. These
databases eschew the more traditional SQL query request-response model
and instead adopt a push model where data, usually in JSON format, is
broadcast to clients. Firebase for example allows data to be synched
out to clients on a global scale. RethinkDB is another example where
based on a query, data is continually pushed to clients in real-time.

Some examples of real-time web applications include:

* Collaborative web and mobile apps
* Slack and similar web chat apps
* Streaming analytics apps
* Multiplayer games
* Real-time marketplaces
* Connected devices
* Trading platforms
* Real-time information displays (e.g. train times on a web site)
* Web applications that represent real-time data form the Internet of Things (IoT)

A personal favourite is [Flight Radar 24](https://flightradar24.com).

## Summing up

This article has touched on aspects of the real-time web. Typically a
connection-oriented full-duplex stream model using TCP is established
via a web sockets interface, the stateless request-response HTTP
protocol being unsuitable for real-time web apps.

In the next article I will take a brief look at the Internet of Things
(IoT), with potential application of real-time web technologies, and
some of the scaling challenges inherent is such a vast network.

---

* Published: 2018-01-19 14:52:00 UTC
* Updated: 2018-01-19 14:52:00 UTC
* UUID: A2409CB8-E30E-4A69-99B9-2DF5291B18A0

