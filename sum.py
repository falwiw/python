#!/usr/bin/python
# -*- coding: UTF-8 -*-
import itertools
num_list = [55,0.93,1.74,45,107.91,60,130.59,60,211.34,60,213.4,70,190.09,1,756,284.04,262.96,22.15,594,104,28.86,810,3.34,6.96,6.39,5.94,180,3.45,1.46,3.85,60,3.25,1.43,418.5,0.53,10,39,39,29,234,268.41]
"""
实现求列表任意数字组合之合等于指定数值
"""
#该方法效率高
def fuc(arr, result):
    count = 1
    while count < 1 << len(arr):
        sum = 0
        temp = ''
        count1 = 0
        while count1 < len(arr):
            if (count & 1 << count1) != 0:
                sum += arr[count1]
                temp = "%s%s + " % (temp, arr[count1])
            count1 += 1
        if sum == result:
            print(temp.strip().strip('+'))
        count += 1

lst = [60,39,39,55,756,284.04,262.96,22.15,28.86,810,3.34,6.96,6.39,5.94,180,3.45,1.46,3.85,3.25,1.43,418.5,0.53,10,29,234,268.41]

fuc(lst, 1850)


"""
#该方法效果慢，列表太长容易报错：MemoryError 【内存异常】
from itertools import *
data = [55,0.93,1.74,45,107.91,60,130.59,60,211.34,60,213.4,70,190.09,1,756,284.04,262.96,22.15,594,104,28.86,810,3.34,6.96,6.39,5.94,180,3.45,1.46,3.85,60,3.25,1.43,418.5,0.53,10,39,39,29,234,268.41]
select = product(range(2), repeat=len(data))
data = [list(compress(data, e)) for e in select]
data = [e for e in data if sum(e) == 1850]
print(data)
"""