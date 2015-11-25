__author__ = 'poplarx'

#-- coding: utf-8 --

import urllib2

page = 1
base_url = "http://www.qiushibaike.com/hot/page/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}


try:
    request = urllib2.Request(base_url + str(page),headers=headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

