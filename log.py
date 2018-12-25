#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-23 11:59:32
# 这只竹鼠很漂亮呀

import os, time
import logging
from settings import *

# encoding=utf-8
import logging,time

# log_path是存放日志的路径
import os


#cur_path = os.path.dirname(os.path.realpath(__file__))
cur_path = os.path.realpath(__file__)
log_path = os.path.join(os.path.dirname(cur_path), 'logs')

class Log(object):

    def __init__(self, module_name):
        # 文件的命名
        self.logname = os.path.join(log_path, module_name+'_%s.log' % time.strftime('%y%m%d%H'))
        self.logger = logging.getLogger(module_name)
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s.%(filename)s - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

log = Log('Scanner')