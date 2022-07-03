t = int(input())
for i in range(t):
    (S, X, Y, Z)=map(int,input().split(' '))
    if X + Y + Z <= S:
        print(0)
    else:
        if Z+min(X,Y) <= S:
            print(1)
        else:
            print(2)
    
