#! python3
# python multidownloadXkcd.py

# downloads xkcd comics using multiple threads. upgrade to chapter 11 program

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic + 1):
        print('Downloading pge http://xkcd.com/{}'.format(urlNumber))
        res = requests.get('http://xkcd.com/{}'.format(urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Find the URL of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('No Image found')
        else:
            comicUrl = comicElem[0].get('src')
            # download the image
            print('Downloading image {}'.format(comicUrl))
            res = requests.get('http://xkcd.com/{}'.format(comicUrl))
            res.raise_for_status()

            # Save the image to .\\xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start the threads
downloadThreads = []            # a list of all the Thread objects
for i in range(0, 1400, 100):   # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for threads to end. I dont get this part at all.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done')