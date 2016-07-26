# coding=utf-8

import sys

sys.path.append('home/yc/PycharmProjects/yqproject/yqproject/settings.py')
from MoblieWeibo import *
from start_search import *

__author__ = 'gu'


def run():
    """
        :return:
    """

    MoblieWeibo().login('1939777358@qq.com', '123456a')
    # '70705420yc@sina.com', '1234567') ('meilanyiyou419@163.com','aaa333') 'odlmyfbw@sina.cn','tttt5555'
    serach_list(["南海", "奥运村", "菲律宾"])


def main_weibo():
    """
        :return:
    """

    run()


main_weibo()
