# -*- coding: utf-8 -*-
from random import randint


f=file('game.txt','r')
score=f.read().split(' ')
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

result='%d %d %d' %(game_times, min_times, total_times)

f=file('game.txt','w')
f.write(result)
f.close()



