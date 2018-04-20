# Simple encrytpion of SMS text messages

Summary: In this article I take a look at a really simple SMS
encryption system you can use for sending ever so slightly more secure
text messages when sending them via an API such as Nexmo or Clockwork.

## A really simple encryption system for SMS





## The strings

There are three components here:

1. The plain text message to be encrypted.
2. The key used in the encryption algorithm.
3. The encrypted text message.

In each of the above cases the only acceptable characters are ASCII 32
through to and including ASCII 126.

## The algorithm

The encryption algorithm works in the following way:

1. Take the first character from the plain text message.
2. Take the first character of the key.
3. Add these character values. 
4. If the result is greater than 126 then subtract 95. If the result
   is still greater than 126 then keep subtracting 95 until the result
   is less than or equal to 126.
5. The result is the first character in the encrypted message.
6. Proceed to the next character in the message and the next character in the key.
7. If the key has no more characters but input message remians then
   return to the first chcracter in the key.
8. Repeat until all characters in the plain text input message have been encrytped.

The decryption algorithm is the reverse of this process.


## Example code

``` python
# Python 3
# *****  NOTE: works with BYTE strings ONLY ***** 
import sys

DEBUG = False

k = b"PythonRocks"
m = b"This message is a little bit more secure than usual."

def reduce (c):

    while c > 126:
        c = c - 95
    return c

def expand (c):

    while c < 32:
        c = c + 95
    return c

def encrypt (k, m):

    es = b"" # es = encrypted byte string 
    kl = len(k) # Length of key byte string
    i = 0 # index into key byte string
    for c in m:
        # Encrypt char
        e = c + k[i]
        e = reduce (e)
        if DEBUG == True:
            print ("k is `%c` e is `%c` %d" % (k[i], e, e))
        es = es + e.to_bytes(1, byteorder='little')
        # Reset key index if required
        i = i + 1
        if i > (kl - 1):
            i = 0
        
    return es

def decrypt (k, m):

    ds = b"" # ds = decrypted string
    kl = len(k) # Length of key string
    i = 0 # index into key string
    for c in m:
        # decrypt char
        e = c - k[i] # subtract for decrypt 
        e = expand(e)
        ds = ds + e.to_bytes(1, byteorder='little')
        # Reset key index if required
        i = i + 1
        if i > (kl - 1):
            i = 0
            
    return ds

if (sys.version_info < (3, 0)):
    print ("Python version 3 and above only - join the future!!")
    exit(-1)

em = encrypt(k, m)
print (em)

dm = decrypt (k, em)
print (dm)

# For Testing only below

if DEBUG == True:
    s = "=k2{ ryw,u[}z($r#imxh&.}0[yvq4Vu)r0cus|!T4"
    em = s.encode('ascii')
    dm = decrypt (k, em)
    print (dm)

    print(reduce (127))
    print(reduce (145))
    print(reduce (126))
```

## Encryption through a pipe

xxx

---

* Published: 2018-11-07 09:00:00 UTC
* Updated: 2018-11-15 12:56:00 UTC
* UUID: B0B83A78-451E-4C0D-88E9-4A78020946A5
