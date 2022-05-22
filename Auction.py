import os
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(f"{logo}\n")
l={}
i=55
while (i!=0):
  n=c=''
  p=0

  n=str(input("Enter your Names\n"))
  p=float(input("Enter Bid\n"))
  c=str(input("Continue Auction\n")).lower()
  l[n]=p
  if(c!='yes'):
    i=0

print(f"The winner is {min(l,key=l.get(1))}")