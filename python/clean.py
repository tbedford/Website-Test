#!/usr/bin/env python

import fileinput
import re
import os
import datetime

template_file = '../templates/template.html'

def get_build_time ():

    build_time = datetime.datetime.utcnow()
    build_time = str(build_time)
    m = re.search(r'(\d\d\d\d-\d\d-\d\d) (\d\d:\d\d:\d\d)', build_time)
    return m.group(1) + ' ' + m.group(2) + ' UTC'


def clean_content(content):

    # Run regexs to clean up HTML
    content = re.sub (r'<style[\s\S]*?<\/style>', r'', content)
    content = re.sub (r'<link[\s\S]*?<\/link>', r'', content)
    content = re.sub (r'<br>', r' ', content)

    # Handle code blocks
    content = re.sub (r'<code class="lang-C">', r'<code class="c">', content)
    content = re.sub (r'<code class="lang-Python">', r'<code class="python">', content)
    content = re.sub (r'<code class="lang-shell">', r'<code class="shell">', content)
    content = re.sub (r'<code class="lang-text">', r'<code class="text">', content)
    content = re.sub (r'<code class="lang-html">', r'<code class="html">', content)
    content = re.sub (r'<code class="lang-xml">', r'<code class="xml">', content)

    # ISO-8601 format dates (YYYY-MM-DD) 2017-10-27
    content = re.sub (r'(\d\d\d\d-[0-1][0-9]-[0-3][0-9])', r'<span class="date">\1</span>', content)

    return content

def get_title (content):

    m = re.search (r'<h1[\s\S]*?>([\s\S]*?)<\/h1>', content)
    return m.group(1)
    
    
# Read template
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
        
    template = template.format(TITLE=get_title(content), CONTENT=content, BUILD_TIME=get_build_time())
    
    # Write out temp file
    fout.write(template)

    # close down open files
    fin.close()
    fout.close()
    
