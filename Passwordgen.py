# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['4', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nlet = int(input("How many letters would you like in your password?\n"))
nsym = int(input(f"How many symbols would you like?\n"))
num = int(input(f"How many numbers would you like?\n"))

j = m = y = k = []
for i in range(0, nlet):
    l = random.randint(0, 52)
    j.insert(i, [letters[l]])
#print(j)
#

for n in range(0, num):
    u = random.randint(0, 9)
    m.insert(n, [numbers[u]])
#print(m)
for p in range(0, nsym):
    s = random.randint(0, 8)
    y.insert(p, [symbols[s]])
#print(y)
random.shuffle(y)
print(y)