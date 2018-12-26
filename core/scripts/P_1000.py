#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-13 15:16:39
# 这只竹鼠很漂亮呀

import datetime

class P_1000():

    def __init__(self):

        self.svid = 'P_1000'
        self.name = "nmap扫描开放端口"
        self.description = "普通的 -Pn 最基本的扫描方式"
        
        """
        规则配置
        """

    def main(self, ip):
        import nmap

        nm = nmap.PortScanner()
        nm.scan(ip, arguments='-v -Pn')
        # 很慢 -sn
        self.list_nmap_report(nm)
        
    # 列出结果
    def list_nmap_report(self, nm):
        for host in nm.all_hosts():
            print nm[host]
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

        '''
        这里封装好返回给上层处理
        '''

        return 


