# Bootstrapping

Summary: A look back at 'bootstrapping' in the 1980s.

It was 1984 and I was a Twin Otter flight and a white-knuckled chopper
ride out of Khartoum and in the middle of the desert. It was my first
day working in the Veribo. The Veribo was basically a big wooden box,
the size of a small mobile home, with an aircon bolted on, and didn't
look like much from the outside but the magic happened within.

Inside was the equipment for testing the cable telemetry boxes used in
seismic exploration.

The telemetry boxes hooked into geophones and then hundreds of them
were all connected up by cable sections over miles of exploration
prospect. This network was known as "The Line".

The Line was connected at the roughly half-way point to something
ignomiously named "the dogbox". The dogbox was the main command and
control centre that committed all data to magnetic tape and printed
the received seismic signals out onto thermally-sensitive paper.

Explosions were set off, shock waves travelled down through the Earth
and bounced back, reflected by the layers of rock. Geophones (think
microphones you stick in the dirt) converted the received sound waves
into electrical signals, which were then amplified, filtered,
digitized, encoded, time-stamped, synchronized and transmitted down
The Line by the magic of the telemetry boxes. Each telemetry box also
acted as a repeater, boosting and re-synchronizing the data as it
moved down The Line.

In short it was all a miracle of analogue and digital electronics
created by some very celever people.

The problem was the telemetry boxes would get thrown about like loaves
of stale bread, despite the fact that they were several thousand
dollars apiece. That's where I came in. When broken telemetry boxes
came back in from the field to the main camp it was my job was to
troubleshoot them and repair them at component level. This was back
when component level troubleshooting was a Happening Thing - these
days it isn't - you just throw out the old and in with the new. That
wasn't economically viable for these boxes back in 1984 and that's why
we had the Veribo.

The Veribo was essentially computer automated test equipment. In short
you hooked up your telemetry box to a computer and it injected various
signals, ran various tests, and lo and behold out came what the
problem was. The trouble was the test didn't get very far if the power
supply unit in the box was damaged or another major malfunction was in
play, so this was where I dived in with a soldering iron and an
oscilloscope and realized the three years I'd spent studying maths on
my electronic engineering degree course was a complete waste of time.

But I am getting ahead of myself. Before any of that you had to boot
up the Veribo at the beginning of the day, which was a bit more
involved than just "switching it on".

First, the main computer controlling the Veribo had to be booted. That
was a 4K Control Data Corporation microcomputer. First job of the
day - enter the boostrap code. You had to open the manual to the
bootstrapping page. Here was a listing of assembly language code, with
machine code equivalents handily provided. Each line of the boostrap
program had to be entered manually by flicking switches to the right
position. You had a nice User Experience feature here because each
switch had a corresponding red LED you could check against! So if the
machine code was 0xF0 you'd have four switches up (on) and four LEDS
lit, and four switches down (LEDs) off. You'd then press another
button to enter that code in. At this point I can imagine today's Java
programmers breaking out in a cold sweat. But we are just getting
started here.

Once all the lines of machine code had been entered you now had a mini
bootstrap program to play with. The code could be executed by pressing
another button. There were no end of User Experience wins as this
button was a large one with a green lamp in it! 

Of course the boostrap program didn't do a lot - in fact it only had
one function, to enable a paper tape reader to work. Yes, the main
program that needed to be loaded was on a reel of punched paper tape!
We had a box with about half a dozen or so of these paper tape reels
in them, in various states of decomposition from heat, humidity and
termites, but they basically did the same thing - bring up the
Veribo's main computer fully.

So next job was to load the paper tape into the paper tape reader. Its
little lamp could be seen quite readily and created a cosy glow in the
Veribo. The paper tape reader worked by using a lamp and a series of
light sensors so that the pattern of ones and zeroes on each line of
the paper tape could be read. If there was a hole in the paper tape
the light would shone through at that point and activate the sensor (a
binary 1) if there was no hole you'd get a binary 0 (zero). Those Java
programmers' toes are probably now curling up like bananas.

At this point you had reached the climactic event. Basically you
pressed another button and all hell would break loose. The paper tape
would go whizzing through the reader at what I can only call an
alarming rate, and end up in a tangled heap on the floor of the Veribo
unit. Next job was to wind up the paper tape, put it back in the box
and hope that everything had worked. It might not have. The paper tape
reader was a bit vulnerable to condensation. The high outside
temperatures and aircon didn't help. Sometimes you made a mistake
entering the bootstrap program and so you had to painstakingly flick
switches, check LEDs and enter the minimal boostrap code again. All in
all it was a right pain but could be a lot of fun too.

If it all worked then it was time for the real work to begin and
that's when we'd whack a Bob Marley album into the cassette player,
dig out the scope probes, and get the first patient in from the big
pile of broken boxes outside the Veribo unit. Ah, I love the smell of
solder in the morning...

**Author's note:** The telemetry system we used in Sudan was the
Sercel 348. A system that primarily consisted of discrete TTL
components and analogue electronics. I later used the more modern
Sercel 368 system in Nigeria. The telemetry boxes were more compact
and used more modern types of components including more Integrated
Circuits. You still had to boot up the Veribo though! :)

A nice page looking at Sercel's history can be found here:

* [Sercel history](http://www.sercel.com/about/Pages/history.aspx)

The modern systems look very impressive indeed.

---

* Published: 2018-02-28 09:30:00 UTC
* Updated: 2018-02-28 09:30:00 UTC
* UUID: 395DF47F-F2B3-4FF0-B728-F3CC43A89FA0


