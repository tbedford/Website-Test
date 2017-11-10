#!/usr/bin/env python

import fileinput
import re
import os

html_head = '''
<html>
  <head>
<title>TITLE</title>

<link href="/style.css" rel="stylesheet" type="text/css" media="all">
<link rel="stylesheet"
      href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/mono-blue.min.css">
  </head>  
  <body>
'''

html_foot = '''
    <hr/>
    <div class="footer">
       <p><a href="https://coffeeandcode.neocities.org">Home</a> | (c) 2017 Tony Bedford</p>
    </div>
    <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>
  </body>
</html>
'''


# Read filename from stdin
for filename in fileinput.input():
    
    # chomp
    filename = filename.rstrip()

    print ("Markdown file: "+filename)
    
    # HTML file name
    base = os.path.basename(filename)
    base = os.path.splitext(base)[0]
    html_filename = base + '.html'
    print ("HTML file: "+html_filename)
    
    # Run markdown on .md
    cmd = "markdown " + filename  + " > " + html_filename
    print ("System command: " + cmd)
    os.system(cmd)
    
    # Determine output file name
    out_filename = base + '.tmp'

    # open files
    fin = open (html_filename, 'r')
    fout = open (out_filename, 'w')

    # Grab all of HTML
    html = fin.read()

    # Run regexs to clean up HTML
    html = re.sub (r'<style[\s\S]*?<\/style>', r'', html)
    html = re.sub (r'<link[\s\S]*?<\/link>', r'', html)
    html = re.sub (r'<br>', r' ', html)

    # Handle code blocks
    html = re.sub (r'<code class="lang-C">', r'<code class="c">', html)
    html = re.sub (r'<code class="lang-Python">', r'<code class="python">', html)
    html = re.sub (r'<code class="lang-shell">', r'<code class="shell">', html)
    html = re.sub (r'<code class="lang-text">', r'<code class="text">', html)
    html = re.sub (r'<code class="lang-html">', r'<code class="html">', html)
    html = re.sub (r'<code class="lang-xml">', r'<code class="xml">', html)

    # ISO-8601 format dates (YYYY-MM-DD) 2017-10-27
    html = re.sub (r'(\d\d\d\d-[0-1][0-9]-[0-3][0-9])', r'<span class="date">\1</span>', html)
    
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
    
