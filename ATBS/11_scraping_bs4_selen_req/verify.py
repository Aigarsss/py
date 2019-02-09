#! python3
#Link Verification
# Write a program that, given the URL of a web page, 
# will attempt to download every linked page on the page. 
# The program should flag any pages that have a 404 “Not Found” 
# status code and print them out as broken links.

import os, requests, bs4

url = 'https://automatetheboringstuff.com/chapter11/'
os.makedirs('.\\verifyPage', exist_ok=True)

re = requests.get(url)
#re.raise_for_status()
soup = bs4.BeautifulSoup(re.text, features='html.parser')
links = soup.select('a[href]')

caughtLinks = []
for i in range(len(links)):
    finalLink = links[i].get('href')
    if 'http' in finalLink:
        caughtLinks.append(finalLink)

#print(len(caughtLinks))

# write the files
for i in range(len(caughtLinks)):
    re = requests.get(caughtLinks[i])
    # handle the broken links 
    if re.status_code == 404:
        print('The page {} does not exist. Reutrned 404'.format(caughtLinks[i]))
    else:
        #handle the file creation
        file = open(os.path.join('.\\verifyPage', 'page_number_' + str(i) + '.html'), 'wb')
        for chunk in re.iter_content(100000):
            file.write(chunk)
        file.close()


