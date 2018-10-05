#coding-utf-8
import re,sys
from bs4 import BeautifulSoup
import time
from util import getUrl
from selenium import webdriver
import time

'''
使用方式：
https://blog.csdn.net/florachy/article/details/77750991
按上文安装环境
运行程序，在弹出的Firefox窗口中 选项卡 中的 安全 中选择  提示保存密码
在手动登录网站
在程序交互窗口中按任意键继续
'''
sys.setrecursionlimit(1000000)
baseUrlList = []
firstUrl = ''
filePath = 'E:\\tumblr.txt'
secondUrl=firstUrl+"/page/"
startPage = 1
endPage = 4
result = {
    "img_list" : [],
    "video_list" : []
    }

testFile="E:\\test.txt"

driver=webdriver.Firefox()

driver.get('https://www.tumblr.com/dashboard')
#driver.maximize_window()
input("press any key to continue")
while True:
    try:
        driver.get('https://www.tumblr.com/dashboard')
        print("complete")
        break
    except Exception:
        print("wait to complete")
        time.sleep(1)
        continue



def tumblrDownHtml():
    currentPage = startPage
    secondUrl=firstUrl+"/page/"
    while currentPage <= endPage:
        print('第%d页\n'%(currentPage))
        if currentPage == 1:
            url = firstUrl
        else:
            url = secondUrl+str(currentPage)
        downLoader(url);
        currentPage = currentPage + 1

def downLoader(url):
    print('downLoader: '+url)
    while True:
        try:
            driver.get(url)
            data = driver.page_source
            break
        except Exception:
            time.sleep(1)
            continue
    soup = BeautifulSoup(data,"html5lib")
    postList = soup.find_all("section", class_="post")
    #Analysis direct img link
    for i in postList:
        imgList = i.find_all("img")
        for j in imgList:
            imgLink = j["src"]
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
            driver.get(url)
            data = driver.page_source
            break
        except Exception:
            time.sleep(1)
            continue
    soup = BeautifulSoup(data,"html5lib")
    if not url.find("instagram") == -1:
        try:
            videoLink = soup.find_all("div", class_="EmbedFrame EmbedMedia")
            videoLink1 = videoLink[0]
            videoLink2 = videoLink1.a
            handleInsLink('https://www.instagram.com'+videoLink2['href'])
        except IndexError as e:
            print(e)
        return
    videoList = soup.find_all("video")
    for i in videoList:
        try:
            print(i["src"])
            result["video_list"].append(i["src"])
        except KeyError:
            sourceLink = i.source
            print(sourceLink["src"])
            result["video_list"].append(sourceLink["src"])
        isVideo = True

    if isVideo == False:
        imgList = soup.find_all("img")
        for j in imgList:
            imgLink = j["src"]
            if not imgLink.endswith(".png"):
                print(imgLink)
                result["img_list"].append(imgLink)

def handleInsLink(url):
    print("handleInsLink: "+url)
    while True:
        try:
            driver.get(url)
            data = driver.page_source
            break
        except Exception:
            time.sleep(1)
            continue
    soup = BeautifulSoup(data,"html5lib")
    link = soup.find_all("meta")
    for i in link:
        try:
            if i['property'] == 'og:video:secure_url':
                print(i['content'])
                result["video_list"].append(i['content'])
        except KeyError:
            continue

if __name__=="__main__":
    print('start')
    with open(filePath, 'r', encoding='UTF-8') as f:
        baseUrlList = f.read()
    baseUrlList = re.split('\n|\s', baseUrlList)
    temp = []
    for i in baseUrlList:
        if i.endswith('/'):
            temp.append(i[0:len(i)-1])
    baseUrlList = temp
    totalNum = len(baseUrlList)
    currentNum = 0
    for ilink in baseUrlList:
        print("######start now is %dth link, total number is %d, is %f%%"%(currentNum, totalNum, currentNum*100/totalNum))
        print("link: "+ilink)
        firstUrl = ilink
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
        currentNum = currentNum + 1
        result["img_list"] = []
        result["video_list"] = []







