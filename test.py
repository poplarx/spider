import urllib2
import cookielib
from bs4 import BeautifulSoup

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

url = 'http://www.baidu.com'
response = opener.open(url)

for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value

