# Emacs keyboard configuration on Mac

Summary: In this article I talk about configuring Emacs for use on Mac
OS X. The configuration works with both Terminal Emacs and Cocoa Emacs
(Desktop).

A rite of passage, and some would say trial by fire, of working with
Emacs on Mac, is getting your keyboard configuration set up
correctly. The actual setup depends on your needs. For example, things
might be simpler if you only ever use Terminal Emacs. Although I
mostly use Emacs in the terminal, there have been a number of
occasions where working with the Desktop (Cocoa) version of Emacs is
useful - mainly when I wanted to copy and paste large blocks of code
to another app. This is tricky with the terminal version of Emacs,
especially when you have split frames. I also used to be an avid user
of Aquamacs before I had problems with upgrading it, so a cross-Emacs
configuration is certainly a very nice thing to have.

This article assumes you know a bit about Emacs such as the importance
of the Control and Meta keys as used for correct Emacs operation.

## Getting a '#' character

When you start using Emacs on the Mac, one of the first issues you run
into is how to get the darn '#' character to work! It seems like such a
basic thing. But many fall at this first hurdle. The easiest solution
I have come across is to insert the following line of Elisp into your
`.emacs` file:

``` lisp
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
they are usually designated in Emacs are the two most important keys
in Emacs.

So, for example, to execute a command in Emacs you would use `M-x`
where M is the Meta key, which is the `option` key on Mac. There is
thus a conflict here where Mac wants to use the `option` key as, well,
the option key, and Emacs wants to use it as the Meta key.

So, how to get around this conflict between Option and Meta in the
terminal?

Well there's a sneaky little keyboard config option in the Terminal
Preferences (Terminal/Preferences/Keyboard) known as 'Use Option as
Meta key'. Make sure that checkbox is ticked and lo and behold your
option key now works correctly as the Emacs Meta key.

## Start and end of buffer hot keys

If you only ever use the terminal version of Emacs then everything is
plain sailing, more or less, from now on. 

Let's look at an example. 

I personally find the default key options of `M-<` and `M->` to be
awkward as they require the use of the shift key. You can fix that
issue with:

``` lisp
(global-set-key (kbd "M-,") 'beginning-of-buffer)
(global-set-key (kbd "M-.") 'end-of-buffer)
```

Here you are using the same keys but without the for the additional
shift.

But I prefer the use of `M-up` and `M-down` (Meta with the arrow
keys). So you want to configure `M-up` as 'go to start of
buffer' and `M-down` as 'go to end of buffer', you could use some
config such as:

``` lisp
(global-set-key [27 up] (quote beginning-of-buffer))
(global-set-key [27 down] (quote end-of-buffer))
```

You can now easily jump to the start or end of a buffer with `M-up` or
`M-down` (Meta and up arrow key or Meta and down arrow key).

This works well in the Terminal version of Emacs. However, if you then
use the desktop version of Emacs on Mac this will not work. Oh dear...

## Desktop Emacs

When you fire up the Desktop version of Emacs you'll find the previous
key setup no longer works - you can't jump to start and end of buffer
using `M-up` or `M-down`. 

Why? 

Well the first thing we did was configure Terminal to 'Use Option as
Meta key'. Still, it should be possible to achieve the same effect. We
are treating the Meta key slightly differently in the Terminal
version.

You can achieve the same thing in the desktop version using a slightly
different configuration:

``` lisp
(global-set-key [(meta up)] 'beginning-of-buffer)
(global-set-key [(meta down)] 'end-of-buffer)
```

This fixes things. This won't work in the Terminal version as we
currently have it configured though due to that "Use Option as Meta
key" thing we checked. But the two configurations can remain in your
`.emacs` file and they will work quite happily together.

## Summary

So we configured Emacs so the '#' key worked. We also configured
`M-up` and `M-down` for both the Terminal and Desktop version.

For your convenience here's the complete config:

``` lisp
;; get hash key working on Apple Mac!
(global-set-key (kbd "M-3") '(lambda () (interactive) (insert "#")))

;; Terminal Emacs
(global-set-key [27 up] (quote beginning-of-buffer))
(global-set-key [27 down] (quote end-of-buffer))

;; Desktop Emacs
(global-set-key [(meta up)] 'beginning-of-buffer)
(global-set-key [(meta down)] 'end-of-buffer)

;; Also convenient
(global-set-key (kbd "M-,") 'beginning-of-buffer)
(global-set-key (kbd "M-.") 'end-of-buffer)
```

I can't pretend that keyboard configuration for Emacs on Mac isn't
something of a Battle Royale, but with a bit of playing around you
will get something that works for you in the end. I will keep playing
with it - eventually I will get the "Perfect Emacs Configuration", but
don't hold your breath on that one! :)


## Resources

* [Use Stack Overflow article](https://stackoverflow.com/questions/4351044/binding-m-up-m-down-in-emacs-23-1-1)
* [Emacs key bindings article](http://www.nongnu.org/emacs-tiny-tools/keybindings/)

---

* Published: 2018-11-02 11:29:00 UTC
* Updated: 2018-11-02 08:33:12 UTC
* UUID: B53B71D3-740F-45A9-B1A6-B6FFA73B4968

