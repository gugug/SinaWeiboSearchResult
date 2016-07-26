# coding=utf-8
import multiprocessing
import re
import urllib2

__author__ = 'gu'

forward_page = """<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="Cache-Control" content="no-cache"/><meta id="viewport" name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0, maximum-scale=2.0" /><link rel="icon" sizes="any" mask href="http://h5.sinaimg.cn/upload/2015/05/15/28/WeiboLogoCh.svg" color="black"><meta name="MobileOptimized" content="240"/><title>转发微博</title><style type="text/css" id="internalStyle">html,body,p,form,div,table,textarea,input,span,select{font-size:12px;word-wrap:break-word;}body{background:#F8F9F9;color:#000;padding:1px;margin:1px;}table,tr,td{border-width:0px;margin:0px;padding:0px;}form{margin:0px;padding:0px;border:0px;}textarea{border:1px solid #96c1e6}textarea{width:95%;}a,.tl{color:#2a5492;text-decoration:underline;}/*a:link {color:#023298}*/.k{color:#2a5492;text-decoration:underline;}.kt{color:#F00;}.ib{border:1px solid #C1C1C1;}.pm,.pmy{clear:both;background:#ffffff;color:#676566;border:1px solid #b1cee7;padding:3px;margin:2px 1px;overflow:hidden;}.pms{clear:both;background:#c8d9f3;color:#666666;padding:3px;margin:0 1px;overflow:hidden;}.pmst{margin-top: 5px;}.pmsl{clear:both;padding:3px;margin:0 1px;overflow:hidden;}.pmy{background:#DADADA;border:1px solid #F8F8F8;}.t{padding:0px;margin:0px;height:35px;}.b{background:#e3efff;text-align:center;color:#2a5492;clear:both;padding:4px;}.bl{color:#2a5492;}.n{clear:both;background:#436193;color:#FFF;padding:4px; margin: 1px;}.nt{color:#b9e7ff;}.nl{color:#FFF;text-decoration:none;}.nfw{clear:both;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.s{border-bottom:1px dotted #666666;margin:3px;clear:both;}.tip{clear:both; background:#c8d9f3;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tip2{color:#000000;padding:2px 3px;clear:both;}.ps{clear:both;background:#FFF;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tm{background:#feffe5;border:1px solid #e6de8d;padding:4px;}.tm a{color:#ba8300;}.tmn{color:#f00}.tk{color:#ffffff}.tc{color:#63676A;}.c{padding:2px 5px;}.c div a img{border:1px solid #C1C1C1;}.ct{color:#9d9d9d;font-style:italic;}.cmt{color:#9d9d9d;}.ctt{color:#000;}.cc{color:#2a5492;}.nk{color:#2a5492;}.por {border: 1px solid #CCCCCC;height:50px;width:50px;}.me{color:#000000;background:#FEDFDF;padding:2px 5px;}.pa{padding:2px 4px;}.nm{margin:10px 5px;padding:2px;}.hm{padding:5px;background:#FFF;color:#63676A;}.u{margin:2px 1px;background:#ffffff;border:1px solid #b1cee7;}.ut{padding:2px 3px;}.cd{text-align:center;}.r{color:#F00;}.g{color:#0F0;}.bn{background: transparent;border: 0 none;text-align: left;padding-left: 0;}</style><script>if(top != self){top.location = self.location;}</script></head><body><div class="tm"><a href="http://weibo.cn/msg/?unread=1"><span class="tmn">1</span>私信</a>&nbsp;&nbsp;<a href="http://weibo.cn/msg/clearAllUnread?type=dcm&amp;rl=2"><img src="http://u1.sinaimg.cn/upload/2011/08/01/5366.gif" alt="[X]" /></a><br/></div><div class="n" style="padding: 6px 4px;"><a href="http://weibo.cn/?tf=5_009" class="nl">首页<span class="tk">!</span></a>|<a href="http://weibo.cn/msg/?tf=5_010" class="nl">消息</a>|<a href="http://huati.weibo.cn" class="nl">话题</a>|<a href="http://weibo.cn/search/?tf=5_012" class="nl">搜索</a>|<a href="/repost/E0dNsuFx5?uid=3192422090&amp;rl=1&amp;page=3&amp;rand=9919&amp;p=r" class="nl">刷新</a></div><div class="c"><a href="/comment/E0kZKj4FU?page=7&amp;rand=770595">返回评论列表</a></div><div class="s"></div><div class="c"><div>    <a href="/repost/E0dNsuFx5?rl=1">小五同学:菲律宾人民开始方...</a></div></div><div class="c"></div><div><span class="pms" id="rt">转发[6907]&nbsp;</span><span>&nbsp;<a href="/comment/E0dNsuFx5?&amp;uid=3192422090&amp;rl=1#cmtfrm" >评论[2493]</a>&nbsp;</span><span >&nbsp;<a href="/attitude/E0dNsuFx5?rl=1#attitude">赞[26755]</a>&nbsp;</span><br/></div><div class="pms">转发理由只显示前140字<form action="/repost/dort/E0dNsuFx5?st=abc2b3" method="post" id="mblogform"><div>    <input type="hidden" name="act" value="dort" />            <input type="hidden" name="rl" value="2" />    <input type="hidden" name="id" value="E0dNsuFx5" />    <textarea name="content" rows="2" cols="20" id="content"></textarea><br/>            <input type="submit" value="转发" />&nbsp;<input type="submit" name="rtmsg" value="私信转发" /> <br/>    <input type="checkbox" name="rtrootcomment"  />同时作为给小五同学<img src="http://h5.sinaimg.cn/upload/2016/05/26/319/5547.gif" alt="达人"/><img src="http://h5.sinaimg.cn/upload/2016/05/26/319/donate_btn_s.png" alt="M"/>的评论发布.      </div></form></div><div class="c"><a href="/u/5611291828">-麦兜-丫</a>:转发微博 <a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRt43xRt&amp;ep=E0sL9EBof%2C5611291828%2CE0sL9EBof%2C5611291828">http://t.cn/Rt43xRt</a>&nbsp;<span class="cc"><a href="/attitude/E0sL9EBof/add?uid=5663861322&amp;rl=2&amp;do=rt&amp;st=abc2b3">赞[0]</a></span><span class="ct">&nbsp;今天 12:36&nbsp;来自iPhone 6s Plus</span></div><div class="s"></div><div class="c"><a href="/u/3227958433">逗比怪兽就素我</a>:233333//<a href="/n/%E9%95%BF%E4%B8%8D%E8%BF%87%E6%89%A7%E5%BF%B5%E7%9F%AD%E4%B8%8D%E8%BF%87%E5%96%84-%E5%8F%98">@长不过执念短不过善-变</a>: 哈哈哈哈哈哈<a href="/n/Honey_Guagua">@Honey_Guagua</a> <a href="/n/Yyyy%E5%92%BF%E5%91%80%E5%92%BF%E5%91%80">@Yyyy咿呀咿呀</a> <a href="/n/%E9%80%97%E6%AF%94%E6%80%AA%E5%85%BD%E5%B0%B1%E7%B4%A0%E6%88%91">@逗比怪兽就素我</a> <a href="/n/%E5%A4%A7%E5%AE%9DSOD%E8%9B%8B">@大宝SOD蛋</a>&nbsp;<span class="cc"><a href="/attitude/E0sEOlROM/add?uid=5663861322&amp;rl=2&amp;do=rt&amp;st=abc2b3">赞[0]</a></span><span class="ct">&nbsp;今天 12:20&nbsp;来自360安全浏览器</span></div><div class="s"></div><div class="c"><a href="/u/5709450390">风圈圈圆</a>:转发微博&nbsp;<span class="cc"><a href="/attitude/E0sEHjf6k/add?uid=5663861322&amp;rl=2&amp;do=rt&amp;st=abc2b3">赞[0]</a></span><span class="ct">&nbsp;今天 12:20&nbsp;来自华为Ascend手机</span></div><div class="s"></div><div class="c"><a href="/u/2267682944">zaishenlan旅行的叶子</a>:转发微博&nbsp;<span class="cc"><a href="/attitude/E0sDVpjyh/add?uid=5663861322&amp;rl=2&amp;do=rt&amp;st=abc2b3">赞[0]</a></span><span class="ct">&nbsp;今天 12:18&nbsp;来自红米Note 3</span></div><div class="s"></div><div class="c"><a href="/u/3962437924">刘英俊超级无敌帅到爆</a>:[微笑]//<a href="/n/Sakura%E6%B6%BC%E5%AD%90">@Sakura涼子</a>:去找你美爹[微笑]//<a href="/n/jump%E7%96%AF%E7%88%B7">@jump疯爷</a>:http://t.cn/RtbwnqH 海风大，听不见//<a href="/n/%E5%98%BF%E9%A6%99%E8%95%89%E4%B8%AA%E6%8B%94%E8%BE%A3%E6%9D%A5%E4%B8%80%E5%A5%97">@嘿香蕉个拔辣来一套</a>:哈哈哈哈哈哈哈哈哈&nbsp;<span class="cc"><a href="/attitude/E0sD5nLph/add?uid=5663861322&amp;rl=2&amp;do=rt&amp;st=abc2b3">赞[0]</a></span><span class="ct">&nbsp;今天 12:16&nbsp;来自手机微博触屏版</span></div><div class="s"></div><div class="c"><a href="/u/5864835772">苏_Delieved</a>:唉 //<a href="/n/jump%E7%96%AF%E7%88%B7">@jump疯爷</a>:海风大，听不见//<a href="/n/%E5%98%BF%E9%A6%99%E8%95%89%E4%B8%AA%E6%8B%94%E8%BE%A3%E6%9D%A5%E4%B8%80%E5%A5%97">@嘿香蕉个拔辣来一套</a>:哈哈哈哈哈哈哈哈哈&nbsp;<span class="cc"><a href="/attitude/E0sz0t6UK/add?uid=5663861322&amp;rl=2&amp;do=rt&amp;st=abc2b3">赞[0]</a></span><span class="ct">&nbsp;今天 12:06&nbsp;来自iPhone 6</span></div><div class="s"></div><div class="c"><a href="/u/2548242534">Sakura涼子</a><img src="http://h5.sinaimg.cn/upload/2016/05/26/319/5547.gif" alt="达人"/><img src="http://h5.sinaimg.cn/upload/2016/05/26/319/donate_btn_s.png" alt="M"/>:去找你美爹[微笑]//<a href="/n/jump%E7%96%AF%E7%88%B7">@jump疯爷</a>:海风大，听不见//<a href="/n/%E5%98%BF%E9%A6%99%E8%95%89%E4%B8%AA%E6%8B%94%E8%BE%A3%E6%9D%A5%E4%B8%80%E5%A5%97">@嘿香蕉个拔辣来一套</a>:哈哈哈哈哈哈哈哈哈&nbsp;<span class="cc"><a href="/attitude/E0sxCuUu5/add?uid=5663861322&amp;rl=2&amp;do=rt&amp;st=abc2b3">赞[2]</a></span><span class="ct">&nbsp;今天 12:02&nbsp;来自三星android智能手机</span></div><div class="s"></div><div class="c"><a href="/u/2163365734">jump疯爷</a><img src="http://h5.sinaimg.cn/upload/2016/05/26/319/5547.gif" alt="达人"/>:海风大，听不见//<a href="/n/%E5%98%BF%E9%A6%99%E8%95%89%E4%B8%AA%E6%8B%94%E8%BE%A3%E6%9D%A5%E4%B8%80%E5%A5%97">@嘿香蕉个拔辣来一套</a>:哈哈哈哈哈哈哈哈哈&nbsp;<span class="cc"><a href="/attitude/E0svS1nTx/add?uid=5663861322&amp;rl=2&amp;do=rt&amp;st=abc2b3">赞[1]</a></span><span class="ct">&nbsp;今天 11:58&nbsp;来自华为P9手机摄影再突破</span></div><div class="s"></div><div class="c"><a href="/asako1226">嘿香蕉个拔辣来一套</a><img src="http://h5.sinaimg.cn/upload/2016/05/26/319/5547.gif" alt="达人"/>:哈哈哈哈哈哈哈哈哈&nbsp;<span class="cc"><a href="/attitude/E0stcxc5Q/add?uid=5663861322&amp;rl=2&amp;do=rt&amp;st=abc2b3">赞[0]</a></span><span class="ct">&nbsp;今天 11:51&nbsp;来自微博 weibo.com</span></div><div class="s"></div><div class="pa" id="pagelist"><form action="/repost/E0dNsuFx5?uid=3192422090&amp;rl=1" method="post"><div><a href="/repost/E0dNsuFx5?uid=3192422090&amp;rl=1&amp;page=4">下页</a>&nbsp;<a href="/repost/E0dNsuFx5?uid=3192422090&amp;rl=1&amp;page=2">上页</a>&nbsp;<a href="/repost/E0dNsuFx5?uid=3192422090&amp;rl=1">首页</a>&nbsp;<input name="mp" type="hidden" value="691" /><input type="text" name="page" size="2" style='-wap-input-format: "*N"' /><input type="submit" value="跳页" />&nbsp;3/691页</div></form></div><div class="s"></div><div class="c"><a href="/comment/E0kZKj4FU?page=7&amp;rand=770595">返回评论列表</a></div></body></html>"""
forward_patterns = re.compile(
    # '<div class="s"></div><div class="c"><a href="/u/(.*?)">(.*?)</a>.*?:(.*?)&nbsp'   # 匹配全部转发者
    '//<a href="/n.*?>(@.*?)</a>:(.*?)&nbsp;')  # 去除最后一个转发者的路径
other_patterns = re.compile('//<.*?>')
label_pattern = re.compile('<.*?>')
useless = re.compile('</a>.*$')
link_pattern = re.compile('http.*?</a>')  # 去除链接
space_pattern = re.compile('&nbsp;')

forward_path = forward_patterns.findall(forward_page)

for k in forward_path:
    k0 = re.sub(label_pattern, '', k[0])
    kk = re.sub(other_patterns, '', k[1])
    forward_reason1 = re.sub(link_pattern, '', kk)
    forward_reason2 = re.sub(label_pattern, '', forward_reason1)
    forward_reason = re.sub(space_pattern, '', forward_reason2)
    forward_string = str(k0) + ": " + str(forward_reason)

    print forward_string

s = "oafce : 图片评论 http://t.cn/Rtbyof2"
link_pattern = re.compile('http.*?$')  # 去除链接
a = re.sub(link_pattern,'',s)
print a