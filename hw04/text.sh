# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/new_boris.png

# From: http://www.imagemagick.org/Usage/text/
convert ./tux_rot.png -background Khaki \
      label:'      OH HE CRAZY     ' \
      -gravity Center\
      -append\
      $TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE

# convert -list font
