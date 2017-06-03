#coding-utf-8
import re,sys
from bs4 import BeautifulSoup
import time
from util import getUrl

sys.setrecursionlimit(1000000) 

#firstUrl="https://fangyuanyuan2017.tumblr.com"
firstUrl="https://baby258.tumblr.com"

secondUrl=firstUrl+"/page/"
startPage = 1
endPage = 4
result = {
    "img_list" : [],
    "video_list" : []
    }

def tumblrDownHtml():
    currentPage = startPage
    while currentPage <= endPage:
        print('第%d页\n'%(currentPage))
        if currentPage == 1:
            url = firstUrl
        else:
            url = secondUrl+str(currentPage)
        downLoader(url);
        currentPage = currentPage + 1

def downLoader(url):
    while True:
        try:
            get_url = getUrl(url)
            break
        except Exception:    
            time.sleep(1)
            continue
    codingTypr = get_url.encoding
    soup = BeautifulSoup(get_url.text,"html5lib")
    postList = soup.find_all("section", class_="post")
    #Analysis direct img link
    for i in postList:
        imgList = i.find_all("img")
        for j in imgList:
            imgLink = j["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore')
            if not imgLink.endswith(".png"):
                print(imgLink)
                result["img_list"].append(imgLink)
    #Analysis iframe img link   
    for i in postList:
        iframeLink = i.find_all("iframe")      
        for j in  iframeLink:
            print("find a iframe")
            if j["src"].startswith("http"):
                urlLink = j["src"]
            elif j["src"].startswith("//"):
                urlLink = "https:"+j["src"]
            else:
                urlLink = firstUrl+j["src"]
            print(urlLink)    
            downIframe(urlLink)   

def downIframe(url):
    isVideo = False
    while True:
        try:
            get_url = getUrl(url)
            break
        except Exception:    
            time.sleep(1)
            continue
    codingTypr = get_url.encoding
    soup = BeautifulSoup(get_url.text,"html5lib")
    if not url.find("instagram") == -1:
        videoLink = soup.find_all("div", class_="EmbedFrame EmbedMedia")
        videoLink1 = videoLink[0]
        videoLink2 = videoLink1.a
        handleInsLink('https://www.instagram.com'+videoLink2['href'])
        return
    videoList = soup.find_all("video")        
    for i in videoList:
        try:
            print(i["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))
            result["video_list"].append(i["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))  
        except KeyError:
            sourceLink = i.source
            print(sourceLink["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))   
            result["video_list"].append(sourceLink["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))      
        isVideo = True
        
    if isVideo == False:    
        imgList = soup.find_all("img")
        for j in imgList:
            imgLink = j["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore')
            if not imgLink.endswith(".png"):
                print(imgLink)
                result["img_list"].append(imgLink)

def handleInsLink(url):
    print("handleInsLink: "+url)
    while True:
        try:
            get_url = getUrl(url)
            break
        except Exception:    
            time.sleep(1)
            continue
    codingTypr = get_url.encoding
    soup = BeautifulSoup(get_url.text,"html5lib")
    link = soup.find_all("meta")
    for i in link:
        try:
            if i['property'] == 'og:video:secure_url':
                print(i['content'].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))
                result["video_list"].append(i['content'].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))
        except KeyError:
            continue

if __name__=="__main__":
    tumblrDownHtml()
    p = re.compile("[^\w]*")
    fileName = p.sub('', firstUrl)
    fpath = 'D:\\3333\\'+fileName+'.txt'
    try:
        with open(fpath, 'w') as f:
            f.write('')
        with open(fpath, 'a') as f:
            f.write('result:\n')
            f.write('img:\n')
            for i in result["img_list"]:
                f.write(i+'\n')
            f.write('video:\n')    
            for i in result["video_list"]:
                f.write(i+'\n')  
    except OSError as e:
        print(e)
    print('done')        
        
        
        
        
        
        
        
        
        