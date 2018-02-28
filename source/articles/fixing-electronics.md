# The lost art of fixing electronics

Summary: Some thoughts on the lost art of fixing electronics.

The soldier pointed the gun and me and screamed, his face contorted in
rage. We froze. I thought my number was up. Slowly, very slowly, the
taxi driver reversed up the dirt path. We had wanted to see Entebbe
airport close up, but this was a little too close for comfort. It was
the mid-90s in Uganda, and Idi Amin was long gone, but things were
perhaps more volatile than we'd anticipated. We headed back to the
hotel and finally started to breath normally as Entebbe dropped away
behind us into the distance.

I'd been hired by the British Council to set up electronic repair
courses in Uganda. The brain child of a biology lecturer at the tech
college where I worked the project had had a long and convoluted
history. He'd been on a recuitment drive in Uganda and had literally
tripped over a pile of electronics. When he asked what it was he was
told it was there because no one knew how to fix it. He'd had a light
bulb moment. All he needed now was some money and someone who knew how
to fix electronics. The British Council provided the money. Then I was
invited down to the college's cavernous tea rooms by someone I didn't
know. 

It turned out he'd been asking around and found he had two
problems. The first was you could count on one hand the number of
people in the college who could repair electronics. The second was
they hadn't the slightest interest in going to Africa, even when cold
hard cash was placed on the table in front of them. 

Not only did I know how to fix electronics but I'd spent three years
working in various countries in Africa and had built up some
resistence to possible culture shock. I'd had malaria, been bitten by
rats, spiders and snakes, had slept next to a river full of crocodiles
in nothing more than a flimsy tent, and had walked, driven, floated,
and flown my way over four vast countries on the continent. He knew I
was the man for the job. He just had to convince me I wanted it.

It was my kitchen that swung things in his favour.

The wife wanted a new one and we didn't have any money as we were
surviving on my lecturer's salary and we had two children to feed and
clothe. And the wife really wanted that new kitchen.

We hacked out a deal, the wife would get rid of me over the summer,
and get a new kitchen to boot, so she was happy. I might just about
survive the trip, so I was happy. They were putting me up in a decent
hotel too which helped soften the blow - I was not going back to
sleeping in tents in the bush again.

So I designed an electronic repair course and went out to Uganda that
summer and trained the trainers at Uganda Polytechnic Kyambogo
(UPK). I ended up going back again several times and the courses were
very successful. The trainers trained others and everything from
hearing aids to electron microscopes were repaired.

Unfortunately couldn't leave well alone, and what had been a very
successful and long term operation fell to dust. I moved on. I had
learned two things though 1) College politics are ruinous. 2)
Electronic repair was an extremely useful skill that can changed
lives.

My own career moved away from electronic repair towards software
development, in part because the economic realities were that few
people found component level repair to be cost effective in the late
90s. At least in the UK. There were certain pieces of very expensive,
very specialized equipment, like electron microscopes, gas
chromatographs, and some medical equipment that were still being
repaired to component level, but generally electronic repair was,
commercially, a dying sector.

Fast forward to 2018. Is electronic repair a forgotten art now?

## South East Asia

Recently I was in Manila and I have some good news to report.
Component level repair of all kinds of devices is still a
reality. This was a phenomenon I had first noticed in Bangkok back
in 2003. The malls would often have a whole floor devoted to
electronics. These were Aladdin's caves of flashing LED displays,
colourful racks of electronic components, and fresh solder
fumes. These places were a hive of activity where you could get more
or less anything electronic repaired, a phone unlocked, or spare parts
for your laptop. The phenomenon was also were much present in
Philippines in 2011.

When I visited Bangkok again in 2016 I was pleased to see the repair
shops were by and large still intact.

