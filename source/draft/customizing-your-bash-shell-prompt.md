# Customizing your Bash shell prompt

Summary: blah.


First look at simple uncolourized prompt string:

```

```



Example prompt string:

```
PS1='\[\033[01;31m\]\u@\h\[\033[00m\]: \[\033[01;33m\]\w\[\033[00m\] \[\033[01;35m\][$(git branch 2>/dev/null | grep '^*' | colrm 1 2)]\[\033[00m\] \[\033[01;36m\]\$\[\033[00m\] '
```

Breaking it down...

Start of colourize code:

```
\[\033[01;31m\]
```

End of colourize:

```
[\033[00m\]
```

The actual colours can vary quite a bit - especially of you are using Terminal themes.

Example, colourized `$` character for the prompt:

```
\[\033[01;36m\]\$\[\033[00m\]
```

You Git branch displayed in your Bash shell prompt:

```
[$(git branch 2>/dev/null | grep '^*' | colrm 1 2)]
```

And you can then colourize it with:

```
\[\033[01;35m\][$(git branch 2>/dev/null | grep '^*' | colrm 1 2)]\[\033[00m\]
```

Screenshot of finished prompt:



---

* Published: 2017-11-07 09:00:00 UTC
* Updated: 2017-11-15 12:56:00 UTC
* UUID: 


