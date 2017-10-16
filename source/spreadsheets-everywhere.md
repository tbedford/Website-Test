# Spreadsheets everywhere

It starts off innocently enough. I've got a few customer contacts
here, I'll just whop them in an Excel spreadsheet for now. And then
before you know it you have this giant Frankenstein monster on your
hands, and it's covered in data warts, and boils and hideous
scars. And it wants to eat you for breakfast. Everyone has seen one of
those spreadhseets right? I've seen too many than is healthy for
you. I still have nightmares about some of them.

So, it's usually at the Frankenstein monster stage that I get the
call. The conversation usually goes something like this: "I've got
this spreadsheet, and I wanna get stuff out of that and over there." I
can do that for you...but...hasn't there got to be a better way? Well
yes there is, but I'll save databases for another article or two. I'll
start with the first part of that conversation - getting data out of
the spreadsheet. Python makes this so trivial it's almost a travesty
to bill clients for it.

``` python

# grabs data from XLS file. Delimits columns by '|'. Use redirection
# to write out to file, otherwise output is to stdout

import sys

import openpyxl
from openpyxl import load_workbook

file = sys.argv[1]  # 'XYZ.xlsx'
wb = load_workbook(filename = file)

sheet1 = wb.get_sheet_by_name('ABC')
sheet2 = wb.get_sheet_by_name('DEF')

ws = sheet1
rows = ws.rows

for row in ws.rows:
    record_string = ""
    for cell in row:
        record_string = record_string + str(cell.value)
        record_string = record_string + "|" 

# Remove carriage returns from within row 
record_string = record_string.replace('\n', '~') 
    
# if column 1 and column 2 are None then ignore row
record_array = record_string.split('|') 
colstr1 = record_array[0].strip()
colstr2 = record_array[1].strip()
if not colstr1 == "None":
    if not colstr2 == "None":
        print(record_string) 

```

So, the code is easy enough. A spreadsheet file usually has one or
more worksheets contained inside, and the wonderful `openpyxl` makes it
easy to get any and all sheets. You then pick a sheet and process it
to your heart's content.

My usual strategy is to get in and out of a spreadsheet ASAP. I want
to generate some kind of sane intermediate file. If I can do some
processing cheaply while I'm in there I will do it. For example, in
this case, I delimit outputted fields with '|' to make subsequent
processing easier. Where fields contain hard carriage returns I
replace those by twiddle ('~') as an aid to later debugging of the
sheet. Bits and pieces like that. But generally I prefer to get in and
out fast. Get my data into an intermediate format, and then take the
processing from there.

As a general note I do like to take the Unix approach to data
processing. I tend to write several small programs that do one thing,
and then chain them together with a shell script, redirection and
pipes and whatever's needed. It's much easier and more flexible than
one big hullabaloo program that tries to do everything. You'll tend to
find the smaller programs can be reused in multiple projects with
minor changes. The code above has been used several times now in
different projects, with the only changes being to the sheet
names. You could even pass those in as command-line parameters, like I
do with the spreadsheet filename, if you wanted to be even more
generic.

