# coding=utf-8
from time import sleep

__author__ = 'gu'
import sys
sys.path.append('home/yc/PycharmProjects/yqproject/yqproject/settings.py')
from MoblieWeibo import *

def run():
    """
        通过先检测，进行更新话题列表，以类进行搜索
        :return:
    """


def main_weibo():
    """
        模拟登陆后，每一小时运行一次
        :return:
    """
    MoblieWeibo().login('account','password')

    while True:
        run()
        print "即将休息一下"

        sleep(3600)
        print "程序睡醒"

main_weibo()
