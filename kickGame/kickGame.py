from random import choice
score=[0,0]

def kcik():
    for i in range(0,5):
        print'left,centre,right'
        you=raw_input()
        print'you choose '+you
        direction=['left','centre','right']
        p=choice(direction)
        print 'computer saved '+p
        if you==p:
            print 'what a pity!!!'
            score[1]+=1
        else:
            print'goal!!!'
            score[0]+=1
    print '\n'
    print 'score of you is '+str(score[0])
    print 'score of pc is '+str(score[1])

print score

while score[0]==score[1]:
    kcik()
