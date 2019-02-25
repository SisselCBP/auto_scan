#!/usr/bin/python
# coding:utf-8



import os
import nmap

nm = nmap.PortScanner()

nm.scan('25.25.205.36', arguments='-v -Pn')
# 列出结果
def list_nmap_report(nm):
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


list_nmap_report(nm)

# webshell
  
def web_shell(url, exec_cmd):
    try:
        shell = requests.get(url+exec_cmd)
        if shell.code >= 400:
            return False
        else:
            return shell.content
    except Exception as err:
        print err
        return False


# arp获得 - NMAP有一点重，用指令有一点慢

from scapy.all import srp, Ether, ARP

def arp_scan():
    IpScan = '192.168.114.1/24'
    try:
        ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=IpScan), timeout=2)
    except Exception as e:
        print(e)
    else:
        for send, rcv in ans:
            ListMACAddr = rcv.sprintf("%Ether.src%---%ARP.psrc%")

'''
40:5E:2A:6C:90:98--192.168.31.1
20:42:EC:51:F3:8E--192.168.31.114
'''

# shell管理

