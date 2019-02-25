#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-13 15:16:39
# 这只竹鼠很漂亮呀

# 这里是linux下的一些指令，以及返回内容的处理

import re

class LinuxInstruction():

    def __init__(self):
        pass

    def ifconfig(self):
        return 'ifconfig'
         
    def ifconfig_analysis(self, result):
        ip_re = "inet (\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})"
        ip = re.findall(ip_re, result)
        print ip
        # 分析网卡，拿到本机ip，dns

    def etc_passwd(self):
        return 'cat /etc/passwd'

    def etc_passwd_analysis(self, result):
        print result
        return 



