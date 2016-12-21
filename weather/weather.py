# -*- coding: utf-8 -*-

import json
import city
import urllib2

cityname=raw_input('你想查哪个城市的天气？\n')
citycode=city.city.get(cityname)
if citycode :
    url=('http://www.weather.com.cn/weather1d/%s.shtml' %(citycode))
    content=urllib2.urlopen(url).read()
    f=open('weather.html','w')
    f.write(content)
    #print content
    f.close()
    

