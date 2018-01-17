#!/bin/sh
# NOTE: Requires mmv

BUILD_DIR=build
HTML_DIR=html
SRC_DIR=../source
ART_DIR=$SRC_DIR/articles
PY_DIR=../python
CSS=../css/style.css
IMAGES_DIR=images
IMAGES_SRC=../$IMAGES_DIR
IMAGES_DEST=$HTML_DIR/$IMAGES_DIR

# Check we have the necessary build directories and if not create them
if [ ! -d $BUILD_DIR ]; then
    echo "Creating build directory..."
    mkdir $BUILD_DIR
    cd $BUILD_DIR
    if [ ! -d $HTML_DIR ]; then
        echo "Creating HTML directory"
        mkdir $HTML_DIR
        cd $HTML_DIR
        mkdir $IMAGES_DIR
        cd ../..
    fi
fi

# NOTE: Make sure we build in the build directory
cd $BUILD_DIR

# Convert Markdown to HTML and clean HTML
find $SRC_DIR -name "*.md" -type f | $PY_DIR/clean.py

# FIXME: Remove uncleaned HTML
rm *.html

# Rename *.tmp files to *.html
mmv '*.tmp' '#1.html'

# Move to build/html
mv *.html $HTML_DIR

# Run HTML through Tidy
# -m = modifies input files (so you don't have to deal with output files)
# tidy.cfg contains a few configuration options
find $HTML_DIR -type f -name "*.html" -exec tidy -config ../tidy.cfg -f errors.txt -m {} \;

# Copy stylesheet into upload package
cp $CSS $HTML_DIR

# copy images into package
cp -R $IMAGES_SRC/* $IMAGES_DEST

# Finally build Atom feed
echo "Generating Atom feed..."
find $ART_DIR -name "*.md" | $PY_DIR/generate_atom_feed.py
cp atom.xml $HTML_DIR
echo "Done."

