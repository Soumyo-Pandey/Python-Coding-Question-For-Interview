def denomations():
    t=int(input())
    if t%10 == 0:
        print(int(t/10))
    elif t%10 == 5:
        print(int(t/10+1))
    else:
        print("-1")
u=int(input())
while u>0:
    u=u-1
    denomations()
