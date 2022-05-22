import random
r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
c=random.randint(1,3)
u=input("Rock Paper Scissors\n").lower()
if(c==1):
  c=r
if(c==2):
   c=p
else:
    c=s
if(u=='r'):
    print(f"\n{r}")
    if(c==r):
        print(f"\n{r}\nDraw")
    elif (c==p):
        print(f"\n{p}\nLost")
    else:
        print(f"\n{s}\nWon")
if(u=='p'):
    print(f"\n{p}")
    if(c==r):
        print(f"\n{r}\nWon")
    elif (c==p):
        print(f"{p}\nDraw")
    else:
        print(f"{s}\nLost")
if(u=='s'):
    print(f"\n{s}")
    if(c==r):
        print(f"{r}\nLost")
    elif (c==p):
        print(f"{p}\nWon")
    else:
        print(f"{s}\nDraw")











