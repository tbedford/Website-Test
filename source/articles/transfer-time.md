# How long to transfer a 1TB file?

Summary: How long does it take to transfer a 1TB file? Python can
help.

Well, let me ask you a question, how long would it take to transfer a
1TB file electronically?

This isn't a trick question, but it does highlight something that
people (meaning me) have problems with, visualizing very big numbers.

My own guess of a few hours turned out to be way out as the following
Python code shows:


``` Python
# Python 2.7

fs = 1 # 1 in TBs
rate = 10 # in Mbps

print "Time to transfer a %d TB file at %d Mbps" % (fs, rate) 

fs = fs * 1000000000000 * 8 # convert to bits
rate = rate * 1000000 # convert to bit per second

time = fs / rate # in seconds

print "Transfer time in seconds:", time
print "Transfer time in minutes:", time / 60 
print "Transfer time in hours:", time / (60 * 60)
print "Transfer time in days:", time / (60 * 60 * 24)
```

A run of the code shows how long in would really take assuming a
modest 10Mbps internet connection.

``` shell
Time to transfer a 1 TB file at 10 Mbps
Transfer time in seconds: 800000
Transfer time in minutes: 13333
Transfer time in hours: 222
Transfer time in days: 9
```

Now, if you just had one of those 1 Gbps Google Fibre pipes in your
house, I wonder how long it would take?

---
* Published: 2017-10-31 17:20:43 UTC
* Updated: 2017-11-15 17:43:00 UTC
* UUID: 94F751C6-C1A5-4844-8F9C-60C981A5BFD8