Fast forward again to Philippines 2018 and malls like MegaMall have a
whole floor devoted to electronics. These floors are vast - there are
probably a hundred or more outlets on one floor. Of course some of the
shops are now devoted primarily to the ubiquitous smart phone and
tablet sales, but there are still the little units that will repair
pretty much anything for you. [SST
Repair](http://sstrepair.com/services) is a great example. They will
fix just about anything and unlock just about anything. They have
branches outside of Manila too.

Of course in countries like Thailand and Philippines it is still
economically viable to repair these devices. Labour is relatively
cheap at the moment, and the devices relatively expensive. In the UK
the economics are different - labour is expensive, making the cost of
repair less viable, and people are generally better off, simply
replacing devices that no longer work or even replacing perfectly
viable devices with the very latest model. As Thailand and Philippines
continue to develop, salaries will increase, labour will become more
expensive and the devices will become less economically viable to
repair. Many of the repair outlets will either die, or change to a
sales-only mode of operation - it will be a sad loss.

## Age of the Raspberry Pi

To a certain extent the Raspberry Pi was meant to get students back
into the DIY culture that existed back in the 1980s. If you wanted a
computer back then you went to your local ElectroValue store and
bought the bits and built one. I actually cut my teeth by building my
own TTY out of TTL components using the book "Television Typewriter
Cookbook" written by Don Lancaster and published by Sams. Most people
today don't know what a TTY is. 

The Pi has been successful, but basically represents a cheap(ish) way
to get into programming. Some do build extension circuits for it, but
I think in this respect the Arduino is a better option - it's a lot
simpler and is relatively easier to understand fully. It's also
cheaper to replace when you accidentally blow one up!


## Where to start?

I personally don't believe the Pi is a good starting point to learn
electronics repair. The Pi is a very sophisticated piece of
electronics that has very complicated software. I think there is much
value to be had from starting with a simpler device such as an Arduino
and building some simple interface circuits (a 7-segment LED interface
is a good starting point) and some software and go from there. 

If time was no object I would dust off my soldering iron and build a
Z80 Single-Board Computer (SBC) from scratch. These days it's quite
feasible to build your own Floppy Disk Controller (FDC) and write the
software for it. [It's a big project but
doable](https://www.youtube.com/watch?v=01FP3vsBzvI).

There are some interesting repair projects out there. There are some
nice channels on YouTube where people are doing interesting projects
such as [troubleshooting arcade
electronics](https://www.youtube.com/watch?v=WgB-VDo02vk).

You can pick up practical electronics by building simple circuits on a
breadboard and then getting them working. This usually requires basic
troubleshooting skills. This was how I learned. I also picked up old
radios and attempted to repair them - I wasn't always successful.

## Components

My local components store, ElectroValue, is now long gone, wound up
in 2005. I bought components there from 1981 to the
mid-nineties. Those were days when people knew about building their
own computers and making sure your ICs had 10nF de-coupling
capcitors and a stable 5V line. 

The Last Great Hope in the UK seems to be Maplins. They do at least
sell some components and hobbyist equipment. Online, AdaFruit is also
a shining beacon of what is possible.

There is a lot to be said for getting a circuit diagram, buying some
components and building a certain from scratch - and getting it
working of course!

## Hope

It's not all bad news. There is hope. The Maker culture and the
occasional occurrence of a local Maker Space is very welcome.

There are signs that people are understanding that electronic repair
is often the evironmentally thing to do - rather than throwing broken
items into landfill they can often be repaired for free. [Repair
Cafes](http://www.tewkesburyrepaircafe.co.uk/recent-repairs/) are a
good indication of this trend. It can be quite educational simply to
watch someone who knows what he or she is doing reapir a piece of
equipment - it can be a very positive experience!

## Conclusion

The art of electronics repair is probably not quite as lost as it
appears to be at face value.  While it is true that electronic repair,
especially to component level, is not as commercially viable as it
once was, there are still electronics hobbyists out there keeping the
electronic repair flag flying. Long may that continue!


## Resources

* YouTube - there are many videos on electronic repair - [EEV Blog is a good channel](https://www.youtube.com/user/EEVblog).
* A review of the [state of electronics](https://www.youtube.com/watch?v=9GTgQrP5_c8) in Australia/The West 
* Books: Electronic Troubleshooting by Tromal et alia, Practical Electronics for Inventors by Paul Scherz and Simon Monk.
* Book: Radio Repair by Les Lawry-Johns (old but good).
* PDF: [Les Lawry-Johns wonderful articles on TV
  repair](https://www.vintage-radio.info/llj/). Wonderful to read even
  if you haven't got a clue about analogue electronics! Of course TV
  repair was one of those things that became less economically viable
  over the years.

---

* Published: 2018-03-01 06:30:00 UTC
* Updated: 2018-03-01 06:30:00 UTC
* UUID: 4DCA8997-FBCE-4104-BD37-1A97637AC3B4

