from Downloader_base  import DownloaderBase
import requests
from datetime import datetime
import time
import sys, getopt,os
outpath = 'D:\\MY_DownLoad\\'
kind_dict_link=[
    {
        'key_word':'live_panda/',
        'start_str':'live_panda/',
        'end_str':'?sign',
        'type':'panda'
    },
    {
        'key_word':'huyalive/',
        'start_str':'huyalive/',
        'end_str':'?wsSecret',
        'type':'huya'
    },
    {
        'key_word':'panda-xingxiu/',
        'start_str':'panda-xingxiu/',
        'end_str':'?',
        'type':'panda'
    },
    {
        'key_word':'lzlive/',
        'start_str':'lzlive/',
        'end_str':'?',
        'type':'longzhu'
    },
    {
        'key_word':'panda-xingyan/',
        'start_str':'panda-xingyan/',
        'end_str':'?',
        'type':'panda'
    },
    {
        'key_word':'onlive/',
        'start_str':'onlive/',
        'end_str':'?',
        'type':'HUYA'
    },
    {
        'key_word':'live.panda.tv/p2p/flv/hint?sign=',
        'start_str':'&rid=',
        'end_str':'&stream=',
        'type':'panda'
    },
]

class DownloaderStableLink(DownloaderBase):
    def __init__(self, link):
        self.link = link
        self.fileName = self.analysisFileName()
        
    def analysisFileName(self):
        for type_record in kind_dict_link:
            if self.link.find(type_record['key_word']) != -1:
                print('it is a '+type_record['type']+'tv link')
                index1 = self.link.find(type_record['start_str']) + len(type_record['start_str'])
                index2 = self.link.find(type_record['end_str'])
                break
        file_name = self.link[index1:index2]
        outfile = outpath+file_name
        date = datetime.now().__str__()
        date = date.replace(' ', '').replace('-', '').replace(':', '').replace('.', '')
        outfile = outfile.split('.')[0]+'_'+date+'.flv'
        return outfile
        
    def get_next_file_name(self):
        index1 = self.fileName.split('.')[0]
        index2 = index1.find('##')
        index3 = 1
        if index2 == -1:
            index2 = len(index1)
        else:
            index3 = self.fileName[index2+2:len(index1)]
            index3 = int(index3) + 1
        self.fileName = self.fileName[:index2]+'##'+str(index3)+'.flv'
        return self.fileName
        
    def get_next_link(self):
        return self.link