# python resizeAndAddLogo.py

# At a high level, here’s what the program should do:
# Load the logo image.
# Loop over all .png and.jpg files in the working directory.
# Check whether the image is wider or taller than 300 pixels.
# If so, reduce the width or height (whichever is larger) to 300 pixels and scale down the other dimension proportionally.
# Paste the logo image into the corner.
# Save the altered images to another folder.

# This means the code will need to do the following:
# Open the catlogo.png file as an Image object.
# Loop over the strings returned from os.listdir('.').
# Get the width and height of the image from the size attribute.
# Calculate the new width and height of the resized image.
# Call the resize() method to resize the image.
# Call the paste() method to paste the logo.
# Call the save() method to save the changes, using the original filename.

 # in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

os.makedirs('watermarked', exist_ok = True)

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoIm = logoIm.resize((int(logoIm.size[0]/7), int(logoIm.size[1]/7))) # this was not in the book, but otherwise logo is too big
logoWidth, logoHeight = logoIm.size


# loop over all files in working dir
for filename in os.listdir('.\\'):
    if not (filename.endswith('.png') or filename.endswith('.jpeg')) or filename == LOGO_FILENAME:
        continue
    else:
        im = Image.open(filename)
        width, height = im.size
        # check if image needs to be resized
        if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
             # calculate the new widh and height to resize to
            if width > height:
                height = int((SQUARE_FIT_SIZE / width) * height)
                width = SQUARE_FIT_SIZE
            else:
                width = int((SQUARE_FIT_SIZE / height) * width)
                height = SQUARE_FIT_SIZE

            # Resize
            print('Resizing {}'.format(filename))
            im = im.resize((width, height))

        # add logo
        print('Adding logo to {}'.format(filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm) # third argument makes white block transparent
        # Save changes
        im.save(os.path.join('watermarked', filename))

