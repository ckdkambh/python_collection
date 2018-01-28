import requests
from datetime import datetime
import time
import sys, getopt

maxSize = 100*1024000
maxConnectTry = 300
outpath = 'D:\\MY_DownLoad\\'
file_url = """"""

def analysisFileName():
    index1 = file_url.find('live_panda/') + len('live_panda/')
    index2 = file_url.find('?sign')
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

#
# with open("outfile", "wb") as pdf:
#     for chunk in r.iter_content(chunk_size=1024):
#         if chunk:
#             print('download one chunk')
#             pdf.write(chunk)

count = 0
connectTryCount = 0

if __name__=="__main__":
    opts, args = getopt.getopt(sys.argv[1:], "u:")
    for op, value in opts:
        if op == "-u":
            file_url = value
    print(file_url)
    fileName = analysisFileName()
    # try:
    #     fo = open(fileName, 'wb')
    #     print('open new file:',fileName)
    # except IOError as e:
    #     print(e)

    while(True):
        try:
            r = requests.get(file_url, stream=True,timeout=1)
        except OSError as e:
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
        print('complete')
        # for chunk in r.iter_content(chunk_size=1024):
        #     if count < maxSize:
        #         fo.write(chunk)
        #     else:
        #         count = 0
        #         fo.close()
        #         fileName = getNextFileName(fileName)
        #         try:
        #             fo = open(fileName, 'wb')
        #             print('open new file:', fileName)
        #         except IOError as e:
        #             print(e)
        #             break
