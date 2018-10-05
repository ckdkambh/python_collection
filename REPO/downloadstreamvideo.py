import requests
from datetime import datetime
import time
import sys, getopt,os

maxSize = 100*1024000
maxConnectTry = 300
outpath = 'D:\\MY_DownLoad\\'
file_url = """https://flv-live-ws.xingxiu.panda.tv/panda-xingxiu/3ae42880751055ae101acbe8247b2b67.flv?0.964914960321039
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
    elif file_url.find('live.panda.tv/p2p/flv/hint?sign=') != -1:
        print('it is a panda tv link')
        index1 = file_url.find('&rid=') + len('&rid=')
        index2 = file_url.find('&stream=')
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

def get_is_dispersed(link):
    print(link.find('type='))
    print(len(link))
    if link.find('type=')>len(link)-8:
        return True
    return False
    
def get_dispersed_index(link):
    i=link.rfind('/')
    j=link.rfind('.')
    if i!=-1 and j!=-1:
        return link[i+1:j]
    else:
        print('get_dispersed_index error')
        exit(0)
    
def get_next_num_link(link):
    cur_num=get_dispersed_index(link)
    next_num=hex(int(cur_num,16)+1)
    i=link.rfind('/')
    j=link.rfind('.')
    return link[:i+1]+next_num[2:]+link[j:]
    
count = 0
connectTryCount = 0

if __name__=="__main__":
    opts, args = getopt.getopt(sys.argv[1:], "u:")
    for op, value in opts:
        if op == "-u":
            file_url = value
    print(file_url)
    
    is_dispersed = get_is_dispersed(file_url)
    if is_dispersed:
        print('current index is:%s'%(get_dispersed_index(file_url)))
        print('nxet index is:%s'%(get_next_num_link(file_url)))
        exit(0)
    
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
