# Emacs keyboard configuration on Mac

Summary: In this article I talk about configuring Emacs for use on Mac
OS X. The configuration works with both terminal Emacs and Cocoa Emacs
(desktop).

A rite of passage, and some would say trial by fire, of working with
Emacs on Mac, is getting your keyboard configuration set up
correctly. The actual setup depends on your needs. Things might be
simpler for example if you only ever use terminal Emacs. Although I
mostly use Emacs in the terminal, there have been a number of
occasions where working with the Desktop (Cocoa) version of Emacs is
useful - mainly when I wanted to copy and paste large blocks of code
to another app. This is tricky with the terminal version of Emacs,
especially when you have split frames. I also used to be an avid user
of Aquamacs before I had problems with upgrading it, so a cross-Emacs
configuration is certainly a very nice thing to have.

This article assumes you know a bit about Emacs such as the importance
of the Control and Meta keys as used for correct Emacs operation.

p.s. I still haven't got this quite right!

## Getting a '#' character

When you start using Emacs on the Mac, one of the first issues you run
into is how to get the darn '#' character to work! It seems like such a
basic thing. But many fall at this first hurdle. The easiest solution
I have come across is to insert the following line of Elisp into your
`.emacs` file:

``` clojure
;; get hash key working on Apple Mac!
(global-set-key (kbd "M-3") '(lambda () (interactive) (insert "#")))
```

Ah, so now we have a working '#' character at least! Or do we?

## Terminal Emacs

The problem at this point, if you are running Emacs in a terminal, is
that the key combination you use to insert a '#' character is the Mac
`option` key followed by the '3' key, also marked '£' and '#' if you
are in the UK. In other countries this may well be
different. Sigh. Another complication. 

Anyway, the `option` key is normally designated as the very important
Meta key in Emacs. On PC type keyboards the `option` key is actually
the `alt` key and is also next to the `Ctrl` key which makes it very
convenient for Emacs users. Both Ctrl and Alt keys, or `C` and `M` as
they are usually designated in Emacs are two important keys in Emacs.

So for example to execute a command in Emacs you would use `M-x` where
M is the Meta key, which is the `option` key on Mac. There is thus a
conflict here where Mac wants to use the `option` key as, well, the
option key, and Emacs wants to use it as the Meta key.

So, how to get around this conflict between Option and Meta in the
terminal? Well there's a sneaky little keyboard config option in the
Terminal Preferences known as 'Use Option as Meta key'. Make sure that
is ticked and lo and behold your option key now works correctly as the
Emacs Meta key.

## Start and end of buffer hot keys

If you only ever use the terminal version of Emacs then everything is
plain sailing, more or less, from now on. So for example, let's say
you want to configure `M-up` as 'go to start of buffer' and `M-down`
as 'go to end of buffer', you could use some config such as:

``` clojure
(global-set-key [27 up] (quote beginning-of-buffer))
(global-set-key [27 down] (quote end-of-buffer))
```

You can now easily jump to the start or end of a buffer with `M-up` or
`M-down` (Meta and up arrow key or Meta and down arrow key).

However, if you then use the desktop version of Emacs on Mac this will
not work. Oh dear...

## Desktop Emacs

When you fire up the Desktop version of Emacs you'll find the previous
key setup no longer works - you can't jump to start and end of buffer
using `M-up` or `M-down`. Why? The reason is that in the terminal
version we'd configured the Terminal application itself in Preferences
to 'Use Option as Meta key'. We need the same sort of config for the
Desktop. Well there isn't one. So you have to do something else. One
thing you *could* do is you can reassign the Option key.

**UPDATE1:** While this does work if you only use Emacs, it kills the '#'
for other apps!! Not good. I am working on a fix. I have gone back to
setting the Mac key to its default and switching 'Use Option as Meta
key' in Terminal. I think I am going to have to use a different key
combo for beginning and end of buffer in the Desktop Emacs. You can
use Esc-< and Esc->, but this requires using the shift key which is
awkward. Esc-, and Esc-. might work, so you don't have to use the
Shift key, but I need to do some more testing.

**UPDATE2:** So rather than leave you in the lurch I've come up with a
quick fix. You can use the M-, and M-. to go to beginning and end of
buffer in desktop Emacs. My fingers are still wired to using M-up and
M-down, which is what I use in the Terminal Emacs, but I've never been
able to get that to work for some reason in Desktop Emacs. At least
M-, and M-. is a bit easier to use than the usual M-< and M->, which
is the default setting for Emacs and a pain to use due to the need to
use Shift as well. Anyway, sorry about this confusion and here's the
additional config:

``` lisp
(global-set-key (kbd "M-,") 'beginning-of-buffer)
(global-set-key (kbd "M-.") 'end-of-buffer)
```

So go to System Preferences/Keyboard. There's a button called "Modifer
Keys...". Click that. You can then reassign the Option key. I reassign
it to Escape. This is all cool because in Emacs the Meta key can be
the alt/option or Escape key, although the Esc key is not normally
used as it's up there out of the way on the top left of the
keyboard. So now the Option key no longer does the usual Mac things,
which frees it up for use in Emacs. You'll find once you've done this
that `M-up` and `M-down` now works as expected in both terminal Emacs
and Desktop Emacs.

But going back to the terminal Emacs...your key config no longer works
there! Arrrrgggghhhh!!

Luckily the solution is simple. You can now simply turn off the 'Use
Option as Meta key' in Terminal preferences and it's all good. Phew!

## Summary

I can't pretend that keyboard configuration for Emacs on Mac isn't
something of a Battle Royale, but with a bit of playing around you
will get something that works for you in the end. My setup is not
perfect. For example, you need to press option-3 each time you want a
'#' character. That's a pain. You can't hold down option and press 333
for multiple hashes. If anyone knows the fix for this please let me
know. On the other hand I'm pretty happy with my config overall.

---

* Published: 2018-11-02 11:29:00 UTC
* Updated: 2018-11-02 11:29:00 UTC
* UUID: B53B71D3-740F-45A9-B1A6-B6FFA73B4968

