f=file('scores.txt')
lines=f.readlines()
print lines
f.close()

results =[]
for line in lines:
    #print line
    data=line.split(" ")
    print data
    sum=0
    for note in data[1:]:
       point=int(note)# transfer in integer first
          if point<60:
          continue
       sum+=int(note)


    result='%s \t: %d\n' %(data[0],sum)
    print result
    results.append(result)

#print results
output=open('results.txt','w')
output.writelines(results)
output.close()
