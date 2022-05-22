x=input("Enter your Name\n")
y=input("Enter her name\n")
x=x.lower()
y=y.lower()
z=x+y
t=(z.count("t"))

r=(z.count("r"))
u=(z.count("u"))
e=(z.count("e"))
c=str(t + r + u + e)
l=(z.count("l"))
o=(z.count("o"))
v=(z.count("v"))
e=(z.count("e"))
b=str(l + o + v + e)
s=int(c+b)
if(s<10 or s>90):
    print("Coke Mentos")
elif(x>=40 or x<=50):
    print("Alright")




print(f"\n{c+b} ")