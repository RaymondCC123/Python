# -*- coding: utf-8 -*-

import json
import city
import ville
import urllib2

cityname = raw_input('Whose temperature you want to know ？\n')
citycode = ville.ville.get(cityname)
#citycode = city.city.get(cityname)
if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % (citycode))
        content = urllib2.urlopen(url).read()
        #print content
        data = json.loads(content)# transfer String into Dictionary
        #print type(content)
        #print type(data)
        #print data
        result = data['weatherinfo']
        #print result
        str_temp = '%s\n%s ~ %s' % (result['weather'], result['temp1'], result['temp2'])
        print str_temp
    except:
        print 'search failed'
else:
    print 'city not existed'


