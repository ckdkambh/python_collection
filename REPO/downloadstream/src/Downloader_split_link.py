from Downloader_base  import DownloaderBase
import requests
import sys, getopt,os

outpath = 'D:\\MY_DownLoad\\'
kind_dict_link=[
    {
        'key_word':'live_panda/',
        'name_str_start':'live_panda/',
        'name_str_end':'/',
        'name_start':'/',
        'num_end':'.wsv',
        'type':'panda'
    },
    {
        'key_word':'douyucdn2.cn/',
        'name_str_start':'video/',
        'name_str_end':'/',
        'num_start':'UHD/',
        'num_end':'.m4s',
        'type':'douyu'
    },
]
class DownloaderSplitLink(DownloaderBase):
    def __init__(self, link):
        self.link = link
        self.file_name = 'undefinded'
        self.is_valid = True
    
    def get_valid(self):
        return self.is_valid
    
    def get_next_file_name(self):
        for type_record in kind_dict_link:
            if self.link.find(type_record['key_word']) != -1:
                print('it is a '+type_record['type']+'tv link')
                index1 = self.link.find(type_record['name_str_start']) + len(type_record['name_str_start'])
                index2 = self.link.find(type_record['name_str_end'], index1)
                index3 = self.link.find(type_record['num_start'], index2) + len(type_record['num_start'])
                index4 = self.link.find(type_record['num_end'], index3)
                break
        try:
            self.file_name = self.link[index1:index2]
            num = self.link[index3:index4]
            return self.file_name+'_'+num+'.flv'
        except Exception as e:
            #print(e)
            self.is_valid = False
        
    def get_next_link(self):
        if self.is_valid == False:
            print("link is invalid")
            return ""
        for type_record in kind_dict_link:
            if self.link.find(type_record['key_word']) != -1:
                print('it is a '+type_record['type']+'tv link')
                index1 = self.link.find(type_record['name_str_start']) + len(type_record['name_str_start'])
                index2 = self.link.find(type_record['name_str_end'], index1)
                index3 = self.link.find(type_record['num_start'], index2) + len(type_record['num_start'])
                index4 = self.link.find(type_record['num_end'], index3)
                break
        num_str = self.link[index3:index4]
        num = int(num_str, 16)
        num_str = hex(num + 1)
        self.link = self.link[0:index3]+num_str[2:]+self.link[index4:]
        return self.link

if __name__=="__main__":
   tester = DownloaderSplitLink("https://0521771057e89199ce0bed31485c4100.v.smtcdns.net/hlsh5p1.douyucdn2.cn/video/3559749rGnNf0VCv_2000/UHD/5bfd6efd.m4s")
   print(tester.get_next_file_name())
   print(tester.get_next_link())
   print(tester.get_valid())
   tester = DownloaderSplitLink("123")
   print(tester.get_next_file_name())
   print(tester.get_next_link())
   print(tester.get_valid())
   