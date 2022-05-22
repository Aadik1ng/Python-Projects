import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def card(a):
      emc=0
      ecc=0
      if(a==0):
          mci = random.randint(0, len(cards))
          emc = cards[mci]
          return(emc)
      else:
           cci=random.randint(0,len(cards))
           ecc=cards[cci]
           return(ecc)
      #return(emc,ecc)
cmi=random.randint(0,len(cards))
ci=random.randint(0,len(cards))
mc=[]
mc.append(cards[cmi])
cc=[]
cc.append([ci])
print(sum(cc))
print(sum(mc))
summ=sum(mc)
sumc=sum(cc)
while summ>17:
    mccc=0
    x=card(mccc)
    mc.append(cards[cmi])
    summ=sum(mc)
while sumc>17:
    cccc=0
    y=card(cccc)
    cc.append([ci])
    sumc=sum(cc)
if(sum[cc]>21):
    print(f"You won\n")
if(sum[mc]>21):
    print("You lost\n")