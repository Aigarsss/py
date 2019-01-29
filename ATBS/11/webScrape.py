#! python3
##Chapter 11 – Web Scraping

# import webbrowser
# webbrowser.open(<site>) # opens in a new tab

# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res.text))
# print(res.status_code == requests.codes.ok) #checks status
# print(len(res.text))
# print(res.text[:250])

# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

# try:
#     print(res.raise_for_status()) # this needs to be checked each time requests.get() is called
# except Exception as exc:
#     print('There was a problem {}'.format(exc))

# write to file
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status()
# playFie = open('RomeoAndJuliet.txt', 'wb')

# for chunk in res.iter_content(100000):
#     playFie.write(chunk)
# playFie.close()

# pip install beautifulsoup4

# import requests, bs4
# res = requests.get('http://nostarch.com')
# res.raise_for_status()
# noStartchSoup = bs4.BeautifulSoup(res.text, features='html.parser') #feature because of the warning
# print(type(noStartchSoup))


# import bs4
# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features='html.parser')
# elems = exampleSoup.select('#author')
# print(type(elems)) # <class 'list'>
# print(len(elems)) # 1
# print(type(elems[0])) # <class 'bs4.element.Tag'>
# print(elems[0].getText()) # Al Sweigart
# print(str(elems[0])) # <span id="author">Al Sweigart</span>
# print(elems[0]) # <span id="author">Al Sweigart</span>
# print(elems[0].attrs) # {'id': 'author'}

# pElems = exampleSoup.select('p')
# print(len(pElems))
# print(str(pElems[0]))
# print(pElems[0].getText())
# print(str(pElems[1]))
# print(pElems[1].getText())
# print(str(pElems[2]))
# print(pElems[2].getText())

# import bs4
# soup = bs4.BeautifulSoup(open('example.html'), features='html.parser')
# spanElem = soup.select('span')[0]
# print(len(soup.select('span')))
# print(spanElem) #<span id="author">Al Sweigart</span>
# print(spanElem.get('id')) #author
# print(spanElem.get('some_non_eistent_addr') == None) # True
# print(spanElem.attrs) #{'id': 'author'}


#### controlling browser
# from selenium import webdriver

# browser = webdriver.Chrome() # worked when chromedriver.exe was installed in path
# #browser = webdriver.Firefox() #ff didnt work even with geckodriver installed in path
# print(type(browser))
# browser.get('http://inventwithpython.com')

# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://inventwithpython.com')
# try:
#     elem = browser.find_element_by_class_name('card-img-top') #used this instead of bookcover as bookcover doesnt exist anymore
#     print('Found {} element with that class name'.format(elem.tag_name))
# except:
#     print('Was not able to find that element')


#### click on a link in a page
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://inventwithpython.com')
# linkElem = browser.find_element_by_link_text('YouTube')
# print(type(linkElem))
# linkElem.click() # follows youtube link

# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://mail.yahoo.com')
# emailElem = browser.find_element_by_id('login-username')
# emailElem.send_keys('Not_my_real_mail')
# #passwordElem = browser.find_element_by_id('login-password') #page has different layout now
# #passwordElem.send_keys('12345') #page has different layout now
# logIn = browser.find_element_by_id('login-signin')
# logIn.submit() #click() would work as well


# #### importing keys that cannot be turned into strings
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys # you do this, so keys can be called easier later
# browser = webdriver.Chrome()
# browser.get('http://nostarch.com')
# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END) #scrolls down
# htmlElem.send_keys(Keys.HOME) #scrolls up

##Browser clicks that can be simulated:
# browser.back(). Clicks the Back button.
# browser.forward(). Clicks the Forward button.
# browser.refresh(). Clicks the Refresh/Reload button.
# browser.quit(). Clicks the Close Window button.