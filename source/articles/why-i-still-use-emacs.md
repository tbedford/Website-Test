# Why I still use Emacs

I was chilling out in the office when Terry came in and announced he
and a couple of the lads were going up to London to sort out this damn
James Gosling guy, who was giving a talk that evening, about this
newfangled thing called NetBeans, and did I want to come. You
betcha. Their main aim was to take him to task over what was going on
with this Java malarkey, which they weren't happy with, and bend his
ear about about pretty much all of it. I thought it would be a great
opportunity to see the man himself, who is a A Legend, jealously
admire his magnificent hacker beard and shiny pate combo (I have one
of the two), and ask one or two questions of my own.

James gave a really great talk, but I always remember one thing he
said about NetBeans, the Java IDE. He said "I'm just trying to get
you away from the whole 'Emacs in a terminal situation'".

Hand raised. Guiiiillllltttty!

Here, we are, nearly twenty years on, and I'm still using Emacs in a
terminal as I write this. All my coding is done here too. All my
technical writing in DITA or DocBook or Markdown is done here as
well. Poor James would be pulling out great tufts of beard hair in
frustration.

But it begs the question - why?

Now, I will say, I'm not one of these Emacs wizzzards, who, with about
three keystrokes, can take a dodgy old Windows text file version of
The Bible (aka Kernighan & Ritchie's The C Programming Language)
convert it into Man pages, and have it spellchecked, detabified and
with correct Holy Unix line endings, while simultaneously playing the
flute. Well, I exaggerate, but you know what I mean. They are a sight
to behold. Well, I'm not one of _those_ Emacs gurus. I'm an Emacs
basics kind of guy. I have to look up how to do a search and replace,
especially a regex one. Emacs is not exactly intuitive. So why keep
using it?

I can only say for mysef - these are my reasons...

## Handles any type of file

Emacs can handle any type of text file you'd care to throw at it. From
the same editor you can edit plain text, Markdown, AsciiDoc, Python,
Ruby, Java, C, XML, XSLT - the list goes on.

If you have a language-specific editor or IDE, and it just doesn't
handle the coding language you need to work with, you need to fire up
another editor. Many years back I worked on MySQL Connector
documentation and there were many connectors - one for each of the
main programming languages. I also had to edit DocBook files at the
same time. With Emacs I could load any code up, have it syntax
highlighted, and have special language specific modes - even for XML
(NXML is a thing of beauty). 

And then you get a new file format from left-of-field. No worries with
Emacs. I recently had the misfortune to have to edit vast numbers of
TeX files. Emacs has a nice TeX mode which made things a lot easier.

I never had to change editor. It's the same now. I can edit pretty
much anything I want, from Bash shell scripts to DITA in the same
editor.

## It can handle giant files without having a heart attack

I've edited massive files with Emacs and it loads them in a
flash. Back in the day we had this doc system that use to munge all of
the individual DocBook files into one giant DocBook file, so it was
possible to validate references. Sometimes you had to check that file
to help fix an issue and this thing was monstrous. Imagine about
15,000 files of on average a hundred or so lines all munged into one
big file. I'm on line 81 of this text file and it's already nearly 4K
in size. So, my doc file would have been 60MB or so right? Phew. I've
known a few editors that would have choked on that. Not Emacs. Oh no
siree!

## Available everywhere

Emacs is ubiquitous. It's available on virtually every platform you
can imagine, not just the big three (Mac OS X, Linux, Windows). It's
on pretty much every system you might have to work on. Many years ago
I used to love using PSPad. But it was Windows only. When I shifted to
Mac OS X as my main platform I couldn't take PSPad with me. I was sad
about that. You can take Emacs with you whereever you go.

## Runs fine in a terminal

Emacs comes in a full blown graphics mode version, as well as a
terminal only version. I use the terminal only version. On Windows I
use the graphical version. On the Mac I use Aquamacs, but mostly the
terminal Emacs.

## Keystrokes ubiquitous: command line (Unix), various editors, email 

Once you get used to commands like `C-a` (go to start of a line), you
find they work in many places you hadn't expected, line on the
terminal command line. In in your email editor, or in that Mac app you
use to take notes. A lot of text editor components support Emacs key
strokes by default. This gives you a key stroke command set you can
use all over the place. This is efficient. You only need to learn one
set of keystroke commands, you can then use them in many places.

## Automatic backups

Emacs backs up your work automatically. I once wrote a Bash shell
script that was supposed to rename some text files. Instead it deleted
them all! Luckily Emacs saved the day - I was able to recover
everything from the backups folder.

## Really nifty search facility (use this a lot) 

`C-s` and `C-r` are probably the two commands I use the most in Emacs,
once I've got a file loaded (`C-x C-f` to do that - with tab
completion). This give you very fast incremental search (forwards and
backwards respectively). It lets you zip through a file trying to find
what you want, and it amazes the hell out of people when they see how
quickly you can find stuff. What's more `C-r` is incredibly useful on
the command line to find previously entered shell commands. This alone
will save you lots of time (and typing). I should also mention you can
actually run a terminal in an Emacs buffer too - quite handy as you
can compile and run code without having to leave the magnificence of
Emacs.

## It's really, really fast

I mostly use the terminal mode Emacs. It loads instantly. It loads
files instantly. It lets me edit without any delays. It lets me search
quickly. It never slows me down. Given the sort of processor and RAM
we have in today's computers this should not come as a surprise. The
fact that it does says a lot about the terrible state of most software
today. It's refreshing to use a genuinely fast editor.

## Has its own quirky charm

Emacs grows on you. The first time you use it you will probably want
to throw it, or yourself, out of the nearest window. It's made a few
people turn to drink. But stick with it, the learning curve, the
frustration of configuring the damn thing, but the warm fuzzy feeling
you get when it does your bidding is worth it.

## It will always be there

Emacs isn't going anywhere. There are a few good editors out there
that came and went. Or went through a very dodgy patch. It would be a
shame to invest in learning an editor only to have it disappear
overnight. Emacs isn't going anywhere.

