import requests
from datetime import datetime
import time
import sys, getopt,os

maxSize = 100*1024000
maxConnectTry = 300
outpath = 'D:\\MY_DownLoad\\'
file_url = """
https://f2d5b78b3ba75e91ecebaf183f56ec8c.v.smtcdns.net/mobilep2.douyucdn2.cn/dyliveflv3a/7659399rM8QMlAla.xs?playid=1631896668846-1603860141&uuid=f806ed7c-2c24-4483-a6b0-cb1c64d7a00b&txSecret=d304cdc083ba7f10f0475afcc89c2fd1&txTime=6144c6b5&origin=tct
"""

# True False
# 斗鱼需要 flash模式的 高清才能下载，超清无法下载  11111 影熙热舞妖精 恩熙ovo 小深深儿 朴雨彬

g_UseDirName = True 
# 腐团儿 Minana呀 苏恩Olivia Chance喵  张琪格 Sun佐伊  小a懿 南妹儿呀 夏只只i 性感热舞阿离 乔妹eve 大宝好哇塞呀  宝儿lucky 暴躁的鹿鹿猪  王羽杉Barbieshy 陈小花呢 Lovely璐璐酱 猫九酱O3O      暴走小卡车 萌宝绵绵Z啊 王羽杉Barbieshy 米儿啊i 素素不吃肉  淼淼喵酱呀 是Ari瑞哥 
# 湖南小橙子 沈亦Mona 尹恩恩1 VIVI小小酥 阿让让丶 Y智恩 何菱

# 秀秀呢 lone考拉  你的咪咪酱 子诺小姐姐 Ss莹莹酱 珊儿兔兔兔 MICO要抱抱 子然学姐 舞法天女小慕林 Ellin艾琳  同桌小美 Sunny温晴
# 你的口罩表妹 陈小花呢 血色东霓 秀秀呢 王雨檬呀 温柠c丶 下凡的张美男 上蓝冰儿



DirName = "温柠c丶"

def analysisFileName():
    fileName = DirName
    print(fileName)
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
    
    last_work_time = time.time()
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
        if time.time() - last_work_time < 2:
            time.sleep(10)
            print('too fast, stop download!')
            continue
        else:
            last_work_time = time.time()
            
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
        if os.path.exists(fileName) and get_FileSize(fileName) < 800:
            print('file:%s too small(%dKB), delete!'%(fileName, get_FileSize(fileName)))
            try:
                os.remove(fileName)
            except IOError as e:
                print(e)
                continue
        print('complete')
