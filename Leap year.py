x= int (input("Enter Year\n"))
if x%4==0:
      if x%100 != 0:
              print("leap\n")
      else :
          if x%400 == 0:
             print("Leap \n")
          else:
             print("Not leap\n")

else:
 print("Not leap")