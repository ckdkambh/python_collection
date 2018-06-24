import requests
from datetime import datetime
import time
import sys, getopt,os

maxSize = 100*1024000
maxConnectTry = 300
outpath = 'D:\\MY_DownLoad\\'
file_url = """http://111.202.98.180/hdl1201.plures.net/onlive/78720fef3b954d58baca843af7728647.flv?txSecret=2a9ea3a4179dde2f7f503d9a73e4341a&txTime=5b2ce7d4&dispatch_from=ztc10.236.21.177&utime=1529669025242
"""

def analysisFileName():
    if file_url.find('live_panda/') != -1:
        print('it is a panda tv link')
        index1 = file_url.find('live_panda/') + len('live_panda/')
        index2 = file_url.find('?sign')
    elif file_url.find('huyalive/') != -1:
        print('it is a huya tv link')
        index1 = file_url.find('huyalive/') + len('huyalive/')
        index2 = file_url.find('?wsSecret')
    elif file_url.find('panda-xingxiu/') != -1:
        print('it is a panda tv link')
        index1 = file_url.find('panda-xingxiu/') + len('panda-xingxiu/')
        index2 = file_url.find('?')
    elif file_url.find('lzlive/') != -1:
        print('it is a panda tv link')
        index1 = file_url.find('lzlive/') + len('lzlive/')
        index2 = file_url.find('?')
    elif file_url.find('panda-xingyan/') != -1:
        print('it is a panda tv link')
        index1 = file_url.find('panda-xingyan/') + len('panda-xingyan/')
        index2 = file_url.find('?')  
    elif file_url.find('onlive/') != -1:
        print('it is a HUYA tv link')
        index1 = file_url.find('onlive/') + len('onlive/')
        index2 = file_url.find('?')         
    fileName = file_url[index1:index2]
    outfile = outpath+fileName
    date = datetime.now().__str__()
    date = date.replace(' ', '').replace('-', '').replace(':', '').replace('.', '')
    outfile = outfile.split('.')[0]+'_'+date+'.flv'
    return outfile

def getNextFileName(fileName):
    index1 = fileName.split('.')[0]
    index2 = index1.find('##')
    index3 = 1
    if index2 == -1:
        index2 = len(index1)
    else:
        index3 = fileName[index2+2:len(index1)]
        index3 = int(index3) + 1
    return fileName[:index2]+'##'+str(index3)+'.flv'

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024)
    return round(fsize,2)

count = 0
connectTryCount = 0

if __name__=="__main__":
    opts, args = getopt.getopt(sys.argv[1:], "u:")
    for op, value in opts:
        if op == "-u":
            file_url = value
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
