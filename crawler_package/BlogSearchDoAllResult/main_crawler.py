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
    MoblieWeibo().login('meilanyiyou419@163.com','aaa333')#('1939777358@qq.com', '123456a') #'70705420yc@sina.com', '1234567')
    # 'odlmyfbw@sina.cn','tttt5555')#'1939777358@qq.com', '123456a')

    while True:
        run()
        # copy_file()
        print "即将休息一下"

        sleep(3600)
        print "程序睡醒"

main_weibo()


# def main_crawler():
#     s = multiprocessing.Semaphore(2)
#     db_cnt = Content()
#     db_save = Database()
#     wp = WeiboPage()
#     search_tp = SearchTopic()
#     result = []
#     unsearched_topic = []
#     detection()
#     topic_tuple = db_cnt.get_topic_tuple() #({topic,blog_id,topic_words})
#
#
#     for i in topic_tuple:
#         result = function(topic_tuple) #聚类,默认结果形式[{eid:1,blog_id:111},{eid:1,blog_id:222]
#
#     for i in result:
#         db_save.update_eid(i['blog_id'],i['eid'])  #打标签
#     ##此时content表是完整的,都是猎头的博文
#     if len(WeiboPage.searched_tpdict)==0:
#         for i in topic_tuple:
#             unsearched_topic.append(i)
#     else:
#        #判重,此处one_id_txt应该与get_topic合并
#     for i in unsearched_topic:
#         search_tp.search_topic('对是否需要uid有疑问',i) #搜索未检索过的topic
