#coding-utf-8
import re,sys
from bs4 import BeautifulSoup
import time
from util import getUrl
import inspect

sys.setrecursionlimit(1000000) 
firstUrl="http://www.xiuren8.com/index-"
startPage = 1
endPage = 1

def xiuren8_1_Html():
    currentPage = startPage
    while currentPage <= endPage:
        print('第%d页\n'%(currentPage))
        url = firstUrl+str(currentPage)+'.htm'
        print(url)
        while True:
            try:
                get_url = getUrl(url)
                break
            except Exception:    
                time.sleep(1)
                continue
        codingTypr = get_url.encoding
        soup = BeautifulSoup(get_url.text,"html5lib")
        postList = soup.find_all("a", class_="product-title")
        print(postList)
        '''
        for i in postList:
            try:
                #print('http://www.xiuren8.com/'+i.a['href'])
                print(i)
            except UnicodeEncodeError:    
                print('UnicodeEncodeError...')
        '''        
        currentPage = currentPage + 1

if __name__=="__main__":
    xiuren8_1_Html()
    print('done')        
        
        
        
        
        
        
        
        
        