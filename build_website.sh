#!/bin/sh

####
# REQUIRES : mmv
# sudo apt-get install mmv
####

# Convert Markdown to HTML and clean HTML
find ./source -name "*.md" -type f | ./clean.py

# Remove uncleaned HTML
rm *.html

# Rename *.tmp files to *.html
mmv '*.tmp' '#1.html'

mv *.html ./html

#cd ..

# Run HTML through Tidy
# -m = modifies input files (so you don't have to deal with output files)
# tidy.cfg contains a few configuration options
find ./html -type f -name "*.html" -exec tidy -config tidy.cfg -f errors.txt -m {} \;

# Copy stylesheet into upload package
cp ./css/style.css ./html

# copy images into package
cp -R ./images/* ./html/images


#echo "Done."

#zipfile="userguide-${PRODUCT}.zip"

# zip up
#echo "INFO: Creating package..."
#zip -Rq $zipfile ./package/*.html ./package/images/* 
#echo "Done."
# Test package integrity
#echo "INFO: Testing package integrity..."
#zip -T $zipfile
#echo "Done."

# clean up
#rm -rf package/

