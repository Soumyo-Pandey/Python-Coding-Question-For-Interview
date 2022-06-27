#House Construction[TCS NQT]

def costOfGarden(side, length, breadth, cost):
    ans = 0
    if (side<=0 or length<=0 or breadth<=0 or cost<=0 or side<length or side<length):
        print("Invalid Input")
    else:
        ss = side*side
        areah = length*breadth
        t = ss-areah
        ans = (t*cost)//100
        print(ans)
        print('\n')
costOfGarden(50,40,35,65);
