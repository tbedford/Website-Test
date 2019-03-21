# Hacking fun with OpenTok

Summary: Creating video chat applications with OpenTok.

I was lucky enough to attend an OpenTok training session run by Manik
Sachdeva of TokBox. I thought I would capture a few technical notes on
it here, as that is why this website was created in the first place! I
will include the code I wrote (not pretty, but functional) and bit of
technical detail.

## Source code

The [source code for this
project](https://github.com/tbedford/OpenTok-Hackathon) is available
via GitHub under the MIT license.

## What is OpenTok?

OpenTok is a platform and API for developing your own audio-visual and
messaging web and mobile applications. There are three main components
you need:

1. Dashboard
2. Server SDK
3. Client SDK

You create an account with [TokBox](https://tokbox.com), the company
behind OpenTok, this gives you access to the Dashboard where you can
create and manage your applications. You can of course access all this
functionality using the APIs.

The Server SDK is available for a variety of programming languages. I
used the Python Server SDK. It was simple to install, `pip install
opentok`.

I used the JavaScript Client SDK (also known as the Web Client
SDK). There are also Client SDKs for Android, iOS, and various other
platforms.

## First thoughts on the OpenTok ecosystem

The OpenTok developer centre is very informative, with various sets of
documentation, building blocks (called developer guides), references
and very useful example apps and tutorials. I basically built a
working application by copying and basic the basic web client and
modifying the code. I also built the server-side component from
scratch using the Python SDK documentation. There is a useful PHP
server which you can deploy to Heroku with a single click. I found
this useful initially to get my head around what kind of API the
server might need to implement.

## Architecture overview

Although you can get something up and running using just the Client
SDK, you should not create Sessions (think of Sessions as rooms) in
the client for production systems as you would be explosing your API
Key and API secret. There are also other functions that are perhaps
best carried out on the server side, such as archiving control (you
can save your video chats to disk very easily).

So the basic functional split I came up with was as follows:

Server side provides a little REST API:

1. Session creation
2. Archiving control
3. Session monitoring (via callback)
4. Broadcast message (via signal)

Client side:

1. Create a session - calling server (see above). Returns API key, session ID and token.
2. Connect to Session
3. Publish to Session
4. When Stream created, subscribe to it
5. UI for session creation, archive control, screensharing control etc.


## Some key concepts

As mentioned the main "room" for video chats is the Session. You can't
get far without creating a Session. In production systems this should
be done server-side, not client-side. Sessions are identified by a
Session ID. The client also needs to get a Token, so that subsequent
calls can be authenticated. While Session ID identifies the room, the
Token identifies (really authenticates), the User.

The client then establishes a Connection to the Session. The client
can then Publish an audio-visual stream to the session, and listen for
any events such as other Users joining the Session (and publishing
streams).

Once a client is connected into a Session it can subscribe to other
client's Streams.

## Example

1. Client 1 creates a Session ("room") - via server API
2. Client 1 publishes its video stream
3. Client 2 connects to the Session
4. Client 2 subscribes to Client 1's video stream
5. Client 1 subscribes to Client 2's video stream

### Summary of concepts

These are the key concepts:

* Session - The "room" for the video chat.
* Token - Identifies and autheticates a valid User.
* Connection - The client (User) joins a Session via a Connection.
* Stream - The media stream that is published or subscribed to.

## Server code

For the server-side code I used the OpenTok Python Server SDK and
Flask. Flask makes it easy to create a nice little REST API server in
next to no time. I already had Flask installed so there was no extra
set up required. With OpenTok Server SDK being a single `pip install`
I was writing useful code within seconds. 

The server code:

``` python
#!/usr/bin/env python3

import requests
import json

from requests.auth import HTTPBasicAuth
from flask import Flask, request, jsonify, render_template
from pprint import pprint

# OpenTok Server SDK
from opentok import OpenTok
from opentok import MediaModes
from opentok import ArchiveModes

api_key = "API_KEY"
api_secret = "API_SECRET"
opentok = OpenTok(api_key, api_secret)

# create session
session = opentok.create_session(media_mode=MediaModes.routed)
session_id = session.session_id

# generate token
token = opentok.generate_token(session_id)

# archive ID for this session
archive_id = ""

app = Flask(__name__)

@app.route("/session")
def session_get():
    obj = {}
    obj['apiKey'] = api_key
    obj['sessionId'] = session_id
    obj['token'] = token
    j = json.dumps(obj)
    return (j)

@app.route("/monitoring", methods=['POST'])
def monitoring():
    print ("Monitoring:")
    data = request.get_json()
    pprint(data)
    return ("200")

@app.route("/archive/get")
def archive_get():
    archive = opentok.get_archive(archive_id)
    j = json.dumps(archive)
    return (j)

@app.route("/archive/start")
def archive_start():
    global archive_id
    archive = opentok.start_archive(session_id, name=u'Important Presentation')
    archive_id = archive.id
    print ("Started archive: %s" % archive_id)
    j = json.dumps(archive_id)
    return (j)

@app.route("/archive/stop")
def archive_stop():
    opentok.stop_archive(archive_id)
    print ("Stop archive: %s" % archive_id)
    j = json.dumps(archive_id)
    return (j)

@app.route("/archive/delete")
def archive_delete():
    opentok.delete_archive(archive_id)
    print ("Delete archive: %s" % archive_id)
    j = json.dumps(archive_id)
    return (j)

@app.route("/archive/list")
def archive_list():
    archive_list = []
    archives = opentok.list_archives() 
    for archive in archives:
        print(archive.id)
        archive_list.append(archive.id)
    j = json.dumps(archive_list)
    return (j)

@app.route("/broadcast/msg")
def broadcast_msg():
    payload = {'data': "This is a broadcast message from the server!"}
    opentok.signal(session_id, payload)
    j = json.dumps(payload)
    return (j)

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
```

## Session monitoring

In your TokBox Dashboard it is possible to set a callback URL for
receiving Events that can be used for Session monitoring by the
server. This is not only very simple to set up, but very useful, as
the Event objects contain important information:

``` json
Monitoring:
{'event': 'streamDestroyed',
 'projectId': '12345',
 'reason': 'clientDisconnected',
 'sessionId': '1_MX40NjI4OTIxMn5-MTU1MzA4NDY0OTIyNCWFJCM3hRbTA3Y1ZhVjh-fg',
 'stream': {'connection': {'createdAt': 1553097719716,
                           'data': None,
                           'id': '0ad658ba-b71c-4473-976f-ca99fe4cf490'},
            'createdAt': 1553097719777,
            'id': 'b78d4d54-e5bc-4583-9f31-f582910bf18c',
            'name': '',
            'videoType': 'camera'},
 'timestamp': 1553098058663}
127.0.0.1 - - [20/Mar/2019 16:07:39] "POST /monitoring HTTP/1.1" 200 -
Monitoring:
{'connection': {'createdAt': 1553097719716,
                'data': '',
                'id': '0ad658ba-b71c-4473-976f-ca99fe4cf490'},
 'event': 'connectionDestroyed',
 'projectId': '12345',
 'reason': 'clientDisconnected',
 'sessionId': '1_MX40NjI4OTIxMn5-MTU1MzA4NDY0OTIyNCWFJCM3hRbTA3Y1ZhVjh-fg',
 'timestamp': 1553098058664}
```

As I was testing everything locally I simply set up Ngrok (see my
[Intro to Ngrok](./intro-to-ngrok.html)) to receive the callback POSTs
from TokBox and redirect these to my locally running server. I could
then trace out the events received in the terminal, or perform other
processing as required in the server.

The server code was simply run locally with:

``` shell
$ python3 server.py
```

## Client code

The client code was as follows:

``` javascript
var apiKey, sessionId, token;
var session;
var publisher;
var SERVER_BASE_URL = 'http://localhost:9000';

fetch('/session').then(function (res) {
  return res.json()
}).then(function (res) {
  console.log(res);
  apiKey = res.apiKey;
  sessionId = res.sessionId;
  token = res.token;
  initializeSession();
}).catch(handleError);


// Handling all of our errors here by alerting them
function handleError(error) {
  if (error) {
    alert(error.message);
  }
}

function initializeSession() {
  session = OT.initSession(apiKey, sessionId);

  // Subscribe to a signal event
  session.on('signal', function (event) {
    console.log("Event data: ", event);
    console.log("From: ", event.from.id);
    console.log("Signal data: " + event.data);
  });

  // Subscribe to a newly created stream
  session.on('streamCreated', function (event) {
    session.subscribe(event.stream, 'subscriber', {
      insertMode: 'append',
      width: '100%',
      height: '100%'
    }, handleError);
  });

  session.on('sessionConnected', function (event) {
    console.log("Session Connected: Event data: ", event)
  });

  // Create a publisher
  publisher = OT.initPublisher('publisher', {
    insertMode: 'append',
    width: '100%',
    height: '100%'
  }, handleError);

  // Connect to the session
  session.connect(token, function (error) {
    // If the connection is successful, publish to the session
    if (error) {
      handleError(error);
    } else {
      session.publish(publisher, handleError);
    }
  });
}

function listArchives() {
  //alert('List archives');
  fetch('/archive/list').then(function (res) {
    return res.json()
  }).then(function (res) {
    console.log(res);
  }).catch(handleError);
}

function startArchive() {
  //alert('Start archive');
  fetch('/archive/start').then(function (res) {
    return res.json()
  }).then(function (res) {
    console.log(res);
  }).catch(handleError);
}

function stopArchive() {
  //alert('Stop archive');
  fetch('/archive/stop').then(function (res) {
    return res.json()
  }).then(function (res) {
    console.log(res);
  }).catch(handleError);
}

function broadcastMsg() {
  //alert('Broadcast Msg');
  fetch('/broadcast/msg').then(function (res) {
    return res.json()
  }).then(function (res) {
    console.log(res);
  }).catch(handleError);
}

function screenShare() {
  OT.checkScreenSharingCapability(function (response) {
    if (!response.supported || response.extensionRegistered === false) {
      // This browser does not support screen sharing.
    } else if (response.extensionInstalled === false) {
      // Prompt to install the extension.
    } else {
      // Screen sharing is available. Publish the screen.
      var publisher = OT.initPublisher('screen-preview',
        { videoSource: 'screen', width: '100%', height: '100%', insertMode: 'append' },
        function (error) {
          if (error) {
            // Look at error.message to see what went wrong.
          } else {
            session.publish(publisher, function (error) {
              if (error) {
                // Look error.message to see what went wrong.
              }
            });
          }
        }
      );
    }
  });
}
```

There was also some CSS to provide some *very* basic layout:

``` css
body, html {
    background-color: gray;
    height: 100%;
}

#videos {
    position: relative;
    width: 100%;
    height: 100%;
    margin-left: auto;
    margin-right: auto;
}

#subscriber {
    position: absolute;
    left: 10;
    top: 10;
    width: 80%;
    height: 80%;
    z-index: 10;
    border: 6px solid blue;
    border-radius: 6px;
}

#publisher {
    position: absolute;
    width: 360px;
    height: 240px;
    top: 60px;
    left: 30px;
    z-index: 100;
    border: 6px solid red;
    border-radius: 6px;
}

#screen-preview {
    position: absolute;
    width: 720px;
    height: 480px;
    top: 60px;
    right: 30px;
    z-index: 120;
    border: 6px solid greenyellow;
    border-radius: 6px;
}

.topnavbar li {
    display: inline;
}
```

And finally some HTML to hold it all together:

``` html
<html>

<head>
    <title> OpenTok Getting Started </title>
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
    <link href="css/app.css" rel="stylesheet" type="text/css">
    <script src="https://static.opentok.com/v2/js/opentok.min.js"></script>
</head>

<body>

    <div class="topnavbar">
        <ul>
            <li>
                <button onclick="listArchives()">List Archives</button>
            </li>
            <li>
                <button onclick="startArchive()">Start Archive</button>
            </li>
            <li>
                <button onclick="stopArchive()">Stop Archive</button>
            </li>
            <li>
                <button onclick="broadcastMsg()">Broadcast Message</button>
            </li>
            <li>
                <button onclick="screenShare()">Screen Share</button>
            </li>
        </ul>
    </div>

    <div id="videos">
        <div id="subscriber"></div>
        <div id="publisher"></div>
        <div id="screen-preview"></div>
    </div>

    <script type="text/javascript" src="js/app.js"></script>
</body>

</html>
```

Note this was a static HTML file loaded by Flask. The file needs to be
located in the `static` folder in the web server root. The file could
be loaded with `localhost:9000/static/index.html`.

Yes, this needs to be improved!

## Screensharing

I'm running Chrome 73 so adding support for screensharing was easy -
no browser extensions needed to be installed, or worse, written. The
screenshare stream is highlighted using CSS in `greenyellow`, just to
delineate it was the publisher (red) and subscriber (blue) areas.

## Future work

I do plan to continue working on this when hacking time is allowed. At
Nexmo we usually have one hack day per month to work on any project we
like, although I will probably squeeze some extra time to work on
this. Here are some of the features I plan to add:

* First, improve the UI. It should have a Create Room or Join Room facility.
* Tidy up the Python code.
* Improve layout for multiple clients connected (some kind of CSS tiling to organize the streams).
* Get it hosted on the Net. Most likely I will use Heroku. In the past I would have used Digital Ocean.
* Add database support. 
* Multiple session support.
* Add a mobile client (Android).

## Summary

Hacking on OpenTok was a thoroughly enjoyable experience (thank you
Manik). Getting a video chat going relatively quickly, without much
coding, is instant gratification. You even get to like (or ignore)
those audio feedback squeeks and whistles - it means it's working!

## Resources

* [TokBox](https://www.tokbox.com)
* [TokBox Developer Centre](https://tokbox.com/developer)
* [My hacking session code on GitHub](https://github.com/tbedford/OpenTok-Hackathon)

---

* Published: 2019-03-21 07:11:12 UTC
* Updated: 2019-03-21 07:11:12 UTC
* UUID: BE505895-B41D-4EC9-B3ED-FD83ECD724EA

