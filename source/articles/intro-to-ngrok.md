# Intro to Ngrok

Summary: A quick intro to the wonders of Ngrok.

[Ngrok](https://ngrok.com) is one of those things that I really can't
understand how I never heard of until recently.

This post is *not* going to be a deep dive into Ngrok. The docs on the
Ngrok site give you all the gristly details, so there's no need to
replicate that here. I just wanted to give Ngrok a mention and explain
a little about what it does and how incredibly useful it is proving to
be.

So here's the scenario. You are working on a little web app on your
development machine. You are using a service like Nexmo, Twilio, or
SendGrid. Those services will typically interact with your web app by
calling back on webhook URLs to let you know what's going on. For
example, with Nexmo, the `events` webhook is used by the Nexmo service
to callback on, delivering information about the current call state,
letting you know a call has been answered.

But the problem is if your web app is running on your local machine,
say on `localhost:9000`, the external service can't reach you as your
web app is not exposed to the public Internet. Your web app will
therefore not work as if it had been deployed to the public
Internet. Ngrok to the rescue!

What Ngrok does is create a secure tunnel between the public Internet
and your web app running locally on your machine. Your local app then
appears to work as if it were deployed to the public Internet.

Let's say you are running your web app on `localhost:9000`. After
you've launched Ngrok:

``` shell
$ ngrok http 9000
```

Ngrok will provide a mapping from public URLs to your local web app:

``` shell
...
Web Interface  http://127.0.0.1:4040
Forwarding     http://92832de0.ngrok.io -> localhost:9000
Forwarding     https://92832de0.ngrok.io -> localhost:9000
```

I've excluded some unnecessary information in the above output.

There are a couple of things to notice here. Note that both HTTP and
HTTPS are forwarded to your app. Notice also there is a web interface
provided. Just launch a web browser tab and navigate to localhost port
4040 and you will see a lot of very useful information. Rather than
explain the information there, it's best to just see for
yourself. This feature is great for debugging, such as double-checking
the responses of API calls are what the docs say they are!

In the above you'll see the free version of Ngrok will generate
slightly strange looking URLs - `92832de0` in this case. Although not
a problem for local testing and playing about you can change this wth
a paid plan (about $5 a month). With a paid plan you can use
sub-domains. So you'd be able to do something like:

``` shell
$ ngrok http -subdomain=mangosauce 9000 
```

There are many other useful features of Ngrok that are explained in
the documentation.

So, what are the downsides? The main one is in exposing your web app
to the public machine you are in effect raising the possibility that
an external entity i.e. hacker, could in theory access your
machine. Web apps can be hacked, and if that web app happens to be
running on your local machine that can be a cause for concern. I make
sure I fire up Ngrok only for testing, and I don't leave the Ngrok
tunnel running any longer than I need to.

My previous approach to developing my little web apps was to deploy
them to my Ubuntu server running on Digital Ocean. I usually keep a
Digital Ocean Droplet up and running for various bits and pieces of
testing work. It is quite useful to have your own Unix box connected
to the public Internet. Still, with Ngrok, I expect I will be using
the server a little less often than usual.

---

* Published: 2018-04-13 05:27:04 UTC
* Updated: 2018-04-13 05:27:04 UTC
* UUID: 0134E17B-2745-4043-B553-1BDAE8A3ACAF








