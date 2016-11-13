import unicodedata
import requests
from bs4 import BeautifulSoup
def get_single_url(url):
    file = open("jiagox.html","a")
    sourceCode = requests.get(url)
#    print(sourceCode)
    plaintext = sourceCode.text
    soup = BeautifulSoup(plaintext,"lxml")
#    for item in soup.findAll('div',{'class':'i-name'})
    for item in soup.find('h2',{'class':'rich_media_title'}):
        file.write("<a href=\""+str(url)+"\">")
        file.write(item.encode('utf-8')+"</a><br>")

def readurl():
    file = open("newdb.txt","r")
    for line in file:
        get_single_url(line)

readurl()
