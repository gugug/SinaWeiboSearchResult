# coding=utf-8

import random
import sys
from time import sleep
import urllib2
import re
from create_file import *
from multiprocessing import Process, Manager
import os
import multiprocessing

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'gu'
"""
7.25
测试完毕,会出现掉线的问题,可能是频率太高
"""


class WeiboPage:
    """
    父类
    定义了一些变量和一些公用方法
    """
    manager = Manager()

    detected_tpdict = {}
    detected_tpdict = manager.dict()

    all_hunterlist = []
    all_hunterlist = manager.list()  # 保存猎头的全部博文,点赞之类的

    def __init__(self):
        """
        :param one_user: 用户的id，即是猎头的id
        :return:
        """
        self.weibo_list = []
        self.time_list = []
        self.weibo = []
        self.writing_time = []
        self.base_page = []
        self.dictwt = {}
        self.no_repeat_list = []
        self.comment_dir = os.path.join(BASE_DIR, 'documents', 'comment/')  # 猎头微博的评论内容
        self.forward_path_dir = os.path.join(BASE_DIR, 'documents', 'forward_path/')  # 猎头的微博的转发路径
        self.header = {'User-Agent': 'Mozilla/' + str(
            float(int(random.uniform(1, 6)))) + '(X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/' + str(
            float(int(random.uniform(29, 36))))}

        self.blog_id = ''
        self.post_time = ''
        self.event_id = ''
        self.corpus_dir = ''
        self.link = ''

    def cleaned_wbtime(self, item1):
        """
        转化时间格式
        :param item1: 时间
        :return:标准格式的时间 h:m:s
        """
        extra = re.compile('</span>.*$')  # 匹配输入字符串的结束位置
        today = re.compile('今天')
        ago = re.compile('\d+分钟前')

        post_time = re.sub(extra, '', item1)
        t = time.strftime('%m' + '月' + '%d' + '日', time.localtime())
        t = t.decode('utf-8')
        post_time = re.sub(today, t, post_time)
        post_time = re.sub(ago, t, post_time)
        return post_time

    def cleaned_weibo(self, item0):
        """
        净化博文
        :param item0:博文
        :return:净化干净的博文
        """
        sub_title = re.compile('<img.*?注')
        tag = re.compile('<.*?>')  # 去除标签
        link = re.compile('<a href=.*?>|http.*?</a>')  # 去除链接
        content = re.sub(link, "", item0)
        content = re.sub(tag, '', content)
        content = re.sub(sub_title, '', content)
        # content = content.encode('utf-8', 'ignore')  # content为完成的博文
        return content

    def get_forward_common(self, forward_url):
        """
        匹配转发路径及理由，用列表返回
        :param forward_url: 转发页的链接
        :return:该页的转发路径及理由
        """
        # 转发页需要用到的正则
        forward_patterns = re.compile(
            # '<div class="s"></div><div class="c"><a href="/u/(.*?)">(.*?)</a>.*?:(.*?)&nbsp'   # 匹配全部转发者
            '//<a href="/n.*?>(@.*?)</a>:(.*?)&nbsp;')  # 去除最后一个转发者的路径
        other_patterns = re.compile('//<.*?>')
        label_pattern = re.compile('<.*?>')
        useless = re.compile('</a>.*$')
        link_pattern = re.compile('http.*?</a>')  # 去除链接
        link_pattern1 = re.compile('<a href="')
        space_pattern = re.compile('&nbsp;')
        extral_pattern = re.compile('//')

        req = urllib2.Request(url=forward_url, headers=self.header)
        forward_page = urllib2.urlopen(req).read()
        time.sleep(int(random.uniform(0, 2)))

        forward_path = forward_patterns.findall(forward_page)

        blog_origin_pattern = re.compile('>(http://t.cn/.*?)</a></span>')
        forward_participants_pattern = re.compile(
            '<div class="c"><a href="/\D.*?">(.*?)</a>'
        )
        blog_origin = blog_origin_pattern.findall(forward_page)
        forward_participants = forward_participants_pattern.findall(forward_page)

        if len(blog_origin) > 0:
            blog_origin = [re.sub(useless, '', blog_origin[0])]
            self.link = blog_origin[0]
        else:
            blog_origin.append(str(None))

        forward_string_list = []
        for k in forward_path:
            k0 = re.sub(label_pattern, '', k[0])
            kk = re.sub(other_patterns, '', k[1])
            forward_reason1 = re.sub(link_pattern, '', kk)
            forward_reason2 = re.sub(label_pattern, '', forward_reason1)
            forward_reason3 = re.sub(space_pattern, '', forward_reason2)
            forward_reason4 = re.sub(extral_pattern, '', forward_reason3)
            forward_reason = re.sub(link_pattern1, '', forward_reason4)

            forward_string = str(k0) + ": " + str(forward_reason)
            forward_string_list.append(forward_string)
        no_repeat_list = list(set(forward_string_list))
        no_repeat_list.sort(key=forward_string_list.index)
        return no_repeat_list, forward_participants  # 返回转发路径和博文源,参与人
