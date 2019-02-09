#! python3
# lucky.py - Opens several Google search results.
# python lucky.py arg

import sys, requests, webbrowser, bs4

print('Googling...')
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
print(res.raise_for_status())

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features='html.parser')
linkElems = soup.select('.r a')

# open a browser tab for each resut
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    #print('http://google.com' + linkElems[i].get('href'))
    webbrowser.open('http://google.com' + linkElems[i].get('href'))


