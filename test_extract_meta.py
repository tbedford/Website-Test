import re

s = '''
# Generating ISO-8601 dates on Mac OS X

Published: 2017-10-01 12:21:36 UTC
Updated: 2017-11-10 12:26:00 UTC 

Summary: In this article I talk about how you can generate ISO-8601
format dates on the Mac OS X command line, and also how you can do it
in Python too.

Main article text starts here...
'''

# title
m = re.search (r'# (.*)', s)
title = m.group(1)
print("Title> "+title)

# Published
m = re.search (r'Published: (.*)', s)
published = m.group(1)
print("Published> "+published)

# Updated
m = re.search (r'Updated: (.*)', s)
updated = m.group(1)
print("Updated> "+updated)

# Summary
m = re.search (r'Summary: ([\s\S]*)\n\n', s)
summary = m.group(1)
print("Summary> "+summary)



