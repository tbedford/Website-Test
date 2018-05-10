# A gentle introduction to Nexmo

Summary: In this article I attempt to provide you with a gentle
introduction to what Nexmo is, some of the things it can be used for,
and provide some simple example code in Python.

Having done a few articles now on this website where I use the Nexmo
API, I thought I should perhaps provide a more in-depth tutorial for
you. Sure there's always the [Nexmo
documentation](https://developer.nexmo.com), but hopefully this will
help too if you have no background in Cloud Communication APIs. 

I came into Nexmo with no experience of Cloud Communications so over
the first couple of weeks I put together some notes before breakfast
to get my head straight, and this tutorial is a tidied up version of
those notes. I hope they will be useful to you if you decide to get to
grips with the Nexmo API.

## Objectives

- Learn a little about Nexmo.
- Learn some of the most important concepts for understanding the
  Nexmo service.
- Create a simple Nexmo application to handle an inbound call, with
  custom business logic in a simple Python web application.

## Pre-requisites

- You have Python 3 installed and some basic knowledge of Python (you
  should however be able to apply a lot of what you learn here to
  other languages).
- No knowledge of Nexmo is required.

## Concepts

This section provides a handy reference to some common terms and
concepts. This blog post will explores some of these terms in more
detail later.

**Nexmo - the company**

Nexmo is now part of [Vonage](https://www.vonage.co.uk/about/), a
leading provider of cloud-based communications services. The primary
product of Nexmo is an API that interfaces with the Vonage cloud-based
service.

**Nexmo API**

The API for the Vonage network. This API allows you to make and
receive calls, set up and manage conferences, send messages via SMS,
FaceBook Messenger and Viber, to mention just a few of the
capabilities. The [Nexmo Developer
Portal](https://developer.nexmo.com/) provides extensive
documentation on using the API.

**Nexmo Dashboard**

To be able to use the Nexmo API you need to create a Nexmo
account. Once created you will have access to the Dashboard. From here
you can obtain important information, such as your API Key and API
secret. You can also purchase Nexmo Numbers, and create new Nexmo
Applications. There are many other features of the Dashboard that are
beyond the scope of this post.

**Nexmo Application**

Once you have created a Nexmo account you will be able to create a
Nexmo Application in the Dashboard. It is also possible to create a
new application programmatically, or using the Nexmo command line
tools, but again this is beyond the scope of this tutorial. In this
blog post you will create a Nexmo Application using the Dashboard, and then
add business logic in a Python web application.

**Nexmo Number**

You will need to purchase a Nexmo Number for most applications. This
number can be assigned to your Nexmo Application. Typically, callers
would dial this number, say to join a conference call. Alternatively,
if your application calls users, this is the number they will see on
their incoming call. An important point to note is that a single Nexmo
Number cannot be shared by multiple applications. However, it is
possible for a Nexmo Application to have multiple Nexmo Numbers
assigned to it.

**Public/Private Key** 

When you create a Nexmo Application you will create a public/private
key pair for it. This is used in authenticating API requests. In this
post you will see how to create this key pair in the Dashboard, but it
can also be done programmatically (using one of the client libraries),
or using the command line tools.

**NCCO**

The Nexmo Call Control Object (NCCO) is a key part of implementing
your application. The NCCO is a JSON object that controls how your
application will handle a particular call. A simple example might be
when a call is answered you might play a voice message.

**Inbound/Outbound**

When you read through the documentation you will see references to
inbound and outbound calls and messages. Your Nexmo Application is the
point of reference. So for example, a call going from your Nexmo
Application to an end user would be an _outbound_ call. An end user
calling your Nexmo Application would represent an _inbound_ call.

**Answer URL**

When your Nexmo Application answers an inbound call, or the user
answers an outbound call, the Nexmo application calls back on what is
known as the Answer URL using the HTTP GET method. The Answer URL is
used to provide the relevant NCCO as part of the business logic you
will implement. A simple NCCO might specify an action such as `talk`
and then specify a text message. This NCCO can be programmatically
generated, or coud be a static NCCO saved in a file. When a call is
answered the NCCO is requested from the Answer URL. You will see an
example of this later in this blog post.

**Event URL**

When the Nexmo Application is running it calls back on the Event URL
with application status using the HTTP POST method. This information
can be used by your web aplication to detect when certain state
transitions occur (for example, call answered), and take action
accordingly. This is critical to being able to implement the business
logic of your application.

**Webhooks**

Answer URL and Event URL are examples of webhooks that are used
through the Nexmo API. For example, it is possible to set a webhook
URL for an incoming SMS. Other webhooks are not covered in this blog
post.

## Example application overview

In this blog post you will create a simple application. Its purpose is
to receive inbound calls on a Nexmo number and play a message to the
caller. It achieves this by providing an NCCO on the `answer_url`. It
also logs events posted to the `event_url`.

The following diagram illustrates the overall set up. You call into
Nexmo's cloud service on your Nexmo Number. The Nexmo service will
call back on the Event URL and Answer URL webhooks. Your web
application implements any business logic and handles the callbacks:

![Overview](./images/inbound-call-overview.png "Overview")

In this case your web application only receives callbacks from Nexmo
Service, it does not need to call the Nexmo API directly.

## Down to work

Here's a summary of what you will do:

- [ ] Sign up for a Nexmo account
- [ ] Review the Nexmo Dashboard
- [ ] Create a new Nexmo Application
- [ ] Generate your application's public/private key pair
- [ ] Purchase a Nexmo Number and assign it to your application
- [ ] Set callback links for your application
- [ ] Add business logic to your application
- [ ] Deploy your application
- [ ] Test your application
- [ ] Have fun!

### 1. Sign up for a Nexmo account

The first thing you need to do is [sign
up](https://dashboard.nexmo.com/sign-up) for a Nexmo account. From
your account you will be able to create Nexmo Applications, purchase
Nexmo Numbers and obtain important information you need in order to be
able to use the Nexmo API. Go to the sign up page, fill out the
required information, and follow the instructions.

NOTE: You will be given some free credit when you first create an
account - just enough to test things out.

### 2. Review the Nexmo Dashboard

Once you've signed up, log into your account. The Nexmo Dashboard is
displayed, as you can see in the following screenshot:

![Nexmo Dashboard](./images/nexmo-dashboard-clean.png "Nexmo Dashboard")

You can find some important pieces of information here. You will
need the API Key and API Secret when using the Nexmo API, but actually
for this tutorial you won't need them. Just be aware of where to find
them.

As you will create a Voice API application in this tutorial,
click on the Voice menu item in the main menu bar as shown in the
following screenshot:

![Voice Link Main Menu](./images/nexmo-dashboard-voice-link.png "Voice Link Main Menu")

A list of your applications is displayed: 

![Nexmo Dashboard Voice](./images/nexmo-dashboard-voice.png "Nexmo Dashboard Voice")

You have not created any applications yet of course. That is the next
step.

### 3. Create a new Nexmo Application

To create a new application click `Add new application`.

The following form is displayed:

![Create an application](./images/nexmo-dashboard-create-application.png "Create an application")

You need to enter the following information:

- [ ] Application name
- [ ] Event URL
- [ ] Answer URL

You also need to:

- [ ] Generate a public/private key pair

**Enter an application name**

You can enter anything you like here. For example "Incoming Call Server" is fine.

**Enter an Event URL**

This will depend on how you deploy your application. The URL must be
accessible to the Nexmo service, as it will use HTTP POST to send
information to this URL over the public Internet. Assuming you are
running your business logic (which you will implement later in Python)
at `example.com` on port 3000, the URL would be
`http://www.example.com:3000/event`. For now, set it to
`http://www.example.com:3000/event`, you can edit this again later.

**Enter an answer URL**

As with the Event URL this depends a little on how you will be
deploying your application. The Nexmo service will access to URL to
obtain an NCCO to control the call. For now, set it to
`http://www.example.com:3000/answer`, you can edit this again later.

### 4. Generate a public/private key pair

When building out your application you will have code that calls the
Nexmo API to help perform your business logic. Nexmo libraries will
reference a private key and this key is involved to
authenticate API calls.

In this tutorial you will not use these keys as you will not make any
API calls, but you can still generate the key pair to use later by
clicking the `Generate public/private key pair` link. The private key
for the application will be downloaded by your browser. Keep this safe
in a location accessible to your application code but not accessible
to the public.

### 5. Purchase a Nexmo Number and assign it

You need to have a Nexmo Number associated with your application. In
this tutorial your application will accept inbound calls, so the
caller needs a number to dial in on. This is where you can use your
free credit to good use.

To see your already purchased numbers you can click on your Numbers link:

![Nexmo Numbers](./images/nexmo-dashboard-your-numbers-link.png)

This will display any numbers you have:

![Nexmo Numbers](./images/nexmo-dashboard-your-numbers.png)

You can purchase a number buy clicking on the `Buy numbers` link
towards the top left of the Your numbers page. You can also buy
numbers from your application's page.

Go ahead and purchase a number by clicking the `Buy numbers` link. You
can select a mobile number with both SMS and Voice support.

Now go back to your application in the Dashboard and click the Numbers
tab:

![Nexmo Numbers](./images/nexmo-dashboard-app-numbers.png)

You now need to link the purchased number to your application. Just
click the Link button for the number you just purchased. That number
is now assigned to your application.


### 6. Set callback URLs for your application

If you have not already done so, you now need to edit your
application's details to provide callback URLs. You will set one for
the Answer URL and one for the Event URL. What these values should be
depends on how you are going to deploy your application. For now
assume a domain of example.com, a port of 3000, and so the URLs will
be http://www.example.com:3000/event and
http://www.example.com:3000/answer. In the section on deployment you
will read about several options for deployment and testing.

### 7. Add business logic to your application

You will write a simple web application to react to Nexmo application
callbacks. This web application typically implements the business
logic of your application. Very often this code will call the Nexmo
API. 

Inbound call server code:

``` python
# Python 3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from urllib.parse import parse_qs

import time
import json

# HTTP response codes
OK = 200

hostName = "www.example.com" # Change as required
hostPort = 3000 # Change as required

NCCO = '''
[
    {
        "action": "talk",
        "voiceName": "Russell",
        "text": "Hello world! This message is from my first Nexmo web app."
    }
]
'''

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):

        if self.path.startswith('/answer') :

            self.send_response(OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            self.wfile.write(bytes(NCCO, "utf-8"))

            result = urlparse(self.path)
            params = parse_qs(result.query)

            phone_to = params['to'][0]
            phone_from = params['from'][0]

            print ("TRACE: to: %s from: %s" % (phone_to, phone_from))
        

    def do_POST(self):

        if self.path.startswith('/event'):
        
            len = int(self.headers['Content-Length'])
            content = self.rfile.read(len)
            msg = json.loads(content.decode('utf-8'))
            print ("TRACE: Message status: %s" % msg['status'])
            
        self.send_response(OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

            
# Run server - Ctrl-c to break
myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
        
try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass
    
myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
```


### 8. Deploy your application

There are numerous ways to deply your application. You only really
have to deploy the business logic in this case. For testing purposes I
created a Digital Ocean droplet and assigned a spare domain name I had
as this was a simple but realistic deployment scenario.

Another interesting option is to run the business logic on your local
machine. As Nexmo attempts to call back on the webhook URLs you
provided, this would not usually work, as the URLs need to point to
locations that are accessible over the public Internet. You can get
around this by using a tool such as [Ngrok](https://www.ngrok.com),
which will expose your callback URLs to nexmo through a tunnel. How to
do this is beyond the scope of this blog post - but do not fear this
has already been covered in an [in-depth blog
post](https://www.nexmo.com/blog/2017/07/04/local-development-nexmo-ngrok-tunnel-dr/)
by Aaron Bassett. If using Ngrok your webhook URLs would typically be
something like `http://1234ABCD.ngrok.io/webhooks/event` and
`http://1234ABCD.ngrok.io/webhooks/answer`. See also my [Intro to
Ngrok](https://coffeeandcode.neocities.org/intro-to-ngrok.html).


### 9. Test your application

Now at last you are ready to test your application! All you need to do
is make sure your inbound call server (the business logic code written
in Python) is deployed and running so it can deliver the NCCO. Then
call your Nexmo number! After a little while you will hear the message
you set in your business logic code. You can check the trace messages
in a terminal window to see how the Nexmo service interacts with your
business logic.

Terminal output (with details changed for security):

``` shell
$ python3 blogpost-server.py 
Fri Apr  6 05:07:52 2018 Server Starts - www.example.com:3000
TRACE: Call status: ringing
174.34.196.123 - - [06/Apr/2018 05:08:21] "POST /event_url HTTP/1.1" 200 -
TRACE: Call status: started
174.34.196.123 - - [06/Apr/2018 05:08:21] "POST /event_url HTTP/1.1" 200 -
174.34.196.123 - - [06/Apr/2018 05:08:22] "GET /answer_url?from=447700900000&to=447700900001&conversation_uuid=CON-<snipped>&uuid=c8b721<snipped> HTTP/1.1" 200 -
TRACE: to: 447700900000 from: 447700900001
TRACE: Call status: answered
174.34.196.123 - - [06/Apr/2018 05:08:22] "POST /event_url HTTP/1.1" 200 -
TRACE: Call status: completed
174.34.196.123 - - [06/Apr/2018 05:08:27] "POST /event_url HTTP/1.1" 200 -
```

Here you can clearly see the sequence of events as you call into your
Nexmo Number. The Nexmo Application calls back on the Event URL and
Answer URL, delivering a variety of useful information. In this simple
example the call status is traced out. You can also clearly see the
HTTP methods Nexmo uses to interact with your business logic.

### 10. Have fun with your application

Here are a few simple changes you can make to explore your application further:

1. Change the [voice name](https://developer.nexmo.com/api/voice/ncco#payload-6) and message.
2. Print a tracing message that is conditional on call state. For example
   when the call is answered print "Call now answered".
3. Add support for URLs of the form `/call?to=447700900000`, which
   when referenced, makes an outbound call to the number specified as
   a URL parameter and plays a standard message when answered. To make this as easy as possible use the [Nexmo Python library](https://github.com/Nexmo/nexmo-python).
4. Add a little bit of error handling!

## Summary

In this article you created your first Nexmo application, complete
with some simple business logic written in Python. You deployed and
tested your application by making an inbound call and hearing a
message generated by the text to voice facility of Nexmo. This has
been quite a long tutorial, but hopefully you now have a good
foundation on which to continue your explorations of the Nexmo API.

## Next steps

1. Have a read of the [developer
   documentation](https://developer.nexmo.com/).
2. Read the blogpost on [using
   Ngrok](https://www.nexmo.com/blog/2017/07/04/local-development-nexmo-ngrok-tunnel-dr/).
3. Check out the [Nexmo Python
   library](https://github.com/Nexmo/nexmo-python)
4. Check out [Nexmo command line
   tools](https://github.com/Nexmo/nexmo-cli). This allows you to test
   out the API using simple commands and scripts.

---

* Published: 2018-05-10 06:00:00 UTC
* Updated: 2018-05-10 06:00:00 UTC
* UUID: 401CAFF8-5681-4D9E-B2B6-3A73432BD67A

