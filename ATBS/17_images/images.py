# pip install pillow

'''

# PIL uses same naming as HTML colors
from PIL import ImageColor
print(ImageColor.getcolor('red', 'RGBA')) # (255, 0, 0, 255)
print(ImageColor.getcolor('chocolate', 'RGBA')) # (210, 105, 30, 255)

from PIL import Image # it needs to be formated like this. import pillow will not work
catIm = Image.open('zophie.png')
print(catIm.size)           # (816, 1088)
width, height = catIm.size 
print(catIm.filename)       # zophie.png
print(catIm.format)         # PNG
# catIm.save('zophie.jpeg')


from PIL import Image 
catIm = Image.open('zophie.png')
# new image
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im = Image.new('RGBA', (20, 20))
im.save('transparent.png')

# cropping
from PIL import Image 
catIm = Image.open('zophie.png')

croppedIm = catIm.crop((335,345,565,650))
croppedIm.save('cropped.png')

# copy on top
from PIL import Image 
catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()

faceIm = catIm.crop((335,345,565,650))
print(faceIm.size) # 230, 215

catCopyIm.paste(faceIm,(0,0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.png')

# create multiple tile copies

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))

catCopyTwo.save('tiled.png')

# resize
from PIL import Image 
catIm = Image.open('zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize((int(width/2), int(height / 2)))
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.png')

# rotate image 
from PIL import Image 
catIm = Image.open('zophie.png')

#catIm.rotate(90).save('rotated90.png')
catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand = True).save('rotated6_expanded.png')

# flip image
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png') # other option FLIP_TOP_BOTTOM


# changing indiviual pixels
from PIL import Image 
im = Image.new('RGBA', (100,100))
print(im.getpixel((0,0))) # 0 0 0 0 
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

from PIL import ImageColor
for x in range(100):
    for y in range(50,100):
        im.putpixel((x,y), ImageColor.getcolor('darkgray', 'RGBA'))
print(im.getpixel((0,0))) # (210, 210, 210, 255)
im.save('putPixel.png')

# drawing on images
from PIL import Image, ImageDraw
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.line([(0,0), (199,0),(199,199), (0, 199), (0,0)], fill = 'black') # cube
draw.rectangle((20, 30, 60, 60), fill = 'blue') # cube within the line cube
draw.ellipse((120, 30, 160, 60), fill='red') # red circle
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown') # poly

for i in range(100, 200, 10):
    draw.line([(i,0), (200, i - 100)], fill='green')

im.save('drawing.png')

# drawing text
from PIL import Image, ImageDraw, ImageFont
import os
im = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'C:\\Windows\\fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font = arialFont)
im.save('text.png')

'''


