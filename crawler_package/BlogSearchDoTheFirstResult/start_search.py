# coding=utf-8

import multiprocessing
from multiprocessing import Manager
from MoblieWeibo import *
from write_everything import *
from create_file import *
from search_topic import SearchTopic as st

__author__ = 'gu'

"""
result_dict 全局变量作为输出结果。
"""

manager = Manager()
result_dict = manager.dict()


def serach_list(blog_list):
    """
    传入一个博文标题列表，然后多进程对每一个元素进行搜索
    :return:
    """
    time_dir = create_time_file()
    threads = []
    for blog in blog_list:
        search_process = multiprocessing.Process(target=start_search, args=(time_dir, blog))  # 搜索每一个blog
        search_process.start()
        threads.append(search_process)

    for j in range(len(threads)):
        threads[j].join()


def start_search(time_dir, one_blog):
    """
    对一个博文在微博平台进行搜索
    :return:
    """
    total_dir = create_topic_file(time_dir, one_blog)
    print total_dir
    print "正在进行搜索并爬取..."

    total_result_list, total_reason_list, total_comment_list, total_participants_list = st().search_topic(one_blog)

    if len(total_result_list) > 0:
        # 写入内容
        write_forward(total_dir, total_reason_list)
        write_comment(total_dir, total_comment_list)
        write_participants(total_dir, total_participants_list)

        # [[blog_id, content, user_name, user_id, ptime, topic, like_num, rpt_num, cmt_num]]
        blog_id = total_result_list[0][0]
        content = total_result_list[0][1]
        originator = total_result_list[0][2]
        originator_id = total_result_list[0][3]
        post_time = total_result_list[0][4]
        like_num = total_result_list[0][5]
        repost_num = total_result_list[0][6]
        comment_num = total_result_list[0][7]

        print "博文id ", blog_id
        print "博文内容 ", content
        print "发源者昵称 ", originator
        print "发源者id ", originator_id
        print "发表时间 ", post_time
        print "点赞数 ", like_num
        print "转发数 ", repost_num
        print "评论数 ", comment_num

        result_dict.setdefault(one_blog, total_result_list[0])
        # [blog_id,content,originator,originator_id,post_time,like_num,repost_num,comment_num])
    else:
        print "爬取失败"


