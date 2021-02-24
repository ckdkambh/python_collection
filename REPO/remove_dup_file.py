
import os
from collections import defaultdict
import hashlib

def show_files(path, all_files):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            all_files.append(os.path.join(path,file))

    return all_files

def get_file_md5(file_name):
    """
    计算文件的md5
    :param file_name:
    :return:
    """
    m = hashlib.md5()   #创建md5对象
    with open(file_name,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)  #更新md5对象
    return m.hexdigest()    #返回md5对象

def findDupFile(fileList):
    fileSizePathMap = defaultdict(lambda: set())
    for i in fileList:
        fsize = os.path.getsize(i)
        fileSizePathMap[fsize].add(i)
    return fileSizePathMap

def deleteDupFile(fileSizePathMap):
    count = 0
    for k, v in fileSizePathMap.items():
        if len(v) > 1:
            md5Val = None
            for i in v:
                if not md5Val:
                    md5Val = get_file_md5(i)
                else:
                    if md5Val != get_file_md5(i):
                        break
                    else:
                        print('remove %s'%(i))
                        os.remove(i)
        count = count + 1
        print('进度%4.2f%%'%(100*count/len(fileSizePathMap)),end='\r')

if __name__=="__main__":
    # fileList = show_files(r'D:\code\TiMidity++-2.15.0-w32\TiMidity++-2.15.0', [])
    fileList = show_files(r'\\Lenovo-pc\k\weibo', [])
    # fileList = show_files(r'D:\test', [])
    fileSizePathMap = findDupFile(fileList)
    deleteDupFile(fileSizePathMap)