#! python3
# Write a program that checks the websites of several web comics and 
# automatically downloads the images if the comic was updated since 
# the program’s last visit. Your operating system’s scheduler 
# (Scheduled Tasks on Windows, launchd on OS X, and cron on Linux) 
# can run your Python program once a day. The Python program itself 
# can download the comic and then copy it to your desktop so that it 
# is easy to find. This will free you from having to check the website 
# yourself to see whether it has updated.

# this program is for a single new comic download per day

# python scheduleDownload.py

import requests, bs4, os

# create dir
os.makedirs('Downloads', exist_ok=True)

# Get the comic page
re = requests.get('https://xkcd.com/')
re.raise_for_status()

# get the current comic id=comic, img
soup = bs4.BeautifulSoup(re.text, features='lxml')
selection = soup.select('#comic img')
pic = 'https:' + selection[0].get('src')

# check if comic is already in dir
if os.path.basename(pic) not in os.listdir('Downloads'):
    print('This is a new pic')
    # load the pic in requests
    re = requests.get(pic)
    re.raise_for_status()
    imageFile = open(os.path.join('Downloads', os.path.basename(pic)) , 'wb')
    for chunk in re.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

# download comic