#!/bin/sh

#
# This version builds one page only
#

####
# REQUIRES : mmv
# sudo apt-get install mmv
# Designed for Mac OS X or Linux
####

if [ $# -eq 0 ]; then
    echo "You need to specify a page to build."
    echo "USAGE: ./build_page about.md"
  exit 1
fi

if [ ! -d "html" ]; then
    mkdir html
    cd html
    mkdir images
    cd ../..
fi

# Remove old HTML files - we don't need them
rm html/*.html

# Convert Markdown to HTML and clean HTML
find ./source -name "$1" -type f | ./clean.py

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
cp ./css/style*.css ./html

# copy images into package
cp -R ./images/* ./html/images

