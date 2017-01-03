import urllib2

url1 = 'http://m.weather.com.cn/data5/city.xml'
content1 = urllib2.urlopen(url1).read()
print content1
provinces = content1.split(',') #split elements
#print provinces[1]

eles = []
cities = []
result = {}# define dictionary
#result = 'city = {\n'

url = 'http://m.weather.com.cn/data3/city%s.xml'# grab city_info in each province
for i in provinces[1:2]:
    eles = i.split('|')
    url2 = url % (eles[0])
    content2 = urllib2.urlopen(url2).read()
    print content2
    cities = content2.split(',')

    for c in cities:# grap district info in each city
        eles = c.split('|')
        url3 = url % (eles[0])
        content3 = urllib2.urlopen(url3).read()
        print content3
        districts = content3.split(',')

        for d in districts:# grap the exact code of each district
            eles = d.split('|')
            name = eles[1]
            url4 = url % eles[0]
            content4 = urllib2.urlopen(url4).read()
            #print content4
            code = content4.split('|')[1]
            result[name] = code
            #line = "'%s': '%s',\n" %(name,code)
            print name
            #result += line
            print result

f = file('ville.py', 'w')
f.write('ville = ' + str(result))
f.close()
