# -*- coding: utf-8 -*-
import sys

getin = input()
tmp = []
for i in range(0,len(getin)):
    tmp.append(getin[i])
    if (tmp[i] == 'c'):
        break

password = ''.join(tmp)
print(password)
    
