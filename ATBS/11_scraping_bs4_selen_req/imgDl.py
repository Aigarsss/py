# Write a program that goes to a photo-sharing site 
# like Flickr or Imgur, searches for a category of photos, 
# and then downloads all the resulting images. You could write 
# a program that works with any photo site that has a search feature.

import os, requests, bs4, re

category = 'Nature'
url = 'https://www.reshot.com/search/' # add the category
os.makedirs('pics', exist_ok=True)

# get the web text

res = requests.get(url + category)
res.raise_for_status()

# extract the hrefs of the pictures
soup = bs4.BeautifulSoup(res.text, features='html.parser')
linkSelection = soup.select('img[src]')[:10]

for i in linkSelection:
    src = i.get('src')
    if 'cloudinary' in src:
        res = requests.get(src)
        res.raise_for_status()
        # write pictures to file using requests and loop iter_content(100000).
        imageFile = open(os.path.join('.\\pics', os.path.basename(src)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

 
