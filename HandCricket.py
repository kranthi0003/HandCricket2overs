#HandCricket
#seg-1:Toss Time
import time
import random
def User_Batting1st():
    print("                   Batting starts                \n")
    score_sys,score_user=0,0
    for i in range(12):
        print("Ball",(i+1),"\n")
        b=int(input())
        if(b>6 or b<1):
          print("Enter value b/w 1 and 6")
          i-=1
          continue
        ran=random.choice([0,1,2,3,4,5,6])
        if(ran==b):
            print("----Out------\nYour Batting is Over")
            break
        print(b,"runs")
        if(1<=b<=6):
          score_user+=b
    print("------",(score_user+1),"is the target----")
    print("...........Innings break............")
    time.sleep(7)
    print("                   Your Opponent Batting Starts                 \n")
    for i in range(12):
        print("Ball",(i+1),"\n")
        bo=int(input())
        if(bo>6 or bo<1):
          print("Enter value b/w 1 and 6")
          i-=1
          continue
        ranbo=random.choice([1,2,3,4,5,6])
        if(bo==ranbo):
            print("----Out------\n")
            break
        print(ranbo,"runs")
        if(1<=bo<=6):
          score_sys+=ranbo
        if(score_sys>score_user):
            print("You lost the match\n")
            print("                      Game Ends                       ")
            break
    if(score_user>score_sys):
        print("You Won the match by",(score_user-score_sys),"runs\n")
        print("                      Game Ends                       ")
    if(score_user==score_sys):
        print("              Game Draw              ")
        
def User_Bowling1st():
    print("               Your Opponent Batting starts                \n")
    score_sys,score_user=0,0
    for i in range(12):
        print("Ball",(i+1),"\n")
        b=int(input())
        if(b>6 or b<1):
          print("Enter value b/w 1 and 6")
          i-=1
          continue
        ran=random.choice([1,2,3,4,5,6])
        if(ran==b):
            print("----Out------\nYour Opponent Batting is Over")
            break
        print(ran,"runs")
        if(1<=b<=6):
          score_sys+=ran
    print("------",(score_sys+1),"is the target----")
    print("...........Innings break............")
    time.sleep(7)
    print("                    Batting Starts                 \n")
    for i in range(12):
        print("Ball",(i+1),"\n")
        bo=int(input())
        if(bo>6 or bo<1):
          print("Enter value b/w 1 and 6")
          i-=1
          continue
        ranbo=random.choice([1,2,3,4,5,6])
        if(bo==ranbo):
            print("----Out------\n")
            break
        print(bo,"runs")
        if(1<=bo<=6):
          score_user+=bo
        if(score_user>score_sys):
            print("You won the match")
            print("                      Game Ends                       ")
            break
    if(score_user<score_sys):
        print("You Lost the match by",(score_sys-score_user),"runs")
        print("                      Game Ends                       ")
    if(score_user==score_sys):
        print("              Game Draw              ")
    


print("-------It's a Two over,one Wicket Game---------\n")
print("Rules:\n1-6 score\nsame number result in wicket\nEnter only between 1 and 6 otherwise a ball will be wasted\n")
print("Enter H or heads and T or Tails\n")
s=input()
print("coin flips\n")
time.sleep(1)
to=random.choice(['H','T'])
print(to)
if(to=='H'):
  print("Its Heads")
else:
  print("Its Tails")
if(s==to):
  print("Enter 1 for Batting and 0 for Bowling\n")
  t=int(input())
  if(t==1):
    User_Batting1st()
  else:
    User_Bowling1st()
else:
  t1=random.choice([1,2])
  if(t1==1):
    print("Your Opponent chose to bat first\n")
    User_Bowling1st()
  else:
    print("Your Opponent chose to bowl first\n")
    User_Batting1st()
    
    
