#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-20 14:46:40
# 这只竹鼠很漂亮呀

"""
本文件负责导入规则。
"""

import re, os, sys

from settings import *
from log import log

class Script(object):
    def __init__(self):
        self.script_path = SCRIPT_PATH
        if not os.path.exists(self.script_path):
            log.error("[INIT] can't found scripts in '%s' !", self.script_path)
            #os.mkdir(self.rules_path) # 创建规则目录

        self.rule_list = self.list_parse()

        # import function from rule
        self.rule_dict = {}
        for rule in self.rule_list:
            rulename = rule.split('.')[0]
            rulefile = RULES_MODULES_PATH + rulename
            self.rule_dict[rulename] = __import__(rulefile, fromlist=rulename)

    def list_parse(self):
        files = os.listdir(self.rules_path)
        result = []

        for f in files:
            if f.startswith(ETH_RULES_NAME):
                result.append(f)

        return result

if __name__ == '__main__':
    rule = Rule()
    #print rule.rule_dict['eth_1000']
    rule_test = rule.rule_dict['eth_1000'].eth_1000

    rule_test.main()
