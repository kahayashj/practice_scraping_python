import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import numpy as np
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

'''
import requests
import logging

import http.client
http.client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
'''


driver = webdriver.Chrome(executable_path='E:\Download\chromedriver_win32\chromedriver.exe')
driver.get('https://www.spectrum.com/mobile')

soup = driver.find_element_by_xpath("/html/body").text

print(soup)

wordlist = []

words = soup.split()

symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
misc = ['a', 'an', 'the', 'of', 'in', 'for', 'and', 'with', 'or', 'by', 'to', 'from']
for word in words:
    for i in range(len(symbols)):
        #word = word.replace(symbols[i],"")
        if not word in misc:
            wordlist.append(word)

d = {}
for w in wordlist:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

print(d)

data = pd.DataFrame({
    'word': d.keys(),
    'count':d.values()
})
data.sort_values(by=['count'], ascending=False)

count = Counter(d)
print(count.most_common(10))







def start(url):
 
    # empty list to store the contents of
    # the website fetched from our web-crawler
    wordlist = []
    source_code = requests.get(url).text
 
    # BeautifulSoup object which will
    # ping the requested url for data
    soup = BeautifulSoup(source_code, 'lxml')
 
    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text
 
        # use split() to break the sentence into
        # words and convert them into lowercase
        words = content.lower().split()
 
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)
 
# Function removes any unwanted symbols
 
 
def clean_wordlist(wordlist):
 
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
 
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
 
        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)
 
# Creates a dictionary conatining each word's
# count and top_20 ocuuring words
 
 
def create_dictionary(clean_list):
    word_count = {}
 
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
 
    ''' To get the count of each word in
        the crawled page -->
 
    # operator.itemgetter() takes one
    # parameter either 1(denotes keys)
    # or 0 (denotes corresponding values)
 
    for key, value in sorted(word_count.items(),
                    key = operator.itemgetter(1)):
        print ("% s : % s " % (key, value))
 
    <-- '''
 
    c = Counter(word_count)
 
    # returns the most occurring elements
    top = c.most_common(10)
    print(top)
 
 
# Driver code
if __name__ == '__main__':
    url = "https://wikipedia.com/"
    # starts crawling and prints output
    start(url)