import unicodedata
import requests
from bs4 import BeautifulSoup

# def trade_spider(max_pages):
#     page = 84
#     while page <= max_pages:
#         url = 'http://library.skillport.com/courseware/Content/cca/df_ahec_a06_it_enus/output/t' + str(page) + '/misc/transcript.html'
#         sourceCode = requests.get(url)
#         print(sourceCode)
#     #    plaintext = sourceCode.content.decode('gb2312','ignore')
#         # plaintext = sourceCode.content
#         plaintext = sourceCode.text
#         soup = BeautifulSoup(plaintext,"lxml")
#         title = ""
#         for i in soup.find('h1',{'class':'title'}):
#             title = i
#         file = open(str(page)+title+".xml","w")
#
#         for link in soup.findAll('p',{'class':'bodytext'}):
#             file.write(str(link))
#
#         page+=4
#         file.close()

def get_single_url(url):
    file = open("wePython.txt","a")
    sourceCode = requests.get(url)
#    print(sourceCode)
    plaintext = sourceCode.text
    soup = BeautifulSoup(plaintext,"lxml")
#    for item in soup.findAll('div',{'class':'i-name'})
    for item in soup.find('h2',{'class':'rich_media_title'}):
        file.write(str(url))
        file.write(item.encode('utf-8').strip()+"\n\n")

def readurl():
    file = open("list.txt","r")
    for line in file:
        get_single_url(line)

readurl()


#
# get_single_url('http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652563925&idx=1&sn=2c6dffa2e2b8fcdbbfe1483f50d8e171&scene=4#wechat_redirect')
# get_single_url('http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=403797468&idx=1&sn=b9af1fc851fcc001cdfcdf183434d282&scene=4#wechat_redirect')
