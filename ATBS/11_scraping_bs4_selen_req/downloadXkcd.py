#! python3
# downloads all xkcd comics on PC

import requests, os, bs4

url = 'http://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd. Param - OK if folder eists already
while not url.endswith('#'):
    # download the page
    print('Downloading the page {}'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features='html.parser')

    # find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find an image')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            #download the image
            print('Downloading the image {}...'.format(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic (get the prev button url)
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http:/xkcd.com' + prevLink.get('href')
            continue
    
    # save the image to .\\xkcd
    imageFile = open(os.path.join('.\\xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    url += '#' # not to download all of them
    print('Done')
