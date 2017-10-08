#!/bin/sh

####
# REQUIRES : mmv
# sudo apt-get install mmv
####

# Convert *.md to *.html
find ./source -type f -name "*.md" -exec markdown {} \;
mkdir html
mv source/*.html html/

cd html

# Fix up HTML
find . -name "*.html" -type f | ./clean.py # clean generates *.tmp files

# Rename *.tmp files to *.html
mmv '*.tmp' '#1.html'

cd ..

# Run HTML through Tidy
# -m = modifies input files (so you don't have to deal with output files)
# tidy.cfg contains a few configuration options
find ./html -type f -name "*.html" -exec tidy -config tidy.cfg -f errors.txt -m {} \;


# copy images to package
#echo "INFO: Copy image files to package..."
#cp -R ./build/html/images/* ./package/images
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

