#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-23 11:59:32
# 这只竹鼠很漂亮呀

import os
import nmap

nm = nmap.PortScanner()

nm.scan('25.25.205.36', arguments='-v -Pn')

# 列出结果
def list_nmap_report(nm):
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

if __name__ == "__main__":
    list_nmap_report(nm)
