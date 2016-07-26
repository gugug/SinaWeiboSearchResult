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
        search_process = multiprocessing.Process(target=start_search, args=(time_dir, blog)) # 搜索每一个blog
        search_process.start()
        threads.append(search_process)

    for j in range(len(threads)):
        threads[j].join()


def start_search(time_dir,one_blog):
    """
    对一个博文在微博平台进行搜索
    :return:
    """
    total_dir = create_topic_file(time_dir, one_blog)
    print total_dir
    print "正在进行搜索并爬取..."

    # [blog_id, ptime, topic, content, user_id, user_name,like_num, rpt_num, cmt_num]

    total_result_list, total_reason_list, total_comment_list, total_participants_list, total_originator, lfc_all_num = st().search_topic(one_blog)

    # 写入内容
    write_forward(total_dir, total_reason_list)
    write_comment(total_dir, total_comment_list)
    write_participants(total_dir, total_participants_list)

    # lfc_all_num = [该话题的点赞规模,该话题的转发规模,该话题的评论规模]
    print '*******************************'
    print "该话题的点赞规模", lfc_all_num[0]
    print "该话题的转发规模", lfc_all_num[1]
    print "该话题的评论规模", lfc_all_num[2]

    blog_id = total_result_list[0]
    content = total_result_list[3]
    post_time = total_result_list[1]
    comment_num = lfc_all_num[2]
    like_num = lfc_all_num[0]
    repost_num = lfc_all_num[1]
    result_dict.setdefault(one_blog,[blog_id,content,total_originator,post_time,comment_num,repost_num,like_num])


MoblieWeibo().login('1939777358@qq.com', 'password') # 登陆
serach_list(["奥运村", "曼联VS曼城", "台湾游览车起火", "南海"])


