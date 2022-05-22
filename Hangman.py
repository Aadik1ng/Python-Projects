import random
import collections


def check(us, d, ch):
    x = 0
    cd = []
    cd = d

    # print(len(ch))
    for i in range(0, len(ch)):
        if (x != len(ch)):
            if (ch[i] == us):
                d[i] = us

            else:
                x += 1

        else:
            print("Wrong")

    if collections.Counter(cd) == collections.Counter(d):
        print("Wrong")
    print(d)
    return [d, x]


w = ["Aaditya", "Aaryan"]
ch = []
d = []
q = 0
ch[:0] = random.choice(w).lower()
for o in range(0, len(ch)):
    d.append('_')
print(d)
# while d[-1]=='_':
us = input("\nGuess a letter\n").lower()
e = 1
md = []
mx = 0
md = check(us, d, ch)
e += md[-1]
k = s = 0
while k <= 2:
    if (md[0][-1] == '_'):
        us = input("\nGuess a letter\n").lower()
        k += 1
        md = check(us, d, ch)
        mx = md[-1]
        md.pop(-1)
    else:
        s += 1



