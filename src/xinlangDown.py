# coding=UTF-8

import re

modeIndex = 0

with open('C:\\Users\\ff\\Desktop\\1', 'r', encoding='UTF-8') as f:
    L = f.read()
    
if L.find('\'video\''):
    modeIndex = 1

L = re.split('\n|\s', L)

for i in L:
    if modeIndex == 0:
        if not i.find('thumb150') == -1:
            print(i.replace('thumb150', 'large'))
    else:
        if not i.find('http://us.sinaimg') == -1:        
            print(i)    