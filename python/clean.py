#!/usr/bin/env python

import fileinput
import re
import os
import datetime

def get_build_time ():
    build_time = datetime.datetime.utcnow()
    build_time = str(build_time)
    m = re.search(r'(\d\d\d\d-\d\d-\d\d) (\d\d:\d\d:\d\d)', build_time)
    return m.group(1) + ' ' + m.group(2) + ' UTC'


# We end up with two h1's, so remove the second (in the content only)
# We want the first in the div class header
def remove_h1 (content):
    content = re.sub (r'<h1[\s\S]*?>([\s\S]*?)<\/h1>', r'', content)    
    return content

def clean_content(content):
    # Run regexs to clean up HTML
    content = re.sub (r'<style[\s\S]*?<\/style>', r'', content)
    content = re.sub (r'<link[\s\S]*?<\/link>', r'', content)
    content = re.sub (r'<br>', r' ', content)

    # Handle code blocks
    content = re.sub (r'<code class="lang-C">', r'<code class="c">', content)
    content = re.sub (r'<code class="lang-Python">', r'<code class="python">', content)
    content = re.sub (r'<code class="lang-python">', r'<code class="python">', content)
    content = re.sub (r'<code class="lang-shell">', r'<code class="shell">', content)
    content = re.sub (r'<code class="lang-text">', r'<code class="text">', content)
    content = re.sub (r'<code class="lang-html">', r'<code class="html">', content)
    content = re.sub (r'<code class="lang-xml">', r'<code class="xml">', content)
    content = re.sub (r'<code class="lang-json">', r'<code class="json">', content)

    return content

def get_title (content):
    m = re.search (r'<h1[\s\S]*?>([\s\S]*?)<\/h1>', content)
    return m.group(1)

# Read template
template_file = '../templates/template.html'
ft = open (template_file, 'r')
template = ft.read()
ft.close()

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

    # Grab all of HTML and clean
    content = clean_content(fin.read())
    title = get_title(content)
    content = remove_h1(content)
    
    html = template.format(TITLE=title, CONTENT=content, BUILD_TIME=get_build_time())
    
    # Write out temp file
    fout.write(html)

    # close down open files
    fin.close()
    fout.close()
    
