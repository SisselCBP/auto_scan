#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-13 15:16:39
# 这只竹鼠很漂亮呀

# 对于找到的ip，在这里再分析一下

from log import *

def get_dns():
    # /etc/resolvconf/
    # 内网的怎么获得呢，通过调指令读东西吗？
    return '8.8.8.8'

def verify_dns(ip):
    import dns.resolver

    myResolver = dns.resolver.Resolver()
    myResolver.nameservers = [ip]
    try:
        myAnswers = myResolver.query("www.baidu.com", "A")
        for rdata in myAnswers:
            log.debug(rdata)
        return True
    except Exception as err:
        log.error(err)
        return False
    return False

if __name__ == "__main__":
    log.debug('DNS Test Start')
    dns_ip = get_dns()
    assert verify_dns(dns_ip) == True
    log.debug('dns Test Finish')

