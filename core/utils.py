#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-23 11:59:32
# 这只竹鼠很漂亮呀

# 这里放工具函数

# netmask = '255.255.255.0'
# num = 24
# ip = '127.0.0.1'
# IpScan = '127.0.0.0/24'

def netmask_to_num(netmask):
    #netmask = '255.255.255.0'
    result = ""
    print netmask
    for num in netmask.split('.'):
        temp = str(bin(int(num)))[2:]
    result = result + temp
    return len("".join(str(result).split('0')[0:1]))


def num_to_IpScan(ip, num):
    #num = 24
    #ip = '127.0.0.1'
    
    # 最后几位抹了就完了
    return '127.0.0.0/24'

