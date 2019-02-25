#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-23 14:59:32
# 这只竹鼠很漂亮呀

# ssh
import paramiko

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
    pkey='./ssh_key'  #本地密钥文件路径[此文件服务器上~/.ssh/id_rsa可下载到本地]
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