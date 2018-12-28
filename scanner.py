#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-23 14:59:32
# 这只竹鼠很漂亮呀

from core.scanner import *

if __name__ == "__main__":
    print 'system start'
    #host_scanner = HostScanner()
    port_scanner = PortScanner()
    ip = '192.168.31.1'
    port_scanner.start(ip)

    

    
