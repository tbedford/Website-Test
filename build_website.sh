#!/bin/sh

####
# REQUIRES : mmv
# sudo apt-get install mmv
# Designed for Mac OS X or Linux
####

if [ ! -d "html" ]; then
    mkdir html
    cd html
    mkdir images
    cd ../..
fi

# Convert Markdown to HTML and clean HTML
find ./source -name "*.md" -type f | ./clean.py

# Remove uncleaned HTML
rm *.html

# Rename *.tmp files to *.html
mmv '*.tmp' '#1.html'

mv *.html ./html

# Run HTML through Tidy
# -m = modifies input files (so you don't have to deal with output files)
# tidy.cfg contains a few configuration options
find ./html -type f -name "*.html" -exec tidy -config tidy.cfg -f errors.txt -m {} \;

# Copy stylesheet into upload package
cp ./css/style.css ./html

# copy images into package
cp -R ./images/* ./html/images

# Finally build Atom feed

find ./source/articles -name "*.md" | ./generate_atom_feed.py
cp atom.xml ./html

