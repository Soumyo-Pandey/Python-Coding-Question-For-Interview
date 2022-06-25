#Dice Problem

t=int(input())
count = 0
if t>=0 and t<=12:
    for i in range(1,7):
        for j in range(1,7):
             if i+j==t:
                 count+=1
    print(count)
else:
     print(0)