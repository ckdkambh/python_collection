from Downloader_base  import DownloaderBase
import requests
import sys, getopt,os

outpath = 'D:\\MY_DownLoad\\'
kind_dict_link=[
    {
        'key_word':'live_panda/',
        'start_str':'live_panda/',
        'end_str':'/',
        'num_end':'.wsv',
        'type':'panda'
    },
]
class DownloaderSplitLink(DownloaderBase):
    def __init__(self, link):
        self.link = link
    
    def get_next_file_name(self):
        for type_record in kind_dict_link:
            if self.link.find(type_record['key_word']) != -1:
                print('it is a '+type_record['type']+'tv link')
                index1 = self.link.find(type_record['start_str']) + len(type_record['start_str'])
                index2 = self.link.find(type_record['end_str'], index1)
                index3 = self.link.find(type_record['num_end'], index2)
                break
        file_name = self.link[index1:index2]
        num = self.link[index2+1:index3]
        return file_name+'_'+num+'.flv'
        
    def get_next_link(self):
        for type_record in kind_dict_link:
            if self.link.find(type_record['key_word']) != -1:
                print('it is a '+type_record['type']+'tv link')
                index1 = self.link.find(type_record['start_str']) + len(type_record['start_str'])
                index2 = self.link.find(type_record['end_str'], index1)
                index3 = self.link.find(type_record['num_end'], index2)
                break
        num_str = self.link[index2+1:index3]
        num = int(num_str, 16)
        num_str = hex(num + 1)
        self.link = self.link[0:index2+1]+num_str[2:]+self.link[index3:]
        return self.link
    