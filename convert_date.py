# Convert date from
# 2017-10-01 12:21:36 UTC format to
# 2017-11-10T13:28:59Z
# NOTE: I use UTC dates/times ONLY as would be obtained with:
# date -u +"%Y-%m-%dT%H:%M:%SZ"
# I NEVER use the format that shows time difference to UTC.

import re

s = "2017-10-01 12:21:36 UTC"

m = re.search (r'(\d\d\d\d-\d\d-\d\d)', s)
date = m.group(1)
print (date)

m = re.search (r'(\d\d:\d\d:\d\d)', s)
time = m.group(1)
print (time)

iso_date = date + "T" + time + "Z"
print (iso_date)
