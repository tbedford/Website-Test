# Dial-a-chiptune

Summary: In this article I talk about a fun little project I whipped
up in about an hour of pre-breakfast hack time. It's super easy, but
could provide the basis for your own more ambitious projects.

So I was hacking around with Nexmo and needed a little bit of light
relief. I've been listening to quite a lot of chiptune music recently,
so decided to do something that combined Nexmo and my love of
chiptunes. Dial-a-chiptune was the result. It's not meant to be a
serious project - but it could be. You could take the basic idea and
some of the code I describe here, and develop a much more ambitious
project, such as a full-blown Interactive Voice Response system.

## The basics

So the idea is you dial a Nexmo number, select an option, and you get
to hear a chiptune. Simple. Nexmo makes doing things like this
relatively easy. 


## The code

Here's the full code. You have to have a Nexmo Number, configure your
webhooks and deploy to your web server (or use Ngrok). I have covered
all these topics in previous articles so I am going to assume you know
how to do all of those things already.

``` python
#!/usr/bin/env python3
from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

tune_1 = ["https://raw.githubusercontent.com/tbedford/git-testing-repo/master/tunes/Komiku_Sunset_on_the_beach.mp3"]
tune_2 = ["https://raw.githubusercontent.com/tbedford/git-testing-repo/master/tunes/Rushjet1_Azureflux_Remix.mp3"]
tune_3 = ["https://raw.githubusercontent.com/tbedford/git-testing-repo/master/tunes/Kris_Keyser_Only.mp3"]

@app.route("/webhooks/answer")
def answer_call():
    params = request.args
    print("DIAL_A_CHIP_TUNE CALL FROM: >%s<" % params['from'])
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco = [
        {
            "action": "talk",
            "text": "Welcome to dial a chiptune. Press 1 or 2."
        },
        {
            "action": "input",
            "maxDigits": 1,
            "timeOut": 5,
            "eventUrl": [input_webhook_url]
        } 
    ]
    return jsonify(ncco)

@app.route("/webhooks/dtmf", methods=['POST'])
def dtmf_webhook():
    data = request.get_json()
    #pprint(data)
    selection = data['dtmf']
    print("TUNE SELECTED = %s" % selection)
    MESSAGE = "Playing tune " + selection
    if selection == "1":
        #print("DEBUG: Selecting tune 1")
        tune_x = tune_1
    elif selection == "2":
        tune_x = tune_2
    else:
        tune_x = tune_3 

    ncco = [
        {
            "action": "talk",
            "text": MESSAGE
        },
        {
            "action": "stream",
            "streamUrl": tune_x
        }
    ]
    return jsonify(ncco)


if __name__ == '__main__':
    app.run(host="www.fuddyduddies.org", port=9000)
```

A few points about the code:

- Yes, I am abusing my GitHub account by storing MP3s there. They
  would be far better off in an Amazon S3 bucket or something similar.
- Setting 'maxDigits' to 1 makes sure only one key is actually listened to. 
- Operation is much more reliable if I set the `timeOut` to 5,
  rather than using the default setting of 3. It gives a little more
  time to fiddle with the keypad etc.
- It's a Flask application. I've not done a Flask tutorial
  yet. Basically I did a `pip install Flask` and then wrote this
  code. It was pretty easy once you know about `@app.route`. Once you've
  seen an example of how it's done it's easy to write your own routes as
  I did in this case.
- There's a "hidden tune". You are prompted to press 1 or 2, but
  actually hitting any other key will play a third tune.
- The NCCOs are where the real action happens (excuse the pun). These
  are described in detail in the [Nexmo NCCO Reference
  Guide](https://developer.nexmo.com/voice/voice-api/ncco-reference) so I won't repeat
  that here.

Hopefully mostly the code is self-explanatory. The Flask app mostly
provides the webhook implementation with the main control being done
by the NCCOs. Contact me if you have any questions on the code, or
something is really not clear.

## Testing the code

Couldn't be easier. Simply dial the Nexmo Number you linked to your
Nexmo Application and select 1, 2 or actually any other digit key. You
will then receive confirmation of your selection before hearing a
chiptune. Sure the quality of the sound is not great - this is a phone
line with limited bandwidth after all, but that's not the important
thing here. The point is you have a basic IVR application. You can
extend this to suit your own projects.

## Summary

This has been a fun little hack and actually my first Flask
application. You saw how to build a simple IVR application using Nexmo
webhooks and Nexmo Call Control Objects (NCCOs).

## Resources

* [Free chiptune music](http://freemusicarchive.org/genre/Chiptune/) 
* Music acknowledgements: 
  - Komiku - Sunset on the Beach
  - Kris Keyser - Only
  - Rushjet - Azureflux
  
---

* Published: 2018-05-11 07:12:00 UTC
* Updated: 2018-07-05 17:53:00 UTC
* UUID: 5424F74B-749B-42AA-A726-40EE59463EE3


