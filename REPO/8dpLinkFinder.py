#coding-utf-8
import re,sys
from bs4 import BeautifulSoup
import time
from util import getUrl

sys.setrecursionlimit(1000000) 
firstUrl="http://bhdp.blog.fc2blog.us"
secondUrl="http://bhdp.blog.fc2blog.us/page-"
startPage = 16
endPage = 18

error_str = ""

def badpdownHtml():
    currentPage = startPage
    while currentPage <= endPage:
        print('第%d页\n'%(currentPage))
        if currentPage == 1:
            url = firstUrl
        else:
            url = secondUrl+str(currentPage)+".html"
        while True:
            try:
                get_url = getUrl(url)
                break
            except Exception:    
                time.sleep(1)
                continue
        soup = BeautifulSoup(get_url.text,"html5lib")
        postList = soup.find_all("div", class_="entry")
        for i in postList:
            titleLink = i.find("div", class_="tit")
            print(titleLink.h2.text)
            timeStamp = i.find('div', class_="date")    
            print(timeStamp.p.text)
            linkBody = i.find('div', class_="body")
            linkList = linkBody.find_all('a')
            isFind = False
            for j in linkList :
                p = re.compile("[^\d]*")
                feeLink = p.sub('', j['href'])
                if len(feeLink) != 7:
                    continue
                isFind = True
                feeLink='vip_downvip_down(\'com\',\''+feeLink+'\')'
                print(j['href'])
                print(feeLink)
            if not isFind :
                global error_str
                error_str = error_str+titleLink.h2.text+"数据可能错误\n"
            '''
            print(feeLink)
            p = re.compile("[^\d]*")
            feeLink = p.sub('', feeLink)
            global error_str
            if len(feeLink) != 7:
                error_str = error_str+(i.h3.a.string.encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))+"数据可能错误\n"
                continue
            feeLink='vip_downvip_down(\'com\',\''+feeLink+'\')'
            print(feeLink)
            '''
        currentPage = currentPage + 1

if __name__=="__main__":
    badpdownHtml()
    sys.stderr.write(error_str)
    print('done')        
        
        
        
        
        
        
        
        
        