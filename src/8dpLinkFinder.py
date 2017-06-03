#coding-utf-8
import re,sys
from bs4 import BeautifulSoup
import time
from util import getUrl

sys.setrecursionlimit(1000000) 
firstUrl="http://8haodangpu.info/"
secondUrl="http://www.8haodangpu.info/page/"
startPage = 1
endPage = 2

def badpdownHtml():
    currentPage = startPage
    while currentPage <= endPage:
        print('第%d页\n'%(currentPage))
        if currentPage == 1:
            url = firstUrl
        else:
            url = secondUrl+str(currentPage)
        while True:
            try:
                get_url = getUrl(url)
                break
            except Exception:    
                time.sleep(1)
                continue
        codingTypr = get_url.encoding
        soup = BeautifulSoup(get_url.text,"html5lib")
        postList = soup.find_all("div", class_="post post-text")
        for i in postList:
            try:
                print(i.h3.a.string.encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))
            except UnicodeEncodeError:    
                print('UnicodeEncodeError...')
            timeStamp = i.find('p', class_="posttime")    
            print(timeStamp.a.string.encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))
            linkFind = i.find_all('a', target="_blank")
            #print(linkFind[0].string)
            feeLink = linkFind[0].string
            p = re.compile("[^\d]*")
            feeLink = p.sub('', feeLink)
            feeLink='vip_downvip_down(\'com\',\''+feeLink+'\')'
            print(feeLink)
        currentPage = currentPage + 1

if __name__=="__main__":
    badpdownHtml()
    print('done')        
        
        
        
        
        
        
        
        
        