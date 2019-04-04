# How to take out a contract on John Wick

Summary: I show you how to take out an open contract on John Wick with
a bit of help from Nexmo and Python.

The better half was wondering why she'd received a message from the
Continental Hotel letting her know there was an open contract out on
John Wick worth $7 million. She waved her phone at me - do you know
anything about this? 

Let me explain...

We watched [John Wick: Chapter
2](https://www.imdb.com/title/tt4425200/) last night and really
enjoyed it. There's one scene where they put out an open contract for
$7 million on John Wick and various contract killers receive an SMS
with details of the contract. I thought (being someone who needs to
get out more) oh you could do that easily in Python with Nexmo. So
this morning I had something up and running in less than five minutes.

So you have a list of contract killer phone numbers and that could
come from a YAML file, a database, or in my example code a static
array, as I don't know too many contract killers. 

The core code is essentially a loop that uses the [Nexmo Python Client
library](https://github.com/Nexmo/nexmo-python) to send the SMS. Just
to spice things up a little I put in a couple of Unicode skuls as
Nexmo easily supports Unicode SMS.

Here's the code:

``` python
import nexmo

NEXMO_API_KEY = "your key"
NEXMO_API_SECRET = "your secret"

message = "☠ Open contract on John Wick for $7 million ☠"
contract_killers = [ "447700000001", "447900000002", "447500000003"]

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

for killer in contract_killers:
    print ("Sending message to %s..... " % killer)
    client.send_message({
        'from': 'Continental',
        'to': killer,
        'text': message, 
        'type': 'unicode',
    })
```

![John Wick contract](./images/john-wick-contract.png "John Wick contract")

## Resources

* Nexmo Code Snippets: [Sending a Unicode SMS](https://developer.nexmo.com/messaging/sms/code-snippets/send-an-sms-with-unicode)
* [W3Schools Python Tutorial](https://www.w3schools.com/python/)

NOTE: Just so you're clear, the author and Nexmo do not condone the use of
contract killers! ;)

---

* Published: 2019-04-04 09:24:12 UTC
* Updated: 2019-04-04 09:24:12 UTC
* UUID: 9A77B4F2-4746-4BD0-8BA8-4004D871EE64


