# -*- coding: utf-8 -*-
import sys

tmp = input()

tmp = tmp.split()

answer = int(tmp[0]) + int(tmp[1])*(int(tmp[2]) -1)
print(answer)