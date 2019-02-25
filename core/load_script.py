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
        SCRIPT_PATH = './scripts'
        self.script_path = SCRIPT_PATH
        if not os.path.exists(self.script_path):
            log.error("[INIT] can't found scripts in '%s' !".format(self.script_path))

        self.script_list = self.list_parse()

        # import function from script
        self.script_dict = {}
        for script in self.script_list:
            scriptname = script.split('.')[0]
            scriptfile = SCRIPTS_MODULES_PATH + scriptname
            self.script_dict[scriptname] = __import__(scriptfile, fromlist=scriptname)

    def list_parse(self):
        files = os.listdir(self.script_path)
        result = []

        for f in files:
            if f.startswith(PORT_SCRIPT_NAME):
                result.append(f)
        print result
        return result

if __name__ == '__main__':
    script = Script()

    print script
