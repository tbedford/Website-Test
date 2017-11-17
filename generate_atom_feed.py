#!/usr/bin/env python

# Generate Atom feed 

import fileinput
import re

# NOTE: Header must be patched with correct datetime (feed build)

header = '''
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Coffee and Code Feed</title>
  <link href="https://coffeeandcode.neocities.org/"/>
  <updated>2017-11-10T08:15:26+0000</updated>
  <author>
    <name>Tony Bedford</name>
  </author>
  <id>urn:uuid:B2F5F303-9B73-4D58-B4DF-32EC8F74136F</id>
  <!-- Entries go here -->
'''

footer = '''
</feed>
'''


# Convert date from:
# 2017-10-01 12:21:36 UTC format to ISO-8601:
# 2017-11-10T13:28:59Z
# NOTE: In my Atom feed I use UTC dates/times ONLY as would be obtained with:
# date -u +"%Y-%m-%dT%H:%M:%SZ"

def convert_date (date):

    print("Input date: %s" % date)

    m = re.search (r'(\d\d\d\d-\d\d-\d\d) (\d\d:\d\d:\d\d) (\w\w\w)', date)

    if m.group(3) != "UTC":
        print("ERROR: Only UTC format should be specified!")
        exit(-1)

    return m.group(1) + "T" + m.group(2) + "Z"

# Extracts metadata from HTML and converts as required

def extract_metadata (html):

    # title
    m = re.search (r'# (.*)', html)
    title = m.group(1)
    print("Title >%s<" % title)

    # Published
    m = re.search (r'Published: (.*)', html)
    published = convert_date(m.group(1))
    print("Published >%s<" % published)

    # Updated
    m = re.search (r'Updated: (.*)', html)
    updated = convert_date(m.group(1))
    print("Updated >%s<" % updated)

    # UUID
    m = re.search (r'UUID: ([A-F0-9-]*)', html)
    uuid = m.group(1)
    print("UUID >%s<" % uuid)

    # Summary
    m = re.search(r'Summary: ([\s\S]*?)\n\n', html)
    summary = m.group(1)
    print("Summary >%s<" % summary)

    return title, published, updated, uuid, summary

# Encode an entry in XML
#<entry>
#  <title>Creating an Atom feed</title>
#  <link href="https://coffeeandcode.neocities.org/creating-atom-feed.html"/>
#  <id>urn:uuid:2E4A626F-FF02-47F0-9538-254F76F5C7EF</id>
#  <updated>2017-11-10T11:07:29+0000</updated>
#  <published>2017-11-10T11:07:29+0000</published>
#  <summary>This is a summary of the article.</summary>
#</entry>

base_url = "https://coffeeandcode.neocities.org/"

template = '''
<entry>
  <title>%s</title>
  <link href="%s%s"/>
  <id>%s</id>
  <updated>%s</updated>
  <published>%s</published>
  <summary>%s</summary>
</entry>
'''

def encode_entry (filename, title, published, updated, uuid, summary):

    return template % (title, base_url, filename, uuid, updated, published, summary)

# Main

# TODO: Patch header file with correct date-time 
feedfile = "atom.xml"
fout = open (feedfile, 'w')
fout.write (header)

for filename in fileinput.input():

    # chomp
    filename = filename.rstrip()
    print ("HTML file:>%s< " % filename)

    fin = open (filename, 'r')
    html = fin.read ()

    # extract entry metadata from HTML
    title, published, updated, uuid, summary = extract_metadata(html)

    # Write out encoded entry
    fout.write(encode_entry (filename, title, published, updated, uuid, summary))
    
    fin.close ()

# Close down feed file
fout.write(footer)
fout.close()
    
