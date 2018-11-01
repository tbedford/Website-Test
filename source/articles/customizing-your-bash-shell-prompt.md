# Customizing your Bash shell prompt

Summary: In this article I look at customizing your Bash shell prompt.

When you are working on the command line with Git it can get confusing
as to what branch you are currently in. Both Emacs (with the right
plugin) and VS Code are good at handling this - in both cases an
indication of the current branch is clearly displayed. But if you are
on the command line you have no clear indication of your current Git
branch - you'd have to type `git branch` or `git status` to see where
you are.

I'm assuming you're on a Mac and editing the `.bash_profile` file, but
most of that discussed below would also work on Linux.

First look at simple uncolourized prompt string:

``` shell
PS1='\u@\h'
```

This would simply display a prompt such as `username@computername`. It
would not use custom colours.

However, using ANSI _escape codes_ you can colourize the prompt.

Note that to a certain extent the final look of the shell prompt will
be determined by any Terminal themes you might be using.

Example prompt string (this is what I use):

``` shell
PS1='\[\033[01;31m\]\u@\h\[\033[00m\]: \[\033[01;33m\]\w\[\033[00m\] \[\033[01;35m\][$(git branch 2>/dev/null | grep '^*' | colrm 1 2)]\[\033[00m\] \[\033[01;36m\]\$\[\033[00m\] '
```

Here's the same prompt but I've manually wrapped it over multiple
lines to make it easier to read:

``` shell
PS1='\[\033[01;31m\]\u@\h\[\033[00m\]: \
\[\033[01;33m\]\w\[\033[00m\] \
\[\033[01;35m\][$(git branch 2>/dev/null \
| grep '^*' \
| colrm 1 2)]\[\033[00m\] \
\[\033[01;36m\]\$\[\033[00m\] '
```

Breaking it down...

Start of escape code to set an ANSI colour:

``` shell
\[\033[01;31m\]
```

End of colourize escape code:

``` shell
\[\033[00m\]
```

For example, to get a colourized `$` character in the prompt you could use:

``` shell
\[\033[01;36m\]\$\[\033[00m\]
```

To get your Git branch displayed in your Bash shell prompt use:

``` shell
[$(git branch 2>/dev/null | grep '^*' | colrm 1 2)]
```

Note, `grep` is used to find the `*` character, as your current branch
is marked with `*` when you type a `git branch` command.

The column remove command `colrm` simply removes the first colum in
the output of the `git branch` command, leaving you with just the name
of the current branch (without the `*`).

And you can then colourize it with:

``` shell
\[\033[01;35m\][$(git branch 2>/dev/null | grep '^*' | colrm 1 2)]\[\033[00m\]
```

You will end up with a prompt that looks something like:

``` shell
abedford@bilbo ~/checkouts/tbedford/Website-test [master] $
```

The actual colours that will appear depend on any Terminal themes being used.


## Resources

Some resources you might find useful:

* [Escape codes reference](https://github.com/mbadolato/iTerm2-Color-Schemes)

---

* Published: 2018-07-06 05:59:00 UTC
* Updated: 2018-07-06 05:59:00 UTC
* UUID: 234A2B17-6C78-4D5A-98CB-7D02BEA8F7EE

