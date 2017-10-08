#!/usr/bin/env python

import fileinput
import re
import os

html_head = '''
<!DOCTYPE html>
<html>
  <head>
<title>TITLE</title>

<link rel="stylesheet"
      href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/solarized-dark.min.css">

  </head>
  
  <body>
'''

html_foot = '''
    <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>
  </body>
</html>
'''


# Read filename from stdin
for filename in fileinput.input():

    print ("- File: "+filename)
    
    # chomp
    filename = filename.rstrip()

    # Determine output file name
    base = os.path.basename(filename)
    base = os.path.splitext(base)[0]
    base = base + '.tmp'

    # open files
    fin = open (filename, 'r')
    fout = open (base, 'w')

    # Grab all of HTML
    html = fin.read()

    # Run regexs to clean up HTML
    html = re.sub (r'<style[\s\S]*?<\/style>', r'', html)
    html = re.sub (r'<link[\s\S]*?<\/link>', r'', html)
    html = re.sub (r'<br>', r' ', html)
    html = re.sub (r'<code[\s\S]*?>', r'<code>', html)

    # Add header and footer
    html = html_head + html
    html = html + html_foot

    # Fix Title
    m = re.search (r'<h1[\s\S]*?>([\s\S]*?)<\/h1>', html)
    title = m.group(1)
    title = '<title>' + title + '</title>'
    html = re.sub (r'<title>[\s\S]*?<\/title>', title, html)
    
    # Write out temp file
    fout.write(html)

    # close down open files
    fin.close()
    fout.close()
    
