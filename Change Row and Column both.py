t = int(input())
for i in range(t):
    a,b,c,d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if a!=c and b!=d:
        x = 1 
    else:
        x = 2
    print(x)
