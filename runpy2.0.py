import unicodedata
import requests
from bs4 import BeautifulSoup



def get_single_url(url):
    file = open("MLresearch.html","a")
    sourceCode = requests.get(url)
#    print(sourceCode)
    plaintext = sourceCode.text
    soup = BeautifulSoup(plaintext,"lxml")
#    for item in soup.findAll('div',{'class':'i-name'})
    for item in soup.find('h2',{'class':'rich_media_title'}):
        try:
            file.write("<a href=\""+str(url)+"\">")
            file.write(item.encode('utf-8')+"</a><br>")
        except:
            continue
             

def readurl():
    file1 = open("MLresearch.html","a")
    file1.write("<!doctype html>\n<html>\n<head>\n<meta charset=utf-8>\n<title>White Board demo</title>\n</head>\n<body>\n")
    file1.close()
    count = 0
    file = open("MLresearch.txt","r")
    for line in file:
        try:
            if count%5==0:
                print(count)
            count = count + 1
            get_single_url(line)
        except:
            continue
        

readurl()
