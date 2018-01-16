import sys,os
import re
from functools import reduce

FILE_PATH = 'E:\\迅雷下载\\20180116\\'

def getAllMp4File(inPath):
    fileList = os.listdir(inPath)
    out = []
    for i in fileList:
        path = os.path.join(inPath, i)
        if i.endswith('mp4') and os.path.isfile(path):
            out.append(path)
    return out

if __name__ == '__main__':

    # str = u"1月15日00:05正恒-小野，精彩舞蹈，虎牙90020@小野野野野马【01月14日录制】L卡么2014的秒拍视频????​"
    #
    # # pattern =re.compile(u'[\u4e00-\u9fa5]')
    # pattern = re.compile(u"[0-9\u4e00-\u9fa5]+")
    # result = re.findall(pattern, str)
    # result = reduce(lambda x,y:x+y,result)
    # print(result)
    pattern = re.compile(u"[0-9\u4e00-\u9fa5]+")
    infoFileName = FILE_PATH+'123.txt'
    if os.path.exists(infoFileName):
        try:
            f = open(infoFileName, 'rb')
        except IOError as e:
            print(e)
        text = f.read()
        textLink = text.decode('gbk', errors='ignore')
        textLink = re.split('[\r\n]', textLink)
        linkList = []
        titleList = []
        for i in textLink:
            if i != '':
                if i.startswith('http'):
                    index1 = i.find('mp4')
                    str3 = ''
                    if index1 != -1:
                        str2 = i[:index1+3]
                        index2 = str2.rfind('/')
                        str2 = str2[index2+1:]
                        str2 = str2[:10]
                    linkList.append(str2)
                else:
                    instr = re.findall(pattern, i)
                    instr = reduce(lambda x, y: x + y, instr)
                    titleList.append(instr)

        for i in getAllMp4File(FILE_PATH):
            for j in range(len(linkList)):
                if i.find(linkList[j]) != -1:
                    pathName = os.path.dirname(os.path.realpath(i))
                    outName = pathName+'\\'+titleList[j]+'.mp4'
                    print(i)
                    print(outName)
                    try:
                        os.rename(i,outName)
                    except Exception as e:
                        print(e)
        f.close()
    else:
        print('no %s exist !!!'%(infoFileName))
