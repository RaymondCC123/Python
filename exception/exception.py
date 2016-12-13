try:
    f=file("fuck.txt",'r')
    print 'File opened'
    f.close()
except:
    print 'File not existed'

print 'Done'
