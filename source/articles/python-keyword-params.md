# Python's keyword parameters

Summary: In this article I take a quick look at Python keyword (named)
parameters.

In a [previous article](./understandintg-jwts.html) I looked at a use
case where Python keyword parameters could be quite useful. This was
in building the payload for a JWT. If you remember, I built the
payload at the time using the following code snippet:

``` python
payload = {
    'application_id': application_id,
    'iat': int(time.time()),
    'jti': str(uuid4()),
}
```

As I also mentioned in that article, some of the components of the
payload were mandatory, and some were optional. It would be nice to
have a function where the mandatory items are added into the payload,
and then optional items are then added to the payload if specified.

I will look at one way to do this. Note this is only one way, and
there are probably better ways, but the idea of this article is to
introduce the concept of keyword parameters in Python, and also look
at how to handle optional parameters.

In the above snippet the `application_id` is going to have to be
passed in as a mandatory parameter, as we don't know what ID will be
passed in when the function is called. The caller will need to provide
this value.

The `application_id` item, being mandatory to build the payload, makes
for an ideal named keyword parameter. 

The `iat` and `jti` claims are also mandatory in our use case, but we
can easily generate those inside the function. They don't need to be
passed in.

Further, there may be optional parameters. For example `exp` is an
optional claim. `user` is also optional, although it was not used in
my previous use case. `acl` is yet another optional claim. These could
all be handled as optional parameters, as you will see.

One thing, `exp` is a little bit special, because it requires us to do
some processing as a convenience for the caller. We are going to
assume that the user passes in the time before the JWT expires in
seconds. So for example, if they want the JWT to last 24 hours, the
maximum, they will pass in 24 * 60 * 60. However, because `exp` is
actually the [Unix timestamp](./unix-time.html) of the expiry point,
we would need to do some additional hokey pokey. We would of course
need to be clear to the user of the function that we provide this
convenience for them. I've added this functionality inside the
function because it shows another nice little use case where you need
to process optional parameters.

So, let's take a look at some working code:

``` python
import time
from uuid import uuid4

def build_payload (application_id,  **kwargs):
    
    payload = {}
    payload['application_id'] = application_id
    payload['iat'] = int(time.time())
    payload['jti'] = str(uuid4())

    if "exp" in kwargs:
        payload['exp'] = int(time.time()) + kwargs.pop('exp')

    for k in kwargs:
        payload[k] = kwargs[k]
    
    return payload

print(build_payload("123"))
print(build_payload("123", exp=24*60*60))
print(build_payload(application_id="123", exp=24*60*60))
print(build_payload(application_id="123", exp=24*60*60, user="tony"))
```

Looking at the function definition, there's nothing special you need
to do regarding a keyword parameter, it looks the same as a normal
positional parameter. However, when you call the function you can
specify a name. This makes the nature of the parameter very
specific. For example, in the first two example calls I treat
`application_id` as a positional parameter - the name is not
specified. However, in the subsequent two example calls I do specify
the name - this makes what's going on very explicit. Also, if I do not
specify an `application_id` parameter I will get an error, which is
good because that is a mandatory item. As a general rule of thumb it's
good to be explicit in your code where possible.

We can also see that the other two mandatory items, `iat` and `jti`
are taken care of for us. No further comment is required on that.

Now, how to deal with optional parameters? This is where `**kwargs`
comes in, these are optional keyword paramters, and you can have any
number of them at this point. 

The `kwargs` is really just a Python dictionary with the `**` as a
little syntactic sugar. This makes it easy to work with. In the
function I grab `exp` if it's present, and work out the correct Unix
timestamp. If no `exp` parameter is passed in that's no problem as the
JWT will have a default expiry of fifteen minutes anyway. Once I've
calculated the correct value for `exp` in the payload I pop it out of
the `kwargs` dictionary as I don't need it any more. This won't affect
other optional parameters.

In the final example call the `user` optional keyword parameter is
passed in. That is just added to the payload without further ado,
although you could add in error handling and so on. I have not
included any of that in the interests of clarity.

If any more optional keyword parameters, such as `acl` were provided,
they would also be added to the payload.

## Default values

One thing I didn't show in the above eample is that keyword parameters
can have default values specified in the function definition. For
example:

``` python
def myfunc(amount=3*4, user="tony"):
    print(amount, tony)
    
myfunc()
```

Although no parameters are specifed in the function call, this would
actually print `12, tony` as the default parameter values specified in
the function definition would be used, if not specified in the
function call.

So, that just about wraps things up for this piece. Hope you found
that useful.

## Summary
 
This article has taken a quick look at Python keyword (named)
parameters and optional keyword parameters. I also took a quick look
at default parameters which can be very useful.

---

* Published: 2018-11-02 06:27:13 UTC
* Updated: 2018-11-02 06:27:13 UTC
* UUID: 87C0EBF5-689F-4C1A-B6F6-B9A54E16A14D

