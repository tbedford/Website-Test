# Excel ain't a database!

Summary: A light-hearted story on the problems of using Excel as a
database.

So I got a call from a mate who owns an oil services company. He was a
gibbering wreck on the end of the phone "I've got this spreadsheet
with my customer list in it and I need to get these companies out
based on categories and into MailChimp" he jabbered, barely coherent.

"OK calm down. How many companies have you got in this spreadsheet?" 

"Five or six thousand."

OH. MY. GOD.

My turn to be a gibbering wreck.

"DATABASE! DATABASE! DATABASE!" I screamed down the phone and hung up.

When I'd calmed down and had a stiff drink I called him back and had a
long heart-to-heart with him. Things were worse than I had
thought. They were emailing this customer list around the company as
an XLSX file and random people were modifying it, adding new
contacts. There was no one source of The Truth. The other thing was
each company was categorized, and actually might be in multiple
categories like Marine, Oil and Gas, and so on. He wanted to extract
companies from certain categories and add them to specific targeted
mailing lists in MailChimp.

This is the sort of project that Python just CHEWS THROUGH with ease!

I could talk about that, and will in other articles. 

But in this article I want to get across one thing:

Excel is a great spreadsheet application, but it makes for a lousy
database system once you get beyond a certain size. I think if you are
managing more than a hundred companies in a spreadsheet you are
certifiably insane.

As a first stop measure you really want to get a spreadsheet of that
size into something like Google Sheets. You can then have multiple
people working on a single source of truth. It's also less vulnerable
there. Laptops get stolen, left on airplanes and on trains. Hard disks
are often unencrypted, exposing valuable contact lists to all and
sundry. Obviously, if the main XLSX file is lost, and there's no
backup, it's sayonara baby.

But really it just becomes hard to manipulate the data in an XLSX
file, because especially where the data is relational it should be in
a Database Management System (DBMS). Even Access would be better than
Excel for the job (although I don't necessarily recommend it).

Also, you try accessing the customer database in Excel over the
Internet. What tends to happen is some rep in Abu Dhabi says - can you
email me the latest version of the customer list? Hard to believe this
sort of thing still happens in the 21st century. But the reality is
that most companies whose core business is not IT or software
development are clueless about such matters.

How do you sort that spreadsheet to generate a list of all companies
in Abu Dhabi, or all companies in Oil and Gas, or all companies that
recently placed an order?

But I can understand why it happens. A lot of small companies don't
have IT strategies. They don't have a good IT guy they can trust. The
spreadsheet starts off innocently enough, and then it just grows and
grows, into some kind of monster that you can no longer control. And
that's when I get that caffeine-fuelled call in the middle of the
night, the sound of sheer panic on the other end of the line.

And that's when I change into my best coding T-Shirt, put on a brew,
and call my superhero Python to come down and do its thing.

---

* Published: 2017-10-15 07:34:16 UTC
* Updated: 2017-10-15 07:34:16 UTC
* UUID: 9AD44013-4732-46A2-831C-154913C1AF5F

