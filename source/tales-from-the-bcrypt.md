# Tales from the Bcrypt

So, I had to write a little piece of code to authorize users into my
web app. I know enough that you really don't want to store passwords
in plain text. But simply hashing a password leaves it vulnerable to
dictionary lookup attacks. You need to spice up the hash a bit with
some salt. You could just generate a GUID for your salt and that would
work.

You could also use the random module to generate a random number, or
perhaps use a datetime value somehow as a salt. Of course you'd need
to pick a hashing algorithm, and one that was not too fast mind (the
faster the hashing algorithm is, the more vulnerable it is to brute
force attacks), and you'd also need to store the salt on your
database, along with the hashed password.

Well, you could do all that. 

But why do that when the hard work's been done for you?

That's where the wonderful `bcrypt` module comes in. Bcrypt is a
little different in that it's a hashing algorithm that stores the salt
with the hashed value. So you don't need to store the salt
separately. That's good. It's also incredibly easy to use in Python
too.

You have a little function that hashes up the plain text password. The
hashed password can get stored in your database with the user's
credentials. When the user logs in you need to retrieve the hashed
password. You then need to hash the plain text password the user has
just given you, and here's the mind-blowing bit, using the hashed
password you've just retrieved. The salt will be extracted from it and
used to hash the plaintext password again, to give you a hashed
password generated from the given plaintext password the user just
gave you.

You can now check the hashed password you've just generated against
the one you've fetched from the database. A match? Great! Don't match?
Wrong password!

The code will hopefully help explain it:

``` python
import bcrypt

# hashes a plaintext password using bcrypt with bcrypt the hash
# contains the salt, so no need to store separately.

def hash_password (password):

    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password, salt)

    return hash

def check_password (password, hash):

    hashpw = bcrypt.hashpw(password, hash)

    if hashpw == hash:
        return True
    else:
        return False

password = "secret".encode('utf-8')

hash = hash_password (password)
print (hash)


new_pword = "secret!!!".encode('utf-8')

if check_password(new_pword, hash):
    print ("passwords match!")
else:
    print ("passwords DON'T match!")

```

Pretty simple heh? I love Python!

The only other thing worth pointing out there is that the bcrypt
function expects a sequence of bytes, and as Python stores strings
internally as Unicode, actually as UCS-2 or UCS-4 characters (probably
UCS-4), so you need to encode the Unicode as UTF-8, hence the call to
the ```.encode('utf-8')``` method. 

Actually the default for the encode method is UTF-8 anyway, but it
doesn't hurt to be explicit, especially in this area of Python
(strings, encodings) where there is ample scope for SNAFUs to happen!
