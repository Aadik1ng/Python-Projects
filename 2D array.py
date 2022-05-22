
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))
r = int(position%10)
c = int(position/10)%10
print(f"Column = {r}\n Row = {c}")
r=r-1
c=c-1
map[r] [c] = "x"
print(f"{row1}\n{row2}\n{row3}")