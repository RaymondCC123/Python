# -*- coding: utf-8 -*-
from random import randint

name=raw_input()
f=file('game.txt','r')
lines=f.readlines()
scores={}
for i in lines:
    s=i.split(' ')
    scores[s[0]]=s[1:]
score=scores.get(name)
if score==None :
    score=[0,0,0]

#score=f.read().split(' ')
game_times=int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times>0:
    avg_times=float(total_times)/game_times
else:
    avg_times=0
print '你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案\n' % (game_times, min_times, avg_times) 

num=randint(1,100)
print 'Guess what i m thinking'
times=0#记录每次游戏所用的轮数
    
bingo=False
while bingo==False:
    times+=1
    ans=input()
    if ans<num:
        print 'too small'
    if ans>num:
        print 'too big'
    if ans==num:
        print 'bingo'
        bingo=True

    #如果是第一次玩，或者本次的轮数比最小轮数还少，就记录本次成绩为最小轮数：
if game_times==0 or times<min_times:
    min_times=times

total_times+=times#把本次轮数加到游戏总轮数里：
game_times+=1#把游戏次数加1

scores[name]=[str(game_times), str(min_times), str(total_times)]

#把scores中的每一项按照“名字 游戏次数 最低轮数 总轮数\n”的格式拼成字符串，再全部放到result里
result=''
for i in scores:
    line=i+' '+' '.join(scores[i])+'\n'
    result+=line

f=file('game.txt','w')
f.write(result)
f.close()



