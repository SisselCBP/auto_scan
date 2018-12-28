#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-13 15:16:39
# 这只竹鼠很漂亮呀

import datetime

class H_1000():

    def __init__(self):

        self.svid = 'H_1000'
        self.name = "arp 扫描"
        self.description = "broadcast相应的包"
        
        """
        规则配置
        """

    def main(self, IpScan):
        from scapy.all import srp, Ether, ARP
        self.arp_scan(IpScan)

        #处理一下返回的包
        
        return 

    def arp_scan(self, IpScan):
        # IpScan = '192.168.114.1/24'
        try:
            ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=IpScan), timeout=2)
        except Exception as e:
            print(e)
        else:
            for send, rcv in ans:
                ListMACAddr = rcv.sprintf("%Ether.src%---%ARP.psrc%")

        return