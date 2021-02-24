import downloadstreamvideo
import requests
from datetime import datetime
import time
import sys, getopt,os
import win32clipboard as wc
import win32con
import Downloader_stable_link
maxSize = 100*1024000
maxConnectTry = 300
outpath = 'D:\\MY_DownLoad\\'
file_url = """https://flv-live-ws.xingxiu.panda.tv/panda-xingxiu/3a4da01471a2621fd062a42865647725.flv?0.3675273242406547
"""



if __name__=="__main__":
    print(file_url)
    
    
    fileName = analysisFileName()
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}
    while(True):
        try:
            r = requests.get(file_url, stream=True,timeout=1, headers=headers,verify=False)
        except OSError as e:
            print(e)
            print('link break wait to connect, %dth try...'%connectTryCount)
            time.sleep(1)
            connectTryCount = connectTryCount + 1
            if connectTryCount > maxConnectTry:
                print('reach maxmium times of try, exit')
                break
            continue
        connectTryCount = 0
        count = 0
        fileName = getNextFileName(fileName)
        print('start download to ', fileName)
        with open(fileName, "wb") as pdf:
            try:
                for chunk in r.iter_content(chunk_size=1024000):
                    if count < maxSize and chunk:
                        pdf.write(chunk)
                        count = count + chunk.__sizeof__()
                    else:
                        break
            except OSError as e:
                print('link break close current file, wait for link resume')
                time.sleep(3)
                continue
        if os.path.exists(fileName) and get_FileSize(fileName) < 200:
            print('file:%s too small(%dKB), delete!'%(fileName, get_FileSize(fileName)))
            try:
                os.remove(fileName)
            except IOError as e:
                print(e)
                continue
        print('complete')
