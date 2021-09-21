import requests
from datetime import datetime
import time
import sys, getopt,os
from hashlib import md5


def walkFile(file):
    ret = set()
    for root, dirs, files in os.walk(file):
        for d in files:
            ret.add(os.path.join(root, d))
    return ret

def getFileMd5(file):
    with open(file, "rb") as f:
        count = 1
        ret = b''
        for i in f:
            if count > 6:
                if count < 10:
                    ret = ret + i
                else:
                    break
            count = count + 1
        result = md5(ret).hexdigest()
        return result

if __name__=="__main__":
    path = r'D:\MY_DownLoad\11111\cut'
    fileList = walkFile(path)
    md5Map = {}
    count = 0
    remove_count = 0
    add_count = 0
    for i in fileList:
        currentMd5 = getFileMd5(i)
        if currentMd5 in md5Map:
            oldSize = os.path.getsize(md5Map[currentMd5])
            newSize = os.path.getsize(i)
            if newSize > oldSize:
                print("remove %s"%(md5Map[currentMd5]))
                os.unlink(md5Map[currentMd5])
                md5Map[currentMd5] = i
            else:
                print("remove %s"%(i))
                os.unlink(i)
            remove_count = remove_count + 1
        else:
            md5Map[currentMd5] = i
            add_count = add_count + 1
        count = count + 1
        print('进度%4.2f%%'%(100*count/len(fileList)), end='\r')
    print('共删除%d个文件, 理论剩余%d个文件, 总共%d个文件, add_count=%d' % (remove_count, len(md5Map), len(fileList), add_count))
    #with open('D:\\code\\' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.txt', 'w') as f:
    #    for i in sorted(md5Map):
    #        f.write('%s, %s\n' % (i, md5Map[i]))
