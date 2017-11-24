# Limits of Markdown

Summary: In which I discuss the limitations of Markdown when
constructing websites and documentation systems.

So, building this site from nothing has been fun. I wrote everything
myself starting from the simplest HTML file. I added simple CSS, and
Python code to process the HTML produced by the Markdown tool into
servicable HTML. I added in a few features like syntax colouring and
some Bash shell scripts to build everything. 

If you've looked at my GitHub repository you'll see this project was
named Website-Test. This was always meant to be a test bed to learn
how to create my own website in a sane way. So far so good. It has
worked quite well.

Recently though I've been delving into CSS more. For example I've been
looking at using CSS to create a top navbar, rather than using my
rather brutalist list o' links. I would like article-specific styling
too, and unique styling for the footer, and then I want to add
different styling for admonitions and so on. 

This is all very doable using CSS classes like header, footer,
topnavbar, note, sidebar and so on. But this is where I run into a
problem. In Markdown source how to I say "this is an article"? And how
do I say in Markdown "this is a topnavbar, not a list o' links"? We
are back to the old semantic vs presentational argument as I touched
on in my article on the [woeful web](./woeful-web.html).

As a technical writer I've come to appreciate the huge benefits of
using a semantic markup (like DocBook, DITA). This has been learned
the hard way, over many years experience of running into the headaches
you get when you use presentational-only markups. Now I find myself
running into those same old issues, albeit on a somewhat smaller
scale.

So, I've decided to move away from using Markdown as the source format
and move to a custom XML markup. It's early days yet, and I've not
worked out the XML markup I'm going to use. DITA and DocBook are far
too heavyweight for this scenario. I will also avoid XSL (in a
nutshell it's too ugly and too slow). I would rather generate the HTML
from Python.

As usual I will start with baby steps. I want to convert the Links
page and Presentations page to XML and do the conversion with Python
and see how that goes. 

In theory I should be able to generate much more sophisticated HTML,
which will then allow me to use much more sophisticated CSS. This
could also scale up to being able to build much more complex static
sites - and I have a few ideas in that direction, but more on that in
another article.

All in all, this should result in a much more powerful and easier to
use website.

Stay tuned!

---

* Published: 2017-11-24 12:15:37 UTC
* Updated: 2017-11-24 12:15:37 UTC
* UUID: 9AB8236F-054E-478D-B464-7E44E639D3A6


